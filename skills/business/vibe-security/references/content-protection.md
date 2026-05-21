# Content Protection & API Hardening

This reference covers vulnerabilities specific to apps that sell content — courses, lessons, articles, media, or any gated digital product. These issues are distinct from general auth/payment bugs because the content itself is the product, and a single successful scrape can extract your entire catalog.

In a real-world audit of a production education app, an attacker extracted all 274 paid lessons across 29 courses in under 30 minutes using only the APK file and curl. Every vulnerability below was present.


## Server-Side Entitlement Checks

The most critical vulnerability in content apps: the API returns full paid content to any authenticated user, regardless of subscription status. The paywall exists only in the app UI — the server doesn't check whether the user has actually paid.

This happens because developers build the paywall as a UI gate (show/hide content based on a local subscription flag) but forget that the API endpoint backing that UI is a public HTTP endpoint anyone can call directly.

```dart
// BAD: returns full content to any authenticated user
Future<Response> getLesson(Request request, String lessonId) async {
  final user = await authenticateRequest(request); // checks token only
  final lesson = await db.lessons.findById(lessonId);
  return Response.ok(jsonEncode(lesson)); // full content, no entitlement check
}

// GOOD: checks subscription AND content access before returning content
Future<Response> getLesson(Request request, String lessonId) async {
  final user = await authenticateRequest(request);

  // Check active subscription
  final subscription = await db.subscriptions.findActive(userId: user.id);
  if (subscription == null) {
    // Return preview only — title, description, first paragraph
    final preview = await db.lessons.findPreview(lessonId);
    return Response.ok(jsonEncode(preview));
  }

  // Check content tier — does this subscription include this lesson?
  final lesson = await db.lessons.findById(lessonId);
  if (!subscription.includesContent(lesson.tier)) {
    return Response.forbidden('Upgrade required for this content');
  }

  return Response.ok(jsonEncode(lesson));
}
```

### What to check for:
- Do content endpoints (lessons, articles, chapters, media files) verify subscription status before returning the payload?
- Is there a distinction between preview content (free) and full content (paid)?
- Does the server check content *tier* — can a basic-plan user access premium-only content?
- Are progression gates enforced server-side? (e.g., "must complete lesson 1 before accessing lesson 2")
- Is subscription status checked against the database (webhook-updated), not a cached JWT claim?


## CDN Content Protection

Static content served from CDN (CloudFront, Cloud Storage, S3) without access control is public content — regardless of whether the app UI makes it look gated.

Common mistakes:
- Course JSON files served directly from CDN with no auth (anyone who guesses the URL gets the content)
- Quiz answer keys embedded in the JSON response (the client receives correct answers before the user submits)
- Images and media on CDN paths discoverable by pattern (e.g., `/lessons/image-1.png`, `/lessons/image-2.png`)

```dart
// BAD: hardcoded CDN URL, no access control
final contentUrl = 'https://d2h7i1o4snhir4.cloudfront.net/lessons/$lessonId.json';
final response = await http.get(Uri.parse(contentUrl)); // anyone can call this

// GOOD: server generates a short-lived signed URL after verifying entitlement
final response = await http.get(
  Uri.parse('$apiBaseUrl/lessons/$lessonId/content-url'),
  headers: {'Authorization': 'Bearer $token'},
);
final signedUrl = jsonDecode(response.body)['url']; // expires in 15 minutes
final content = await http.get(Uri.parse(signedUrl));
```

### Signed URL pattern (server-side):
```javascript
// Node.js — generate CloudFront signed URL after entitlement check
const { getSignedUrl } = require('@aws-sdk/cloudfront-signer');

app.get('/lessons/:id/content-url', requireAuth, requireSubscription, (req, res) => {
  const url = getSignedUrl({
    url: `https://cdn.example.com/lessons/${req.params.id}.json`,
    keyPairId: process.env.CF_KEY_PAIR_ID,
    privateKey: process.env.CF_PRIVATE_KEY,
    dateLessThan: new Date(Date.now() + 15 * 60 * 1000).toISOString(), // 15 min
  });
  res.json({ url });
});
```

### Quiz answer keys:
```dart
// BAD: answer key sent to client before user answers
{
  "question": "What does AI stand for?",
  "options": ["Artificial Intelligence", "Auto Input", "Applied Internet"],
  "correct_index": 0  // attacker sees the answer
}

// GOOD: server validates answer, client never sees the key
// Client sends: POST /quiz/answer { questionId: "abc", selectedIndex: 1 }
// Server responds: { correct: false, correctIndex: 0, explanation: "..." }
```

### What to check for:
- Are any content files (JSON, images, media) served from CDN without signed URLs or token-based access?
- Do quiz/assessment responses include correct answers before the user submits?
- Are CDN paths predictable/enumerable? (sequential IDs, guessable slugs)
- Can an attacker list all content by pattern (e.g., incrementing IDs or locale codes)?


## Device Attestation

SSL pinning protects against man-in-the-middle attacks (intercepting traffic between app and server) but does nothing when an attacker calls your API directly from curl, Python, or Postman. The server has no way to distinguish a request from your app vs a request from curl — they look identical.

Device attestation solves this by having the device's secure hardware generate a cryptographic proof that the request originates from a legitimate, unmodified install of your app.

### Google Play Integrity API (Android):
```dart
// Client: request integrity token
import 'package:play_integrity/play_integrity.dart';

final token = await PlayIntegrity.requestIntegrityToken(nonce: serverNonce);
// Send token with API request
final response = await http.get(
  Uri.parse('$apiUrl/lessons/$id'),
  headers: {
    'Authorization': 'Bearer $authToken',
    'X-Integrity-Token': token,
  },
);
```

```javascript
// Server: verify the integrity token
const { PlayIntegrity } = require('google-auth-library');

app.use('/api/*', async (req, res, next) => {
  const integrityToken = req.headers['x-integrity-token'];
  if (!integrityToken) return res.status(403).json({ error: 'Missing attestation' });

  const result = await playIntegrity.decodeIntegrityToken(integrityToken);
  if (result.deviceIntegrity.deviceRecognitionVerdict !== 'MEETS_DEVICE_INTEGRITY') {
    return res.status(403).json({ error: 'Device integrity check failed' });
  }
  next();
});
```

### Firebase App Check (cross-platform, simpler):
```dart
// Flutter: Firebase App Check — works on both Android and iOS
import 'package:firebase_app_check/firebase_app_check.dart';

await FirebaseAppCheck.instance.activate(
  androidProvider: AndroidProvider.playIntegrity,
  appleProvider: AppleProvider.appAttest,
);
// App Check token is automatically attached to Firebase requests
// For custom backends, get the token manually:
final appCheckToken = await FirebaseAppCheck.instance.getToken();
```

### What to check for:
- Does the server accept requests from any HTTP client, or does it verify request origin?
- Is there device attestation (Play Integrity, App Attest, Firebase App Check)?
- If SSL pinning is present, is it the *only* protection? (it shouldn't be)


## Request Signing

For APIs that can't use device attestation (or as an additional layer), HMAC request signing makes it harder to forge requests from outside the app. Each request includes a signature computed from the request body, a timestamp, and a secret.

### Level 1: Basic HMAC Signing (raises the bar)

The signing secret is hardcoded in the app binary. This stops casual attackers but can be defeated by decompilation.

```dart
// Client: sign each request
import 'dart:convert';
import 'package:crypto/crypto.dart';

Map<String, String> signRequest(String body, String secret) {
  final timestamp = DateTime.now().millisecondsSinceEpoch.toString();
  final payload = '$timestamp:$body';
  final hmac = Hmac(sha256, utf8.encode(secret));
  final signature = hmac.convert(utf8.encode(payload)).toString();
  return {
    'X-Timestamp': timestamp,
    'X-Signature': signature,
  };
}
```

```javascript
// Server: verify signature and reject stale requests
app.use('/api/*', (req, res, next) => {
  const timestamp = req.headers['x-timestamp'];
  const signature = req.headers['x-signature'];

  // Reject requests older than 5 minutes (prevents replay attacks)
  if (Date.now() - parseInt(timestamp) > 5 * 60 * 1000) {
    return res.status(403).json({ error: 'Request expired' });
  }

  const expected = crypto
    .createHmac('sha256', process.env.REQUEST_SIGNING_SECRET)
    .update(`${timestamp}:${JSON.stringify(req.body)}`)
    .digest('hex');

  if (signature !== expected) {
    return res.status(403).json({ error: 'Invalid signature' });
  }
  next();
});
```

**Limitation:** The signing secret is embedded in the app binary and can be extracted via decompilation (`strings libapp.so` or jadx). Request signing raises the bar but isn't unbreakable with a hardcoded secret.

### Level 2: Encrypted HMAC Signing (RECOMMENDED — stopped a real attack)

This is the strongest pattern we've seen in a production app. It successfully blocked content extraction during a real reverse engineering attempt. The attacker found all API URLs but could not forge requests because the signing key is never stored in plain text in the binary.

**How it works:**
1. The app fetches an encrypted signing key from a config API at startup
2. The app decrypts it using an AES key embedded in the compiled native code
3. Each request is signed with HMAC-SHA256 using the decrypted key
4. The server verifies the signature before processing any request

**Why this is hard to break:**
- The HMAC signing key is never in the binary — it's downloaded encrypted at runtime
- The AES decryption key IS in the binary, but it's in compiled Dart/native code (not a string literal), making it extremely hard to extract via simple string search
- An attacker needs MITM proxy (capturing live traffic from the running app) or ARM64 disassembly to bypass this
- Even if one key is compromised, the server can rotate the encrypted key without an app update

```dart
// Client: encrypted HMAC signing (Flutter/Dart)
import 'dart:convert';
import 'package:crypto/crypto.dart';
import 'package:pointycastle/block/aes.dart';

class RequestSigner {
  late String _signingKey;
  late String _authKey;

  /// Fetch and decrypt the signing key from the config API
  Future<void> initialize(String appId, String version) async {
    final response = await http.get(Uri.parse(
      'https://your-config-api.com/config?app_id=$appId&version=$version',
    ));
    final config = jsonDecode(response.body);
    final encryptedKeys = config['payload']['encrypted_keys'];

    // AES key is compiled into the native code (not a string literal)
    // Use a constant that's computed/obfuscated, not a plain string
    _signingKey = _decryptAES(encryptedKeys, _getCompiledAESKey());
    _authKey = config['payload']['auth_key'];
  }

  /// Sign a request with HMAC-SHA256
  Map<String, String> sign(String body, String path) {
    final ts = DateTime.now().millisecondsSinceEpoch.toString();
    final signatureInput = [body, _authKey, ts, path].join('_');
    final hmac = Hmac(sha256, utf8.encode(_signingKey));
    final signature = hmac.convert(utf8.encode(signatureInput)).toString();
    return {
      'authorization': _authKey,
      'ts': ts,
      'rs': signature,
    };
  }
}
```

```javascript
// Server: verify encrypted HMAC signatures
const crypto = require('crypto');

// The signing key is known only to the config API and the backend
const SIGNING_KEY = process.env.HMAC_SIGNING_KEY;
const AUTH_KEY = process.env.API_AUTH_KEY;

app.use('/api/*', (req, res, next) => {
  const authKey = req.headers['authorization'];
  const ts = req.headers['ts'];
  const rs = req.headers['rs'];

  // Validate auth key
  if (authKey !== AUTH_KEY) {
    return res.status(401).json({ error: 'Invalid authentication headers' });
  }

  // Reject stale requests (5 minute window)
  if (Math.abs(Date.now() - parseInt(ts)) > 5 * 60 * 1000) {
    return res.status(401).json({ error: 'Request expired' });
  }

  // Verify HMAC signature
  const signatureInput = [JSON.stringify(req.body), authKey, ts, req.path].join('_');
  const expected = crypto
    .createHmac('sha256', SIGNING_KEY)
    .update(signatureInput)
    .digest('hex');

  if (rs !== expected) {
    return res.status(401).json({ error: 'Invalid authentication headers' });
  }

  next();
});
```

```javascript
// Config API: serve encrypted signing keys
app.get('/config', (req, res) => {
  const { app_id, version } = req.query;

  // AES encrypt the signing key — only the app can decrypt it
  const encrypted = aesEncrypt(
    process.env.HMAC_SIGNING_KEY,
    process.env.AES_KEY_FOR_APP // must match the key compiled into the app
  );

  res.json({
    payload: {
      auth_key: process.env.API_AUTH_KEY,
      encrypted_keys: encrypted,
    }
  });
});
```

**Key design principles:**
- The signing key NEVER appears as a plain string in the app binary
- The AES decryption key should be computed/obfuscated in native code, not stored as a literal
- Use different signing keys per app version so compromised old versions can be revoked
- The server returns a generic "Invalid authentication headers" for ALL auth failures (don't leak which check failed)
- Rotate the encrypted signing key periodically via the config API (no app update needed)

### What to check for:
- Is request signing implemented? (if not, any decompiled APK can call your API with curl)
- Is the signing secret a plain string in the binary? (Level 1 — extractable with `strings`)
- Is the signing secret encrypted and decrypted at runtime? (Level 2 — much harder to extract)
- Does the server return the same error for all auth failures? (prevents attackers from narrowing down what's wrong)
- Can the signing key be rotated without an app update? (config API pattern)


## Content Scraping Prevention

Even with proper auth and entitlement checks, a paying user (or someone with a stolen/shared account) can still scrape all content. Defense in depth:

### Rate limiting on content endpoints:
```javascript
// Different rate limits for different endpoint types
const contentLimiter = rateLimit({
  windowMs: 60 * 1000,       // 1 minute
  max: 10,                    // 10 lesson fetches per minute (normal use: 1-2)
  message: 'Too many requests',
});

const catalogLimiter = rateLimit({
  windowMs: 60 * 60 * 1000,  // 1 hour
  max: 5,                     // listing all guides is infrequent
});

app.use('/api/lessons/:id', contentLimiter);
app.use('/api/guides', catalogLimiter);
```

### Access pattern monitoring:
```javascript
// Log and flag suspicious patterns
async function checkAccessPattern(userId, contentId) {
  const recentAccesses = await redis.lrange(`access:${userId}`, 0, -1);
  const uniqueLessons = new Set(recentAccesses).size;
  const timeWindow = Date.now() - parseInt(recentAccesses[recentAccesses.length - 1] || '0');

  // Flag: more than 20 unique lessons in 10 minutes
  if (uniqueLessons > 20 && timeWindow < 10 * 60 * 1000) {
    await flagAccount(userId, 'bulk_scraping_suspected');
    // Optionally: start returning degraded content or require re-auth
  }

  await redis.lpush(`access:${userId}`, `${contentId}:${Date.now()}`);
  await redis.ltrim(`access:${userId}`, 0, 99); // keep last 100
}
```

### What to check for:
- Are content endpoints rate-limited separately from general API limits?
- Is there monitoring for bulk access patterns? (many unique pieces of content in a short window)
- Does the app return full content in a single response, or paginate/stream it?
- Could a single paying account extract the entire catalog?


## Content Watermarking

If content does get scraped, invisible watermarks let you trace the leak back to the account that did it.

### Text watermarking techniques:
- **Zero-width characters**: Insert invisible Unicode characters (zero-width space, zero-width joiner) that encode the user ID
- **Synonym substitution**: Swap words with synonyms in a pattern that encodes the user ID (e.g., "use" vs "utilize", "start" vs "begin")
- **Whitespace variation**: Vary the number of spaces or line breaks in ways invisible to readers

```javascript
// Simple zero-width character watermark
function watermarkText(text, userId) {
  const binary = userId.charCodeAt(0).toString(2).padStart(8, '0');
  const zwChars = binary
    .split('')
    .map(bit => bit === '1' ? '\u200B' : '\u200C') // zero-width space vs joiner
    .join('');
  // Insert after first paragraph
  return text.replace(/\n/, `${zwChars}\n`);
}
```

### What to check for:
- Is any form of content watermarking in place?
- Can scraped content be traced back to the account that extracted it?
- Are there canary/honeypot content items that only appear via API (not in the app UI)?


## Mobile Bundle Security

Everything in an APK (Android) or IPA (iOS) is extractable. This is not theoretical — tools like jadx (Android) and Hopper/class-dump (iOS) make decompilation trivial.

### What's always extractable from a mobile bundle:
- **API endpoint paths** — Retrofit annotations (native Android), Dio base URLs (Flutter), Alamofire routes (iOS). In Flutter, `strings libapp.so | grep https://` extracts every URL in seconds.
- **Client IDs and API keys** — Any string constant compiled into the binary.
- **Firebase configuration** — API key, project ID, storage bucket, app ID from `res/values/strings.xml`.
- **Third-party service keys** — Adjust, AppsFlyer, Iterable, Facebook, Smartlook, analytics, push notification keys.
- **Base URLs** — Every server your app talks to, including staging/preprod environments if URLs are compiled in.
- **SSL pin hashes** — The exact certificate hash, though this is only useful for MITM, not direct API calls.
- **Auth flow details** — Login request/response structure, token storage patterns, method names.
- **Content structure** — Data model classes reveal the exact JSON schema of every API response.

### What's NOT easily extractable (strong defenses):
- **AES encryption keys** compiled as computed values in Dart AOT code (not string literals) — requires ARM64 disassembly
- **Runtime-fetched secrets** that are downloaded encrypted and decrypted in native code
- **Server-side logic** — the backend's entitlement checks, rate limits, and business rules

### Split APKs provide zero security:
Modern Android uses split APKs (base + ABI + density + language). The native code (`libapp.so`) is in the ABI split. This adds no security — XAPK bundles are freely available from APKPure, APKMirror, and the Play Store itself via `adb`.

### Web companion apps are a major leak vector:
If your mobile app has a companion web app (onboarding, payment, admin), the JavaScript bundles expose:
- Backend API domains and subdomains (easily found via `grep -oE 'https://[^"]+' bundle.js`)
- API keys and auth tokens hardcoded in the JS
- The exact request signing implementation (HMAC functions visible in source)
- All client-side API endpoint paths

**Defense:** Use server-side rendering for sensitive operations. Keep API keys in server-side environment variables only. If using Nuxt/Next, use server routes (`/api/*`) for anything that touches secrets.

### What SSL pinning does and doesn't do:
| Protects against | Does NOT protect against |
|-----------------|------------------------|
| MITM proxy (Charles, mitmproxy) intercepting traffic | Direct API calls from curl/Python/Postman |
| Network-level eavesdropping | Attacker who decompiled the APK and knows the endpoints |
| Modified DNS/routing | Automated scraping scripts |

SSL pinning is implemented in the app's HTTP client (OkHttp, Alamofire, Dio). When an attacker calls your API directly, the app's HTTP client isn't involved — the pin is never checked.

### What to check for:
- Are API keys, client IDs, or third-party service keys hardcoded in the app bundle?
- Is SSL pinning the only API protection? (it shouldn't be — add device attestation + request signing)
- Are there server-side checks that requests come from the actual app? (attestation, encrypted HMAC signing)
- Could someone decompile the APK, read the API URLs, and call every endpoint from curl?
- Does the app have a companion web app? Are its JS bundles exposing backend infrastructure?
- Are staging/preprod URLs compiled into the production binary? (they often are and may have weaker security)
- Does the app use encrypted request signing (Level 2 HMAC)? This is the strongest pattern we've seen.
