---
name: newsletter-analyst
description: Analyzes newsletter performance using Beehiiv analytics, benchmarks against industry standards, identifies bottlenecks, and prescribes optimization actions. Use when user wants to analyze newsletter metrics, improve open rates, diagnose subscriber churn, optimize newsletter performance, or review content strategy.
---

# Newsletter Analyst

## Prerequisites

- Active newsletter on Beehiiv with at least 30 days of data
- Beehiiv API credentials configured in `.env` (BEEHIIV_API_KEY, BEEHIIV_PUBLICATION_ID)
- Data pipeline backfilled: `cd agents/data-pipeline && python main.py --backfill 200`

## Data Sources

### Primary: SQLite Database (`private project notes/db/business/business.db`)
The data-pipeline agent stores per-post engagement data in the `daily_newsletter` table:
- `date`, `newsletter`, `sent`, `opens`, `open_rate`, `clicks`, `ctr`, `unsubscribes`, `new_subscribers`, `title`, `subject_line`

Query helpers in `agents/data-pipeline/queries.py`:
- `get_newsletter_trend(days=30)` -- open rate and CTR trend
- `get_daily_snapshot(date)` -- all data for one day
- `get_anomalies(days=7)` -- recent anomalies

### Secondary: Beehiiv API Direct
For data not in the DB, use the API via `agents/data-pipeline/fetchers/beehiiv.py` or the CLI `tools/clis/beehiiv.js`.

**CRITICAL**: Always include `expand[]=stats` when fetching posts. Without it, stats are empty.
Stats are nested under `stats.email` (not top-level `stats`):
- `stats.email.recipients`, `stats.email.unique_opens`, `stats.email.open_rate`
- `stats.email.unique_clicks`, `stats.email.click_rate`, `stats.email.unsubscribes`

## Workflow

### Step 1: Collect Beehiiv Metrics

Pull from the SQLite database (preferred) or Beehiiv API:

- **Open Rate** (average over last 30 days)
- **Click Rate** (average over last 30 days)
- **Subscriber Growth Rate** (net new subscribers per month)
- **Unsubscribe Rate** (per issue and monthly average)
- **Revenue Per Subscriber** (if monetized)
- **A/B Test Results** (winning subject lines, engagement patterns)
- **Verified Clicks** (actual engagement vs bot clicks)
- **Top-performing issues** (by open rate and click rate)
- **Subject line patterns** (correlate subject line style with open rate)
- **Link count per email** (from master analysis file)
- **Subscriber segments** (by activity level, acquisition source)

### Step 2: Benchmark Against Industry Standards

Compare each metric against the benchmarks in `references/newsletter-benchmarks.md`.

Rate each as: **Poor** / **Below Average** / **Average** / **Good** / **Great**

Identify the weakest metric, this is your primary bottleneck.

### Step 3: Identify the Bottleneck

The bottleneck framework (adapted from `cro-funnel`):

- **Low open rate** → Subject line problem or list quality issue
- **Low click rate** → Content relevance or CTA problem
- **Low growth** → Acquisition channel or landing page problem
- **High unsubscribes** → Content quality, frequency, or expectation mismatch
- **Low revenue** → Monetization strategy or product-market fit problem

Focus on ONE bottleneck at a time. Fix the biggest leak first.

### Step 4: Diagnose Root Causes

| Bottleneck | Possible Causes | Diagnostic Questions |
|---|---|---|
| Low opens | Bad subject lines, wrong send time, list fatigue, deliverability | Are opens declining over time? Do A/B tests show clear winners? What time do you send? |
| Low clicks | Weak CTAs, irrelevant content, no clear next step | Are clicks concentrated on specific links? Do you have a clear CTA in every issue? |
| Low growth | Weak acquisition, no referral program, no viral content | Where do subscribers come from? Do you have a Beehiiv referral program active? |
| High churn | Unmet expectations, too frequent, not enough value | When do people unsubscribe (after which email)? What does your welcome sequence say? |
| Low revenue | Wrong model, too few subscribers, weak offers | Which monetization models are active? What's your subscriber-to-revenue conversion? |

### Step 5: Prescribe Action Plan

Route to the relevant upstream skill based on bottleneck:

- **Subject line problem** → `newsletter-writer` (Step 6: subject lines & hooks)
- **Content problem** → `newsletter-writer` (Step 4-5: templates & structure)
- **Growth problem** → `newsletter-grower` (all steps)
- **Monetization problem** → `newsletter-monetizer` (choose/optimize models)
- **Automation problem** → `newsletter-automator` (fix sequences)

Be specific: "Your open rate is 22% (below average). Run 4 weeks of A/B tests on subject lines using the hooks framework in `newsletter-writer`. Target: 35%+ open rate."

### Step 6: Content Strategy Iteration (The Vortex Model)

- **Review content pillars**: What 3-5 categories of content do you publish?
- **Identify winners**: Which content pillar drives the best engagement?
- **Double down on winners**, reduce or cut losers
- **The Vortex cycle**: Create content -> Measure performance -> Double down on what works -> Create more of it -> Performance improves -> Repeat
- Detail in `references/content-strategy-vortex.md`

### Step 7: Power Law Distribution Analysis

Standard analytics look at averages. Power law analysis looks at outliers. Both matter, but outliers are where the real signal lives.

**Run this on the last 90 days of data:**

1. **Distribution check:** Look at open rates and click rates across all issues. Are they clustered around an average (normal), or do a few issues dramatically outperform everything else (power law)? If power law: you have untapped hits to compound.

2. **Outlier identification:** Find all issues that performed 2x+ above the 90-day average on ANY metric (open rate, click rate, replies, forwards). These are your hits.

3. **Pattern extraction for each outlier:**
   - Subject line type (what kind of hook?)
   - Content format (which template/structure?)
   - Topic category (which pillar?)
   - Day and time sent
   - Personal story vs generic advice
   - Tool demo vs no tool demo
   - Emotional hook used (which of the 12 emotions?)

4. **Compounding check:** After each outlier, did the NEXT issue on a related topic also outperform? If not, you're leaving value on the table by not doubling down on hits.

5. **Add to the analytics report:**
   - Top 3 outlier issues with pattern analysis
   - Recommended follow-up topics based on hit patterns
   - **Double-down score:** percentage of hits that were followed up within 2 weeks (target: 100%)

For the math behind this and the full Double-Down Playbook: See `content-strategy/references/power-law-framework.md`

## Output Format

Newsletter Analytics Report containing:

- Current metrics with benchmark comparisons
- Primary bottleneck identification
- Root cause diagnosis with supporting evidence
- Prioritized action plan with specific skill references and target metrics

Use the template in `templates/analytics-report.md`.

## Known Issues (Last Audit: 2026-03-12)

Based on analysis of 447 broadcasts and 200 posts with engagement data:

### Critical
1. **Open rate declining fast**: 42% (Jan 2026) -> 37% (Feb) -> 33% (Mar). 9-point drop in 3 months.
2. **CTR critically low**: 0.21% average (industry benchmark: 2-3%). 10x below standard.
3. **30.3 links per email**: Hick's Law -- too many choices = close the email. Dilutes sponsor CTR too.

### High Priority
4. **Pirate emoji banner blindness**: Every subject line starts with the same emoji. Pattern interrupt is now invisible.
5. **Subject line fatigue**: Listicle format ("X prompts that...", "Y ways to...") dominates 80%+. Too repetitive.
6. **Zero segmentation**: Same payload to all 213K subscribers. 50% say they're overwhelmed (survey data).
7. **~400 unsubs per send**: 0.2%/send. Sustained = 12K lost/month.

### Action Items (aligned with Session #6)
- **Link diet**: 1 primary CTA + 3 secondary links max ("Gold Doubloon" method)
- **Emoji rotation**: Pirate flag for build-in-public only. Plain text or varied emojis for other types.
- **Subject line shift**: More personal stories, fewer listicles. "I almost canceled this newsletter" > "7 prompts that slap"
- **Beehiiv tagging**: Tag last 90 days by topic to correlate content type with engagement
- **Reduce to 4-5/week**: Less volume, more impact per send

### Reference Data
- Master analysis file: `private project cyber_corsairs_master_analysis.md`
- Engagement database: `private project notes/db/business/business.db` (199 rows, Aug 2025 - present)
- Survey results: `private project coaching/session-6/session-6-surveys.md`

## Kennedy Tracking Rules

Two non-negotiable rules from Kennedy's direct response playbook. Apply them to every analytics report.

1. **Rule #4: If you can't measure it, kill it.** Every tactic, content format, and growth channel needs a number. If a CTA doesn't get clicked for 3 consecutive issues, change it or cut it. If you can't calculate CPA for a growth channel, you can't scale it intelligently. Track the 5 core metrics weekly: revenue per subscriber, open rate trend, primary CTA click rate, unsubscribe rate per issue, referral rate.
2. **Rule #9: Results rule. Period.** The market votes with purchases, not compliments. High open rate with zero sales = entertaining but not converting. Lots of "love this!" replies but no buyers = audience of fans, not customers. The only metrics that ultimately matter are tied to money: revenue per subscriber, CAC vs LTV, conversion rate from free to paid, revenue per email sent. Everything else is a leading indicator.

See `references/kennedy-tracking.md` for the full tracking checklist and measurement hierarchy.

## Integration

- **Reference**: `cro-funnel` for diagnostic framework patterns
- **Routes to**: `newsletter-writer` (content fixes), `newsletter-grower` (growth fixes), `newsletter-monetizer` (revenue fixes), `newsletter-automator` (sequence fixes)
- **Loops back**: After implementing fixes, re-run this analysis to measure improvement
