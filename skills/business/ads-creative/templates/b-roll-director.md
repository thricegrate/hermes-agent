# Template: Visual B-Roll and Voiceover Director

**Phase**: 3 (Scripting engine)
**Use when**: The product is visually demonstrable. The voiceover acts as narrator while the visual B-roll does 80% of the heavy lifting. Best for visual products (skincare, supplements, food, fabric, home goods) where extreme close-ups and satisfying applications drive retention.
**Output**: Visual hook, script + shot list, creator briefing, creative tracker name.
**Cross-link**: `skills/video-scriptwriter/references/long-form-formats.md` for the format theory.

---

## The prompt

```
SYSTEM IDENTITY
You are a Meta ad video editor and creative director. You specialize in "Show, Don't Tell" creatives. Your job is to write a script where the voiceover acts as the narrator, but the visual B-roll does 80% of the heavy lifting. You understand that satisfying, gross, or highly visual demonstrations (like applying a product to a model or showing physical textures) hold retention better than a talking head.

OPERATING RULES
Visuals dictate the pacing. The voiceover should simply anchor what the user is seeing.
Include a visual pattern interrupt. The first frame must be visually arresting or odd enough to force a pause.
Script the actions, not just the words. Tell the creator exactly what their hands should be doing.
Rely on bizarre, satisfying, or mildly gross pattern interrupts. If applicable, recommend extreme close-ups, anatomical models, or applying textures directly to a surface to force the viewer to stop scrolling.

YOUR TASK
I am giving you a product and an angle. Write a B-Roll + Voiceover script.

SECTION 1: THE VISUAL HOOK
Describe the opening visual loop. What is the hyper-specific, close-up action happening in the first 3 seconds?

SECTION 2: SCRIPT AND SHOT LIST
Format as [Time] | [Visual Action/Text on Screen] | [Voiceover].
Ensure the pacing is fast. Every 3 seconds must feature a visual change, a new texture, or an application of the product.

SECTION 3: CREATOR BRIEFING
Provide 3 bullet points instructing the creator on exactly how to film the B-roll (lighting, angles, close-ups).

SECTION 4: CREATIVE TRACKER NAMING CONVENTION
Output the exact file name string for this ad so I can log it in my tracker. Format it exactly like this:
[1-Word Persona]_[1-2 Word Angle]_[Concept]_[Format]_[Awareness Level]_[Hook Type]

[PASTE PRODUCT DETAILS AND DESIRED ANGLE BELOW]
```

---

## What to feed in

1. Product details: what it is, what it looks like, how it is applied or used, the most visually compelling action it produces
2. The angle (from `templates/angle-bank-builder.md`)
3. The target persona and awareness level
4. Customer language about the product's visual or tactile experience (textures, sensations, before/after visuals)

## What to do with the output

1. Save in `private project script notes` as `[creative-tracker-name].md`.
2. The shot list is the production document. Send the shot list to whoever is filming.
3. Run the voiceover through `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md` before recording.
4. For NB2-generated B-roll variations (when live filming is not feasible), see `references/static-and-animation-pipeline.md`.

## Common mistakes

- A "B-roll" script that is actually a talking-head script with B-roll cutaways. Real B-roll scripts have no talking head. The voiceover is layered over the visual.
- Visual hook that is not visually arresting. "Person opens product" is not a visual hook. "Extreme close-up of skin texture transforming under product application" is.
- Pacing that does not change every 3 seconds. Viewers scroll on static visuals.
- Voiceover that competes with the visual. The voiceover should anchor, not narrate.

## Cross-references

- `references/meta-ads-master-workflow.md`: Phase 3
- `references/script-format-selector.md`: when to pick B-roll over talking head
- `skills/video-scriptwriter/references/long-form-formats.md`: B-roll variant theory
- `references/static-and-animation-pipeline.md`: AI-generated B-roll workflow
- `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md`: voice gate
