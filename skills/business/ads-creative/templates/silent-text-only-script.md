# Template: Silent / Text-Only Script

**Phase**: 3 (Scripting engine)
**Use when**: High-volume testing. Captions-off feeds. Cheap-to-produce format. Striking background visuals + ASMR-style actions + punchy text overlays carry the whole ad. Works at every awareness level when the visual bedrock and text copy are sharp.
**Output**: Visual bedrock, text timing + copy, creative tracker name.
**Cross-link**: `skills/video-scriptwriter/references/silent-text-only-format.md` for the deeper format theory.

---

## The prompt

```
SYSTEM IDENTITY
You are a visual retention expert. You write ads that perform with the sound off. You rely on striking background visuals, ASMR-style actions, and punchy, high-contrast text overlays to tell the entire story. You know that text on screen must be short, easily readable, and paced perfectly to match the viewer's reading speed.

OPERATING RULES
No voiceover.
Text must be absolute fire. Every sentence must hit an emotional trigger or make a bold claim.
Visuals must prove the text. If the text says "Destroys bacteria," the visual must be an extreme close-up of the product working.

YOUR TASK
Write a silent video ad brief:

SECTION 1: VISUAL BEDROCK
What is the continuous, satisfying background action happening? (e.g., Swatching product, mixing ingredients, extreme close-up of skin).

SECTION 2: TEXT TIMING AND COPY
Format as [Timestamp] | [Text on Screen].
Create a 15 to 20 second sequence of text overlays that take the user from a bold hook, through the problem, to the guarantee/CTA.

SECTION 3: CREATIVE TRACKER NAMING CONVENTION
Output the exact file name string for this ad so I can log it in my tracker.

[PASTE PRODUCT DETAILS, BIGGEST CLAIM, AND GUARANTEE BELOW]
```

---

## What to feed in

1. Product details + the specific visual demonstration that proves the product works (texture, application, before/after on a model)
2. The biggest claim you can make (specific outcome with a timeline or quantity)
3. The guarantee (risk reversal language: money back, free returns, free trial)
4. The CTA (low-friction: "Link below", "Try it free")

## What to do with the output

1. Save in `private project script notes` as `[creative-tracker-name].md`.
2. The visual bedrock needs to be continuous and satisfying. Coordinate with production to capture the loop (or generate the loop via NB2/Kling per `references/static-and-animation-pipeline.md`).
3. Text rendering matters. Use the Reels native text tool for organic feel, not third-party caption tools that look corporate.
4. The 2-3 seconds per card timing is non-negotiable. Cards that flash too fast cannot be read. Cards that linger too long lose the viewer.
5. Pair with a trending audio track for organic-feel placements (TikTok especially). For paid Meta placements, silent often works without audio.

## Common mistakes

- Too much text per card. One bold claim per card. If it needs two lines, split into two cards.
- Visual that does not prove the text. The text says "instantly absorbs", the visual must show actual absorption.
- Generic visual bedrock. Stock-looking product shots fail. The visual needs to be either ASMR-satisfying or pattern-interrupt strange.
- Skipping the guarantee. The closing card needs the risk reversal. Without it, the format under-converts at the bottom of the funnel.

## Cross-references

- `references/meta-ads-master-workflow.md`: Phase 3
- `references/script-format-selector.md`: when to pick silent over voiceover
- `skills/video-scriptwriter/references/silent-text-only-format.md`: format theory + timing models
- `references/static-and-animation-pipeline.md`: when the visual bedrock is AI-generated
- `references/static-headline-formulas.md`: the headline copy patterns for the text overlays
- `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md`: voice gate
