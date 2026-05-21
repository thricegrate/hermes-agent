# Mobile Security (React Native / Expo / Flutter)

## APK and IPA Decompilation

Every mobile app binary can be decompiled into readable source code. This is not a theoretical risk — it's a 5-minute process with free tools:

- **Android (APK):** `jadx` converts DEX bytecode back to Java/Kotlin. Class names get obfuscated by R8/ProGuard, but string literals (API URLs, keys, Retrofit annotations) are always preserved in plain text.
- **iOS (IPA):** Hopper Disassembler or `class-dump` extracts Objective-C/Swift class structures. String constants are readable in the binary.
- **Flutter:** Dart AOT-compiled code in `libapp.so` can be analyzed with `strings`, `darter`, or `reFlutter`. API URLs are stored as string literals in the compiled binary and are trivially extractable — even without Dart-specific tools, a simple `strings libapp.so | grep https://` reveals every backend URL.

What this means: assume an attacker has read every line of your app's networking code, knows every API endpoint path, and has copied every hardcoded key. Design your server-side security with this assumption.

### Flutter-Specific Findings (from real reverse engineering)

In a real-world analysis of a production Flutter education app, every API URL was extracted from `libapp.so` in seconds:

```bash
# This is all it takes to find every backend URL in a Flutter app
python3 -c "
import re
with open('libapp.so', 'rb') as f:
    data = f.read()
for m in re.finditer(rb'https?://[a-zA-Z0-9._:/-]{5,200}', data):
    print(m.group().decode())
"
```

**What was found:** Every production, staging, and preprod backend URL; Firebase config; API paths for courses, lessons, chat, user management, and payment verification.

**What was NOT easily extractable:** AES encryption keys used for request signing — these were compiled into native code as computed values, not string literals. This is the key defense: API URLs being discoverable is acceptable if the server requires encrypted signed requests.

### Split APKs Are Not a Defense

Modern Android apps use split APKs (base + config.arm64_v8a + config.en + config.mdpi). The native Dart code (`libapp.so`) is in the ABI split, not the base APK. This adds zero security:
- XAPK bundles containing all splits are freely downloadable from APKPure, APKMirror, and similar sites
- `adb shell pm path <package>` lists all installed splits on any device with USB debugging
- All splits can be extracted and analyzed independently

### Web Companion Apps Leak Backend Infrastructure

If your mobile app has a companion web app (onboarding funnel, payment page, admin panel), the JavaScript bundles are a goldmine for attackers. In a real analysis, a Nuxt.js web app's JS bundles revealed:
- Every backend API domain and subdomain
- API keys for analytics, config, and location services
- The HMAC signing pattern (function implementation visible in JS)
- All API endpoint paths used by the web app

**Defense:** Web companion apps should use server-side rendering for sensitive operations. API keys should be in environment variables accessed only by server routes, never bundled into client JS. If using Nuxt/Next, use server routes (`/api/*`) and never import secrets into client-side code.

## SSL Pinning Is Not API Security

SSL certificate pinning prevents man-in-the-middle attacks (someone intercepting traffic between the app and your server). It does **not** prevent direct API calls. When an attacker calls your API from curl or Python, the app's HTTP client isn't involved — the pin is never checked. The server has no way to tell the difference.

SSL pinning is worth having (it stops casual MITM via Charles Proxy), but it is not a substitute for server-side request verification. See `references/content-protection.md` for device attestation and request signing patterns that actually verify request origin.

## No Secrets in the JavaScript Bundle

All API keys and secrets in the JavaScript bundle are extractable — even with Hermes bytecode compilation. The bundle is a file on the device that can be read, decompiled, and searched for strings.

- `react-native-config` values are baked into the bundle at build time. They are not secret.
- `EXPO_PUBLIC_` values are baked into the bundle at build time. They are not secret.
- Environment variables set via `eas.json` or `app.config.js` that end up in the JS bundle are not secret.

The only safe approach: **use a backend proxy** for all third-party API calls that require secret keys. The mobile app calls your server; your server calls the third-party API with the key.

```typescript
// BAD: API key in the mobile app
const response = await fetch('https://api.openai.com/v1/chat/completions', {
  headers: { 'Authorization': `Bearer ${OPENAI_API_KEY}` }
});

// GOOD: call your own backend, which holds the key
const response = await fetch('https://your-api.com/ai/chat', {
  headers: { 'Authorization': `Bearer ${userSessionToken}` },
  body: JSON.stringify({ message: userInput }),
});
```

## Secure Token Storage

- **Use `expo-secure-store`** (Expo) or **`react-native-keychain`** (bare React Native) for auth tokens.
- **Never use `AsyncStorage`** — it's unencrypted plaintext on disk. On a rooted/jailbroken device, tokens are trivially readable.

```typescript
// BAD: plaintext on disk
await AsyncStorage.setItem('authToken', token);

// GOOD: encrypted in device keychain
await SecureStore.setItemAsync('authToken', token);
```

## Deep Link Security

Deep links (`myapp://path?param=value`) can be triggered by any app or website. They are an attack surface:

- **Validate and sanitize all parameters.** Never trust deep link input.
- **Never include sensitive data in deep link URLs** (tokens, passwords, user IDs that grant access).
- **Don't perform destructive actions** directly from deep link parameters without user confirmation.

## Biometric Authentication

A simple boolean success check from biometric auth (`isAuthenticated = true`) can be hooked with tools like Frida on a jailbroken device. Proper biometric auth must use **cryptographic verification**:

1. Server sends a challenge (random nonce)
2. App signs the challenge with a hardware-backed key (Secure Enclave / Strongbox)
3. Server verifies the signature

This way, even if the biometric check is bypassed, the attacker can't forge the cryptographic signature.

## Firebase Configuration Exposure

Firebase-backed apps expose their configuration in the APK's `res/values/strings.xml`:
- `google_api_key` — Firebase API key (allows Firebase Auth REST API calls)
- `google_app_id` — Firebase App ID
- `google_storage_bucket` — Firebase Storage bucket name
- `project_id` — Firebase project ID
- `gcm_defaultSenderId` — FCM sender ID
- `facebook_client_token` — Facebook SDK token

**What an attacker can do with these:**
- Create accounts via Firebase Auth REST API (`identitytoolkit.googleapis.com`)
- Send password reset emails to any email address
- Check if an email is registered (email enumeration, if not disabled)
- List Firestore collections (if security rules allow)
- Access Firebase Storage (if rules allow authenticated users)

**Defenses:**
- **Firebase App Check** — restricts which apps can access your Firebase services
- **Firestore Security Rules** — never allow `read: if request.auth != null` on content collections (this means any authenticated user, including attackers who created a free account, can read everything)
- **Firebase Storage Security Rules** — use per-user paths and require specific claims
- **Disable email enumeration** in Firebase Auth settings
- **Use a custom backend** for content delivery instead of Firestore direct access — this way Firebase auth is just the identity layer, and your backend enforces entitlement

## Device Attestation

The real solution to verifying that requests come from your actual app (not curl, Postman, or a scraping script). Device attestation uses the device's secure hardware to generate a cryptographic proof of app legitimacy.

- **Google Play Integrity API** — Verifies the app is a legitimate Play Store install running on a genuine device. Returns a signed verdict the server can verify.
- **Apple App Attest** — Uses the Secure Enclave to generate a key pair tied to your app. The server verifies attestation before granting access.
- **Firebase App Check** — Cross-platform wrapper that works with Play Integrity (Android) and App Attest (iOS). Simplest to implement for Firebase-backed apps.

For implementation details and code examples, see `references/content-protection.md`.

## Security Tier Checklist (for content/subscription apps)

From weakest to strongest, based on real reverse engineering attempts:

| Tier | Defense | Stops | Defeated by |
|------|---------|-------|-------------|
| 0 | No protection (Bearer token only) | Nobody | curl after decompilation |
| 1 | SSL pinning | MITM proxy (casual) | Direct API calls from curl |
| 2 | Basic HMAC signing (hardcoded secret) | Casual attackers | `strings` on binary to find secret |
| 3 | Device attestation (Play Integrity / App Check) | Curl/Postman/scripts | Rooted device / Frida |
| 4 | Encrypted HMAC signing (AES-encrypted key from config API) | Decompilation + curl | MITM proxy or ARM64 disassembly |
| 5 | All of the above + content entitlement checks + rate limiting + watermarking | Most attackers | Determined attacker with paid subscription + MITM |

**Minimum recommended for paid content apps: Tier 4** (encrypted request signing + server-side entitlement checks). This is what stopped a real content extraction attempt.
