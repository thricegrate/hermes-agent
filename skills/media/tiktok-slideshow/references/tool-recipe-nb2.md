# Nano Banana 2 Recipe for TikTok Slideshows

The project's default image generation tool. This file covers the slideshow-specific deltas on top of the general NB2 prompt engineering documented in `skills/nb2-image-gen/SKILL.md`. Read that skill first for the formula, the API call patterns, and the batch script.

For tool-agnostic principles (reference layers, skin texture, anti-polish, lighting, variants), read [image-prompting-principles.md](image-prompting-principles.md) first.

## Why NB2 for slideshows

- Strong text rendering when product packaging or product context appears in a slide
- Image grounding for real-world references (useful when the slideshow includes specific products or environments)
- Product image reference via `inlineData` is the right mechanism for the character + scene + aesthetic reference layer architecture
- Project already has `skills/nb2-image-gen/scripts/generate.py` for batch generation

## Loading reference layers in NB2

NB2 accepts reference images via `inlineData`. Use this as the multimodal input that anchors every slide in the slideshow.

### Single-character slideshow

Every slide that includes the character loads the same character reference as `inlineData`. The reference image becomes the visual anchor.

In the prompt JSON:

```json
{
  "prompt": "Close-up mirror selfie of [character description from reference], soft warm bedroom lighting, casual oversized t-shirt, slightly tousled morning hair, authentic phone photo feel, not studio quality. Realistic skin texture, visible pores around nose and cheeks, natural slight unevenness, no filter quality. 9:16 aspect ratio.",
  "reference_image": "path/to/character_ref.png",
  "aspect": "9:16"
}
```

Run the same character reference across every character-included slide in the batch. The model holds the character identity across slides.

### Scene-anchored slideshow

If the slideshow stays in one environment, also load a scene reference. Some slides may use only the scene reference (no character), some use both.

```json
{
  "prompt": "Wide phone-camera shot of the kitchen counter from the same scene, morning light from window at left, organic everyday quality. 9:16 aspect ratio.",
  "reference_image": "path/to/scene_ref.png",
  "aspect": "9:16"
}
```

When using both character and scene references, NB2 handles multiple `inlineData` inputs. Pass both in the request. Test with 2 to 3 variants to confirm the model is honoring both anchors.

## Per-format prompt skeletons

Each skeleton fills the universal disciplines (skin texture, anti-polish, lighting, 9:16) and adapts the framing to the format's narrative beats.

### Personal Story skeleton

Slides typically alternate between selfie-style "moment" shots and candid "context" shots. Example slide breakdown for a 7-slide personal story:

- Slide 1 (hook): Selfie of subject with text overlay space at top. Energy: slight drama or curiosity.
- Slide 2 (the before): Candid wide shot of the "before" context. Subject smaller in frame, environment doing more work.
- Slide 3 (the discovery): Selfie or close-up of the moment of realization. Tighter framing.
- Slide 4 (the mechanism): Candid shot of the mechanism in action (the routine, the tool, the process).
- Slide 5 (mid-result): Mirror or environment shot showing change.
- Slide 6 (final result): Selfie or proof shot. Subject visibly different state from slide 1.
- Slide 7 (CTA): Either continuation of slide 6 framing or a fresh "to-camera" CTA shot.

Use the same character reference across all selfie/character slides. Use a scene reference for slides 2, 4, 5 if the environment matters.

Sample prompt (slide 1, hook):

```
Close-up mirror selfie of [character description], holding her phone, slightly amused expression,
soft warm bedroom light from window at left casting natural shadows, golden hour quality,
casual oversized t-shirt, slightly tousled hair. Realistic skin texture, visible pores around
nose and cheeks, natural slight unevenness, no filter quality. Phone camera framing, organic
not studio quality. Clean negative space in upper third for text overlay. 9:16 aspect ratio.
```

### Ranked List skeleton

Slides 2 through N each show one item being ranked. The item is the focal element, the subject is secondary or absent.

- Slide 1 (theme): Subject introduces the list. Selfie or to-camera framing.
- Slides 2-6 (items 5-2): Each slide centers the item being ranked. If items are products, render the product. If items are concepts, use a representative environment or prop.
- Slide 7 (item 1): The reveal. Most dramatic framing of the batch. Often a hero shot of the top item.

Sample prompt (slide for an item being ranked):

```
Hero shot of [item description] on a desk surface, soft warm afternoon light from window at right,
shallow depth of field, organic phone-photo quality, casual everyday environment, no studio finishing.
Clean negative space in upper third for text overlay. 9:16 aspect ratio.
```

For product items, load the product image as a reference via `inlineData` so NB2 renders the product accurately.

### Realization skeleton

Slides progress emotionally. Framing tightens as the realization deepens. Often selfie-heavy.

- Slide 1 (the moment): Tight selfie or close-up. Pensive or searching expression.
- Slides 2-5: Continue the search. Each slide is a beat of the realization. Subject often in same environment, slight framing changes.
- Final slide: Subject in resolution. Different lighting quality (warmer, brighter) signals the lift.

Use a single character reference across the whole slideshow. Subtle scene shifts work better than dramatic location changes for this format.

Sample prompt (slide 3, mid-realization):

```
Three-quarter close-up of [character description] looking thoughtful, gaze slightly off-camera,
soft warm bedroom light from window at left, late afternoon quality, casual t-shirt, hair down.
Realistic skin texture, visible pores around nose and cheeks, natural slight unevenness, no filter
quality. Phone camera framing, candid lifestyle feel, not posed. Clean negative space in upper
third for text overlay. 9:16 aspect ratio.
```

### Controversial Opinion skeleton

Subject is more confrontational on camera. Framing is direct. Eye contact with camera matters.

- Slide 1 (the position): Direct-to-camera framing. Confident expression.
- Slides 2-6 (the defense): Continue direct framing. Subject more animated.
- Final slide: Subject in calm conviction. Either looking down or away (closing the argument) or directly at camera (calling out the discussion).

Sample prompt (slide 1, the position):

```
Direct-to-camera waist-up shot of [character description], confident expression, slight half-smile,
soft warm interior light from window at left, late morning quality, casual t-shirt or hoodie.
Realistic skin texture, visible pores around nose and cheeks, natural slight unevenness, no filter
quality. Phone-held framing, organic not studio quality. Clean negative space in upper third for
text overlay. 9:16 aspect ratio.
```

### Routine Breakdown skeleton

One step per slide. Each slide shows the step in action. Can be subject-led (subject performing the step) or environment-led (the result of the step shown without the subject).

- Slide 1 (theme): Subject introduces the routine. Wide-ish shot of the environment. Subject in frame.
- Slides 2-6 (steps): Each slide centers the step. Mix of subject-in-action and environment-of-result.
- Final slide: Subject reflective or proof shot. Either showing the routine working or a CTA.

Sample prompt (a step in a morning routine):

```
Close-up over-the-shoulder shot of [character description] pouring coffee into a mug at a kitchen
counter, soft cool morning light from a north-facing window, daytime quality, casual home environment.
Realistic skin texture on visible hand and arm, natural variation, no filter quality. Phone camera
framing, candid lifestyle feel, organic not studio quality. Clean negative space in upper third
for text overlay. 9:16 aspect ratio.
```

## Aspect ratio handling for 9:16 in NB2

NB2 supports 9:16 natively. Pass `--aspect 9:16` in the CLI or `"aspect": "9:16"` in the JSON. NB2 also supports extreme aspect ratios (1:8 to 8:1) but 9:16 is the right call for TikTok slideshows.

Resolution defaults are sufficient for TikTok playback. Do not upscale before posting unless the slideshow needs to render at full quality on a high-DPI test device.

## Batch generation pattern

For a 7-slide slideshow, generate all 7 slides in one batch using the project's batch script:

```bash
python skills/nb2-image-gen/scripts/generate.py \
  --batch slideshow_prompts.json \
  --output ./slideshows/[slideshow-name]/ \
  --count 6
```

Where `slideshow_prompts.json` contains an array of 7 prompt objects (one per slide), and `--count 6` generates 6 variants per slide.

For each slide, review the 6 variants and select the strongest. Move the selected variant to a `final/` subdirectory with a clear filename like `01-hook.png`, `02-context.png`, ..., `07-cta.png`.

If a slide cannot produce a usable variant after one batch, adjust the prompt (see [image-prompting-principles.md](image-prompting-principles.md) under "When the prompt cannot produce a usable variant") and regenerate just that slide.

## Variant selection workflow

For slides with humans:

1. Generate 6 variants with the same prompt
2. Open all 6 in a viewer side by side
3. Reject any with hand artifacts, garbled props, expression issues, or skin that still reads filtered
4. Of the remaining variants, pick the one whose framing leaves the cleanest text overlay space
5. If 2 variants are equally strong, pick the one whose lighting matches the rest of the slideshow most closely

For slides without humans (product hero, environment-only, prop):

1. Generate 4 variants (the hand/face problems do not apply, so fewer variants are needed)
2. Reject any with garbled text on packaging, awkward composition, or color cast that breaks slideshow coherence
3. Pick the variant whose framing leaves cleanest negative space

## Cross-references

- General NB2 prompt engineering, API setup, batch script: `skills/nb2-image-gen/SKILL.md`
- Tool comparison (NB2 vs GPT Image 2 vs others): `skills/ads-creative/references/generative-tools.md`
- Tool-agnostic principles: [image-prompting-principles.md](image-prompting-principles.md)
- GPT Image 2 alternative recipe: [tool-recipe-gpt-image-2.md](tool-recipe-gpt-image-2.md)
