# Revenue Architecture

The concrete math behind quiz funnels vs. standard product pages.

---

## Side-by-Side: Product Page vs. Quiz Funnel

**Scenario:** 8,000 monthly link-in-bio clicks from organic AI UGC content across 20 accounts. Average order value: $85.

### Standard Product Page

```
8,000 clicks
x 2% product page conversion rate
= 160 purchases/month
x $85 AOV
= $13,600/month
```

No email capture. No follow-up. No segmentation data. The 7,840 visitors who didn't buy are gone forever (unless you pay to retarget them).

### Quiz Funnel

```
8,000 clicks
x 65% quiz completion rate = 5,200 quiz completions
x 6% recommendation screen conversion = 312 purchases
x $85 AOV
= $26,520/month (from immediate quiz conversions)

Plus email capture:
5,200 quiz completions
x 80% email capture rate = 4,160 segmented leads
x 15% email sequence conversion over 5 days = 624 purchases
(some double-count with immediate, net new ~780 purchases adjusted)

Conservative total: ~$60,000-$90,000/month
```

Same 8,000 clicks. Same content. Same traffic. The difference is entirely funnel architecture.

---

## Key Conversion Benchmarks

| Stage | Poor | Average | Good | Great |
|-------|------|---------|------|-------|
| Quiz start rate (of page visitors) | <30% | 40-50% | 50-60% | >65% |
| Quiz completion rate (of starters) | <50% | 55-65% | 65-75% | >80% |
| Email capture rate (of completers) | <60% | 65-75% | 75-85% | >90% |
| Recommendation-to-purchase rate | <3% | 4-6% | 6-8% | >10% |
| Email sequence recovery rate (30 days) | <10% | 15-25% | 25-35% | >40% |

---

## Scorecard Quiz Benchmarks

Scorecard quizzes (20 questions, 3 phases) have a different conversion profile than shorter product match quizzes. The trade-off: lower absolute completion rate, higher lead quality and qualification signal.

| Stage | Scorecard Quiz | Standard 5-7 Question Quiz |
|-------|---------------|---------------------------|
| Page-to-full-completion | 20-40% | 24-45% (start rate x completion rate) |
| Contact capture on partials | 60-80% (captured upfront) | 0% (captured at end) |
| Total leads per 1,000 visitors | 200-400 complete + 200-400 partial | 250-450 complete only |
| Qualification accuracy | High (20 data points per lead) | Moderate (5-7 data points) |
| Time to complete | ~3 minutes | ~90 seconds |

The contact-first architecture means scorecard quizzes generate more total leads despite lower completion rates. A visitor who drops at question 12 is still a lead with name, email, and potentially phone. In a standard quiz with end-capture, that same visitor generates zero leads.

For high-ticket offers ($1,000+), the scorecard's qualification signal often makes it the higher-ROI choice despite the lower completion rate. You'd rather have 200 pre-qualified leads than 400 unqualified ones when your sales team's time is the bottleneck.

See `references/priestley-scorecard-framework.md` for the full framework and implementation details.

---

## The 6-Month Compounding Model

Quiz funnels compound in ways product pages can't.

### Month 1
- Quiz is live, converting cold organic traffic at baseline rates
- Email list growing at ~4,000-5,000 leads/month (segmented by quiz path)
- Initial follow-up sequences delivering first recovery conversions

### Month 2
- Email list: ~8,000-10,000 segmented leads
- First targeted campaign to Month 1 non-purchasers (new product, limited offer)
- 30 days of quiz data used to refine content hook angles and script language
- Quiz completion rate improving as drop-off questions get rewritten

### Month 3
- Email list: ~12,000-15,000 segmented leads with known preferences, pain points, and objections
- Content production running on validated audience intelligence
- Average reel performance measurably stronger than Month 1
- Quiz funnel operating with 90 days of optimization data

### Month 6
- Email list: ~25,000-30,000 segmented leads
- Owned audience asset generating revenue independently through campaigns, launches, seasonal offers
- Content operation informed by 6 months of direct audience intelligence from quiz responses
- Quiz conversion rates optimized through A/B testing on questions, answers, and recommendation screens
- Operation fundamentally more valuable than Month 1, from the same content volume

The operation that built the quiz funnel at Month 1 is operating a different business at Month 6 than the one that ran the same content into a product page for the same period.

---

## Revenue Impact Calculator

Use this to estimate the impact for any operation:

```
Current monthly clicks:           [A]
Current conversion rate:          [B]%
Current monthly revenue:          [A] x [B]% x AOV = $[C]

With quiz funnel:
Quiz completions:                 [A] x 65% = [D]
Immediate purchases:              [D] x 6% = [E]
Email leads captured:             [D] x 80% = [F]
Email recovery purchases (30d):   [F] x 20% = [G]
Total monthly purchases:          [E] + [G] = [H]
Projected monthly revenue:        [H] x AOV = $[I]

Revenue improvement:              $[I] / $[C] = [X]x
```

---

## The Retargeting Tax

Without a quiz funnel, the standard response to low product page conversion is retargeting. This works but has a structural cost most operators don't account for:

- Retargeting requires paid budget applied to an audience your organic content generated for free
- The margin on a retargeting conversion is fundamentally different from an organic conversion
- The organic reach advantage of AI UGC is partially neutralized every time you pay to close a sale that organic content opened

The quiz funnel converts a higher percentage on the first visit, before they leave, using the emotional momentum the content created. This preserves the margin advantage of organic traffic instead of converting it into a paid acquisition cost.

---

## When to Expect Results

| Timeline | What to expect |
|----------|---------------|
| Week 1-2 | Quiz live, initial data flowing, conversion rates establishing baseline |
| Week 3-4 | First optimization pass (rewrite low-performing questions, adjust recommendation copy) |
| Month 2 | Email sequences producing measurable recovery revenue, content angles refined from quiz data |
| Month 3 | Conversion rates stabilized after optimization, compounding email list value becoming visible |
| Month 6 | Full compounding effect: optimized quiz + large segmented list + data-driven content = peak performance |
