---
name: cro-funnel
description: |
  Diagnoses funnel bottlenecks and prescribes fixes for digital product sales funnels based on
  7 core metrics including unit economics (CAC/LTV). Covers conversion optimization, economics
  diagnosis, offer health, and the "compete on economics" framework. Use when user wants to
  optimize their funnel, improve conversion rates, diagnose why sales are low, analyze funnel
  performance, troubleshoot their marketing, check unit economics, or understand CAC/LTV.
---

# Funnel Doctor

## Prerequisites

- A live funnel (product launched, receiving some traffic)
- The user's 7 core funnel metrics (any combination available):
  1. Traffic (organic content impressions)
  2. Opt-in rate (newsletter/EEC conversion %)
  3. Email CTR (click-through rate to product landing page)
  4. Landing page visitors (# who visit sales page)
  5. Purchase rate (% who buy)
  6. CAC (Customer Acquisition Cost: total ad spend + content costs / new customers)
  7. LTV (Lifetime Value: average revenue per customer across all purchases including OTOs and backend)
- See `references/economics-framework.md` for unit economics calculations and benchmarks

## Workflow

### Step 1: Collect the 7 Core Metrics

Ask the user to provide whatever data they have:

```
## Funnel Metrics

1. Traffic: [Monthly impressions across platforms]
2. Opt-in Rate: [% of visitors who join email list]
3. Email CTR: [% of subscribers who click product link in emails]
4. Landing Page Visitors: [Monthly visitors to sales page]
5. Purchase Rate: [% of landing page visitors who buy]
6. CAC: [Total acquisition cost per customer - ad spend + content costs / customers]
7. LTV: [Average total revenue per customer - frontend + OTOs + backend over 90 days]
```

If they don't have exact numbers, ask for estimates or ranges. For CAC/LTV, even rough estimates are valuable.

### Step 2: Benchmark Against Standards

| Metric | Poor | Average | Good | Great |
|--------|------|---------|------|-------|
| Opt-in Rate | <1% | 1-3% | 3-5% | >5% |
| Email Open Rate | <15% | 15-25% | 25-35% | >35% |
| Email CTR | <1% | 1-3% | 3-5% | >5% |
| Landing Page Conversion | <0.5% | 0.5-2% | 2-5% | >5% |

### Step 3: Identify the Bottleneck

The weakest metric relative to benchmarks is the bottleneck. Fix the bottleneck first - improving anything else has less impact.

**Bottleneck hierarchy (most common first):**
1. Not enough traffic (most common problem)
2. Low opt-in rate (traffic exists but nobody joins list)
3. Low email engagement (people on list but not clicking)
4. Low landing page conversion (people visit but don't buy)

### Step 4: Diagnose Root Causes

#### If Traffic is the bottleneck:
- **Not posting enough:** Minimum 5x/week on primary platform
- **Wrong platform:** Audience isn't where you're posting
- **No CTA:** Content exists but doesn't drive to email list
- **Content quality:** Posts don't stop the scroll
- **Prescription:** Increase posting frequency, study what performs in your niche, add CTAs to every post. Re-run `content-social` with adjustments.

#### If Opt-in Rate is the bottleneck:
- **Weak lead magnet:** EEC or opt-in offer isn't compelling enough. Diagnostic: Is the lead magnet one of the 3 types that actually work? (1) Reveals a problem they didn't know they had, (2) Gives a trial of the actual result, (3) Delivers one automated step of the full process. If it's a generic PDF or "request a quote" -- that's the problem. See `free-tool-strategy` for the full Hormozi lead magnet taxonomy.
- **Landing page friction:** Too many steps, confusing layout
- **Mismatched audience:** Traffic is coming but it's the wrong people
- **Prescription:** Strengthen the EEC title/promise, simplify opt-in page, audit traffic source alignment. Re-run `email-sequence` to improve EEC.

#### If Email CTR is the bottleneck:
- **Low email frequency:** Sending fewer than 1/week
- **Weak subject lines:** Low open rates indicate this
- **No product mentions:** Emails don't link to landing page
- **Wrong segment targeting:** Not using Clickers segment for objection emails
- **Prescription:** Send more emails, always include product CTA, segment and target Clickers, improve subject lines.

#### If Landing Page Conversion is the bottleneck:
- **Weak headline:** Doesn't speak to the primary pain point
- **Missing social proof:** No testimonials or results
- **Price-value disconnect:** Price feels too high for perceived value
- **Too much friction:** Checkout process is complicated
- **Missing objection handling:** FAQ doesn't address real concerns
- **UGC/social traffic mismatch:** If traffic comes from UGC reels or social content and conversion is below 1.5%, the product page may be the wrong destination entirely. The emotional momentum from the reel collapses on a transactional product page. Consider replacing with a quiz funnel. Run `quiz-funnel` to design the architecture.
- **Prescription:** Rewrite headline and problem section, add testimonials, strengthen bonus stack. Re-run `sales-page-writer` with improvements.

### Step 4b: Economics Diagnosis

After diagnosing the conversion bottleneck, assess the funnel's unit economics:

**CAC/LTV Analysis:**
```
Frontend revenue per customer:  $[price]
OTO 1 revenue (take rate x price): $[OTO1 price] x [15-25%] = $[amount]
OTO 2 revenue (take rate x price): $[OTO2 price] x [5-10%] = $[amount]
------
Total frontend LTV:              $[sum]
CAC:                              $[total spend / customers]
Frontend ROI:                     [LTV / CAC]x
Payback period:                   [days to recoup CAC]
```

**Benchmarks:**
| Metric | Danger | Acceptable | Strong |
|--------|--------|------------|--------|
| LTV:CAC Ratio | <1x (losing money) | 1-2x (break-even) | >3x (profitable) |
| Payback Period | >90 days | 30-90 days | <30 days |
| OTO 1 Take Rate | <10% | 15-20% | >25% |
| OTO 2 Take Rate | <3% | 5-8% | >10% |

**Include backend economics (if applicable):**
```
Backend close rate:              [20-30% of qualified calls]
Backend average deal size:       $[amount]
Backend LTV contribution:        $[close rate x deal size / total frontend customers]
------
Full-stack LTV:                  $[frontend LTV + backend LTV contribution]
Full-stack LTV:CAC:              [full LTV / CAC]x
```

**Conversion Velocity Assessment** (see `references/economics-framework.md` for benchmarks by funnel type):

Conversion velocity = how quickly a buyer gets their first meaningful result. Faster results lead to more testimonials, referrals, and backend conversions.

| Factor | Increases Velocity | Decreases Velocity |
|--------|-------------------|-------------------|
| Onboarding | Quick-start guide, Day 1 email | No guidance, complex setup |
| Content | Short, actionable lessons | Long theory-heavy modules |
| Support | Community, DMs, live calls | Email-only, slow responses |
| Proof | Templates, swipe files, done-for-you | "Figure it out" approach |

**Offer Diagnosis:**

Sometimes the funnel isn't the problem. The offer is. Ask:
- "Are people visiting the sales page but not buying?" -> Offer/page problem
- "Are people buying but not getting results?" -> Product/onboarding problem
- "Are people getting results but not buying backend?" -> Awareness bridge problem
- "Is nobody visiting the sales page at all?" -> Traffic/content problem

If the offer is the root cause, route to `product-offer` before optimizing the funnel.

**"Compete on Economics" Framework:**

The business that can spend the most to acquire a customer wins. If your LTV:CAC is below 2x, you can't outspend competitors on ads or content. Fix economics first:

1. **Raise LTV:** Add/improve OTOs, increase backend close rate, raise prices
2. **Lower CAC:** Improve conversion rates at each funnel stage, shift to organic traffic
3. **Extend the timeline:** A 90-day LTV that's 3x a 30-day LTV changes everything

See `references/economics-framework.md` for full calculations and examples.

### Step 4c: Hormozi Lead Nurture & Revenue Boosters

Layer these Hormozi frameworks on top of the conversion diagnosis:

- **Lead Nurture Four Pillars:** Availability, Speed, Personalization, Volume. Score each 1-10. Low speed (>5 min response time) kills conversion regardless of page quality. See `email-sequence/references/hormozi-lead-nurture.md`.

#### Response Time Impact on Booking Rate

Speed is the most underrated conversion lever. Based on 12,847+ DM conversations:

| Response Time | Booking Rate | Relative Performance |
|--------------|-------------|---------------------|
| Under 5 minutes | 41% | Baseline (best) |
| Under 30 minutes | 34% | -17% vs 5-min |
| Under 2 hours | 23% | -44% vs 5-min |
| Under 24 hours | 12% | -71% vs 5-min |
| Over 24 hours | 4% | -90% vs 5-min |

The difference between a 5-minute response and a 24-hour response is literally 10x in booking rate. Same lead, same offer, same copy. Just speed.

**Diagnosis:** If your funnel has a "lead goes cold" problem, check response time first. It's almost always the bottleneck.

#### Conversation-to-Booking Flow Benchmarks

Not all conversation flows convert equally. The sequence of messages matters more than any individual message.

| Flow | Structure | Conversion | Avg Messages |
|------|-----------|-----------|-------------|
| A (Best) | Question > Pain ack > Case study > Soft pitch > Book | 34% | 8 |
| B | Compliment > Curiosity question > Value share > Direct ask | 29% | 6 |
| C | Pattern interrupt > Pain agitation > Solution tease > CTA | 26% | 7 |
| X (Avoid) | Pitch > Objection handle > Pitch again > Give up | 4% | 12 |
| Y (Avoid) | Small talk > More small talk > Eventually pitch > Ghost | 3% | 15 |

**Key insight:** Flow A takes more messages but converts 8.5x better than Flow X. Patience in the conversation (building trust before pitching) beats aggressive selling every time.

- **Fast Cash Play System:** If revenue needs an immediate boost, run a quarterly ultra-premium promotion to your warmest segment. 7-day Push-to-Consult or 5-day Push-to-Checkout sequence. See `coach-business/references/hormozi-fast-cash.md`.
- **Belief Continuum:** Belief is a spectrum, not binary. If landing page conversion is the bottleneck, map where your traffic sits on the belief spectrum and adjust proof density accordingly. See `sales-page-writer/references/hormozi-proof-checklist.md`.

### Step 4d: Brunson Traffic Temperature + Funnel Benchmarks

Segment conversion data by traffic temperature (hot/warm/cold) and compare against Brunson's funnel-type benchmarks. See `references/brunson-frameworks.md` for temperature diagnosis, funnel hacking process, and conversion rate ranges by funnel type (tripwire, webinar, application, challenge).

### Step 4e: Kennedy Funnel Economics Check

Layer Kennedy's direct response economics on top of the Brunson diagnosis. See `references/kennedy-funnel-economics.md` for full frameworks.

**YC conversion psychology:** Kevin Hale's Conversion Psychology Pyramid (Clarify Value -> Reduce Friction -> Remove Objections -> Accelerate Action), the Three Questions every visitor asks, Friction Audit Framework, trust-building components ranked by strength, and the 5-second clarity test. Complements Brunson/Kennedy with YC's psychology-first approach. See `references/yc-hale-conversion.md`.

- [ ] Full-stack LTV calculated (frontend + OTOs + backend). Back end should be 50%+ of total revenue.
- [ ] Maximum affordable CPA determined. The business that can spend the most to acquire a customer wins.
- [ ] Follow-up sequence runs 7+ emails, including SECOND NOTICE on dead leads.
- [ ] Scarcity deployed at every funnel stage, not just the sales page.
- [ ] Message-Market-Media triangle aligned per stage (top, middle, bottom of funnel).
- [ ] Can answer 7+ of Kennedy's 10 Smart Market Diagnosis Questions.

If the economics are broken (back end is under 50% of revenue, no follow-up sequences, single-stage scarcity), fix those before optimizing conversion rates. Better economics beat better conversion rates every time.

### Step 5: Prescribe Action Plan

Output a prioritized action plan:

```
## Funnel Diagnosis Report

### Current Metrics
[User's metrics with benchmark comparison]

### Primary Bottleneck: [Metric Name]
**Severity:** [Critical / Moderate / Minor]

### Root Cause Analysis
[2-3 likely causes based on the data]

### Recommended Fixes (Priority Order)
1. [Highest-impact fix] - Expected improvement: [X%]
   - Skill to re-run: [relevant skill name]
2. [Second fix] - Expected improvement: [X%]
3. [Third fix] - Expected improvement: [X%]

### A/B Tests to Run
1. [Test description]: [Variant A] vs [Variant B]
2. [Test description]: [Variant A] vs [Variant B]

### Revenue Impact Estimate
Current: [X] sales/month at $[price] = $[revenue]/month
After fixes: [X] sales/month at $[price] = $[revenue]/month
Estimated improvement: [X]%
```

### Step 6: Recommend Next Steps

Based on the diagnosis, point the user to the right skill:
- Traffic problem -> `content-social`
- Opt-in problem -> `email-sequence` (improve EEC)
- Email CTR problem -> `email-sequence` (improve nurture/objection emails)
- Conversion problem -> `sales-page-writer` + `product-offer`
- Economics problem (LTV:CAC < 2x) -> `product-offer` (improve OTOs, pricing) + `high-ticket-closer` (add/improve backend)
- Offer problem (traffic exists but nobody buys) -> `product-offer` (redesign the offer)
- UGC/social traffic conversion problem -> `quiz-funnel` (replace product page with quiz for emotional-momentum traffic)
- Onboarding problem (buyers don't get results) -> `launch-ops` Phase 5b (fix onboarding)
- Backend conversion problem -> `email-sequence` (improve awareness bridge) + `high-ticket-closer` (improve sales process)

## Integration

- **Input:** User's funnel metrics data
- **Receives handoff from:** `launch-ops` (post go-live, ongoing optimization)
- **May trigger re-runs of:** `sales-page-writer`, `email-sequence`, `content-social`, `product-offer`, `high-ticket-closer`
- **This is the optimization loop** - run periodically after launch to continuously improve
- **Economics diagnosis** feeds back to `product-offer` for pricing/OTO improvements and `high-ticket-closer` for backend optimization
