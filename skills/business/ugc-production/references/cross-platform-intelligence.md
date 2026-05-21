# Cross-Platform Intelligence Layer

Every Monday, the weekly intelligence session synthesizes the previous week's performance data across all 4 platforms (TikTok, Instagram Reels, YouTube Shorts, Facebook Reels) into the strategic analysis that updates the upstream creative brief.

This layer is where the unified Claude approach produces intelligence advantages that fragmented operations cannot replicate.

## Why cross-platform synthesis beats single-platform analysis

Operators running separate Claude sessions per platform miss the cross-platform patterns that only emerge when data flows through a single analytical pipeline.

Examples of cross-platform patterns:

- **Hook patterns winning on TikTok inform Instagram content decisions** even when the underlying products differ
- **YouTube subscribe rate patterns translate into Instagram follow rate optimization** because both reward similar identification dynamics
- **Older demographic engagement patterns from Facebook inform script tone** across the entire operation, including younger-platform variants that target adjacent age bands
- **Saturation signals on one platform** (CPA creep, CTR drop) often appear 2-4 weeks before the same signals on another platform, giving early warning for adjustments

These insights only surface when the analyst sees all 4 platforms together. Fragmented operations miss them.

## The weekly intelligence session structure

Run this every Monday (or whichever day you treat as the start of the operating week).

### Step 1: Pull performance data across all 4 platforms

For each platform, pull the previous 7 days:

- **TikTok**: ad-level CPI, CTR, hook rate, hold rate, CPA, conversion volume
- **Instagram Reels**: same metrics + saves rate, comment volume
- **YouTube Shorts**: same metrics + subscribe rate, watch-through rate
- **Facebook Reels**: same metrics + comment substance (length, sentiment)

Centralize the data in a single table. Each row is one ad on one platform. Each column is a metric.

### Step 2: Identify the top 5 performers across all platforms (combined ranking)

Rank ads by a composite score combining the platform's primary metric and CPA:

- **TikTok**: hook rate × (1 / CPA)
- **Instagram**: saves rate × (1 / CPA)
- **YouTube**: subscribe rate × (1 / CPA)
- **Facebook**: comment substance × (1 / CPA)

Pull the top 5 across all platforms combined. These are the cross-platform winners worth understanding.

### Step 3: Extract the cross-platform pattern

Look at the top 5 winners and ask:

- What hook structure repeats across platforms? (Specificity hook? False-opening? Identity?)
- What pain angle repeats? (Frustration framing? Wasted-money framing? Social comparison?)
- What CTA architecture, when adapted to each platform, drove the best results?
- What avatar demographic features showed up in winners vs losers?
- What audio choices (trending vs voiceover-only) correlated with wins on platforms where audio matters?

The patterns that appear in 3 of the 5 winners are the cross-platform signal. Patterns that appear in 1 or 2 are platform-specific (interesting, but less actionable).

### Step 4: Identify cross-platform anti-patterns (the failures)

Pull the bottom 5 across all platforms (highest CPA + lowest primary metric).

Ask:
- What is consistently failing across platforms?
- Are there hook angles that miss everywhere?
- Are there avatar demographics or aesthetics that consistently underperform?
- Are there pain angles that have stopped resonating?

Cross-platform losers often signal saturation in the niche or a shift in audience response to a previously-working pattern.

### Step 5: Update the creative brief

Based on Steps 3 and 4, update the upstream creative brief:

- **Audience insight statement**: refresh if new pain points or language patterns surfaced in comment analysis or competitor reels
- **Product brief**: usually stable, but update the proof points if new customer reviews surfaced strong specific timelines or numbers
- **Structural reference**: replace if a new competitor reel has emerged that is materially outperforming the current reference

The brief feeds the next week's content production. Cross-platform intelligence is what keeps the brief current.

### Step 6: Set the next week's production priorities

Decide:

- Which winning patterns to expand (more variants of the top 5, especially across platforms where they have not been ported yet)
- Which anti-patterns to retire across the library
- Which platforms to weight more heavily this week (if Facebook's CPA dropped while TikTok saturated, shift budget)
- Which new concept angles to test (informed by patterns the data is suggesting)

## The single-Claude-session advantage

The intelligence session runs in ONE Claude session that loads all 4 platforms' data and produces the unified analysis.

The session prompt structure:

```
CROSS-PLATFORM PERFORMANCE DATA (Week of [date]):

# TikTok performance
[Paste 7-day data: ads + metrics]

# Instagram Reels performance
[Paste 7-day data]

# YouTube Shorts performance
[Paste 7-day data]

# Facebook Reels performance
[Paste 7-day data]

CURRENT BRIEF:
[The current 3-input brief: audience insight + product + structural reference]

INSTRUCTIONS:

1. Identify the top 5 ads across all platforms (composite ranking based on each platform's primary
   metric × inverse CPA).
2. Identify the bottom 5 ads across all platforms.
3. Extract cross-platform patterns from the top 5 (hook structure, pain angle, CTA, avatar
   demographic, audio approach).
4. Extract cross-platform anti-patterns from the bottom 5.
5. Recommend updates to the audience insight statement, product brief, and structural reference.
6. Recommend the next week's production priorities (what to expand, what to retire, where to shift
   budget, what new angles to test).

Output as a structured report with each step's findings. Be specific. Reference exact ads where
relevant.
```

The cross-platform synthesis takes Claude 5-10 minutes to produce. Running 4 separate single-platform analyses would take 4x that time and miss the cross-platform patterns.

## What cross-platform intelligence catches that single-platform analysis misses

### The "leading platform" pattern

Often one platform shifts before the others. If TikTok hook rates are declining for a specific hook structure 2 weeks before Instagram shows the same trend, the cross-platform analyst spots this as an early warning. The single-platform analyst running each platform separately misses it.

### The "audience portability" pattern

Sometimes a winning angle on one platform fails on another even with the calibration adjusted. The cross-platform analyst notices this and either retires the angle for the failing platform or investigates why the audience response differs. The single-platform analyst tries to force the failing platform to work without the data showing them why.

### The "concept resonance" pattern

A specific concept (specific pain point, specific mechanism articulation, specific transformation) sometimes wins across all 4 platforms even with very different calibration. That concept is more important than the calibration. The cross-platform analyst doubles down on the concept and produces variants across all 4 platforms simultaneously. The single-platform analyst keeps testing within their platform's silo.

### The "saturation cascade" pattern

When an ad starts to saturate, the symptoms appear in waves: CPA creep first, then CTR drop, then hook rate decline, then volume plateau. Across platforms, the cascade often follows a sequence (TikTok saturation precedes Instagram saturation, which precedes Facebook saturation, etc.). The cross-platform analyst sees the cascade earlier and can produce variants before saturation fully hits.

## Connecting cross-platform intelligence to other workflows

### Feeds the variation generation

When a cross-platform winner is identified, run the variation generation prompt (per [../templates/master-prompts-by-platform.md](../templates/master-prompts-by-platform.md), variation section) to produce 5-6 variations of the winner across all 4 platforms simultaneously. The variations preserve the structural arc but vary the personal details and visual pairing notes.

For component-level variation at scale (1 winner → 1000+ combinations), see [winner-variation-pipeline.md](winner-variation-pipeline.md). The cross-platform intelligence feeds this pipeline by identifying which winners deserve the full multiplication treatment.

### Updates the structural reference

When a cross-platform winner outperforms the current structural reference by 1.5x or more on key metrics, update the structural reference to use the new winner as the blueprint. This ensures the upstream brief stays calibrated to current algorithmic dynamics.

### Informs the daily production schedule

Per [../SKILL.md](../SKILL.md) ("Daily Production Schedule"), the daily production cycle produces 20-25 pieces. The cross-platform intelligence determines what goes into the daily production: more variants of cross-platform winners, fewer variants of cross-platform losers, new angle tests informed by the patterns.

## Common mistakes

### Running separate Claude sessions per platform

Defeats the entire purpose. The intelligence emerges from the unified analysis. 4 single-platform sessions produce 4 single-platform analyses, which miss the cross-platform patterns.

### Running the intelligence session weekly without updating the brief

The intelligence session is supposed to feed the brief. If the brief never gets updated, the next week's production stays calibrated to last month's audience reality. Update the brief as part of the intelligence session output.

### Treating all platforms as equal

The 4 platforms have different volume and different LTV profiles. A pattern that wins on Facebook with 100 conversions per week is more important to the operation than a pattern that wins on YouTube Shorts with 5 conversions per week. Weight the analysis by volume + LTV, not by raw metric values.

### Skipping the bottom 5

The losers tell you what to stop doing. Operators who only analyze winners produce more winners but never retire losers, which means the library bloats with underperformers that drain budget.

### Trying to do this analysis manually in spreadsheets

The cross-platform synthesis has too many dimensions for spreadsheet analysis to surface the patterns efficiently. Claude reads the data, holds the brief in context, and produces the synthesis in 10 minutes. Manual analysis takes hours and produces shallower insights.

## Cross-references

- Brief structure (gets updated by this intelligence): [cross-platform-brief-structure.md](cross-platform-brief-structure.md)
- Platform calibration variables (the variables this intelligence helps tune): [platform-calibration-variables.md](platform-calibration-variables.md)
- Master prompts (consume the updated brief): [../templates/master-prompts-by-platform.md](../templates/master-prompts-by-platform.md)
- Component-level variation pipeline (for the strongest winners): [winner-variation-pipeline.md](winner-variation-pipeline.md)
- Existing weekly optimization framework (concept-level): [optimization-system.md](optimization-system.md)
- Weekly review template: [../templates/weekly-review.md](../templates/weekly-review.md)
