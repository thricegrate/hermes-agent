# TikTok Smart+ Campaign Management

The campaign mechanics that work for iOS app subscriptions on TikTok in 2026. Smart+ is TikTok's automated campaign type that handles audience targeting, bid optimization, and creative testing automatically. For iOS app subscriptions, Smart+ outperforms manual campaigns at most budget levels because the algorithm has more data than any operator does.

## Why Smart+ for iOS apps

Smart+ campaigns work especially well for iOS apps because:

- The algorithm optimizes for the conversion event (subscription) directly, not just clicks
- The targeting expansion automatically finds audience segments the operator would not have tested manually
- The creative testing runs in parallel inside one campaign instead of needing separate ad sets
- The reporting is cleaner (per-creative performance is what you act on, not per-audience)

For founders running ads-only with no UGC creators, Smart+ is the right default. Manual campaigns require more operator time to manage; Smart+ trades flexibility for hands-off scaling.

## Campaign setup

The exact configuration that works:

| Setting | Value | Why |
|---|---|---|
| Campaign type | Smart+ | Automated optimization |
| Optimization event | Subscription / Purchase | NOT installs (installs don't pay) |
| Geography | USA only | Highest LTV market for iOS |
| Starting daily budget | $50/day | Enough data for the algorithm to optimize |
| Bid strategy | Lowest cost (default) | Smart+ handles this |
| Creative count | 4-6 ads to start | Enough variety, not so much that data thins |

### Why $50/day starting budget

Below $30/day, the algorithm does not get enough conversion data to optimize. Above $100/day with no winner yet, you are burning cash without learning faster.

$50/day across 4-6 ads gives you ~$10/ad/day. Over 2-3 days that is $20-30 of spend per ad, which is enough signal to read CTR and CPI. CPA needs another 2-3 days because conversions lag impressions.

### Why optimize for subscriptions, not installs

Installs are a vanity metric. People install apps and never pay. The TikTok algorithm will happily find you cheap installs from users who never convert.

Optimize for the subscription event (or "Purchase" event in TikTok terms, mapped to your in-app subscription via the iOS App Events SDK). The algorithm will then find users who have a high probability of subscribing, not just installing.

Setting this up requires:
1. iOS App Events SDK installed in the app
2. The subscription event firing correctly when the user completes the paywall
3. The TikTok pixel verifying the event in TikTok Ads Manager

Test this BEFORE running any ads. If the subscription event is not firing, you will optimize for nothing and waste budget.

### Why USA only at start

US iOS users have the highest LTV per paid subscriber. Most of the pricing playbook ($12.99/week + $59.99/year) is calibrated to US willingness to pay.

Expand to other countries (UK, Canada, Australia first) only after the US campaign is profitable. Different markets convert at different rates. The signal you get from a multi-country campaign at the start is muddier than a US-only signal.

## The 2-3 day test window

Run any new ad batch for 2-3 days before concluding results. The algorithm needs time to find audiences. Pulling ads after 24 hours kills them before they have a chance to find their pocket.

What "2-3 days" actually means:

- 48-72 hours of continuous spend
- At least $100-150 spent per ad
- At least 5-10 conversions per ad (or strong signal that none are coming)

If a creative has not produced any conversions in 72 hours of spend, kill it. If a creative has produced 5+ conversions and CPA looks good, scale it.

## The 3 metrics that matter

After the test window, only three metrics drive decisions:

| Metric | Target | What it tells you |
|---|---|---|
| CPI (Cost Per Install) | < $2.00 | Hook and creative are working |
| CTR (Click-Through Rate) | > 1.00% | Ad is stopping the scroll |
| CPA (Cost Per Acquisition / subscription) | < LTV | Unit economics work |

LTV with the standard pricing ($12.99/week + $59.99/year + $44.99 retention offer) typically lands around $30/paying user. CPA needs to be under $30 to be profitable.

If CPA is $25 and LTV is $30, profit is $5/subscriber. Across 1,000 subscribers, $5,000 in profit. Across 10,000, $50,000.

### What to do at each metric outcome

| CPI | CTR | CPA | Action |
|---|---|---|---|
| < $2 | > 1% | < LTV | SCALE. Increase budget by +30% every 3 days. |
| > $2 | < 1% | (any) | KILL. The creative is the problem. New ad. |
| < $2 | > 1% | > LTV | INVESTIGATE. Paywall conversion is the issue, not the ad. Test paywall changes. |
| < $2 | < 1% | (any) | INVESTIGATE. Ad gets clicks but the hook is weak. Rewrite hook. |
| > $2 | > 1% | (any) | INVESTIGATE. Hook is fine but the creative is not converting clicks. Rewrite body of the ad. |

## Scaling rules

Once an ad hits the target metrics, scale by +30% every 3 days maximum.

### Why +30% and not more

The TikTok pixel needs time to re-stabilize after a budget change. Scaling too fast (+50%, +100%) breaks the pixel's optimization model and CPI/CPA spike.

Real example:
- Day 1: $50/day, CPA $25
- Day 4: scale to $65/day (+30%), CPA $26
- Day 7: scale to $85/day (+30%), CPA $24
- Day 10: scale to $110/day (+30%), CPA $27

Steady scaling preserves performance. Aggressive scaling burns the campaign.

### When to stop scaling

Watch for:
- CPA creeping up by more than 20% from baseline
- CTR dropping by more than 30% from baseline
- Daily conversions plateauing despite budget increase

These signal the audience is getting saturated. Stop scaling. Either:
1. Make more variants of the winning ad (same hook, different person/story)
2. Expand to a second country (UK, Canada, Australia)
3. Test a new creative angle

## Variant production at scale

You only need ONE winning creative. One. That is the whole game. Find it and throw money at it.

Once you have a winner:

1. **Spin 10-12 variants of it** using the before/after AI workflow ([before-after-ad-workflow.md](before-after-ad-workflow.md))
2. **Same hook structure, different person or story** in each variant
3. **Run all variants alongside the original winner**
4. **The strongest variants become the next round of fuel**

For component-level variation at scale (when you have multiple winners and want to multiply them), see `skills/ugc-production/templates/variation-from-winner-reel.md`.

A winning ad can carry the business for months. Spin variants. Scale slowly. Watch the metrics.

## What NOT to do

### Do not touch campaign settings when an ad is failing

When an ad is underperforming, the temptation is to change the audience, the bid, the budget. Resist.

The creative is almost always the problem. Kill the ad. Make a new creative. Test again.

Touching campaign settings just adds noise to the signal. The Smart+ algorithm is doing its job; the ad is the variable.

### Do not run multiple campaigns testing the same thing

Founders sometimes spin up 3-4 campaigns testing the same creative angle hoping to find a winner faster. This dilutes the data across campaigns and confuses the algorithm.

Run ONE campaign. Add 4-6 ads at a time. Let the algorithm decide.

### Do not optimize for installs

Even if "Subscription" event setup feels harder, do it. Optimizing for installs gives you cheap downloads and zero revenue.

### Do not run ads outside the USA at start

Test markets sequentially after US is profitable. Multi-country campaigns at the start muddy the signal.

### Do not expect immediate profitability

The first 2-4 weeks are testing. Most ads will lose money. The goal of week 1-2 is to find a winner, not to be profitable. Once you find a winner, the next 6-8 weeks of scaling is where profitability comes from.

## Campaign structure example

A worked example of the launch structure:

### Week 1
- Set up Smart+ campaign, USA only, optimize for Subscription event
- Daily budget: $50
- 4-6 ads, all variants of the before/after format from the [before-after-ad-workflow.md](before-after-ad-workflow.md)
- Run for 3 days continuous

### Day 4 review
- 1-2 ads performing at CPI < $2, CTR > 1%, CPA < $30
- Other 4 ads failing
- ACTION: kill failing ads, scale budget on winners (+30% to $65/day)

### Week 2
- Spin 8-10 variants of the winning ad (same hook, different person)
- Run alongside original winner
- Daily budget: $85/day (+30% scale)

### Week 3-4
- Continue scaling +30% every 3 days
- Watch for saturation signals
- Add UK/Canada when US plateaus

### Week 4+
- Steady $200-500/day with the winning creative + variants
- Profitable unit economics
- Begin testing new creative angles for the next winner

## TikTok ad credit (free money)

TikTok matches your first $6,000 in ad spend. This auto-applies on new TikTok Ads accounts.

The math:
- Spend $6,000 on ads
- TikTok credits $6,000 back
- You have $12,000 in distribution

This effectively refunds the entire first month or two of spend. Use it. See [metrics-and-cheat-codes.md](metrics-and-cheat-codes.md) for the full set of cheat codes.

## Cross-references

- Before/after ad creation workflow: [before-after-ad-workflow.md](before-after-ad-workflow.md)
- Metrics, cheat codes, cashflow planning: [metrics-and-cheat-codes.md](metrics-and-cheat-codes.md)
- Paywall and pricing (the conversion event the campaign optimizes for): [paywall-and-pricing.md](paywall-and-pricing.md)
- Apple compliance (subscription event setup): [apple-compliance.md](apple-compliance.md)
- Component-level ad variation at scale: `skills/ugc-production/templates/variation-from-winner-reel.md`
- Broader paid ads strategy across platforms: `skills/ads-strategy/SKILL.md`
- Ad creative principles (hooks, voice): `skills/video-scriptwriter/references/direct-response-voice-system.md`
