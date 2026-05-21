# Funnel Economics Framework

Unit economics calculations, benchmarks, and the AC "compete on economics" methodology.

---

## Unit Economics Calculations

### Customer Acquisition Cost (CAC)

```
CAC = Total Acquisition Spend / New Customers Acquired

Where Total Acquisition Spend includes:
- Paid ad spend (Meta, Google, YouTube, etc.)
- Content creation costs (freelancers, tools, time-valued)
- Software costs attributed to acquisition (email platform, landing page tools)
- Affiliate/referral payouts

For organic-only funnels:
CAC (organic) = Content creation cost / New customers from organic
```

**CAC by channel benchmarks:**

| Channel | Typical CAC Range | Notes |
|---------|------------------|-------|
| Organic social | $0-5 | Time cost often undervalued |
| SEO/content | $5-20 | Compounds over time |
| Meta Ads | $10-50 | Varies wildly by niche |
| Google Ads | $15-75 | Higher intent, higher cost |
| YouTube Ads | $8-40 | Good for education/info products |
| Affiliate/referral | $5-25 | Performance-based, lower risk |

### Lifetime Value (LTV)

```
30-Day LTV = Frontend Price + (OTO1 Price x OTO1 Take Rate) + (OTO2 Price x OTO2 Take Rate)

90-Day LTV = 30-Day LTV + (Backend Price x Backend Close Rate x % Who Reach Backend Offer)

Annual LTV = 90-Day LTV + Recurring Revenue + Repeat Purchases
```

**Example calculation (AC-style funnel):**
```
Frontend ebook:              $27
OTO 1 (video course):        $67 x 20% take rate = $13.40
OTO 2 (templates):           $37 x 8% take rate  = $2.96
------
30-Day LTV:                  $43.36

Awareness bridge converts:   15% of buyers book a call
Call show rate:              70%
Close rate:                  25%
Backend offer:               $5,000
Backend contribution:        15% x 70% x 25% x $5,000 = $131.25 per frontend buyer
------
90-Day LTV:                  $174.61
```

### LTV:CAC Ratio

```
LTV:CAC = Lifetime Value / Customer Acquisition Cost
```

| Ratio | Status | Action |
|-------|--------|--------|
| <1x | Losing money on every customer | Stop spending. Fix offer or economics. |
| 1-1.5x | Break-even zone | Acceptable IF backend exists to profit later |
| 1.5-2x | Marginal | Optimize conversion rates or add revenue layers |
| 2-3x | Healthy | Scale cautiously, reinvest in acquisition |
| 3-5x | Strong | Scale aggressively, test new channels |
| >5x | Exceptional | You're likely under-spending on acquisition |

### Payback Period

```
Payback Period = CAC / (Monthly Revenue Per Customer)

For one-time purchases:
Payback Period = 0 days (if frontend LTV > CAC)
               = Backend conversion timeline (if relying on backend to break even)
```

**Rule:** If payback period > 90 days and you don't have cash reserves, you can't scale.

---

## The AC Economics Principle

**Core idea:** Break even (or lose a little) on the frontend. Profit on the backend.

This is the fundamental insight from the Automatic Clients methodology. Most businesses try to profit on the first sale. AC businesses aim to acquire customers at break-even, knowing the real money comes from backend offers.

**Why this works:**
1. Break-even CAC means you can acquire customers indefinitely without cash flow pressure
2. Every competitor trying to profit on the frontend can't afford to spend as much as you
3. You build a buyer list (not just a subscriber list) which is 10-20x more valuable
4. Backend conversion happens naturally through value bombs and awareness bridge

**The break-even math:**
```
If frontend price = $27 and CAC = $27:
- You break even on Day 1
- Every OTO purchase is pure profit
- Every backend close is pure profit
- You can scale ad spend with zero cash flow risk

If competitor's CAC = $27 but they need profit on frontend:
- They must charge $47+ (pricing themselves out) OR
- They can only spend $15-20 on ads (you outbid them) OR
- They scale slower because every customer costs them profit margin
```

---

## "Compete on Economics" Framework

The business that can spend the most to acquire a customer wins. Period. Not the best product, not the best marketing, not the best brand. The one who can afford to pay the most per customer will always have more customers.

**How to increase what you can afford to spend:**

| Lever | Action | Impact on Economics |
|-------|--------|-------------------|
| Add OTOs | Create post-purchase upsells | Increases 30-day LTV by 30-60% |
| Add backend | Create $3K-$35K offer | Increases 90-day LTV by 3-10x |
| Improve close rate | Better sales scripts, better qualification | More backend revenue per frontend buyer |
| Improve show rate | Better reminders, better confirmation page | More opportunities to close |
| Raise frontend price | Test higher price points | Higher revenue per customer (may lower volume) |
| Improve conversion rates | Better pages, better copy | Lower effective CAC |
| Add retention/recurring | Membership, subscription, continuity | Extends LTV timeline |

**Economics advantage math:**

```
Your funnel:
  90-Day LTV: $175
  Max CAC: $175 (break-even)
  Comfortable CAC: $60 (healthy margin)

Competitor's funnel (no OTOs, no backend):
  90-Day LTV: $27
  Max CAC: $27 (break-even)
  Comfortable CAC: $15

You can outspend them 4x on the same ad auction.
At $60 CAC you're profitable. At $60 they're bankrupt.
```

---

## Conversion Velocity Benchmarks

Conversion velocity = speed from first purchase to meaningful result. The faster buyers see results, the more likely they are to buy backend, refer others, and leave testimonials.

| Funnel Type | Target First Win | What Counts as a Win |
|-------------|-----------------|---------------------|
| Template/swipe file | 24 hours | Used the template, got output |
| Mini-course (5-day) | 3-5 days | Completed a lesson, applied it |
| Challenge (5-14 day) | 7 days | Completed first challenge milestone |
| Membership/community | 14 days | First meaningful engagement or result |
| Coaching program | 30 days | First measurable business improvement |

**Velocity killers (avoid these):**
- Long onboarding before value delivery
- Complex setup required before starting
- No clear "do this first" guidance
- Theory-heavy content without action steps
- No community or support during implementation

---

## Offer Health Checklist

10-point diagnostic to determine if the funnel problem is the offer itself:

| # | Check | Red Flag |
|---|-------|----------|
| 1 | Sales page conversion rate | <0.5% with 500+ visitors |
| 2 | Refund rate | >10% within 30 days |
| 3 | OTO take rate | <10% on OTO 1 |
| 4 | Email unsubscribe rate post-purchase | >5% in first week |
| 5 | Community engagement | <20% of buyers participate |
| 6 | Course/product completion rate | <30% complete first module |
| 7 | Testimonial/review volume | Zero after 50+ customers |
| 8 | Backend call booking rate | <5% of buyers book a call |
| 9 | Price objections in emails/DMs | Majority cite price, not fit |
| 10 | Organic word-of-mouth | Zero referrals after 3+ months |

**Scoring:**
- 0-2 red flags: Funnel is the problem, not the offer. Optimize conversion.
- 3-5 red flags: Offer needs improvement. Route to `product-offer`.
- 6+ red flags: Offer is fundamentally broken. Consider rebuilding from `niche-finder`.

---

## When to Optimize Funnel vs. Fix Offer vs. Change Traffic

| Symptom | Root Cause | Fix |
|---------|-----------|-----|
| Traffic exists, nobody opts in | Lead magnet/EEC is weak | `email-sequence` |
| People opt in, nobody buys | Offer or sales page is weak | `product-offer` + `sales-page-writer` |
| People buy, nobody gets results | Product or onboarding is weak | `launch-ops` Phase 5b |
| People get results, nobody buys backend | Awareness bridge is missing/weak | `email-sequence` Steps 7-9 |
| Unit economics don't work (LTV < CAC) | Missing revenue layers | `product-offer` (OTOs) + `high-ticket-closer` (backend) |
| Good economics but low volume | Not enough traffic | `content-social` + `marketing-ads` |
| Everything works but growth is slow | Underinvesting in acquisition | Scale spend, compete on economics |
