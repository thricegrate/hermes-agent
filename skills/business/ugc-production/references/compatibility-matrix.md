# The Compatibility Matrix

The step most operators skip. They produce 25 hooks, 12 bodies, 10 CTAs and assemble all 3,000 theoretical combinations. Most of those combinations break engagement at the tonal shift between hook and body or body and CTA.

The compatibility matrix tags each component with its emotional register and pain angle. Only compatible pairings get assembled. Incompatible combinations get filtered out before deployment.

The math:
- 25 hooks × 12 bodies × 10 CTAs = 3,000 theoretical combinations
- Compatibility filtering removes incompatible pairings
- Result: roughly 1,000 coherent assembled reels from a single winning original

## Why this filter exists

A specificity hook ("I lost 23 pounds in 11 weeks") sets a register that is data-driven, factual, slightly clinical. A frustration-framing body ("I was so tired of starting another diet on Monday") sets a register that is emotional, fed-up, vulnerable. These two registers do not pair cleanly. The viewer feels the tonal shift between hook and body and bounces.

Versus: the same specificity hook ("I lost 23 pounds in 11 weeks") plus a wasted-money framing body ("I added up what I had spent on weight loss. The number was $4,200"). Both registers are data-driven and factual. The shift from hook to body feels continuous. The viewer holds.

The compatibility matrix is how you systematically identify which combinations feel continuous and which break.

## Tagging dimensions

Each component (hook, body, CTA) gets tagged on these dimensions:

### 1. Emotional register

The dominant emotional tone of the component.

- **Data-driven**: factual, specific numbers, slightly clinical
- **Vulnerable**: emotional, fed-up, fragile
- **Confrontational**: direct, sharp, willing to challenge
- **Warm**: soft, supportive, human
- **Confident**: assured, conviction-driven, direct without sharpness
- **Curious**: searching, asking, slightly uncertain

### 2. Pain angle

The specific underlying pain the component speaks to. This is what stays constant across all variations from the same original. All hooks/bodies/CTAs in the same variation set should share the same pain angle.

If the variation pipeline includes components from multiple original reels (multi-source library), pain angle becomes a filter dimension at assembly time.

### 3. Energy level

The pace and intensity of the component.

- **High**: energetic, urgent, fast-paced
- **Medium**: natural conversational pace
- **Low**: reflective, slower, thoughtful

## Compatibility rules

### Hook to body register matching

The hook's register sets the audience expectation. The body must enter on a register that does not break the expectation.

| Hook register | Compatible body registers | Incompatible body registers |
|---|---|---|
| Data-driven | Data-driven, Confident, Vulnerable (with bridge) | Confrontational, Warm |
| Vulnerable | Vulnerable, Warm, Confident (gentle) | Confrontational, Data-driven (cold) |
| Confrontational | Confrontational, Confident, Data-driven (sharp) | Warm, Vulnerable |
| Warm | Warm, Vulnerable, Confident (soft) | Confrontational, Data-driven (cold) |
| Confident | Most registers compatible (this is the bridge register) | Pure vulnerability or pure confrontation may need careful handling |
| Curious | Vulnerable, Warm, Confident | Confrontational |

Confident is the bridge register. Hooks with Confident register pair cleanly with most body registers because confidence does not lock the audience into a specific emotional pole.

### Body to CTA register matching

Same logic. The body's register sets the closing emotional tone. The CTA must close on a register that does not jar.

| Body register | Compatible CTA types | Incompatible CTA types |
|---|---|---|
| Frustration framing (Vulnerable + Confrontational) | DM share to specific archetype, Save for breaking-point moment | Generic save, comment-funnel without value framing |
| Wasted money framing (Data-driven + Vulnerable) | Comment funnel with specific resource, Save for planning moment | DM share to anyone, generic CTA |
| Social comparison framing (Vulnerable + Curious) | DM share to peer, Save for next reunion/event | Comment funnel that ignores the comparison angle |
| Identity threat framing (Vulnerable + Confident) | Save for trigger moments, DM share to person who will witness change | Generic comment funnel |
| Failure stack framing (Vulnerable + Confrontational) | Save for next attempt, DM share to fellow strugglers | Confident comment funnel that ignores the failure narrative |
| Unfair comparison framing (Confrontational + Curious) | Save for next comparison moment, DM share to peer | Vulnerable save prompt that does not acknowledge unfairness |

### Energy level continuity

Energy levels should step down or hold steady through the reel. Stepping up between hook and body, or body and CTA, breaks the tonal arc.

- **Acceptable**: high → high → high (full-energy reel), high → medium → medium, medium → medium → low
- **Acceptable**: high → high → medium (CTA decompresses)
- **Breaks**: medium → high (energy spike in body), low → high (any spike up)
- **Breaks**: high → low (sudden drop, viewer disengages)

## How to tag components

When generating the variation set, ask Claude to tag each component during generation rather than after. The tagging prompt:

```
For each [hook / body / CTA] variation you generate, tag it with:

1. Emotional register: [Data-driven / Vulnerable / Confrontational / Warm / Confident / Curious]
2. Pain angle: [the specific pain this variation speaks to]
3. Energy level: [High / Medium / Low]

Output the tags inline with each variation, like this:

VARIATION 1: [hook line]
TAGS: register=Data-driven, pain=weight management, energy=Medium
```

Tagging during generation forces the model to be conscious of the register and energy at the moment of writing, which produces more consistent outputs than tagging later.

## How to filter at assembly

Once all 25 hooks, 12 bodies, and 10 CTAs are tagged, the assembly step is:

1. **Filter by pain angle**: only assemble combinations that share the same pain angle (already true if all components came from the same winning original)

2. **Filter by hook-to-body register compatibility**: drop any combination where the hook register does not pair with the body register per the compatibility table

3. **Filter by body-to-CTA register compatibility**: drop any combination where the body framing does not pair with the CTA action type per the compatibility table

4. **Filter by energy continuity**: drop any combination where the energy level violates the continuity rules

After filtering, you typically have 800 to 1,200 combinations remaining out of the 3,000 theoretical. That filtered set is what gets queued for assembly.

## A worked example

Original reel: weight management, specificity hook ("I lost 23 pounds in 11 weeks"), wasted money body ("I added up what I had spent on weight loss"), comment funnel CTA ("Comment WEIGHT and I will send you the plan").

Original tags:
- Hook: Data-driven / weight management / Medium
- Body: Data-driven + Vulnerable / weight management / Medium
- CTA: Confident / weight management / Medium

Now spinning variations:

After generation: 25 hooks, 12 bodies, 10 CTAs all tagged with register, pain, and energy.

Filter step:
- Hooks tagged Data-driven, Confident, or Vulnerable pair with the wasted-money body family. Drop hooks tagged Confrontational or Warm if their body pairings break.
- Bodies tagged with wasted-money framing pair with comment-funnel CTAs that have specific resource framings. Drop combinations where the CTA is generic or DM-share-only without a comparable specific resource.

Result: from 3,000 theoretical, roughly 1,100 coherent combinations after filtering.

## Common mistakes

### Tagging after the fact

Tagging components after they are written produces less accurate tags than tagging during generation. The model's interpretation of "register" can drift between writing and tagging passes.

### Over-filtering

Some incompatible pairings are actually creative wins. If the data shows a "broken" combination performing well, the tag definitions may be too strict. Adjust the compatibility table based on observed performance, not just intuition.

### Under-filtering

Skipping the matrix and assembling all 3,000 burns account warmth on broken-tone reels. Even if a few of those broken reels accidentally perform, the cost of the failures is higher than the wins. Filter.

### Treating compatibility as binary

Some pairings are clearly compatible, some clearly incompatible, and some borderline. For borderline pairings, generate the assembled reel but mark it as a test. If it performs, the compatibility table needs updating. If it does not, the table was right.

### Ignoring energy continuity

Operators sometimes filter on register but ignore energy. Energy spikes (going from medium to high mid-reel) feel jarring even when the registers are compatible. Always check both.

## Cross-references

- Pipeline overview: [winner-variation-pipeline.md](winner-variation-pipeline.md)
- Hook variations: [hook-variation-categories.md](hook-variation-categories.md)
- Body framings: [body-variation-framings.md](body-variation-framings.md)
- CTA types: [cta-variation-types.md](cta-variation-types.md)
- Component-level performance tracking (which signals indicate the table needs updating): [optimization-system.md](optimization-system.md)
