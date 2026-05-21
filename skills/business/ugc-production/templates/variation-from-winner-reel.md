# Variation From Winner Template (UGC Reel)

The prompt that turns one validated AI UGC reel into 25 hook variations + 12 body variations + 10 CTA variations + the compatibility tags needed to filter to roughly 1,000 coherent assembled reels.

For the full pipeline workflow, see [../references/winner-variation-pipeline.md](../references/winner-variation-pipeline.md).

For the slideshow parallel (TikTok slideshows, not reels), see `skills/tiktok-slideshow/templates/variation-from-winner.md`.

## When to use this template

A reel has earned the variation pipeline when:
- Hook rate clears 50%
- Hold rate stays strong behind the hook (drop timestamp is late)
- The signal has confirmed across enough impressions to be real, not random batch noise

If the reel has not cleared these thresholds, do not run this template. Multiplying weak content produces more weak content.

## What this template produces

Single Claude call output:
- 25 hook variations across 4 hook categories (Specificity, False Opening, Result Specificity, Identity)
- 12 to 15 body variations across 6 emotional framings
- 10 to 12 CTA variations across 3 action types
- Compatibility tags on every component (register, pain angle, energy)

Followed by manual or scripted assembly that filters incompatible combinations and queues 800-1,200 coherent reels for Seedance production.

## The variation prompt

```
The following AI UGC reel performed strongly:

[Paste the original reel script in full. Include: hook line, body section, mechanism bridge,
product introduction, CTA. Note the timing of each section.]

PERFORMANCE DATA:
- Hook rate: [percentage, must be 50%+ to qualify for this pipeline]
- Hold rate: [percentage by section]
- CTR: [percentage]
- Distribution: [reach + view count]
- Audience tags from analytics: [age, gender, location, interest signals]

ORIGINAL TAGS (the locked dimensions for the variation set):
- Pain angle: [the specific underlying pain. Examples: "weight management", "burnout", "imposter syndrome",
  "freelance income instability", etc.]
- Character reference: [character description matching the reference image]
- Scene baseline: [setting, time of day, lighting condition, wardrobe family]
- Voice register: [High Energy / Calm Authority]
- Original hook category: [which category from the 4]
- Original body framing: [which emotional entry point]
- Original CTA action type: [Comment funnel / DM share / Save prompt]

GENERATE THREE COMPONENT BATCHES:

==========================
PART 1: HOOK VARIATIONS (25)
==========================

Generate 25 hook variations across the 4 categories. The pain angle stays the same as the original.
Only the psychological trigger changes between hooks.

Distribution (default):
- Specificity hooks: 6-7 variations
- False opening hooks: 6-7 variations
- Result specificity hooks: 6-7 variations
- Identity hooks: 6-7 variations

If the original hook was a specificity hook and that category is the strongest performer in this
audience, weight specificity higher (8-9 variations) and the others lower (5-6 each).

Each hook is 3 to 5 seconds when delivered as a Seedance clip. One short line. Two short sentences
maximum.

For each hook variation, output:

HOOK [N]: [the hook line, exactly as it would be delivered]
CATEGORY: [Specificity / False Opening / Result Specificity / Identity]
TAGS: register=[Data-driven / Vulnerable / Confrontational / Warm / Confident / Curious],
      pain=[the locked pain angle], energy=[High / Medium / Low]
SEEDANCE PROMPT: [The opening scene direction for this hook clip. Include subject action,
expression, line delivery note, 3-5 second timing. Reference the locked character + scene + aesthetic
baseline by saying "use locked character ref + scene ref + aesthetic baseline".]

==========================
PART 2: BODY VARIATIONS (12-15)
==========================

Generate 12 to 15 body variations across the 6 emotional framings. The mechanism bridge and product
introduction structure stay identical to the original. Only the emotional entry point changes.

Default split:
- Frustration framing: 2-3 variations
- Wasted money framing: 2-3 variations
- Social comparison framing: 2-3 variations
- Identity threat framing: 1-2 variations
- Failure stack framing: 1-2 variations
- Unfair comparison framing: 1-2 variations

If the original body used a specific framing, weight that framing higher (4-5 variations) and the
others at 1-2 each.

Each body is the same total duration as the original body. The emotional entry takes the first
~5 seconds, then the bridge and product introduction follow exactly the original structure.

For each body variation, output:

BODY [N]: [the full body section text, including the emotional entry, the locked bridge, and the
locked product introduction structure]
FRAMING: [Frustration / Wasted Money / Social Comparison / Identity Threat / Failure Stack /
Unfair Comparison]
TAGS: register=[Data-driven / Vulnerable / Confrontational / Warm / Confident / Curious + secondary
register if mixed], pain=[locked pain angle], energy=[High / Medium / Low]
SEEDANCE PROMPT: [The opening scene direction for this body clip. Reference the locked character +
scene + aesthetic baseline.]

==========================
PART 3: CTA VARIATIONS (10-12)
==========================

Generate 10 to 12 CTA variations across the 3 action types. The CTA timing stays calibrated to the
original CTA length (2-4 seconds).

Default split:
- Comment funnel keywords: 4 variations (different free resources, different keyword tones,
  different value framings)
- DM share prompts: 4 variations (different person archetypes, different situations, different
  relationship types)
- Save prompts: 4 variations (different use case timings, different reference framings, different
  temporal anchors)

If the original CTA used a specific action type, weight that type higher (5-6 variations) and the
others at 2-3 each.

For each CTA variation, output:

CTA [N]: [the CTA line, exactly as it would be delivered]
ACTION TYPE: [Comment funnel / DM share / Save prompt]
TAGS: register=[Data-driven / Vulnerable / Confrontational / Warm / Confident / Curious],
      pain=[locked pain angle], energy=[High / Medium / Low]
SEEDANCE PROMPT: [The opening scene direction for this CTA clip. Reference the locked character +
scene + aesthetic baseline.]

==========================
VOICE RULES (mandatory across all components)
==========================

- Coffee shop rule: every line must sound like talking to a friend across a cafe table
- No em-dashes anywhere
- Short sentences. One thought per line.
- Simple words. Specific numbers. Real specifics over abstractions.
- Match the original reel's voice intensity exactly. If the original was casual, variations are
  casual. If the original was confrontational, variations are confrontational.
- For CC content specifically: blunt, self-deprecating, dry humor, English is a third language so
  simple word choice is authentic. Numbers over adjectives.

After producing the variation set, list the next steps:
1. Run the compatibility matrix filter (see references/compatibility-matrix.md) to drop
   incompatible component pairings
2. Queue the surviving combinations for Seedance 2.0 production using the consistency patterns
   in references/seedance-consistency.md
3. Deploy first batch of 40-50 across the portfolio with component-level performance tracking
4. Run the 8-week compounding loop
```

## How to use the output

The variation prompt produces a structured component library. The next steps are:

### Step 1: Run the compatibility filter

Take all hooks, bodies, and CTAs with their tags. For each theoretical hook + body + CTA combination, check the compatibility rules in [../references/compatibility-matrix.md](../references/compatibility-matrix.md):
- Hook-to-body register compatibility
- Body-to-CTA register compatibility
- Energy level continuity
- Pain angle match (should always match if all components came from the same original)

Drop any combination that fails the rules. From 3,000 theoretical, expect roughly 1,000 surviving.

### Step 2: Queue for Seedance production

For each surviving combination, queue:
- The hook clip (3-5 seconds)
- The body clip (10-25 seconds depending on original)
- The CTA clip (2-4 seconds)

Use the Seedance consistency patterns in [../references/seedance-consistency.md](../references/seedance-consistency.md) to keep all clips visually coherent. Same character ref + scene ref + aesthetic baseline across every generation.

### Step 3: Deploy first batch (40-50)

Do not deploy all 1,000 at once. First batch is 40-50 across the multi-account portfolio (see [../references/account-portfolio.md](../references/account-portfolio.md) for which accounts get which batch).

Track component-level performance:
- Hook rate per hook clip
- Hold rate drop timestamp per body clip
- CTR per CTA clip

### Step 4: Retire and expand

After 1-2 weeks of deployment data, retire underperforming components across the library. Expand winning components with new variations using the same psychological mechanism. The library compounds in the direction the data points.

### Step 5: Run the 8-week loop

Repeat the deploy-track-retire-expand cycle for 8 weeks. By week 8, the library has more validated audience intelligence than most operators accumulate in a year.

Full loop details: [../references/winner-variation-pipeline.md](../references/winner-variation-pipeline.md).

## Worked example (compressed)

Original winning reel: weight management, specificity hook ("I lost 23 pounds in 11 weeks"),
wasted-money body framing, comment-funnel CTA. Hook rate: 56%. Hold rate: 41% at the bridge. CTR: 2.8%.

Tags on the original:
- Pain angle: weight management
- Character: mid-40s woman, blonde hair, casual home environment
- Scene baseline: kitchen counter morning light from window at left
- Voice register: Calm authority
- Hook: Data-driven / weight management / Medium
- Body: Data-driven + Vulnerable / weight management / Medium
- CTA: Confident / weight management / Medium

Run the prompt above with these inputs. The output will be 25 hook variations, 12-15 body variations, and 10-12 CTA variations, each tagged for compatibility filtering.

After filtering, expect ~1,000 coherent assembled reels ready for production.

## Failure modes when generating variations

### Variations break the pain angle

If variation 7 of the hooks talks about a different pain than the original (e.g., the original is weight management but variation 7 is about productivity), the variation has changed the pain angle. The pain angle must stay constant. Regenerate.

### Variations rewrite the locked structures

The mechanism bridge and product introduction in the body must stay identical. The hook delivery duration must stay 3-5 seconds. The CTA timing must stay 2-4 seconds. If variations change these locked elements, the variation set tests too many things at once and the data becomes unreadable.

### Component tags do not match the content

If a hook tagged "Data-driven" actually reads as "Vulnerable", the compatibility filter will produce wrong results. The model must tag accurately. If tags consistently mismatch the content, re-prompt with the tagging definitions explicitly stated.

### Variations cluster too tightly

If 20 of the 25 hooks are minor remixes of each other, the variation set has not actually explored the 4 categories. Force the model to produce roughly even spread across categories (or the explicit weighted spread if specified).

### Variations dilute the voice

The original was successful because of its voice intensity. If variations soften the voice, they lose the signal. Match the voice exactly across all components.

## Cross-references

- Pipeline overview: [../references/winner-variation-pipeline.md](../references/winner-variation-pipeline.md)
- Hook category taxonomy: [../references/hook-variation-categories.md](../references/hook-variation-categories.md)
- Body framing taxonomy: [../references/body-variation-framings.md](../references/body-variation-framings.md)
- CTA action type taxonomy: [../references/cta-variation-types.md](../references/cta-variation-types.md)
- Compatibility matrix: [../references/compatibility-matrix.md](../references/compatibility-matrix.md)
- Seedance consistency patterns: [../references/seedance-consistency.md](../references/seedance-consistency.md)
- 4-axis concept-level variation (different scale): [../references/variation-matrix.md](../references/variation-matrix.md)
- Slideshow parallel: `skills/tiktok-slideshow/templates/variation-from-winner.md`
