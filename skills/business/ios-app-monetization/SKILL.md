---
name: ios-app-monetization
description: "Use for iOS app monetization, subscription funnels, before/after ad workflows, and app store optimization strategies."
metadata:
---

# iOS App Monetization

End-to-end playbook for launching and monetizing an iOS app at $10K MRR with the lazy approach: ads + paywall + nap. No UGC creators. No influencers. No organic.

The 5-mode loop:

1. **App Launch Strategy**: study what's working, sell to a core human desire, add a viral feature
2. **Paywall & Subscription Design**: pricing, retention offers, Apple compliance
3. **AI Ad Creation**: before/after format with Z-Image + SwapTok, 10-12 variants per hour
4. **TikTok Smart+ Campaign Management**: $50/day start, +30% every 3 days, US-only, optimize for subscriptions
5. **Metrics & Optimization**: CPI < $2, CTR > 1%, CPA < LTV; cheat codes for free money

Each mode below routes to its reference file and templates.

## Before you start

Confirm you have:

- An iOS app concept (existing or planned)
- $300-1000 in ad budget for testing (the TikTok ad credit will match this; see [references/metrics-and-cheat-codes.md](references/metrics-and-cheat-codes.md))
- A TikTok Ads account
- An Apple Developer account
- Time to study 3-5 winning apps in your niche before writing a line of code

For CC-specific application (the 3 Minute AI app context, project at `C:\Users\thric\Claude Code\3minuteai`), see [references/3-minute-ai-application.md](references/3-minute-ai-application.md).

## Mode 1: App Launch Strategy

The single biggest lever in app launches is picking the right concept. Most failed apps fail at this stage, not at execution.

The core checklist:

- **Study 3-5 apps printing money** in your niche. Download them. Screenshot their onboarding. Watch their TikTok ads. Understand WHY they work.
- **Sell to a core human desire** (attractiveness, health, wealth, sex, status, intelligence, identity, fear). "Am I attractive?" beats "Am I productive?" every time.
- **Add a viral feature** that produces a "reveal moment" you can screen-record in 5 seconds (face rating, height predictor, food scan, etc.).

Take the blueprint, improve the execution. Do NOT directly clone (Apple rejects, original founder reports, you get pulled).

Full breakdown: [references/app-strategy.md](references/app-strategy.md). Worked competitor study template: [templates/competitor-study.md](templates/competitor-study.md).

## Mode 2: Paywall & Subscription Design

This is where most apps leak revenue.

The pricing that prints money right now:

- $12.99/week
- $59.99/year (annual)
- $44.99/year retention offer (shown ONLY when user tries to cancel)

The paywall:

- HARD paywall at the end of onboarding. No trial. No freemium.
- Users must pay to satisfy the desire the app sold them
- The retention offer fires inside the cancellation flow, never as a popup

Apple rejects retention offers shown the wrong way. Get the flow right and Apple approves every time.

Full breakdown: [references/paywall-and-pricing.md](references/paywall-and-pricing.md). Apple compliance gotchas (what gets banned and how to avoid it): [references/apple-compliance.md](references/apple-compliance.md).

For the broader paywall framework (trial mechanics, social proof, A/B testing) see `skills/paywall-optimization/SKILL.md` if it exists in the project. The reference here adds the iOS-specific subscription pricing and Apple-specific retention offer flow.

## Mode 3: AI Ad Creation (Before/After)

The highest-converting ad format for iOS apps right now is dead simple: before / after.

Show someone BEFORE using the app. Show the result AFTER. That's the entire ad.

The 4-step workflow that produces 10-12 variants per hour:

1. Record yourself doing the "action" the app performs
2. Generate "before" and "after" face/body images with Z-Image Turbo (LoRA) at fal.ai
3. Use SwapTok to merge the AI face onto your video (both before and after)
4. Edit in CapCut or TikTok Studio with trending music and screenshots

Full workflow with prompts and tool links: [references/before-after-ad-workflow.md](references/before-after-ad-workflow.md). Variant generation prompt: [templates/ad-batch-prompt.md](templates/ad-batch-prompt.md).

For component-level variation at scale (when one before/after ad performs well, spin 10+ variants from it), the parallel pattern lives in `skills/ugc-production/templates/variation-from-winner-reel.md`.

For ad creative principles that apply across the whole stack (hooks, voice, anti-AI tells), see `skills/video-scriptwriter/references/anti-ai-script-tells.md`.

## Mode 4: TikTok Smart+ Campaign Management

The campaign mechanics:

- **Campaign type**: TikTok Smart+
- **Optimize for**: subscription/purchase events, NOT installs
- **Starting budget**: $50/day
- **Geography**: USA only at start
- **Test window**: 2-3 days before concluding results

Scaling rules:

- Target metrics: CPI < $2.00, CTR > 1.00%, CPA < LTV (LTV typically lands around $30/paying user with the pricing above)
- When metrics hit: scale by +30% every 3 days max (faster scaling breaks the TikTok pixel)
- When metrics miss: kill the ad, make a new creative, test again. Do NOT touch campaign settings. The creative is almost always the problem.
- One winning ad can carry the business for months. Spin 10-12 variants of the winner. Same hook, different person/story.

Full breakdown: [references/tiktok-smartplus-campaigns.md](references/tiktok-smartplus-campaigns.md).

## Mode 5: Metrics, Optimization, and Cheat Codes

Daily metric check (under 60 seconds):

- CPI for each ad
- CTR for each ad
- CPA vs LTV
- Decisions: scale, hold, or kill

The free money most founders miss:

- **TikTok ad credit**: matches first $6,000 in spend. Auto-applies on new accounts. $6K becomes $12K in distribution.
- **Apple Small Business Program**: cuts the Apple fee from 30% to 15%. Free to apply.
- **Cashflow planning**: Apple payouts take 45 days. Plan accordingly. If you have $1K, split it across 2 months.

Full breakdown: [references/metrics-and-cheat-codes.md](references/metrics-and-cheat-codes.md). Launch checklist that ties the 5 modes together: [templates/launch-checklist.md](templates/launch-checklist.md).

## Voice rules

When generating ad copy or paywall text, follow the project voice rules:

- No em-dashes (`rules/no-em-dashes.md`)
- Coffee shop rule: every line sounds like talking to a friend (`SOUL.md`)
- Short sentences, simple words
- No "obsessed", "game-changing", "transformational"
- For ad scripts specifically, follow the direct-response system in `skills/video-scriptwriter/references/direct-response-voice-system.md`

Final gate: route all outward-facing ad copy through `humanizer` and `content-review` before delivery.

## The TLDR loop

1. Study what's working in your niche (3-5 apps, screenshots, TikTok ad library)
2. Build an improved version with a viral feature targeting a core human desire
3. Price at $12.99/week + $59.99/year + $44.99 retention offer
4. Run the before/after AI ad workflow to produce 10-12 variants
5. Launch a TikTok Smart+ campaign at $50/day, US-only, optimize for subscriptions
6. Find one winning ad (CPI < $2, CTR > 1%, CPA < LTV)
7. Scale it +30% every 3 days
8. Spin variants of the winner
9. Print cash in your sleep

## Cross-references

- Voice gate before delivery: `skills/humanizer/SKILL.md`, `skills/content-review/SKILL.md`
- Direct-response ad script voice rules: `skills/video-scriptwriter/references/direct-response-voice-system.md`
- Component-level ad variation at scale (Winner Variation Pipeline): `skills/ugc-production/templates/variation-from-winner-reel.md`
- App UI/UX (separate concern): `skills/app-design/SKILL.md`
- Paywall optimization (broader framework, if available): `skills/paywall-optimization/SKILL.md`
- Onboarding flow (the steps before the paywall): `skills/onboarding-ux/SKILL.md` (if available)
- App Store listing optimization: `skills/app-store-optimization/SKILL.md` (if available)
- Push notification retention (post-paywall mechanics): `skills/push-notification-strategy/SKILL.md` (if available)
- Funnel economics: `skills/cro-funnel/SKILL.md`
- Project context (3 Minute AI app, audience profile): see [references/3-minute-ai-application.md](references/3-minute-ai-application.md)