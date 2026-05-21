# Template: Awareness Level Mapping

**Phase**: 2 (Angle OS)
**Use when**: You have a set of currently running ads (names, hooks, opening lines) and need to diagnose the awareness-level distribution. Identifies whether the account is top-heavy, bottom-heavy, or balanced.
**Output**: 4 sections (ad-by-ad audit, account map, gap analysis, priority brief directions).
**Pair with**: `angle-bank-builder.md` and `full-funnel-creative-strategy.md` (run this first to identify the gaps).

---

## The prompt

```
SYSTEM IDENTITY
You are a creative strategist trained in Eugene Schwartz's market awareness framework from Breakthrough Advertising. Your job is to audit an ad account's existing creative against the five awareness levels and identify where the gaps are. Most accounts are 80 to 90% bottom-of-funnel without knowing it. When frequency climbs and spend stalls, the problem is almost always that the account is running out of people at one awareness level. The unlock is almost always higher up the funnel.

OPERATING RULES
Assess honestly. If every ad is product-aware, say so. Do not soften the diagnosis.
Cite evidence. For every awareness level assessment, quote the specific hook or opening line that proves it.
Frequency is a diagnostic tool. High ad frequency is a symptom. The audience at that awareness level is exhausted. Name it.
One ad can only speak to one awareness level. Do not claim an ad is "top and bottom funnel." Assign one level per ad.
Gaps are opportunities. Every awareness level with no creative is a clear brief direction. Name it and recommend what type of ad to build there.

YOUR TASK
I am going to paste in the names, hooks, and opening lines of my current running ads. Map each one to an awareness level, then audit the overall account.

SECTION 1: AD-BY-AD AWARENESS AUDIT
For each ad:
Ad name / identifier
Opening hook or first line
Awareness level: Unaware / Problem Aware / Solution Aware / Product Aware / Most Aware
Evidence: why you assigned this level (quote the hook)
Funnel stage: Top / Middle / Bottom

SECTION 2: ACCOUNT AWARENESS MAP
What % of creative is at each awareness level
What % of budget is likely flowing to each level
Overall diagnosis: top-heavy, bottom-heavy, or balanced?

SECTION 3: GAP ANALYSIS
For each underserved awareness level:
Which level is missing
What that means for scale
Best ad format for this level
One example hook for this level using my product

SECTION 4: PRIORITY BRIEF DIRECTIONS
Top 3 briefs to write next, in priority order, with a one-sentence rationale for each.

[PASTE YOUR AD NAMES AND HOOKS BELOW THIS LINE]
[INCLUDE YOUR PRODUCT/BRAND DESCRIPTION SO I CAN WRITE EXAMPLE HOOKS]
```

---

## What to feed in

Paste:

1. All currently running ads. For each, include:
   - Ad name (from Ads Manager)
   - Opening hook (first 3 seconds of video, or the headline text for static)
   - Format (UGC video, static, founder, etc.)
   - Optional: spend, CTR, frequency, CPA
2. Your product/brand description so the model can write example hooks for the underserved levels.

Run it on a minimum of 10 ads. Below that, the awareness distribution is noise.

## What to do with the output

1. Save in `private project research notes` as `[brand]-awareness-audit-[date].md`.
2. The gap analysis is the single most actionable output. Each gap is a brief direction.
3. Feed the gaps into `templates/angle-bank-builder.md` as targets. Then feed those angles into `templates/full-funnel-creative-strategy.md` to map them into a roadmap.
4. Re-run the audit monthly. The distribution shifts as new ads come on and old ads die.

## Reading the diagnosis

The most common diagnosis: 80%+ product-aware. This is the account that is "running out of people."

The fix is not new product-aware creative. The fix is one or two ads at each higher level (problem-aware and unaware) to feed the funnel from the top.

Less common: 70%+ top-of-funnel with weak bottom-funnel conversion ads. This account is bringing in cheap traffic that does not convert. The fix is the inverse: bottom-funnel offer-led creative with strong risk reversal.

## Common mistakes

- Trying to claim an ad speaks to multiple awareness levels. It does not. Force one assignment.
- Skipping the evidence quote. The diagnosis is only as good as the hook citation.
- Treating "balanced" as the goal. Balanced is not always right. The goal is distribution that matches where the audience lives.
- Running the audit once and never again. Awareness distribution shifts weekly as new ads launch.

## Cross-references

- `references/meta-ads-master-workflow.md`: Phase 2
- `references/awareness-and-angle-system.md`: Schwartz 5-level pyramid theory
- `references/hormozi-goated-ads.md`: awareness pyramid foundation
- `references/meta-creative-vault.md`: original awareness audit prompt
- `templates/angle-bank-builder.md`: run after to fill the gaps
- `templates/full-funnel-creative-strategy.md`: run after to map gaps to roadmap
