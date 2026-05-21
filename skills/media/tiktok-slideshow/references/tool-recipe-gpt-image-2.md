# GPT Image 2 Recipe for TikTok Slideshows

The source playbook's recommended tool. Use this when product text rendering accuracy is critical or when the user explicitly asks for GPT Image 2.

For tool-agnostic principles (reference layers, skin texture, anti-polish, lighting, variants), read [image-prompting-principles.md](image-prompting-principles.md) first.

For the project's default workflow, use [tool-recipe-nb2.md](tool-recipe-nb2.md) instead.

## Why GPT Image 2 specifically

Most AI image models in 2026 still struggle with two specific failure modes that are catastrophic for slideshow production at scale.

### 1. Product text rendering

For product-adjacent slideshows where the product needs to appear visually, packaging text needs to be legible and accurate. Most image models produce garbled or incorrect text on product packaging, which immediately registers as AI to viewers who notice the inconsistency.

GPT Image 2 renders product text accurately. Product reference shots in slideshows show the correct brand name and label content rather than AI-generated approximations.

### 2. Multi-slide consistency

A slideshow needs aesthetic, lighting, and visual style coherence across 6 to 7 independently generated images. Most image models produce strong individual images but fail to maintain the visual coherence across a full slide set.

GPT Image 2's instruction-following capability handles this through the consistent aesthetic baseline in every slide prompt. The model holds the baseline across slides better than most alternatives.

## Loading reference layers in GPT Image 2

GPT Image 2 accepts multimodal inputs (reference images alongside text prompts). Use this to load the character reference, scene reference, and aesthetic baseline.

The mechanism is the same as NB2: load the reference image as multimodal input on every slide that needs it. The model uses the reference as a visual anchor.

For slideshows with a recurring character: load the character reference on every character-included slide.

For slideshows in a consistent environment: load the scene reference on every slide that takes place in the environment.

For slideshows that need both: pass both reference images as multimodal inputs.

## Per-format prompt skeletons

Same beats as the NB2 recipe (Personal Story, Ranked List, Realization, Controversial Opinion, Routine Breakdown). The differences are in how GPT Image 2 prefers prompts to be phrased.

### What GPT Image 2 responds to differently

GPT Image 2 is more responsive to natural-language scene direction than to keyword lists. Where NB2 takes well to keyword-style prompts ("close-up, mirror selfie, warm lighting, oversized t-shirt"), GPT Image 2 produces stronger output from full sentences that direct the scene.

### Sample prompt (Personal Story, slide 1, hook) for GPT Image 2

```
A close-up mirror selfie of a woman in her late twenties holding her phone, taken in her bedroom
in the morning. The light is soft and warm, coming from a window at her left, casting natural
shadows across her face. She is wearing a casual oversized t-shirt and her hair is slightly
tousled from sleep. Her expression is slightly amused, like she just thought of something. The
photo has the realistic skin texture you would see on a real phone selfie: visible pores around
the nose and cheeks, natural slight unevenness, no filter or polish. The framing leaves clean
negative space in the upper third of the image for a text overlay. The aspect ratio is 9:16.
The whole image feels like a real phone photo someone took in their bedroom, not a studio shot.
```

### What works specifically with GPT Image 2

- Full-sentence prompts with explicit scene direction
- Naming the lighting source AND the lighting effect ("light from window at left, casting shadows" rather than just "warm lighting")
- Naming the realism explicitly ("realistic skin texture you would see on a real phone selfie" rather than just "realistic skin")
- Calling out the negative space for text overlay explicitly
- Stating the aspect ratio in the prompt body, not just as a parameter

### What does not work as well with GPT Image 2

- Pure keyword stacking with no narrative direction
- Implicit assumptions ("a typical bedroom" - be specific about which kind)
- Multiple subjects in tight frames (struggles compared to single-subject framing)

## Aspect ratio and resolution

GPT Image 2 supports 9:16 portrait. State the aspect ratio in the prompt body. Resolution defaults are sufficient for TikTok playback.

## Variant generation in GPT Image 2

Generate 6 to 8 variants per slide that includes a human subject. Same selection discipline as in [image-prompting-principles.md](image-prompting-principles.md) under "Generate 6-8 variants for slides with humans".

GPT Image 2's variants tend to vary more in expression and pose than in lighting or composition. This makes the selection step more about reading the moment (which variant feels real) than about matching technical parameters.

## Skin texture phrasing that works specifically with GPT Image 2

GPT Image 2 responds well to descriptive realism rather than specification.

### Instead of (NB2-style)

> "Realistic skin texture, visible pores around nose and cheeks, natural slight unevenness, no filter quality."

### Use (GPT Image 2 style)

> "Her skin has the texture you would see in a real phone selfie: pores visible around her nose and cheeks, natural slight unevenness in tone, no filter or smoothing applied."

The shift to descriptive prose helps the model interpret the realism direction more reliably.

## Anti-polish phrasing that works with GPT Image 2

Same shift from specification to description.

### Instead of

> "Casual phone framing, organic not studio quality."

### Use

> "The photo has the casual feel of a phone shot taken in a real moment, not the polished look of a professional studio image."

## Product context slides

Where GPT Image 2 wins. If the slideshow includes products with packaging text, GPT Image 2 produces accurate text rendering.

### Sample prompt (product context slide)

```
A flat-lay photo of [specific product] sitting on a wood desk, with morning light coming from
a window at the right edge of the frame. The product packaging shows the brand name "[exact brand
name]" in the original typography. The composition leaves negative space in the upper third for
a text overlay. The whole image has the casual feel of a phone shot, not a studio product photo.
The aspect ratio is 9:16.
```

If the product reference is critical, also load the actual product image as multimodal input. GPT Image 2 will hold both the visual identity and the text accuracy.

## Cross-references

- Tool-agnostic principles: [image-prompting-principles.md](image-prompting-principles.md)
- Project default tool recipe: [tool-recipe-nb2.md](tool-recipe-nb2.md)
- Tool comparison: `skills/ads-creative/references/generative-tools.md`

## When to switch back to NB2

If the user is not specifically asking for GPT Image 2, default to NB2. The project's existing infrastructure (`skills/nb2-image-gen/scripts/generate.py`, GEMINI_API_KEY in env, batch script) makes NB2 faster and cheaper to run at slideshow batch volumes.

Switch to GPT Image 2 only when:
- Product text rendering accuracy is critical (product packaging visible in 2 or more slides)
- The user explicitly asks for GPT Image 2
- A test on NB2 produced multi-slide coherence issues that are not fixable by tightening the reference layer architecture
