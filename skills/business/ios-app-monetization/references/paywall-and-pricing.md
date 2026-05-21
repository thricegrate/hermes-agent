# Paywall & Subscription Pricing

The paywall is where the money happens. Get this wrong and no amount of ad spend saves the app. Get it right and you start printing.

## The pricing that prints right now

Three numbers. Test them as the default before testing anything else.

| Tier | Price | When shown |
|---|---|---|
| Weekly | $12.99/week | Default option on the paywall |
| Annual | $59.99/year | Secondary option on the paywall |
| Retention offer | $44.99/year | ONLY shown when a user tries to cancel |

### Why these numbers work

The pricing looks high to founders who have never run paid ads. It is correct. The people clicking your ad are emotionally invested. They want the answer the viral feature promised. They will pay for it.

People who would not pay $12.99/week are the same people who would not pay $4.99/week. They are not your customer. The price is a filter.

## Paywall structure

The structure that maximizes conversion:

1. **Hard paywall at the end of onboarding.** No trial. No freemium.
2. **The paywall sits AFTER the viral feature reveal.** The user has seen what the app can do. They want more. They have to pay.
3. **Two-tier display.** Weekly is default selected. Annual has a small "save 88%" or similar badge.
4. **No trial offer on the main paywall.** The retention offer covers the cost-sensitive segment.

### Why hard paywall, not freemium or trial

Freemium and trial dilute the conversion signal. The user gets the reveal moment for free, then never comes back to buy. Hard paywall forces the moment of truth: do they want this enough to pay right now?

For TikTok-driven traffic specifically, hard paywall converts higher than trial because the audience came in emotionally hot from the ad. They do not need to be eased in.

## The retention offer

This is free money most founders leave on the table.

### How it works

When a user tries to cancel their subscription inside Settings, present a retention offer of $44.99/year. The flow:

1. User goes to Settings → Subscriptions → Cancel
2. Before the cancellation completes, the app shows a screen: "Wait, before you go..."
3. The retention offer appears: $44.99/year (a discount from $59.99)
4. The user can accept the discount and stay, or proceed to cancel

### Why this works

Every user you save from churning at $44.99/year is pure profit you would have otherwise lost. The math is brutal in your favor.

If you save 1 in 10 cancellation attempts at $44.99/year, the LTV math shifts meaningfully. Across thousands of subscribers, this layer compounds.

### Apple compliance for the retention offer

This is the part most founders mess up.

Apple rejects retention offers shown the wrong way. The flow that Apple approves every time:

- Retention offer appears INSIDE the cancellation flow only
- Never as a popup on app open
- Never as a banner on the main feed
- Never as an email push trying to retain

Show the retention offer any other way and Apple will reject the build.

For full Apple compliance details (rejection patterns, what gets banned, how to structure the flow), see [apple-compliance.md](apple-compliance.md).

## Onboarding flow → paywall sequence

The full sequence from app open to paywall:

1. **Splash / brand screen** (1-2 seconds)
2. **Quick personalization questions** (3-5 questions, "Are you male or female?", "What is your goal?", etc.)
3. **The viral feature** (the reveal moment, screen-recordable)
4. **The result page** (showing the user their score, prediction, scan, etc.)
5. **Soft scarcity / loading screen** (a 2-3 second "preparing your full report" beat)
6. **Hard paywall** (Weekly + Annual, no skip button)
7. **In-app experience** (only if the user pays)

The viral feature reveal happens BEFORE the paywall, intentionally. The user sees what the app does. They want more details, more variations, the full report. The paywall converts because the desire is at peak emotional pull.

### What NOT to do in onboarding

- Do not let the user skip the paywall (no "X" button in the corner; no "maybe later" link)
- Do not show the paywall before the viral feature (the user has not earned the desire yet)
- Do not collect more than 5 personalization questions (drop-off)
- Do not show prices before the reveal (they will close the app)

## Studying paywalls in winning apps

Before designing your paywall, screenshot the paywalls of:

- Cal AI (food scanning)
- UMax (face rating)
- Pray Screen (faith)
- Any app you are studying in your specific niche

Note for each:
- Where is the price displayed?
- How is the annual savings communicated?
- Is there urgency (limited-time offer)?
- What social proof is on the paywall (review counts, star ratings, testimonials)?
- Is there a "discount applied" anchor that makes the price feel like a deal?

The patterns are highly consistent. Copy the structural elements. Customize the design to your niche.

## A/B testing the paywall

Once the app is launched, test these in order (one at a time):

1. **Weekly price** ($9.99 vs $12.99 vs $14.99)
2. **Annual price** ($49.99 vs $59.99 vs $69.99)
3. **Retention offer trigger** (immediately on cancel attempt vs after one app close)
4. **Social proof on paywall** (review count vs testimonial vs star ratings)
5. **Anchor pricing** (showing a "regular price" struck through next to the actual price)

Do not test multiple variables at once. The signal will be impossible to read.

## Pricing for non-USA markets

The default playbook is US-only at launch. When expanding:

- Adjust prices per region using App Store Connect's price tier system
- Tier 13 ($12.99) is the standard weekly anchor
- The retention offer should always be a percentage discount from the annual, not a flat number
- Test carefully. Some markets convert at higher prices than the US (UK, Canada, Australia). Some convert lower (most of EU non-UK).

## What gets banned and how to avoid it

Quick summary (full details in [apple-compliance.md](apple-compliance.md)):

- ❌ Retention offer shown outside the cancellation flow → REJECTED
- ❌ Hidden subscription terms → REJECTED
- ❌ Auto-renewal not disclosed clearly → REJECTED
- ❌ Misleading paywall copy ("free trial" when there is no trial) → REJECTED
- ❌ Cloning another app's design directly → REJECTED + reported

Apple's review process is consistent. Follow the rules and approval is fast. Break the rules and the appeal process burns weeks of cashflow.

## Cross-references

- Apple compliance details: [apple-compliance.md](apple-compliance.md)
- App strategy (concept selection that feeds the paywall): [app-strategy.md](app-strategy.md)
- Onboarding UX (the steps before the paywall): `skills/onboarding-ux/SKILL.md` (if available in project)
- Broader paywall optimization framework (multi-platform): `skills/paywall-optimization/SKILL.md` (if available in project)
- Funnel economics (CAC/LTV math that confirms the pricing works): `skills/cro-funnel/SKILL.md`
- Hormozi product offer principles (value stacking, price psychology): `skills/product-offer/SKILL.md`
