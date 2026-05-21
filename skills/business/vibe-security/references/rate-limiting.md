# Rate Limiting & Abuse Prevention

## Where Rate Limiting Is Required

Every one of these endpoints needs rate limiting. AI assistants almost never add it:

- **Auth endpoints** — login, register, password reset, OTP verification, magic link. Without limits, attackers can brute-force passwords or enumerate accounts.
- **AI API calls** — Any endpoint that calls OpenAI, Anthropic, or similar. A single user can drain your entire monthly budget in minutes.
- **Email / SMS sending** — Attackers can use your app as a spam relay.
- **File processing** — Upload, resize, convert. CPU-intensive operations without limits enable denial-of-service.
- **Webhook-like endpoints** — Anything accepting external input at scale.

## Don't Store Rate Limits in Public Tables

If rate limit counters live in a Supabase public table, users can reset their own counters via the REST API. Use:

- **Upstash Redis** — Serverless Redis with built-in rate limiting primitives
- **Private schema table** — Not exposed via PostgREST
- **Middleware-level limiting** — At the edge or API gateway
- **In-memory stores** — For single-server deployments (Redis for multi-server)

## Combine Per-IP and Per-User Limiting

- IP-only limits are defeated by rotating IPs (trivial with VPNs or botnets)
- User-only limits are defeated by creating new accounts
- Use both together for effective protection

## Billing Protection

- Set billing alerts on every cloud provider (AWS, GCP, Vercel, etc.)
- Set **hard spending caps** on AI API providers (OpenAI, Anthropic)
- Use per-user usage quotas with hard limits, not just soft warnings
- Monitor for anomalous usage patterns (sudden spikes, requests at odd hours)


## LLM Token Budget Enforcement (Critical for AI Apps)

Even paying premium users can bankrupt you if they (or a bot using their account) send thousands of AI requests. A single GPT-4 conversation can cost $0.50+ — multiply by a bot doing 1000 requests/hour and you're losing $500/hour on one account.

**The rule: Every AI request must check a budget before calling the LLM. No exceptions — not even for premium users.**

### Server-side token budget pattern (Cloud Functions / backend):

**Hard cost caps:** $1/day and $5/week per user. No exceptions — not free, not premium, not admin. If a user or bot hits the cap, silently stop processing their AI requests. No error messages, no explanations — the app just returns a graceful empty/fallback response. The admin panel gets an alert.

```javascript
// Cost rates per 1M tokens (update when pricing changes)
// Primary models: Gemini Flash-Lite for text, Nano Banana 2 for images
const COST_PER_1M_TOKENS = {
  // Text models
  'gemini-flash-lite':  { input: 0.10, output: 0.40 },   // cheapest text
  'gpt-4o':             { input: 2.50, output: 10.00 },
  'gpt-4o-mini':        { input: 0.15, output: 0.60 },
  'claude-sonnet':      { input: 3.00, output: 15.00 },
  // Image generation (Nano Banana 2 / gemini-3.1-flash-image-preview)
  'nano-banana-2':      { input: 0.50, outputPerImage: 0.0672 },
};

function estimateCost(model, inputTokens, outputTokens, imageCount = 0) {
  const rates = COST_PER_1M_TOKENS[model];
  if (!rates) throw new Error(`Unknown model: ${model}`);
  let cost = (inputTokens / 1_000_000) * rates.input;
  if (rates.outputPerImage) {
    cost += imageCount * rates.outputPerImage; // image gen: fixed cost per image
  } else {
    cost += (outputTokens / 1_000_000) * rates.output; // text: cost per token
  }
  return cost;
}

const COST_CAPS = {
  daily:  1.00,  // $1/day hard cap — ALL users
  weekly: 5.00,  // $5/week hard cap — ALL users
};


// Cloud Function: AI chat endpoint with cost-based budget enforcement
exports.aiChat = onCall(async (request) => {
  const userId = request.auth?.uid;
  if (!userId) throw new HttpsError('unauthenticated', 'Login required');

  // 1. Get current cost usage
  const usageDoc = await db.collection('usage').doc(userId).get();
  const usage = usageDoc.data() || {
    cost_today: 0, cost_this_week: 0,
    requests_today: 0, last_daily_reset: null, last_weekly_reset: null,
  };

  // 2. Reset counters on new day/week
  const today = new Date().toISOString().split('T')[0];
  const weekStart = getWeekStart(new Date()); // Monday of current week
  if (usage.last_daily_reset !== today) {
    usage.cost_today = 0;
    usage.requests_today = 0;
  }
  if (usage.last_weekly_reset !== weekStart) {
    usage.cost_this_week = 0;
  }

  // 3. CHECK COST CAPS — soft bounce if exceeded
  if (usage.cost_today >= COST_CAPS.daily || usage.cost_this_week >= COST_CAPS.weekly) {
    // SOFT BOUNCE: return a graceful fallback, NOT an error
    // The user sees nothing alarming — the app just doesn't produce a response
    // Admin panel gets alerted
    await alertAdmin(userId, 'cost_cap_reached', {
      cost_today: usage.cost_today,
      cost_this_week: usage.cost_this_week,
      cap_hit: usage.cost_today >= COST_CAPS.daily ? 'daily' : 'weekly',
    });
    return { response: null, status: 'unavailable' };
    // Client handles null response gracefully (e.g., "Try again later" or just no response)
  }

  // 4. Estimate cost BEFORE calling the API
  const model = request.data.model || 'gpt-4o-mini';
  const estimatedInputTokens = estimateTokenCount(request.data.message);
  const estimatedCost = (estimatedInputTokens / 1000) * COST_PER_1K_TOKENS[model].input
    + (500 / 1000) * COST_PER_1K_TOKENS[model].output; // assume ~500 output tokens

  if (usage.cost_today + estimatedCost > COST_CAPS.daily) {
    await alertAdmin(userId, 'cost_cap_would_exceed', { estimated: estimatedCost });
    return { response: null, status: 'unavailable' };
  }

  // 5. Call the LLM
  const response = await callLLM(model, request.data.message);
  const actualTokens = response.usage;

  // 6. Calculate actual cost
  const actualCost =
    (actualTokens.prompt_tokens / 1000) * COST_PER_1K_TOKENS[model].input +
    (actualTokens.completion_tokens / 1000) * COST_PER_1K_TOKENS[model].output;

  // 7. Update usage counters (atomic)
  await db.collection('usage').doc(userId).set({
    cost_today: FieldValue.increment(actualCost),
    cost_this_week: FieldValue.increment(actualCost),
    tokens_today: FieldValue.increment(actualTokens.total_tokens),
    requests_today: FieldValue.increment(1),
    last_daily_reset: today,
    last_weekly_reset: weekStart,
    last_request: FieldValue.serverTimestamp(),
    last_model: model,
  }, { merge: true });

  // 8. Alert admin if approaching cap (80% threshold)
  if (usage.cost_today + actualCost > COST_CAPS.daily * 0.8) {
    await alertAdmin(userId, 'approaching_daily_cap', {
      cost_today: usage.cost_today + actualCost,
      cap: COST_CAPS.daily,
    });
  }

  return { response: response.choices[0].message.content };
});


// Admin alert function — writes to admin_alerts collection
async function alertAdmin(userId, alertType, data) {
  await db.collection('admin_alerts').add({
    userId,
    alertType,
    data,
    timestamp: FieldValue.serverTimestamp(),
    resolved: false,
  });
}
```

### Client-side handling (Flutter — soft bounce, no error shown):

```dart
// The client should NEVER show "rate limited" or "budget exceeded" to the user.
// Instead, handle null/unavailable responses gracefully.

Future<String?> sendAiMessage(String message) async {
  final result = await cloudFunctions.httpsCallable('aiChat').call({
    'message': message,
    'model': selectedModel,
  });

  final data = result.data as Map<String, dynamic>;

  // Soft bounce: if response is null, just don't show anything
  // No error toast, no "limit reached" banner — just silence
  if (data['response'] == null || data['status'] == 'unavailable') {
    return null; // caller handles null by not adding a message to the chat
  }

  return data['response'] as String;
}
```

### Admin panel alert display:

```javascript
// Admin panel: query alerts for the dashboard
const alerts = await db.collection('admin_alerts')
  .where('resolved', '==', false)
  .orderBy('timestamp', 'desc')
  .limit(50)
  .get();

// Show: userId, alertType, cost_today, cost_this_week, timestamp
// Admin can investigate and optionally ban/restrict the account
```

### Firestore rules for usage collection:

```javascript
// Users can READ their usage (to show in UI) but NEVER write to it
match /usage/{userId} {
  allow read: if request.auth.uid == userId;
  allow write: if false; // Only Cloud Functions can write
}
```

### What to check for:
- Is there a `usage/{userId}` collection tracking per-user cost in dollars (not just tokens)?
- Are usage counters incremented server-side (Cloud Functions), not client-side?
- Can a user reset their own usage counters? (Firestore rule: `allow write: if false`)
- Is there a hard **cost cap** ($1/day, $5/week) that silently stops AI requests?
- Is cost estimated BEFORE calling the LLM API (prevents single expensive request from exceeding cap)?
- Do ALL users have limits — free, premium, and pro? (no unlimited tier)
- Does the client handle budget-exceeded responses with a **soft bounce** (no error message, just graceful silence)?
- Does the admin panel receive alerts when users hit caps?
- Is there a global spending cap on the AI API provider dashboard (last line of defense)?
- Are cost-per-token rates defined server-side and updated when model pricing changes?

## Implementation Pattern

```typescript
// Example: rate limiting with Upstash Redis
import { Ratelimit } from '@upstash/ratelimit';
import { Redis } from '@upstash/redis';

const ratelimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(10, '1 m'), // 10 requests per minute
});

export async function POST(request: Request) {
  const ip = request.headers.get('x-forwarded-for') ?? '127.0.0.1';
  const { success } = await ratelimit.limit(ip);
  if (!success) {
    return new Response('Too many requests', { status: 429 });
  }
  // ... handle request
}
```
