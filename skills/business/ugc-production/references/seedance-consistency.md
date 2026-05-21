# Seedance 2.0 Consistency Patterns for Variation Sets

The single biggest production failure mode in the Winner Variation Pipeline is visual drift across the 25 hooks (or 12 bodies, or 10 CTAs). When a hook clip and the body clip it gets assembled with do not share the same character look, scene baseline, or wardrobe, the assembled reel breaks at the cut. The viewer reads the discontinuity as evidence the reel is synthetic and bounces.

This file covers how to keep Seedance 2.0 outputs consistent across a variation set.

For the broader generative-tool comparison and Seedance positioning, see `skills/ads-creative/references/generative-tools.md`.

## The drift problem

Seedance 2.0 produces strong individual clips. Strong clips with no discipline across a variation set produce a library of 25 hooks where:

- Character A in hook 1 looks subtly different from character A in hook 7 (face angle, age, build)
- Hook 12 has a different lighting tone (cool vs warm) than hooks 1-11
- Hook 18 has the character in different wardrobe (t-shirt vs hoodie)
- Hook 21 is in a different room than the rest

Each clip is internally fine. The variation set is unusable because the clips do not match each other. When hooks 1-11 are assembled with body 3, the character looks consistent. When hook 18 is assembled with body 3, the character "changes outfit" mid-reel. The viewer drops.

The fix is reference discipline at the production stage.

## The 3-layer reference architecture for variation sets

Same as the slideshow image-prompting principles. The same character ref + scene ref + aesthetic baseline runs across every clip in the variation set.

### Layer 1: Character reference

A locked-in character reference image (or short clip) loaded as multimodal input on every Seedance generation in the variation set. Seedance 2.0 supports up to 12 reference files per generation.

The character reference should be:
- A clean image of the character from the original validated reel
- Front-facing or three-quarter angle (the angle Seedance will hold most reliably)
- The wardrobe from the original (or the wardrobe family the variation set will use)
- The lighting condition that matches the variation set's baseline

If the original validated reel had multiple character angles, pick the one that is the canonical "rest state" for the character. That becomes the anchor reference.

### Layer 2: Scene reference

A locked-in scene reference image. Loaded on every generation alongside the character reference.

The scene reference establishes:
- The environment (kitchen, bedroom, gym, office)
- The lighting source and direction
- The color palette of the room
- Any anchoring props (specific furniture, plants, objects in frame)

If the variation set spans multiple scenes (rare, usually a single scene baseline is best), use one scene reference per scene group and run all variations within a scene group as a sub-batch.

### Layer 3: Aesthetic baseline clause

The same aesthetic baseline clause appears in every Seedance prompt in the variation set. Identical wording. Adapt to the original reel's aesthetic but lock it across the set.

Example baseline clause for a kitchen-scene weight management variation set:

```
Natural daylight from window at left, warm interior tones, casual home environment, organic
phone-camera quality not produced studio quality, slight handheld feel, casual everyday wardrobe,
subject's natural skin texture visible.
```

This clause does not change between generations. It is the third anchor that holds the visual coherence.

## The full Seedance prompt structure for variation clips

Each clip in the variation set follows this structure:

```
[OPENING SCENE DIRECTION specific to this clip]
[CHARACTER REFERENCE: load image]
[SCENE REFERENCE: load image]
[AESTHETIC BASELINE CLAUSE: identical across set]
[LIGHTING CLAUSE: identical across set unless intentional time-of-day shift]
[CLIP DURATION SPEC: 3-5 seconds for hooks, longer for bodies/CTAs as designed]
[VOICE NOTE: voice register matches the original reel]
```

Example (hook variation 7, specificity hook category, weight management variation set):

```
Subject sits at kitchen counter holding a coffee mug, looks up at camera, says: "I lost 23 pounds
in 11 weeks doing this." Natural reaction, slight half-smile after the line lands. 4 seconds.

[Character reference: weight-mgmt-character-ref.png]
[Scene reference: weight-mgmt-kitchen-scene-ref.png]

Aesthetic baseline: Natural daylight from window at left, warm interior tones, casual home
environment, organic phone-camera quality not produced studio quality, slight handheld feel,
casual everyday wardrobe, subject's natural skin texture visible.

Lighting: Natural daylight from a window at left of the frame, casting soft shadows on the
right side of the subject's face, late morning quality.

Voice register: Calm authority, conversational pacing, slightly understated tone matching the
original reel.
```

The opening scene direction (top of the prompt) is the only part that changes between hook variations. Everything else (character ref, scene ref, aesthetic baseline, lighting, voice register) stays identical across all 25 hooks.

## Consistency checks before assembly

Before assembling any of the 1,000+ filtered combinations, run these consistency checks across the produced clips.

### 1. Character coherence

Open all 25 hook clips side by side. Does the character look like the same person across all clips? Pay attention to:
- Face shape and structural features
- Hair style and color
- Build and posture
- Wardrobe (top garment must match across hooks)

Reject any clip where the character has drifted. Regenerate it with the character reference re-loaded and a tighter character description in the prompt.

### 2. Scene coherence

Does the environment look the same across all clips? Pay attention to:
- Background props and furniture
- Color tone of the room
- Lighting source direction
- Time of day implied by the lighting

Reject any clip where the scene drifted. Regenerate with the scene reference re-loaded.

### 3. Lighting coherence

Does the lighting feel like the same time of day and the same source direction across all clips?

Reject any clip where lighting drifted. Lighting drift is the most common subtle discontinuity that breaks the assembled reel.

### 4. Wardrobe coherence

Is the character wearing the same clothing in every clip? If the original reel had the character in a t-shirt, every variation must have the character in the t-shirt (or the same wardrobe family if intentional change).

Reject any clip where wardrobe drifted. This is the easiest discontinuity for viewers to spot.

## When a Seedance generation drifts

Common fixes:

### Reload references with stronger weighting

Some prompts produce drift because the references are not weighting heavily enough. Re-run the generation with the references re-uploaded. If Seedance offers a reference weighting parameter (check current API), increase it.

### Tighten the character description in the prompt

Even with the reference loaded, adding a short text description of the character's key features anchors the generation. Example:

> "Mid-40s man with short brown hair, slight beard, wearing a charcoal t-shirt"

The text description plus the reference image is more reliable than the reference image alone.

### Use a previously-validated clip as the reference instead of an image

Seedance 2.0 accepts video reference inputs. If the first hook clip generated cleanly, use it as the character/scene reference for subsequent hooks instead of the original static image. The video reference holds character motion and behavior more reliably.

### Reduce variation count per scene group

If 25 hooks all in the same scene are too many for Seedance to hold consistency, split into 2 sub-batches of 12-13. Generate the first sub-batch, validate consistency, then use a clip from the validated first batch as the reference for the second sub-batch.

## Variant generation per clip

For each clip in the variation set, generate 3 to 4 variants and select the strongest. Same discipline as in the tiktok-slideshow image-prompting workflow.

Reject variants where:
- Character drifted
- Scene drifted
- Lighting drifted
- Wardrobe drifted
- The voice delivery sounds off (Seedance's audio + visual sync issues)
- Hand or prop interactions look garbled
- The subject's expression reads as fake or unnatural

Accept variants where the clip plugs cleanly into the variation set without breaking continuity.

## Why this matters more for the variation pipeline than for fresh reels

When producing a fresh reel from scratch, drift across clips matters less. The reel is a single piece. The viewer reads the whole thing as one unit.

When producing a variation set where 25 hooks need to plug into 12 bodies need to plug into 10 CTAs, drift compounds. Every break point (hook-to-body cut, body-to-CTA cut) is a chance for visual discontinuity. A single drifted hook ruins all the assembled reels that use that hook.

The variation pipeline is a multiplier. Visual coherence is a multiplier. Drift is the divisor that collapses the multiplier.

## Cross-references

- Pipeline overview: [winner-variation-pipeline.md](winner-variation-pipeline.md)
- Hook variations (which need consistent character clips): [hook-variation-categories.md](hook-variation-categories.md)
- Body variations: [body-variation-framings.md](body-variation-framings.md)
- CTA variations: [cta-variation-types.md](cta-variation-types.md)
- Generative tool comparison (Seedance vs alternatives): `skills/ads-creative/references/generative-tools.md`
- AI avatar video generation (alternative to Seedance for the avatar layer): `skills/jogg-ai/SKILL.md`
- ElevenLabs voice production (the voice that pairs with the visual variations): `skills/elevenlabs/SKILL.md`
