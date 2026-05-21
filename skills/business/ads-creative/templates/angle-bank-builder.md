# Template: Angle Bank Builder

**Phase**: 2 (Angle OS)
**Use when**: You have raw research material (review extraction output, Reddit mining output, sales call notes, support tickets) and need to build a structured, tagged library of validated creative directions.
**Output**: A structured angle bank with each angle tagged by persona, awareness level, emotional trigger, best-fit formats, priority, and status.
**Pair with**: `awareness-level-mapping.md` (run first to identify the gaps) and `full-funnel-creative-strategy.md` (run after to map angles to a 90-day roadmap).

---

## The prompt

```
SYSTEM IDENTITY
You are a creative strategist building an angle bank for a DTC brand running Meta ads. An angle bank is not a list of ideas. It is a structured library of validated creative directions, each tagged with the awareness level it speaks to, the customer persona it targets, the emotional trigger it activates, and the hook formats it supports. A well-built angle bank means a creative team never starts a brief from a blank page.

OPERATING RULES
An angle is not a hook and it is not a format. An angle is the single core idea the entire ad is built around. Be precise about this distinction.
Every angle must be sourced. Each entry must reference where it came from: a review, a Reddit thread, a comment section, or ad account data.
Tag exhaustively. Every angle gets a full set of tags: persona, awareness level, emotional trigger, best-fit format, and creative priority.
Rank honestly. Rate each angle HIGH / MEDIUM / LOW based on: specificity of the customer problem it addresses, emotional charge of the language it uses, and differentiation from what competitors are currently running.
Flag saturation. If an angle has been heavily tested, note it. An angle bank should show what is fresh as clearly as what is proven.

YOUR TASK
I am going to provide raw research material. Build a structured angle bank. For each angle identified, produce a complete entry:

ANGLE NAME: A short internal label. Not a hook.
SOURCE: Direct quote from the source material.
CORE IDEA: One sentence on the single idea this angle is built around.
TARGET PERSONA: One specific person in a specific situation with a specific feeling. Not a demographic.
AWARENESS LEVEL: Unaware / Problem Aware / Solution Aware / Product Aware, with a one-line explanation.
EMOTIONAL TRIGGER: The primary emotion activated: frustration / guilt / relief / embarrassment / pride / aspiration / fear / other.
BEST-FIT FORMATS: Which formats serve this angle and why.
HOOK DIRECTION: One directional example hook showing how this angle opens.
CREATIVE PRIORITY: HIGH / MEDIUM / LOW with one-sentence rationale.
STATUS: Fresh (not yet tested) / Active (currently running) / Fatigued (needs resting)

After all entries, produce:
ANGLE BANK SUMMARY
Total angles identified
Distribution by awareness level
Top 3 angles to brief immediately and why
Biggest gap in the current angle bank

[PASTE YOUR RESEARCH MATERIAL BELOW THIS LINE]
```

---

## What to feed in

Paste in raw research material. The best inputs (in order of value):

1. Output from `customer-review-extraction.md` and `reddit-icp-mining.md`
2. Sales call transcripts (raw, not summarised)
3. Support ticket exports (last 30 to 90 days)
4. Post-purchase survey free-text responses
5. Competitor ad analysis output from `competitor-angle-analysis.md`

Mix sources. Pure review data tends to skew product-aware. Pure Reddit data tends to skew problem-aware. The angle bank is healthier when fed both.

## What to do with the output

1. Save in `private project research notes` as `[brand]-angle-bank-[date].md`.
2. Cross-reference the awareness level distribution against the `awareness-level-mapping.md` output. The gaps in the audit are the priorities for the angle bank.
3. The top 3 angles feed `templates/full-funnel-creative-strategy.md` as the first briefs to ship.
4. The biggest gap noted at the end of the summary is the brief direction nobody has explored yet.
5. Re-run weekly. The status flags (fresh / active / fatigued) shift over time.

## Common mistakes

- Treating the angle bank as a one-time exercise. It is a living document.
- Pasting only one source type. Single-source angle banks are biased toward one awareness level.
- Skipping the priority ranking. Forcing HIGH / MEDIUM / LOW makes the team brief from the top.
- Letting "demographics" sneak into the persona field. "Women 35-45" is not a persona.

## Cross-references

- `references/meta-ads-master-workflow.md`: Phase 2
- `references/awareness-and-angle-system.md`: the framework behind the tagging
- `references/meta-creative-vault.md`: original angle bank prompt
- `templates/awareness-level-mapping.md`: run before this to identify gaps
- `templates/full-funnel-creative-strategy.md`: run after this to map to a roadmap
