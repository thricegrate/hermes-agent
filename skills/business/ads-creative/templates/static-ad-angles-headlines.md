# Template: Static Ad Angles and Headline Generation

**Phase**: 4 (Visual execution)
**Use when**: You need a batch of static ad concepts. Generates 3 distinct concept families (benefit extreme, policy/guarantee, anti-solution) per request, each with headline copy and visual direction. Designed to feed NB2 batch generation directly.
**Output**: 3 concept families with headline + visual direction, plus creative tracker name per concept.
**Cross-link**: `references/static-and-animation-pipeline.md` for the NB2 batching workflow. `references/static-headline-formulas.md` for the 5 proven static headline formulas.

---

## The prompt

```
SYSTEM IDENTITY
You are a direct-response static ad designer. You understand that static ads rely entirely on a single, powerful visual and a hook-driven headline. There is no time to build a narrative. You must grab attention, state a massive benefit or handle a massive objection, and drive the click immediately.

OPERATING RULES
Simplicity wins. Less than 10 words on the creative.
Focus on extremes. "13 years of pain gone in 2 days," "Acne will never return."
Contrarian claims work best. "X is not your only option."

YOUR TASK
I will provide a product and an audience. Generate 3 entirely different static ad concepts:

SECTION 1: BENEFIT EXTREME
Headline copy.
Visual direction (e.g., Product alongside a clear icon/illustration).

SECTION 2: POLICY / GUARANTEE
Headline copy focused on risk reversal (e.g., "Our return policy is simple").
Visual direction (e.g., Aesthetic product lineup).

SECTION 3: THE ANTI-SOLUTION
Headline copy attacking the status quo/toxic alternative.
Visual direction (e.g., Bold text block with product at the bottom).

SECTION 4: CREATIVE TRACKER NAMING CONVENTION
Output the exact file name string for this ad so I can log it in my tracker.

[PASTE PRODUCT DETAILS, FAILED SOLUTIONS, AND GUARANTEE BELOW]
```

---

## What to feed in

1. Product details + the most specific outcome you can claim (with timeline or quantity)
2. Failed solutions from `templates/customer-review-extraction.md` and `templates/reddit-icp-mining.md` (these feed the anti-solution concept)
3. Your guarantee or risk reversal language
4. Target audience and awareness level (the benefit extreme concept calibrates differently for solution-aware vs product-aware audiences)

## What to do with the output

1. Save the prompt outputs in `private project static-ad notes` as `[brand]-static-concepts-[date].md`.
2. Feed each visual direction into NB2 to render the actual static image. Generate 8 to 10 variations per concept (different layouts, hero shots, color palettes within the brand baseline).
3. Pick the strongest 3 to 5 statics from the 24 to 30 renders. Log each in the creative tracker.
4. For the NB2 prompt patterns, cross-link to `references/static-and-animation-pipeline.md` and `skills/nb2-image-gen/SKILL.md`.

## Generation rhythm

The system produces 3 concept families per call. Batch this:

- Generate 3 concept families per persona (typically 3 to 5 personas in `templates/full-funnel-creative-strategy.md`)
- That gives 9 to 15 concepts
- Each concept generates 8 to 10 visual variations in NB2
- Final library: 72 to 150 static renders per round
- Pick the strongest 10 to 20 to test

Most operators run 2 to 3 statics per concept. The winning operators run 8 to 10 and let the algorithm pick.

## Common mistakes

- Headlines over 10 words. Static ads cannot afford a sentence. Cut to the bone.
- Generic visual direction. "Product on a clean background" is not direction. "Product alongside a stack of crossed-out competitor bottles, dark moody lighting" is direction.
- Skipping the anti-solution concept. The category gap usually lives there. It is the most differentiated of the three.
- Generating only 1 static per concept. The economic edge of NB2 is volume. Use it.

## Cross-references

- `references/meta-ads-master-workflow.md`: Phase 4
- `references/static-and-animation-pipeline.md`: NB2 batching workflow
- `references/static-headline-formulas.md`: 5 proven static headline formulas
- `references/meta-creative-vault.md`: original static ad generation prompt
- `skills/nb2-image-gen/SKILL.md`: NB2 prompt engineering
- `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md`: voice gate for headline copy
