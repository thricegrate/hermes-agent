# Money Models: Tactical Play Implementation

> [Source: $100M Money Models -- based on online research. Verify/expand with book.]

For strategic overview and coaching diagnostics, see `coach/references/money-models.md`.
This file covers **how to implement** each of the 15 named plays when designing offers.

## Table of Contents
1. [30-Day Payback Calculator](#30-day-payback-calculator)
2. [Attraction Plays (5)](#attraction-plays)
3. [Upsell Plays (4)](#upsell-plays)
4. [Downsell Plays (3)](#downsell-plays)
5. [Continuity Plays (3)](#continuity-plays)
6. [Play Selection Matrix](#play-selection-matrix)

---

## 30-Day Payback Calculator

Before designing offers, calculate whether the money model works:

```
INPUTS:
  Customer Acquisition Cost (CAC): $___
  Attraction Offer Revenue (Day 1): $___
  Upsell Revenue (Day 1-7): $___
  Downsell Recovery Revenue (Day 7-14): $___
  Continuity Revenue (Day 1-30): $___

CALCULATION:
  30-Day Revenue Per Customer = Attraction + Upsell + Downsell + Continuity
  30-Day Profit Per Customer = 30-Day Revenue - CAC - COGS
  Payback Ratio = 30-Day Profit / CAC

TARGETS:
  Payback Ratio >= 1.0: Break-even (sustainable but not scalable fast)
  Payback Ratio >= 2.0: Healthy (funds next customer acquisition)
  Payback Ratio >= 3.0: Aggressive scaling possible

IF RATIO < 1.0:
  Option A: Reduce CAC (better targeting, organic, referrals)
  Option B: Add/improve upsell offers (most immediate lever)
  Option C: Add continuity (most valuable long-term lever)
  Option D: Raise attraction offer price (test carefully)
```

---

## Attraction Plays

### Play 1: Win Your Money Back

**Definition:** Customer pays upfront for a challenge or program. If they hit a measurable goal, they get their money back as store credit (not cash refund) toward the next purchase.

**Mechanics:**
1. Define a clear, measurable goal with a deadline (e.g., "Lose 10 lbs in 30 days")
2. Set the price high enough to create commitment ($200-$1,000 range)
3. Outcome A: Customer hits goal --> they get store credit toward your core offer (upsell happens automatically)
4. Outcome B: Customer misses goal --> you keep the revenue. They still got value from the attempt.
5. Either way, you're cash-flow positive from day one.

**Best for:** Programs with measurable outcomes, fitness, coaching, skill-building, challenges.

**Economics example:**
```
Challenge price: $500
COGS (delivery): $50
Success rate: 60%

Per 100 customers:
  Revenue: 100 x $500 = $50,000
  COGS: 100 x $50 = $5,000
  60 succeed: get $500 credit toward $997 core offer (40% convert = 24 sales = $23,928)
  40 fail: $500 stays as revenue
  Day 1 cash: $50,000 - $5,000 = $45,000
  30-day total: $45,000 + $23,928 = $68,928
```

**Implementation checklist:**
- [ ] Define measurable success criteria
- [ ] Set challenge price (aim for $200-$1,000)
- [ ] Design the challenge content/program
- [ ] Build tracking mechanism for goal completion
- [ ] Create store credit / upsell path for winners
- [ ] Set up the upsell offer that credit applies to

### Play 2: Giveaways

**Definition:** Give away something genuinely valuable at $0. Not a PDF checklist. Something that would sell if you priced it.

**Mechanics:**
1. Choose something from your product ecosystem that has real standalone value
2. Gate it behind email/contact capture
3. Deliver immediately (no drip, no "check your email in 24 hours")
4. The giveaway experience introduces them to your methodology/brand
5. Follow up with attraction offer within 48 hours

**Best for:** List building, audience growth, top-of-funnel, product launches.

**Implementation checklist:**
- [ ] Select giveaway (tool, mini-course, template pack, audit)
- [ ] Ensure it delivers standalone value (not a teaser)
- [ ] Build landing page with email capture
- [ ] Set up instant delivery mechanism
- [ ] Create follow-up sequence (giveaway --> attraction offer)

### Play 3: Dummy Offers

**Definition:** Intentionally unprofitable offer. You LOSE money on this offer. The only purpose is to get a buyer into your ecosystem where upsells and backend make up the loss.

**Mechanics:**
1. Price below cost (even $0 with shipping, or $1 trial)
2. Acquire a BUYER, not a lead. Someone who has pulled out their credit card.
3. Immediately present upsells/OTOs to recover acquisition cost
4. Backend offers generate the real profit

**Best for:** High-LTV businesses, SaaS with strong retention, coaching/agency with high-ticket backend.

**Economics example:**
```
Dummy offer: $1 trial (7 days)
CAC: $15
Day 1 loss: -$14 per customer
OTO 1 (25% take rate at $47): +$11.75
OTO 2 (10% take rate at $27): +$2.70
Day 1 net: $0.45 (basically break-even)
Continuity conversion (40% stay at $97/mo): $38.80/mo ongoing
```

**Warning:** Only works if your upsell/continuity economics are proven. Don't run dummy offers without a tested backend.

**Implementation checklist:**
- [ ] Verify backend LTV justifies the loss
- [ ] Set dummy price ($0-$7)
- [ ] Build OTO sequence to recover CAC
- [ ] Set up continuity conversion path
- [ ] Calculate break-even threshold

### Play 4: Buy X Get Y Free

**Definition:** Purchase one product, get a complementary product free. The "free" product introduces them to your next offer category.

**Mechanics:**
1. The purchased product (X) is something they already want
2. The free product (Y) exposes them to a different product line or higher tier
3. Y should naturally lead to "I want more of this" --> which is your upsell

**Best for:** Cross-selling between product lines, expanding product awareness, e-commerce.

**Implementation checklist:**
- [ ] Identify primary product (X) that sells well
- [ ] Select complementary product (Y) from a different product line
- [ ] Ensure Y creates desire for more (leads to upsell)
- [ ] Bundle at checkout with clear messaging

### Play 5: Pay Less Now / More Later

**Definition:** Graduated pricing. Low entry, full price later. Removes the initial price objection completely.

**Mechanics:**
1. Offer a significantly reduced rate for the first period (1-3 months)
2. Price graduates to full rate automatically
3. By the time full rate kicks in, customer has experienced enough value to stay
4. Frame it as "introductory rate" not "discount"

**Best for:** Subscriptions, memberships, recurring services, SaaS.

**Economics example:**
```
Normal price: $97/mo
Intro rate: $29/mo for 3 months
Full rate: $97/mo after month 3

Revenue per customer (12 months):
  Months 1-3: $87
  Months 4-12: $873 (if they stay -- 70% retention)
  Expected 12-month value: $87 + ($873 x 0.70) = $698
  vs. no intro rate: $97 x 12 x 0.50 retention = $582
  Intro rate wins because higher initial retention.
```

**Implementation checklist:**
- [ ] Set intro rate (40-70% off normal price)
- [ ] Set intro period (1-3 months)
- [ ] Build auto-graduation into billing system
- [ ] Create "intro period ending" retention sequence (emails at day 20, 25, 28)
- [ ] Frame as "introductory rate" in all copy

---

## Upsell Plays

### Play 6: Classic Upsell

**Definition:** After they buy the solution to Problem A, reveal Problem B (which naturally follows) and sell the solution to that.

**Mechanics:**
1. Identify the NEXT problem that surfaces after solving the first one
2. Present it at the moment of maximum belief (right after purchase, or right after first result)
3. Price at 1.5-3x the initial purchase
4. The upsell must deliver standalone value

**Best for:** Sequential problems, courses with natural "what's next" progressions, service add-ons.

**Implementation checklist:**
- [ ] Map the customer's problem chain (A --> B --> C)
- [ ] Design upsell product for Problem B
- [ ] Price at 1.5-3x initial purchase
- [ ] Set trigger point (post-purchase page, post-result email, or both)

### Play 7: Menu Upsell

**Definition:** Present multiple add-on options like a restaurant menu. Consultant-style: guide them to what they need.

**The Prestige Labs 4-Step Framework:**
1. **Unsell:** Tell them what they DON'T need. ("Based on your goals, you can skip X and Y.")
2. **Prescribe:** Recommend specific items based on their situation. ("For your situation, I'd recommend A and B.")
3. **Offer A or B:** Present a choice, not a yes/no. ("Would you prefer the standard pack or the complete kit?")
4. **Make Easy:** Simplify checkout. One click. No new forms. ("I'll add it to your order. Same card?")

**Best for:** Products with natural add-ons, supplements, service businesses, checkout flows.

**Result benchmark:** Prestige Labs went from $270K to $1.6M/mo using this exact framework. Same products. Same traffic.

**Implementation checklist:**
- [ ] List all possible add-ons/upgrades
- [ ] Script the Unsell (what they DON'T need -- builds trust)
- [ ] Script the Prescribe (personalized recommendation)
- [ ] Design A/B choice (not yes/no)
- [ ] Simplify the checkout flow to one click

### Play 8: Anchor Upsell

**Definition:** Show the most expensive option first. It's not meant to sell -- it's meant to make the mid-tier feel cheap.

**Mechanics:**
1. Create 3 tiers: Premium (anchor), Standard (target), Basic
2. Show Premium first with full price prominently displayed
3. The Standard tier looks like an incredible deal by comparison
4. Basic exists as a downsell for those who still hesitate

**Best for:** Tiered products, SaaS pricing pages, service packages, coaching programs.

**Pricing ratios:**
```
Premium (anchor): $X
Standard (target): $X / 3-5 (where most sales happen)
Basic (downsell): $X / 8-10

Example: Premium $997, Standard $297, Basic $97
Most people buy Standard. The anchor did its job.
```

**Implementation checklist:**
- [ ] Design 3 tiers with clear feature differentiation
- [ ] Price anchor at 3-5x target tier
- [ ] Present anchor first in all sales materials
- [ ] Highlight target tier as "most popular" or "recommended"

### Play 9: Rollover Upsell

**Definition:** Lock the customer into their next transaction before they leave. Offer a future deal at the point of current purchase.

**Mechanics:**
1. At checkout or right after purchase, offer a deal on the NEXT purchase
2. Create urgency: "This rate is only available right now"
3. Collect payment or commitment for the future transaction
4. The customer is locked in before they can reconsider

**Best for:** Subscriptions, events, consumables, appointment-based businesses, seasonal products.

**Implementation checklist:**
- [ ] Identify the natural repurchase cycle
- [ ] Design the "next purchase" offer with urgency
- [ ] Add to post-purchase flow (checkout confirmation or thank-you page)
- [ ] Build fulfillment system for the future transaction

---

## Downsell Plays

### Play 10: Payment Plan

**Definition:** Same product, different payment structure. Never discount the core price. Spread the cost over time.

**Mechanics:**
1. Offer installments that total MORE than the one-time price (compensates for risk)
2. Frame as convenience, not discount
3. Keep the full-pay option visible as the better deal
4. Set up auto-billing for all installments

**Pricing formula:**
```
One-time: $297
Payment plan: 3 x $117 = $351 (18% premium for convenience)
                 or
Payment plan: 4 x $89 = $356 (20% premium)

NEVER: 3 x $99 = $297 (same as one-time -- no incentive to pay upfront)
```

**Implementation checklist:**
- [ ] Set payment plan at 15-25% premium over one-time
- [ ] Set up auto-billing with failed payment recovery
- [ ] Create payment plan specific email sequences
- [ ] Build dunning sequence for failed payments

### Play 11: Feature-Limited

**Definition:** Fewer features, lower price. Remove the parts they don't need rather than discounting everything.

**Mechanics:**
1. Identify which features/modules are "nice to have" vs "must have"
2. Create a stripped-down version with only the must-haves
3. Price at 40-60% of the full version
4. The feature-limited version naturally creates desire for the full version over time

**Best for:** SaaS, course bundles, service packages, membership tiers.

**Implementation checklist:**
- [ ] Audit features: rank by value to customer
- [ ] Split into "core" (must-have) and "premium" (nice-to-have)
- [ ] Price core at 40-60% of full
- [ ] Design upgrade path from limited to full

### Play 12: Free Trial

**Definition:** Full access for limited time. They experience the full value, then decide to pay.

**Mechanics:**
1. Give unrestricted access for 7-14 days
2. Require credit card upfront (increases trial-to-paid by 2-3x vs no-card trials)
3. Focus onboarding on getting them to the "aha moment" within the trial
4. Send conversion sequence starting at day 5 (for 7-day trial) or day 10 (for 14-day)

**Conversion benchmarks:**
```
No-card free trial: 5-15% conversion
Card-required free trial: 25-50% conversion
Card + strong onboarding: 40-65% conversion
```

**Implementation checklist:**
- [ ] Choose trial length (7 or 14 days)
- [ ] Require credit card at signup
- [ ] Design onboarding to hit "aha moment" in first 48 hours
- [ ] Build trial-ending email sequence (start 2-4 days before expiry)
- [ ] Set up auto-billing at trial end

---

## Continuity Plays

### Play 13: Bonus Continuity

**Definition:** Subscriber gets an exclusive bonus that goes away if they cancel. The bonus is the lock-in, not the core product.

**Mechanics:**
1. Identify something genuinely valuable that can be offered exclusively to active subscribers
2. Make it painful to lose (not just "nice to have" -- actually painful)
3. Clearly communicate what they lose on cancellation
4. Add new bonuses periodically to increase switching cost

**Best for:** Communities, memberships, subscriptions, SaaS with network effects.

**Case study:** Gym Launch added an exclusive perk for recurring members only. One-time buyers couldn't access it. Result: $16K to $380K-$1.76M/mo. Business became PE-sellable.

**Implementation checklist:**
- [ ] Identify exclusive bonus (community access, tools, content, features)
- [ ] Ensure bonus is genuinely valuable and painful to lose
- [ ] Add "you'll lose access to..." messaging in cancel flow
- [ ] Schedule periodic bonus additions (quarterly)

### Play 14: Discount Continuity

**Definition:** Subscriber saves money by committing to a longer term. The savings increase with commitment length.

**Mechanics:**
1. Offer monthly, quarterly, and annual billing options
2. Annual should be 15-25% cheaper per month than monthly
3. "Founding rate" or "locked rate" for early subscribers creates FOMO and loyalty
4. Show the savings prominently ("Save $120/yr with annual billing")

**Pricing formula:**
```
Monthly: $49/mo
Quarterly: $42/mo (save 14%, billed $126)
Annual: $39/mo (save 20%, billed $468)
Founding rate: $29/mo locked forever (limited to first 100 members)
```

**Implementation checklist:**
- [ ] Set monthly, quarterly, annual pricing with clear savings
- [ ] Consider a "founding rate" for early adopters
- [ ] Show per-month savings in all pricing displays
- [ ] Build upgrade prompts for monthly subscribers ("switch to annual and save $120")

### Play 15: Waive Fee Continuity

**Definition:** Subscriber avoids a penalty or fee by staying subscribed. Canceling costs them something beyond just losing access.

**Mechanics:**
1. Charge a setup, onboarding, or activation fee for new members
2. Waive this fee for active subscribers
3. If they cancel and want to rejoin, they pay the fee again
4. The fee should be large enough to discourage cancellation but not so large it prevents initial signup

**Best for:** Gyms, premium services, platforms with meaningful onboarding costs, SaaS with data migration.

**Implementation checklist:**
- [ ] Set activation/setup fee ($50-$500 depending on product)
- [ ] Waive fee for active subscribers
- [ ] Add "reactivation fee" messaging in cancel flow
- [ ] Consider a "pause" option instead of cancel (preserves the waiver)

---

## Play Selection Matrix

Use this to quickly identify which plays fit a given business model:

| Business Type | Best Attraction | Best Upsell | Best Downsell | Best Continuity |
|--------------|----------------|-------------|---------------|-----------------|
| **Coaching/courses** | Win Your Money Back | Classic | Payment Plan | Bonus |
| **SaaS** | Free Trial (dummy) | Anchor | Feature-Limited | Discount |
| **E-commerce** | Buy X Get Y | Menu | Payment Plan | Waive Fee |
| **Agency/services** | Giveaway (audit) | Classic | Feature-Limited | Bonus |
| **Newsletter/media** | Giveaway (tool) | Classic | Free Trial | Bonus + Discount |
| **Membership/community** | Pay Less Now | Anchor | Free Trial | Waive Fee |
| **Events/conferences** | Dummy (early bird) | Rollover | Payment Plan | Discount |
