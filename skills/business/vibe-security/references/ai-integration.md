# AI / LLM Integration Security

## API Keys Are Server-Side Only

AI API keys (OpenAI, Anthropic, Google, etc.) must never appear in client-side code. They allow unlimited API usage at your expense. A leaked key can drain thousands of dollars in minutes.

- No `NEXT_PUBLIC_OPENAI_API_KEY`
- No API keys in React Native / Expo bundles
- No API keys in client-side JavaScript

All AI API calls go through your backend. The client sends the user's message to your server; your server calls the AI API.

## Spending Caps & Per-User Token Budgets

Set hard spending caps on every AI API provider:
- OpenAI: Usage limits in dashboard
- Anthropic: Spending limits in console
- Google: Budget alerts in Cloud Console
- ElevenLabs: Usage limits per API key

**Provider-level caps are your last line of defense, not your first.** They may have lag (minutes to hours) and won't protect you from a single user draining your budget before the cap kicks in.

### Per-user budgets are mandatory:

Implement **server-side per-user usage limits** that block requests BEFORE calling the AI API:
- Track token usage per user in a server-controlled collection (Firestore `usage/{userId}`)
- Set daily/monthly caps per subscription tier (free: 2K tokens/day, premium: 50K tokens/day)
- Estimate token count BEFORE calling the API — reject oversized requests early
- Increment counters AFTER the API call with actual token usage
- **Premium users get higher limits, not unlimited access** — even a $30/month subscriber shouldn't be able to generate $500 in API costs
- Users must NEVER be able to write to their own usage collection (Firestore rule: `allow write: if false`)
- Alert on accounts reaching 80% of their daily limit

See `references/rate-limiting.md` for the complete server-side token budget pattern with code examples.

## Prompt Injection

User input must be sanitized before inclusion in prompts. Never concatenate raw user input into system prompts:

```typescript
// BAD: user can override system instructions
const prompt = `You are a helpful assistant. User says: ${userInput}`;

// BETTER: separate system and user messages
const messages = [
  { role: 'system', content: 'You are a helpful assistant.' },
  { role: 'user', content: userInput },
];
```

Even with separate messages, be aware that sophisticated prompt injection can still occur. For high-stakes applications, consider:
- Input validation and filtering
- Output validation before acting on LLM responses
- Limiting the LLM's capabilities (no tool access for user-facing chat)

## LLM Output Is Untrusted

LLM responses should be treated as untrusted user input:

- **Sanitize before rendering as HTML** — LLM output can contain script tags or event handlers
- **Never execute LLM output as code** without sandboxing
- **Validate tool/function call parameters** — if using function calling, validate all returned parameters against an allowlist and schema before executing

## Tool / Function Calling

If your application gives an LLM access to tools (database queries, API calls, file operations):
- Restrict operations to a safe allowlist
- Validate all parameters from the LLM against a schema
- Use least-privilege access (read-only where possible)
- Log all tool invocations for audit
- Never let the LLM construct raw SQL or shell commands from user input
