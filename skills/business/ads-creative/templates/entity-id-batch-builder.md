# Template: Entity ID Batch Builder

**Phase**: Foundation (Step 2 of the 14-day operating cycle)
**Use when**: Building 10 to 15 structurally distinct concepts in one production batch. Each concept must vary at least 2 of the 4 dimensions (persona, format, environment, pain/benefit) so each one produces a distinct Entity ID under Andromeda.
**Output**: 10 to 15 batch briefs, each with the full 4-dimension fingerprint plus the script format template to invoke for production.
**Cross-link**: `references/andromeda-algorithm-architecture.md` for the underlying theory. `templates/fake-vs-real-diversity-audit.md` for the upstream diagnosis that feeds this.

---

## The prompt

```
SYSTEM IDENTITY
You are a Meta ads creative architect trained on the Andromeda retrieval system. Andromeda gives each Entity ID one auction ticket. To scale, an account needs 8 to 12+ distinct Entity IDs across at least 4 branches of the behavioral tree. Your job is to design 10 to 15 structurally distinct concepts in one batch, each producing a different Entity ID, each varying at least 2 of the 4 dimensions.

OPERATING RULES
Each concept must vary at least 2 of the 4 dimensions from every other concept in the batch: persona, format, environment, pain/benefit.
No cosmetic-only variation. Hook copy and font changes do not count. The 4-dimension fingerprint must be structurally different.
Anchor in the brand. Every concept must still serve the brand's actual product and target market. Distinct does not mean random.
Honor the angle bank. If an existing angle bank exists, the 10 to 15 concepts should expand it across underserved branches, not replace it.
Cover multiple behavioral tree branches. If 80% of the batch sits on one branch, the batch fails the diversity test.

YOUR TASK
I am going to provide the brand context, the existing Entity ID audit (if available), and the angle bank (if available). Produce a batch of 10 to 15 structurally distinct concepts.

For each concept produce:

CONCEPT [NUMBER]
Concept name (short internal label)
4-dimension fingerprint:
- Persona (one specific person in one specific situation, not a demographic)
- Format (one of the named script formats)
- Environment (where the ad visually takes place)
- Pain/benefit (the entry point the hook will name in the first 3 seconds)
Why this concept is structurally distinct from the others in the batch (name which 2+ dimensions changed from the closest sibling concept)
Behavioral tree branch this concept will land on
The script format template to invoke for production (one of:
- templates/hook-hold-payoff-script.md
- templates/b-roll-director.md
- templates/before-after-narrative.md
- templates/founder-story-script.md
- templates/listicle-authority-script.md
- templates/podcast-two-actor-script.md
- templates/organic-pov-script.md
- templates/silent-text-only-script.md
- templates/static-ad-angles-headlines.md
- templates/ugc-creator-brief.md + one of the above)
The expected Entity ID it will produce (the 4-tuple fingerprint expressed as one string for tracker logging)

After all concepts, produce:

BATCH SUMMARY
Total concepts: [N]
Distribution by persona: [list with counts]
Distribution by format: [list with counts]
Distribution by environment: [list with counts]
Distribution by pain/benefit: [list with counts]
Behavioral tree branches covered: [list]
The single concept to produce first and why
The concept I would cut if budget forces 10 instead of 15 and why

[PASTE YOUR BRAND CONTEXT, EXISTING ENTITY ID AUDIT, AND ANGLE BANK BELOW THIS LINE]
```

---

## What to feed in

1. Brand and product context (what it is, who it serves, the core mechanism, the offer)
2. Output from `templates/fake-vs-real-diversity-audit.md` if available (this names the existing Entity ID clusters to avoid)
3. Output from `templates/angle-bank-builder.md` if available (this names the angles ready to test)
4. Output from `templates/full-funnel-creative-strategy.md` if available (this names the personas to target)
5. Constraints: budget, production capacity, what formats are excluded for brand reasons

The more upstream artifacts, the sharper the batch. Without them, the batch falls back to generic 4-dimension permutations.

## What to do with the output

1. Save in `private project strategy notes` as `[brand]-entity-id-batch-[date].md`.
2. For each concept, invoke the matched script format template (hook-hold-payoff, before-after, etc.) to produce the actual script.
3. Tag each produced ad with its expected Entity ID fingerprint in the creative tracker. After 14 days of spend, verify the actual Entity ID assignment matches the prediction.
4. Brief production for the priority concept first. The summary names the "produce first" concept and the rationale.
5. The batch covers 14 days of production cycle. Re-run the builder every 14 days with the updated audit.

## Reading the output

Healthy batch: 10 to 15 concepts spread across 4 to 6 personas, 5 to 7 formats, 4 to 6 environments, 4 to 6 pain/benefit entry points. Each branch of the behavioral tree gets at least 2 concepts.

Constrained batch: 10 to 15 concepts but the distribution table shows 70% of concepts share one persona or one format. The model produced cosmetic variation despite the rule. Run again with the constraint "no more than 3 concepts per persona, format, environment, or pain dimension."

## Common mistakes

- Asking for 10 concepts without naming the existing Entity IDs. The model produces overlapping concepts that collapse with the existing library. Always run the audit first.
- Treating "variation" as enough. The rule is variation across at least 2 dimensions per concept. The model will produce 1-dimension variations if not constrained.
- Producing all 15 in the same week. Capacity matters. 10 concepts every 14 days at high production quality beats 15 concepts every 7 days at compromised quality.
- Ignoring the "concept to cut" line in the summary. The cut suggestion is often the right one because the model self-identifies the weakest fit.

## Cross-references

- `references/andromeda-algorithm-architecture.md`: 4-dimension framework + 14-day operating cycle
- `references/meta-ads-master-workflow.md`: how this batch feeds the 5-phase workflow
- `references/script-format-selector.md`: the 10 script formats and their decision tree
- `templates/fake-vs-real-diversity-audit.md`: the upstream audit
- `templates/angle-bank-builder.md`: where the angle library comes from
- `templates/full-funnel-creative-strategy.md`: where the persona architecture comes from
