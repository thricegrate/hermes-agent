# Pre-Launch Economics Validation

Run these 3 calculations BEFORE any creative production begins. If the numbers don't work at the unit economics level, fix the offer before building the content system.

---

## Calculation 1: Maximum Rational Content Investment

**Question:** What is the most you should spend per month on content production?

```
Inputs:
  LTV (average lifetime value per customer):     $[A]
  Target CAC (max spend per acquired customer):   $[B]
  Organic conversion rate (clicks to customers):  [C]%
  Content-to-click ratio (posts per 1,000 clicks): [D] posts

Calculation:
  Revenue per click = LTV x Conversion Rate = $[A] x [C]% = $[E]
  Customers from 1,000 clicks = 1,000 x [C]% = [F] customers
  Max monthly budget = [F] x $[B] = $[G]

  Your content production cost must sit comfortably below $[G]
  with margin for variance between expected and actual conversion.
```

**Example:**
- LTV: $240, Target CAC: $40, Conversion rate: 4%, Content-to-click ratio: 200 posts per 1,000 clicks
- Revenue per click: $240 x 4% = $9.60
- Customers from 1,000 clicks: 40
- Max monthly budget: 40 x $40 = **$1,600/month**

If your tool subscriptions + production time exceed $1,600/month, the offer needs repositioning before content starts.

---

## Calculation 2: Cold Traffic Offer Fit Check

Organic AI UGC traffic is cold traffic. It arrives with emotional resonance from the content but without the purchase intent that warm or search traffic carries. Cold traffic converts most reliably on offers with these characteristics:

**Checklist:**

- [ ] **Price point: $30-150 for first purchase** (with upsell/subscription contributing to LTV). Below $30 = hard to justify content investment. Above $150 = too much friction for cold traffic without a nurture sequence.
- [ ] **Specific, concrete, demonstrable transformation** communicable in 15-45 seconds. If you can't explain the transformation in one sentence, cold traffic won't convert.
- [ ] **Unique mechanism** that explains why previous attempts failed and why this approach addresses the root cause. Without a mechanism, you're just another product in a crowded category.
- [ ] **Low purchase friction** -- available immediately online, minimal steps between decision and completed transaction. Every additional step loses 20-40% of remaining traffic.

**If any answer is "no":**
- Route cold traffic through a quiz funnel with email capture and nurture sequence instead of a direct product page
- This is a funnel architecture decision, not an offer problem
- See `quiz-funnel` for the conversion mechanism that makes higher-price or higher-friction offers viable on cold traffic

---

## Calculation 3: Revenue Target Reverse Calculator

Understand the exact content volume your offer requires to hit a specific revenue target.

```
Inputs:
  Revenue target:                    $[TARGET]
  Average order value (AOV):         $[AOV]
  Funnel conversion rate:            [CVR]%
  Average clicks per content piece:  [CPC]

Calculation:
  Purchases needed = $[TARGET] / $[AOV]
  Clicks needed = Purchases / [CVR]%
  Content pieces needed = Clicks / [CPC]
```

**Example scenarios for $100K revenue:**

| AOV | Funnel Type | Conversion Rate | Clicks Needed | Content Pieces Needed |
|-----|-------------|-----------------|---------------|----------------------|
| $85 | Product page (2%) | 2% | 58,824 | 19,608 |
| $85 | Quiz funnel (6%) | 6% | 19,608 | 6,536 |
| $150 | Quiz + email (8%) | 8% | 8,333 | 2,778 |
| $250 | Quiz + email + nurture (10%) | 10% | 4,000 | 1,333 |

**The pattern:** Higher AOV + more sophisticated funnel architecture = dramatically lower content volume needed. This is why the quiz funnel and email sequence layers are not optional enhancements -- they're the architecture that makes $100K achievable at a content volume a real operation can sustain.

---

## Scale Decision Threshold

Once the campaign is live, these 3 criteria must ALL be met before increasing production investment:

### Criterion 1: Revenue Consistency
**4 consecutive weeks** of revenue without a week-over-week decline greater than 15%.

Why 4 weeks? Shorter periods can be skewed by viral outliers or seasonal effects. 4 weeks shows the baseline system works predictably.

### Criterion 2: Quiz Conversion Validation
Quiz funnel conversion rate **above 5%** (recommendation-to-purchase) on a minimum of **500 completions**.

Why 500? Below 500, statistical noise can make a 3% funnel look like 7%. 500 completions provides enough data to trust the rate.

### Criterion 3: Creative Validation
At least **3 avatar and hook combinations** validated as consistent performers across multiple accounts.

Why 3? A campaign dependent on a single winning creative is fragile. 3 combinations means the system has learned what works and can reliably produce more.

**All 3 must be met.** A campaign that meets 2 of 3 has an unsolved problem that scaling will amplify rather than resolve.

---

## Weekly Performance Benchmark

Once live, calculate the weekly benchmark that tells you if you're on track:

```
Monthly revenue target / 4 = Weekly revenue target
Weekly revenue target / revenue per click = Weekly clicks required
Weekly clicks required / CTR = Weekly views required
Weekly views required / views per content piece = Content pieces required per week
```

**Diagnosing misses:**
- Hitting views but missing clicks? -> **Hook problem** (content isn't compelling action)
- Hitting clicks but missing revenue? -> **Funnel problem** (quiz or product page isn't converting)
- Missing views entirely? -> **Distribution problem** (account authority, posting frequency, or algorithmic suppression)

**North star metric: Revenue per piece of content posted.** Track weekly. Increasing = system is learning. Flat or declining = specific layer needs intervention.

---

## LTV Maximization During Launch (Bustamante Playbook)

Source: Bustamante 6-Figure Launch Playbook ($195.9K from 302 units at $800).

Three bolt-ons that added $40,000+ to a single launch with zero additional marketing effort:

### VIP Tier (3.1x Base Price)
- Base offer: $800. VIP tier: $2,500.
- VIP included more exclusive/hands-on version with closer team access.
- 12 out of 302 buyers upgraded = 4% VIP conversion = $30,000 additional revenue.
- Present on the sales page alongside the core offer. Not a separate launch.

### Community Free Trial (Recurring Revenue Pipeline)
- $99/mo Skool community offered as a free trial for the bootcamp duration.
- 138 out of ~230 eligible customers took the trial = 60% uptake.
- If 30% convert to paid after trial: ~$4,100/mo MRR from a single launch.
- Trial was offered post-purchase (not as an incentive to buy).

### Two-Pay Option (Friction Reducer)
- Split $800 into 2 installments.
- Only 14% chose 2-pay (86% paid in full).
- Reduces barrier for price-sensitive buyers without significantly impacting cash flow.
- Outstanding payments from 2-pay: $10,400.

**Lesson:** Design your offer stack with at least one upsell tier (3-5x base) and a recurring trial. These don't require separate marketing. Present them alongside the core offer. Even small conversion rates compound into meaningful revenue.

For the full launch email system that drove these results, see `newsletter-automator/references/bustamante-launch-playbook.md`.

---

## Integration

- **Run Step 0 before:** `product-offer` Step 1 (Select Pricing Tier). If the numbers don't work, repositioning happens before creative production begins.
- **Calculation 3 informs:** `ugc-production` daily content volume targets
- **Scale thresholds connect to:** `quiz-funnel` Step 8 (Measure and Iterate) and `cro-funnel` (ongoing optimization)
- **Weekly benchmarks feed:** `ads-meta` campaign management and `analytics-tracking` event tracking setup
