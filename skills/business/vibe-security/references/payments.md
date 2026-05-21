# Payment Security (Stripe / In-App Purchases / Webhooks)

## Never Trust Client-Submitted Prices

The #1 payment vulnerability in vibe-coded apps: the price comes from the client. An attacker can set any amount, including $0.

```typescript
// BAD: price comes from the request body
const session = await stripe.checkout.sessions.create({
  line_items: [{
    price_data: {
      currency: 'usd',
      unit_amount: req.body.price, // attacker controls this
      product_data: { name: req.body.name },
    },
    quantity: 1,
  }],
});

// GOOD: look up the price server-side
const product = await db.products.findUnique({ where: { id: req.body.productId } });
if (!product) return new Response('Not found', { status: 404 });

const session = await stripe.checkout.sessions.create({
  line_items: [{ price: product.stripePriceId, quantity: 1 }],
});
```

Use Stripe Price IDs (created via the Stripe dashboard or API) rather than constructing prices from your database. This way, prices are defined in Stripe and can't be manipulated.

## Webhook Signature Verification

Stripe webhooks must have their signatures verified. This requires the **raw request body** — parsing the body as JSON first destroys the signature.

```typescript
// Express: webhook route MUST use express.raw() BEFORE express.json()
app.post('/webhook', express.raw({ type: 'application/json' }), (req, res) => {
  const sig = req.headers['stripe-signature'];
  const event = stripe.webhooks.constructEvent(req.body, sig, webhookSecret);
  // ... handle event
});

// Next.js App Router: use request.text(), NOT request.json()
export async function POST(request: Request) {
  const body = await request.text();
  const sig = request.headers.get('stripe-signature')!;
  const event = stripe.webhooks.constructEvent(body, sig, webhookSecret);
  // ... handle event
}
```

## Subscription Status Validation

Check subscription status **server-side on every protected request** using your database (kept in sync via webhooks). Do not rely on:
- A cached session value from login time
- A client-side flag
- A JWT claim that was set at token creation and never refreshed

Subscriptions can be cancelled, expire, or change tier at any time. Your database (updated via webhooks) is the source of truth.

## Checkout Session Metadata

Validate that checkout session metadata (user ID, plan, etc.) was set **server-side** when creating the session, not passed from the client. If metadata comes from the client, an attacker can claim to be a different user or select a different plan.

## Content Entitlement vs Payment Verification

Payment verification (webhook confirms Stripe received money) and content entitlement (user has the right to access specific content) are two separate concerns. Many apps verify payment correctly but then skip the entitlement check on content endpoints.

The pattern that gets exploited: a user pays for a subscription, the webhook updates a `subscribed: true` flag, and then every content endpoint only checks `if (user.subscribed)`. But when the subscription expires, the flag may not update in real time — or worse, the content endpoint doesn't check it at all.

Every content request needs a fresh entitlement check:

```typescript
// BAD: checks a cached flag that may be stale
async function getLesson(userId: string, lessonId: string) {
  const user = await db.users.findUnique({ where: { id: userId } });
  if (!user.isPaid) throw new Error('Not subscribed'); // flag from signup time
  return db.lessons.findUnique({ where: { id: lessonId } });
}

// GOOD: checks the actual subscription record, updated by webhooks
async function getLesson(userId: string, lessonId: string) {
  const subscription = await db.subscriptions.findFirst({
    where: { userId, status: 'active', currentPeriodEnd: { gte: new Date() } },
  });
  if (!subscription) {
    return db.lessons.findUnique({
      where: { id: lessonId },
      select: { id: true, title: true, description: true }, // preview only
    });
  }
  return db.lessons.findUnique({ where: { id: lessonId } }); // full content
}
```

## Client-Side Paywall Anti-Pattern

The most revenue-critical vulnerability for content apps: the paywall exists only in the UI. The app checks subscription status locally and shows/hides content, but the API endpoint returns full content to any authenticated user regardless of subscription.

This means anyone who can make an HTTP request (curl, Postman, a simple script) with a valid auth token gets all paid content for free. In a real-world audit, 274 paid lessons were extracted in 2 minutes from an app using this pattern.

Signs of a client-side-only paywall:
- Content endpoints don't import or reference any subscription/payment logic
- The server returns the same response for free and paid users
- Paywall logic lives exclusively in UI components (e.g., a Flutter `if (isSubscribed)` widget check)
- No server-side middleware or guard checks subscription status before content routes


## Webhook Signature Verification (ALL Providers)

Every webhook endpoint (Stripe, Beehiiv, Paddle, RevenueCat, Google Play, Apple) MUST verify the request signature. Without verification, anyone can send a fake webhook to grant themselves premium access.

This is not theoretical — in a real audit, a webhook handler was found that accepted POST requests without any signature check. An attacker could forge a webhook to set `is_pro=true` for any email.

```javascript
// BAD: accepts any POST request as a valid webhook
exports.paymentWebhook = onRequest(async (req, res) => {
  if (req.method !== "POST") return res.status(405).send("Method Not Allowed");
  const email = req.body.data.email;
  await db.collection("users").doc(email).update({ is_pro: true }); // anyone can trigger this!
  res.status(200).send("OK");
});

// GOOD: verify webhook signature before processing
exports.paymentWebhook = onRequest(async (req, res) => {
  if (req.method !== "POST") return res.status(405).send("Method Not Allowed");

  // Verify signature (example for Stripe)
  const sig = req.headers['stripe-signature'];
  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;
  let event;
  try {
    event = stripe.webhooks.constructEvent(req.rawBody, sig, webhookSecret);
  } catch (err) {
    return res.status(401).send('Invalid signature');
  }

  // Now safe to process
  // ...
});
```

### Webhook signature verification by provider:

| Provider | Header | Verification Method |
|----------|--------|-------------------|
| Stripe | `stripe-signature` | `stripe.webhooks.constructEvent(rawBody, sig, secret)` |
| Paddle | `paddle-signature` | HMAC-SHA256 of request body with webhook secret |
| Beehiiv | `x-beehiiv-signature` | HMAC-SHA256 of JSON body with webhook secret |
| RevenueCat | `Authorization: Bearer` | Compare with shared webhook auth key |
| Google Play (RTDN) | JWT in body | Verify with Google's public key |
| Apple App Store | `signedPayload` | Verify JWS with Apple's root certificate |

### What to check for:
- Does every webhook endpoint verify the request signature before processing?
- Is the webhook secret stored in environment variables / secret manager (NOT hardcoded)?
- Does the handler use the raw request body for verification (not parsed JSON)?
- Is there a test confirming unsigned webhooks are rejected?


## Client-Side Subscription Status Manipulation

Users must NEVER be able to set their own subscription status. Common vulnerability patterns:

```dart
// BAD: client writes subscription status directly to Firestore
await firestore.collection('users').doc(userId).update({
  'is_pro': true,           // user can call this directly!
  'plan': 'premium',
  'subscription_end': farFutureDate,
});

// GOOD: subscription status is set ONLY by server-side webhook handler
// Client can only READ subscription status, never WRITE it
// Firestore rule enforces this:
```

```javascript
// Firestore security rule — prevent client from modifying payment fields
match /users/{userId} {
  allow read: if request.auth.uid == userId;
  allow update: if request.auth.uid == userId
    // Users can update their profile, but NOT payment/subscription fields
    && !request.resource.data.diff(resource.data).affectedKeys()
        .hasAny(['is_pro', 'plan', 'subscription_end', 'stripe_customer_id',
                 'pro_started', 'pro_plan', 'credits', 'tokens_remaining']);
}
```

### What to check for:
- Can the client write to subscription/payment fields in the database?
- Are Firestore security rules preventing users from modifying `is_pro`, `plan`, `credits`, `tokens_remaining`?
- Is subscription status determined by webhook-updated server data, not client claims?
- If using Firebase custom claims for subscription tier, are claims set only by Cloud Functions (not client SDK)?
- Can a user downgrade their plan but keep premium access by manipulating cached state?


## In-App Purchase Receipt Verification

Mobile in-app purchases (Google Play, Apple App Store) must be verified server-side. The client receives a purchase token/receipt, but this must be validated with the store's API before granting access.

```dart
// Flutter client: after purchase, send receipt to YOUR server for verification
final purchaseDetails = await InAppPurchase.instance.buyNonConsumable(...);
// Don't grant access locally! Send to server first:
await http.post(
  Uri.parse('$backendUrl/api/verify-purchase'),
  headers: {'Authorization': 'Bearer $token'},
  body: jsonEncode({
    'receipt': purchaseDetails.verificationData.serverVerificationData,
    'productId': purchaseDetails.productID,
    'platform': Platform.isAndroid ? 'android' : 'ios',
  }),
);
// Server verifies with Google/Apple API, then updates subscription in database
```

```javascript
// Server: verify with Google Play
const { google } = require('googleapis');
const androidPublisher = google.androidpublisher('v3');

async function verifyAndroidPurchase(packageName, productId, purchaseToken) {
  const result = await androidPublisher.purchases.subscriptions.get({
    packageName,
    subscriptionId: productId,
    token: purchaseToken,
  });
  // Check result.data.paymentState, expiryTimeMillis, etc.
  return result.data;
}
```

### What to check for:
- Does the app verify purchase receipts server-side before granting premium access?
- Can a user use a fake/modified receipt to get premium access?
- Is the purchase verification endpoint protected against replay attacks (same receipt used twice)?
- Does the server check expiration dates on subscription receipts?
