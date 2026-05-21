---
name: vibe-security
description: "Analyze brand voice, tone, and messaging consistency across content and campaigns."
license: MIT
metadata:
  author: Chris Raroque
  version: "2.0"
---

Audit code for security vulnerabilities commonly introduced by AI code generation. These issues are prevalent in "vibe-coded" apps — projects built rapidly with AI assistance where security fundamentals get skipped.

AI assistants consistently get these patterns wrong, leading to real breaches, stolen API keys, and drained billing accounts. This skill exists to catch those mistakes before they ship.

This skill is informed by real-world reverse engineering of two production education apps:
- **App A (weak security):** 100% of paid content extracted in 30 minutes using only the APK + curl. Retrofit endpoints in plain text, Bearer token auth with no entitlement checks, public CDN content.
- **App B (strong security):** Extraction blocked by encrypted HMAC request signing. API URLs discoverable via `strings` on compiled Dart, but every request requires a signature computed from an AES-encrypted key that could not be extracted from the binary. Required MITM proxy to bypass.

The difference: App B assumed the attacker would decompile the APK and designed server-side defenses accordingly. App A assumed the APK was a black box.


## The Core Principle

Never trust the client. Every price, user ID, role, subscription status, content entitlement, feature flag, and rate limit counter must be validated or enforced server-side. If it exists only in the browser, mobile bundle, or request body, an attacker controls it.

This applies equally to content access: if your app checks subscription status in the UI but serves full paid content from the API to any authenticated user, your paywall is decorative. CDN-hosted content without signed URLs is public content, regardless of what the app UI shows. Quiz answer keys embedded in client-side JSON are public answers. Every content endpoint must verify entitlement server-side before returning the payload.

**Assume your APK/IPA is fully decompiled.** Every API URL, every hardcoded key, every string literal is readable. Design your backend as if the attacker has read your entire client source code — because they have.


## Audit Process

Examine the codebase systematically. For each step, load the relevant reference file only if the codebase uses that technology or pattern. Skip steps that aren't relevant.

1. **Secrets & Environment Variables** — Scan for hardcoded API keys, tokens, or credentials. Check for secrets exposed via client-side env var prefixes (`NEXT_PUBLIC_`, `VITE_`, `EXPO_PUBLIC_`). Verify `.env` is in `.gitignore`. See `references/secrets-and-env.md`.

2. **Database Access Control** — Check Supabase RLS policies, Firebase Security Rules, or Convex auth guards. This is the #1 source of critical vulnerabilities in vibe-coded apps. See `references/database-security.md`.

3. **Authentication & Authorization** — Validate JWT handling, middleware auth, Server Action protection, and session management. See `references/authentication.md`.

4. **Rate Limiting & Abuse Prevention** — Ensure auth endpoints, AI calls, and expensive operations have rate limits. Verify rate limit counters can't be tampered with. See `references/rate-limiting.md`.

5. **Payment Security** — Check for client-side price manipulation, webhook signature verification, and subscription status validation. See `references/payments.md`.

6. **Mobile Security & APK Hardening** — Verify secure token storage, API key protection via backend proxy, deep link validation, and resistance to APK decompilation. Check that Flutter apps don't leak API URLs in libapp.so strings, that web companion apps don't expose backend infrastructure in JS bundles, and that the app uses encrypted request signing (not just SSL pinning). See `references/mobile.md`.

7. **AI / LLM Integration** — Check for exposed AI API keys, missing usage caps, prompt injection vectors, and unsafe output rendering. See `references/ai-integration.md`.

8. **Deployment Configuration** — Verify production settings, security headers, source map exposure, and environment separation. See `references/deployment.md`.

9. **Data Access & Input Validation** — Check for SQL injection, ORM misuse, and missing input validation. See `references/data-access.md`.

10. **Content Protection & API Hardening** — Check for client-side-only paywalls, missing server-side entitlement checks on content endpoints, unauthenticated CDN content (unsigned URLs), answer keys or premium data exposed in client-side JSON, missing device attestation or request signing, absence of bulk-scraping detection on content endpoints, and lack of content watermarking. Also check for encrypted request signing (HMAC with server-distributed encrypted keys) — the strongest pattern we've seen in production apps. This is critical for any app that sells content (courses, lessons, articles, media). See `references/content-protection.md`.

If doing a partial review or generating code in a specific area, load only the relevant reference files.


## Core Instructions

- Report only genuine security issues. Do not nitpick style or non-security concerns.
- When multiple issues exist, prioritize by exploitability and real-world impact.
- If the codebase doesn't use a particular technology (e.g., no Supabase), skip that section entirely.
- When generating new code, consult the relevant reference files proactively to avoid introducing vulnerabilities in the first place.
- If you find a critical issue (exposed secrets, disabled RLS, auth bypass), flag it immediately at the top of your response — don't bury it in a long list.
- **For content/subscription apps, always check these five critical areas:**
  1. Can a user modify their own `is_pro`/`plan`/`credits` in the database? (Firestore field-level rules)
  2. Can a user call content endpoints without a valid subscription? (server-side entitlement)
  3. Can a user send unlimited AI requests that drain your API budget? (per-user token budgets)
  4. Can someone forge a payment webhook to grant themselves premium? (webhook signature verification)
  5. Can someone view another user's data by guessing document IDs? (ownership checks on every query)


## Output Format

Organize findings by severity: **Critical** → **High** → **Medium** → **Low**.

For each issue:
1. State the file and relevant line(s).
2. Name the vulnerability.
3. Explain what an attacker could do (concrete impact, not abstract risk).
4. Show a before/after code fix.

Skip areas with no issues. End with a prioritized summary.

### Example Output

#### Critical

**`lib/supabase.ts:3` — Supabase `service_role` key exposed in client bundle**

The `service_role` key bypasses all Row-Level Security. Anyone can extract it from the browser bundle and read, modify, or delete every row in your database.

```typescript
// Before
const supabase = createClient(url, process.env.NEXT_PUBLIC_SUPABASE_SERVICE_KEY!)

// After — use the anon key client-side; service_role belongs only in server-side code
const supabase = createClient(url, process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!)
```

#### High

**`app/api/checkout/route.ts:15` — Price taken from client request body**

An attacker can set any price (including $0.01) by modifying the request. Prices must be looked up server-side.

```typescript
// Before
const session = await stripe.checkout.sessions.create({
  line_items: [{ price_data: { unit_amount: req.body.price } }]
})

// After — look up the price server-side
const product = await db.products.findUnique({ where: { id: req.body.productId } })
const session = await stripe.checkout.sessions.create({
  line_items: [{ price: product.stripePriceId }]
})
```

### Summary

1. **Service role key exposed (Critical):** Anyone can bypass all database security. Rotate the key immediately and move it to server-side only.
2. **Client-controlled pricing (High):** Attackers can purchase at any price. Use server-side price lookup.


## When Generating Code

These rules also apply proactively. Before writing code that touches auth, payments, database access, API keys, or user data, consult the relevant reference file to avoid introducing the vulnerability in the first place. Prevention is better than detection.


## References

- `references/secrets-and-env.md` — API keys, tokens, environment variable configuration, and `.gitignore` rules.
- `references/database-security.md` — Supabase RLS, Firebase Security Rules, and Convex auth patterns.
- `references/authentication.md` — JWT verification, middleware, Server Actions, and session management.
- `references/rate-limiting.md` — Rate limiting strategies and abuse prevention.
- `references/payments.md` — Stripe security, webhook verification, and price validation.
- `references/mobile.md` — React Native and Expo security: secure storage, API proxy, deep links.
- `references/ai-integration.md` — LLM API key protection, usage caps, prompt injection, and output sanitization.
- `references/deployment.md` — Production configuration, security headers, and environment separation.
- `references/data-access.md` — SQL injection prevention, ORM safety, and input validation.
- `references/content-protection.md` — Server-side entitlement checks, CDN signed URLs, device attestation, request signing, scraping prevention, and content watermarking. Essential for any app selling courses, lessons, or premium content.
