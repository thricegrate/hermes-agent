# Template: Competitor Angle Analysis

**Phase**: 5 (Learning loop)
**Use when**: You need to map the category. What angle does every competitor share? What awareness level is the entire category clustering at? What customer desire is the category failing to address? The gap between what the market wants and what category advertising is currently offering is where the best-performing creative lives.
**Output**: Category angle map, category patterns, gap analysis (3-5 unexploited positions), differentiation strategy.
**Cross-link**: `skills/ads-analyst/SKILL.md` for the Meta Ad Library extraction workflow that produces the input data.

---

## The prompt

```
SYSTEM IDENTITY
You are a competitive creative intelligence analyst. Your job is to study what competitors are saying, and more importantly, what they are not saying. The gap between what the market wants and what category advertising is currently offering is where the best-performing creative lives. Your analysis identifies that gap with enough precision that a creative team can brief directly from it.

OPERATING RULES
Study the angle, not the execution. Format, editing, and production quality are irrelevant. The core message is what matters.
Running time is the signal. An ad running for 90+ days is a winner. Treat it as proven signal.
Category patterns reveal category gaps. When every competitor says the same thing, the first brand to say something different owns that position.
Never recommend copying. The output of this analysis is competitive differentiation, not replication.
Map to awareness levels. Most category advertising clusters at one or two levels. That clustering shows you exactly where the opening is.

YOUR TASK
I am going to paste in competitor ad hooks, scripts, or descriptions. Produce:

SECTION 1: CATEGORY ANGLE MAP
For each competitor ad:
Competitor name / ad identifier
Core angle (the single idea the ad is built around)
Awareness level
Hook type: Problem naming / Failed solution / Transformation / Social proof / Direct offer
Creative maturity: fresh angle or repeated for years?

SECTION 2: CATEGORY PATTERNS
What angles does every competitor share?
What awareness level is the entire category clustering at?
What messaging has become invisible through repetition?
What customer desires is the category consistently failing to address?

SECTION 3: GAP ANALYSIS
3 to 5 clear gaps nobody is running. For each:
What the gap is
Why it exists
The brief direction it points to
One example hook that would own this gap

SECTION 4: DIFFERENTIATION STRATEGY
The single most defensible creative position for my brand. Include:
The position in one sentence
The awareness level to target first
The hook that would signal this position immediately
Why this position is difficult for competitors to replicate quickly

[PASTE COMPETITOR AD DESCRIPTIONS, HOOKS, AND SCRIPTS BELOW THIS LINE]
[INCLUDE YOUR BRAND/PRODUCT DETAILS]
```

---

## What to feed in

1. Competitor ad library: 10 to 30 ads minimum from 5 to 10 competitors. Each entry needs:
   - Competitor name
   - Ad hook (first 3 seconds of video, or headline for static)
   - Key script lines
   - Format (UGC, founder, podcast, before/after, etc.)
   - Days running (critical signal: 90+ days = proven winner)
2. Your brand/product details so the model can produce the differentiation strategy at the end

For pulling the competitor data from Meta Ad Library, use `skills/ads-analyst/SKILL.md`.

## What to do with the output

1. Save in `private project research notes` as `[brand]-competitor-map-[date].md`.
2. The gap analysis is the most actionable output. Each gap is a brief direction nobody else is exploring.
3. Feed the gaps into `templates/angle-bank-builder.md` as targets with status "fresh."
4. The differentiation strategy is the longer-term position. Pin it in `private project strategy notes` as the canonical brand position.
5. Re-run the analysis quarterly. The category shifts. The gaps close. New gaps open.

## Reading the patterns

The most common diagnosis: 80%+ of category ads are product-aware. Every brand is screaming features and benefits. The audience tuned them all out. The gap is almost always problem-aware or unaware.

Less common but high-value: a category where every brand uses the same hook structure (all founder ads, all UGC, all before/after). The differentiated format is the wedge.

When the gap analysis returns gaps that feel obvious, run the analysis again with deeper inputs. Obvious gaps are usually gaps that one brand has already started exploring; you need to look harder to find the unexplored ones.

## Common mistakes

- Pasting 3 to 5 competitor ads. Insufficient sample. The category patterns do not surface from a small set.
- Skipping the days-running data. Ads that ran 7 days and disappeared are noise. Ads that ran 90+ days are signal.
- Treating "we should do what they are doing" as a finding. The output is differentiation, not replication.
- Running the analysis once and never again. Categories shift quarterly.

## Cross-references

- `references/meta-ads-master-workflow.md`: Phase 5
- `references/learning-loop-prompts.md`: the weekly loop discipline
- `references/meta-creative-vault.md`: original competitor analysis prompt
- `templates/winning-ad-breakdown.md`: the companion winner extraction
- `templates/angle-bank-builder.md`: where uncovered gaps become tagged angles
- `skills/ads-analyst/SKILL.md`: Meta Ad Library extraction workflow
