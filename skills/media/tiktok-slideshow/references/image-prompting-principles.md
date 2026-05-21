# Universal Image Prompting Principles for Slideshows

Tool-agnostic disciplines that apply whether you use Nano Banana 2 or GPT Image 2. The single biggest failure mode of AI-generated slideshows is independently-generated slides that do not share visual coherence. These principles fix that.

For tool-specific recipes, see:
- [tool-recipe-nb2.md](tool-recipe-nb2.md) (Nano Banana 2)
- [tool-recipe-gpt-image-2.md](tool-recipe-gpt-image-2.md) (GPT Image 2)

## The reference layer architecture

Every slide in the same slideshow loads the SAME multimodal references. This is the difference between a slideshow that feels like one intentional piece and a slideshow that feels like six unrelated images stitched together.

Three reference layers:

### 1. Character reference

If the slideshow includes a recurring person, every slide that includes them loads the same character reference image. The upscaled primary reference becomes the visual anchor for every slide that includes the character.

Without this, the model produces six different people across six slides. The viewer reads the inconsistency in the first second as evidence of AI generation.

### 2. Scene reference

For slideshows that take place in a consistent environment (kitchen, bedroom, desk setup), the scene reference establishes the lighting, the spatial context, and the visual baseline that every slide in the same scene shares.

If the slideshow moves between scenes, use a scene reference per scene group, but keep the lighting and color baseline consistent across scene groups.

### 3. Aesthetic baseline

Every slide prompt includes the same aesthetic baseline instruction as a standalone clause. This is the most copy-pasted element of the whole skill. Example:

> "Warm interior lighting, authentic phone selfie or candid lifestyle feel, soft natural framing, organic not studio quality, casual everyday environments."

Adapt the baseline to the slideshow's mood (warm domestic vs cool tech vs golden hour outdoor) but keep it identical across all slides in the same slideshow.

---

## Scene direction over static description

The foundational discipline that separates slideshow output that passes the organic content test from output that registers as AI-generated.

### Bad (static description)

> "A woman taking a selfie."

This produces a generic stock-style image that fails the authenticity test in the first second.

### Good (scene direction)

> "Close-up mirror selfie of a woman in her late 20s holding her phone, soft warm bedroom lighting, casual oversized t-shirt, slightly tousled morning hair, authentic phone photo feel, not studio quality, 9:16 aspect ratio."

This produces output that looks like a real selfie someone actually took. The difference is specificity: who, where, what they are wearing, what the light is doing, what feel.

### How to write scene direction

Answer these questions in the prompt:

- Who is in the frame? (Age range, gender, what they look like)
- Where are they? (Specific environment, not "a room")
- What are they doing? (Specific action, not "posing")
- What are they wearing? (Specific garment + state, not "casual")
- What is the light doing? (Source, direction, quality)
- What is the framing? (Selfie vs candid vs over-the-shoulder)
- What is the feel? (Phone photo, candid lifestyle, organic)

If any of those answers is generic, the slide will be generic.

---

## Skin texture clause (mandatory for any slide with a face)

Every prompt that includes a human face must include a skin texture clause. No exceptions.

### The clause

> "Realistic skin texture, visible pores around nose and cheeks, natural slight unevenness, no filter quality."

### Why this is mandatory

The smooth poreless skin that AI image models default to is the fastest route to viewers clocking the slideshow as synthetic. The model has been trained on heavily filtered images. Without an explicit pull toward realism, it produces filter-style skin every time.

### Adapt for the subject

For male subjects: add "subtle stubble or beard texture, natural skin variation across cheeks and jawline".

For older subjects: add "natural age-appropriate texture, fine lines around eyes, normal skin variation".

For makeup contexts: "natural makeup not heavy, visible skin texture under any base, no airbrushed quality".

The principle is the same. Pull the model away from filter-default toward what real skin looks like in real phone photos.

---

## Anti-polish language

Replaces the produced aesthetic with the organic quality that registers as authentic. Pull the output away from the polished aesthetic that triggers ad skepticism in cold audience viewers.

### The clauses

Pick two or three per prompt, mix and match:

- "Casual phone framing, photographed in a real environment, not a professional set"
- "Organic not studio quality"
- "Slight natural imperfections in framing"
- "Phone camera quality, not DSLR"
- "Candid lifestyle feel, not posed"
- "Real phone photo, not produced content"
- "Casual everyday quality, no professional finishing"

### When to use each

Use "phone framing" + "phone camera quality" + "candid" for selfie-style slides.

Use "organic not studio" + "real environment" + "no professional finishing" for product or scene shots.

Use "candid lifestyle feel, not posed" + "natural imperfections" for shots with multiple people or social settings.

### What this fights

Without these clauses, the model produces content that looks like an ad. Polished, lit, framed. Viewers in 2026 have learned that polished = ad = skip. Anti-polish language pulls the slide back toward content that reads as native to the platform.

---

## Lighting as a dedicated clause

Lighting controls mood more than any other variable in image generation. Treat it as a standalone element in every prompt that includes a human subject. Do not bury it in a list of other scene elements.

### The structure

> "[Source] light from [direction], casting [shadow quality], [time-of-day quality], [exposure note]."

### Examples

> "Soft warm bedroom light from window at left, casting natural shadows, golden hour quality, no harsh highlights, skin properly illuminated without overexposure."

> "Cool morning light from a north-facing kitchen window, soft even shadows, daytime quality, evenly lit subject without flash."

> "Single warm desk lamp from upper right, deep ambient shadows, late evening quality, subject's face lit but room slightly dark."

### Why dedicated

If you write "warm interior lighting, casual oversized t-shirt, slightly tousled hair", the model averages the lighting against the other scene elements. If you write "Soft warm bedroom light from window at left, casting natural shadows" as its own clause, the lighting controls the whole image. Mood follows.

---

## Generate 6-8 variants for slides with humans

The range of quality across variants from a single prompt is significant. The weakest variant might have skin texture issues, expression problems, or compositional flaws that immediately register as AI-generated. The strongest variant passes the realism test in the first 2 seconds.

### The discipline

For every slide that includes a human subject, generate 6 to 8 variants from the same prompt and select the strongest. Do not accept the first output. The selection step is what gets the slideshow from "passes a casual look" to "passes the swipe test on the platform".

### What to look for in selection

Reject any variant with:
- Garbled hands or hand-prop interactions (especially holding phones, products)
- Skin that still reads filtered despite the texture clause
- Eyes that point in slightly different directions
- Background props that contain garbled text
- Compositions that crop awkwardly at 9:16
- Expressions that read as fake or AI-emotional (too symmetric, too neutral, too "stock")

Accept variants where:
- Hands look right
- Skin has visible texture and natural variation
- The subject's gaze is coherent
- Background reads as the actual scene (kitchen looks like a kitchen)
- The 9:16 framing puts the subject in the upper third or center
- The expression reads as a real moment

### When the prompt cannot produce a usable variant

Adjust the prompt before regenerating. Common fixes:
- Add "natural expression, not posed, mid-action moment" if expressions read as stock
- Add "hands relaxed at sides, no objects in hands" if hand artifacts keep appearing
- Switch the framing ("over-the-shoulder" instead of "front-facing") if compositions feel staged
- Tighten the scene description (add a specific prop, a specific time of day, a specific location detail)

Each prompt adjustment costs one round of generation. Worth it. A slideshow with one obviously-AI slide drops the perceived quality of the whole piece.

---

## TikTok specifications

Every slide gets generated at the correct specifications for TikTok slideshows.

### Aspect ratio and resolution

- Aspect ratio: 9:16 portrait
- Resolution: 1080 x 1920 pixels

This matches TikTok's native vertical format and ensures the slideshow displays correctly in the feed without cropping that would lose critical visual elements.

### Text overlay positioning

Place text in the upper third or center of the frame. Viewer attention enters the frame from the top when they swipe to a new slide. Text overlaid in the bottom third risks being cut off on devices with different display configurations, and viewers' eyes do not naturally land there first on slideshow content.

### Caption styling

Bolder, simpler text overlays that match TikTok's native content aesthetic. Higher contrast, larger text size, more prominent positioning than equivalent Instagram carousel caption styling. The platform-native expectation is more aggressive visual messaging than Instagram's restrained Stories aesthetic.

When generating the image, leave clean negative space in the upper third or center for text overlay. Do not have the model render the slideshow text inside the image (text rendering is unreliable, and the overlay text needs to be editable in the slideshow editor anyway).

---

## The single biggest failure mode

Operators generate slide 1 from one prompt, slide 2 from another prompt, slide 3 from a third prompt. They end up with a slideshow that has six individually high-quality images that do not feel like they belong in the same piece.

The visual coherence breaks across slides. The algorithm reads the inconsistency as evidence the content is not intentional.

The fix is the reference layer architecture above. Same character ref, same scene ref, same aesthetic baseline across every slide in the same slideshow. The slides should look like they were taken on the same phone in the same hour by the same person.

### Quick coherence check before posting

Look at all slides side by side. Ask:

1. Does the subject look like the same person in every slide?
2. Does the lighting feel like the same time of day?
3. Does the environment read as the same place (or a coherent set of places)?
4. Does the color temperature match across slides?
5. Does the framing style stay consistent (all phone selfies, or all candid, not mixed)?

If any answer is no, regenerate the offending slide before posting. The slideshow is judged as a single piece, not as six separate images.
