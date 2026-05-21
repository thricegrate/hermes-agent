# Pricing Psychology for Mobile Subscriptions

## The Anchoring Effect

The first price a user sees becomes their reference point. All subsequent prices are evaluated relative to that anchor.

### How to Apply Anchoring on a Paywall

**Rule: Always show the most expensive option first.**

When the user sees "$9.99/week" first, the "$99.99/year" (~$1.92/week) feels like an 81% discount. Without the anchor, $99.99/year feels expensive on its own.

**Visual hierarchy for a 3-tier paywall:**

```
Position 1 (top):     Weekly  - $9.99/week    [anchor]
Position 2 (middle):  Monthly - $29.99/month  [decoy]
Position 3 (bottom):  Annual  - $99.99/year   [target] ← "BEST VALUE" badge
```

The annual plan should be:
- Pre-selected (radio button or highlight already active)
- Labeled "Best Value" or "Most Popular"
- Show the per-week breakdown: "$1.92/week"
- Show the savings: "Save 81% vs weekly"

---

## The Decoy Effect (Asymmetric Dominance)

A third option that is clearly worse than one option but not the other pushes users toward the "dominant" choice.

### 3-Tier Decoy Structure

| Tier | Price | Annual Equivalent | Per Week | Role |
|------|-------|-------------------|----------|------|
| Weekly | $9.99/wk | $519.48/yr | $9.99 | Anchor (makes everything look cheap) |
| Monthly | $29.99/mo | $359.88/yr | $7.50 | Decoy (clearly worse than annual) |
| Annual | $99.99/yr | $99.99/yr | $1.92 | Target (the plan you want them to pick) |

**Why monthly is the decoy:**
- It is more expensive per week than annual ($7.50 vs $1.92)
- It offers no benefit over annual (same features, same content)
- It exists only to make the jump from monthly to annual feel obvious
- Users compare monthly to annual and think "why would I pay 3.6x more?"

### 2-Tier Alternative (Simpler)

If 3 tiers feel cluttered, use 2 tiers with strong anchoring:

| Tier | Price | Per Week | Display |
|------|-------|----------|---------|
| Monthly | $14.99/mo | $3.75 | Show first |
| Annual | $79.99/yr | $1.54 | "Save 59%" badge, pre-selected |

---

## Trial Length Optimization

### The Data (Based on RevenueCat Aggregated Benchmarks)

**3-Day Trial:**
- Trial start rate: 15-25% of paywall viewers
- Trial-to-paid: 8-12%
- 30-day retention of converts: 55-65%
- Best for: utility apps, impulse-driven categories
- Risk: not enough time to build habit; high post-trial churn

**7-Day Trial:**
- Trial start rate: 12-20% of paywall viewers
- Trial-to-paid: 5-9%
- 30-day retention of converts: 70-80%
- Best for: daily-use apps, learning, fitness, productivity
- Sweet spot: long enough to form habit, short enough to maintain urgency

**14-Day Trial:**
- Trial start rate: 10-15% of paywall viewers
- Trial-to-paid: 3-6%
- 30-day retention of converts: 75-85%
- Best for: complex products requiring extensive onboarding
- Risk: users forget they signed up; requires re-engagement emails at day 10-12

**30-Day Trial:**
- Trial start rate: 8-12% of paywall viewers
- Trial-to-paid: 2-4%
- 30-day retention of converts: 80-88%
- Best for: B2B SaaS, enterprise tools
- Risk: very high drop-off; only viable with high ARPU

### Net Revenue Analysis (Per 1,000 Trial Starts)

| Trial Length | Converts | 90-Day Retention | Active Paid at 90 Days | Revenue (Annual @ $99.99) |
|-------------|----------|------------------|----------------------|--------------------------|
| 3-day | 100 (10%) | 60% | 60 | $6,000 |
| 7-day | 70 (7%) | 75% | 53 | $5,250 |
| 14-day | 45 (4.5%) | 80% | 36 | $3,600 |

At first glance, 3-day wins. But factor in:
- 7-day converts have 25% higher LTV (lower churn months 2-6)
- 7-day trial users who don't convert have higher reactivation rates (they formed more habit)
- At 6 months, 7-day trial cohorts typically generate 15-25% more cumulative revenue

**Recommendation for daily learning apps: 7-day trial.**

---

## Price Point Psychology

### Charm Pricing

Prices ending in .99 outperform round numbers by 8-15% in mobile subscriptions. $9.99 converts better than $10.00. This is well-established and should always be used.

### Price Thresholds

Key psychological barriers in subscription pricing:

| Threshold | Annual | Monthly | Weekly |
|-----------|--------|---------|--------|
| Impulse zone | <$29.99 | <$4.99 | <$1.99 |
| Considered purchase | $29.99-$99.99 | $4.99-$14.99 | $1.99-$6.99 |
| Premium tier | $99.99-$199.99 | $14.99-$29.99 | $6.99-$12.99 |
| Enterprise/luxury | >$199.99 | >$29.99 | >$12.99 |

For a learning app targeting broad consumer market: stay in the "considered purchase" zone. $99.99/year or $79.99/year for annual; $9.99-$14.99/month for monthly.

### "Less Than" Comparisons

Always reframe the price in terms of something the user already spends money on without thinking:

| Price Point | Comparison |
|------------|------------|
| $1.92/week | "Less than one coffee" |
| $0.27/day | "Less than a piece of gum" |
| $8.33/month | "Less than one lunch" |
| $99.99/year | "Less than a single college textbook" |

### Introductory Pricing

First-time subscriber discounts that work:

| Offer | Conversion Lift | Revenue Impact |
|-------|----------------|----------------|
| 50% off first month | +30-50% trial starts | Negative month 1, positive month 3+ |
| 50% off first year | +20-35% trial starts | Break even at month 8 |
| First month free (then full price) | +40-60% trial starts | High churn at month 2 |
| $0.99 first month | +35-50% trial starts | Moderate churn, best net revenue |

**Best intro offer for learning apps:** $0.99 first month, then $9.99/month or $99.99/year. The micro-commitment of $0.99 filters out zero-intent users while keeping the barrier extremely low.

---

## Comparison Tables on Paywall

### Format That Converts

```
Feature              Free          Premium
-----------------------------------------
Daily lessons        1/day         Unlimited
AI tools             2 basic       All 10+
Certificates         --            Included
Progress analytics   Basic         Advanced
Streak protection    --            1 free/week
Ads                  Yes           None
Community            View only     Full access
```

**Design rules:**
- Use checkmarks (green) and X marks (red/gray) for binary features
- Bold the features that are premium-only
- Keep to 5-8 rows maximum (more causes decision fatigue)
- Place the comparison table ABOVE the pricing tiers, so the user understands the value before seeing the cost

---

## A/B Tests to Run

### High-Impact Tests (Run These First)

1. **Trial length**: 3-day vs 7-day (measure trial-to-paid AND 90-day LTV)
2. **Number of tiers**: 2-tier vs 3-tier (measure annual plan selection rate)
3. **Pre-selected tier**: Annual pre-selected vs no pre-selection (measure conversion rate)
4. **Price point**: $79.99/yr vs $99.99/yr vs $119.99/yr (measure revenue per paywall view)

### Medium-Impact Tests

5. **Paywall trigger**: After lesson 1 vs after lesson limit vs after day 3
6. **Social proof**: With reviews vs without reviews
7. **Comparison table**: Present vs absent
8. **CTA copy**: "Start Free Trial" vs "Try Premium Free" vs "Unlock All Lessons"

### Sample Size Requirements

For subscription A/B tests, you need larger samples than web conversion tests because:
- Conversion rates are lower (5-10% vs 20-40%)
- Revenue impact takes weeks to measure
- Minimum: 1,000 paywall views per variant for trial start rate
- Recommended: 5,000+ per variant for trial-to-paid measurement
- Duration: run for at least 2 full billing cycles (60 days for monthly)
