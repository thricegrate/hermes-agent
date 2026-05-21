# Master Prompts by Platform

Six prompts in one template:

1. TikTok video master prompt
2. Instagram Reels master prompt
3. YouTube Shorts master prompt
4. Facebook Reels master prompt
5. Cross-platform parallel generation prompt (all 4 platforms in one Claude session)
6. Whole-script variation prompt (5-6 variations from a winner, per platform)

For the upstream 3-input brief, see [../references/cross-platform-brief-structure.md](../references/cross-platform-brief-structure.md).

For the platform calibration variables these prompts apply, see [../references/platform-calibration-variables.md](../references/platform-calibration-variables.md).

For the weekly cross-platform intelligence layer that updates the brief, see [../references/cross-platform-intelligence.md](../references/cross-platform-intelligence.md).

## Before running any of these prompts

The 3-input brief must be loaded into the Claude session FIRST:

```
SYSTEM CONTEXT (loaded once per session):

# AUDIENCE INSIGHT STATEMENT
[Paste the full audience insight statement, verbatim phrases included]

# PRODUCT BRIEF
- Unique mechanism: [specific articulation]
- Specific proof points: [list with timelines and numbers]
- Price point and offer: [retail price + offer structure]

# STRUCTURAL REFERENCE
[Paste the annotated competitor transcript with structural labels: HOOK, PAIN, MECHANISM BRIDGE,
PRODUCT INTRODUCTION, PROOF, CTA]
```

Once loaded, run any of the prompts below.

## Prompt 1: TikTok Video Master Prompt

```
Using the persona document, product brief, and structural reference loaded above, write a TikTok
video script.

Duration: 15 to 25 seconds.

Format follows this structure:
- Hook in the first 2 to 3 seconds using the specificity hook category (timeline + specific failed
  behavior + emotional state)
- Pain section spending the majority of the script duration acknowledging specific failed
  alternatives the viewer has tried
- Mechanism bridge explaining why those alternatives could not work
- Product introduction as discovery rather than announcement
- Proof element with specific number or timeline
- CTA naming a specific person archetype to share with rather than generic share prompt

Voice rules:
- Pull verbatim phrases from the audience insight statement
- No em dashes
- No "obsessed", "game-changing", "transformational"
- No "It's not X, it's Y" structures
- Short sentences, conversational tone
- Read every line aloud test: if a creator could not say it naturally, rewrite

Include the complete Seedance 2.0 generation prompt in brackets at the end, with:
- Scene direction
- Character demographic matching the persona (and skewing slightly younger for TikTok if the
  audience insight allows)
- Lighting specification (dedicated clause)
- Camera framing
- Emotional arc specification
- Skin texture specification (realistic skin texture, visible pores, natural variation, no filter
  quality)
- Anti-polish language (organic phone-photo quality not studio quality)
- Standing technical specifications (9:16 portrait, 1080x1920, clean negative space in upper third
  for text overlay)

Include trending audio guidance:
- Specify whether the script leaves space for trending audio overlay or whether the voiceover
  carries the full audio
- If trending audio overlay: identify the emotional register the trending audio should match

Output:
- The full script with each line numbered
- The Seedance 2.0 prompt in brackets
- The trending audio guidance
- Estimated runtime (in seconds, calibrated to 2.5-3 words per second)
```

## Prompt 2: Instagram Reels Master Prompt

```
Using the persona document, product brief, and structural reference loaded above, write an
Instagram Reels script.

Duration: 18 to 30 seconds.

Format follows the same structural arc as TikTok (hook, pain, mechanism, product, proof, CTA) but
with these calibration adjustments:
- The CTA shifts to drive saves and/or comment funnel entries rather than DM shares
- Stack the CTA: a specific keyword drop AND a substantive prompt that produces longer comment
  threads
- Example: "Comment ROUTINE for the full setup AND tell me which step you skip on busy days"

Voice rules: same as TikTok prompt above.

Include the complete Seedance 2.0 generation prompt in brackets at the end with the same technical
specifications as TikTok.

Caption styling notes:
- Bold text on semi-transparent dark background
- Positioned in the bottom third of the frame for natural reading patterns
- Caption length: 100-200 characters

Output:
- The full script with each line numbered
- The Seedance 2.0 prompt in brackets
- The caption text (100-200 characters)
- The text overlay styling notes
- Estimated runtime
```

## Prompt 3: YouTube Shorts Master Prompt

```
Using the persona document, product brief, and structural reference loaded above, write a YouTube
Shorts script.

Duration: 30 to 45 seconds.

Format follows the same structural arc but with these calibration adjustments:
- The CTA includes a subscribe prompt because subscribe rate is the primary distribution signal
  YouTube weights
- The subscribe prompt should feel natural rather than aggressive, integrated into the closing
  rather than as a hard sales close
- Example: "Subscribe for the full series on this exact problem" or "Hit subscribe if you want
  the science behind this"

Voice rules: same as TikTok prompt above.

Also generate the YouTube Shorts associated metadata:
- Title (60 characters maximum, optimized for search and click-through)
- Description first 150 characters (which appear above the fold and serve as additional motivation
  for the click and the watch)
- Longer description body (200-400 words) with relevant SEO keyword density
- Thumbnail concept: a single subject in the foreground with clear focal point, high contrast colors
  visible against YouTube's dark UI, emotional facial expression, minimal text overlay

Include the complete Seedance 2.0 generation prompt in brackets at the end with the same technical
specifications.

Output:
- The full script with each line numbered
- The Seedance 2.0 prompt in brackets
- The Title (≤60 characters)
- The Description first 150 characters
- The longer Description body (200-400 words)
- The Thumbnail concept (1 sentence)
- Estimated runtime
```

## Prompt 4: Facebook Reels Master Prompt

```
Using the persona document, product brief, and structural reference loaded above, write a Facebook
Reels script.

Duration: 25 to 45 seconds (Facebook tolerates slightly longer content than Instagram).

Format follows the same structural arc but with these calibration adjustments for the older
demographic Facebook reaches:
- Less casual slang
- More conversational warmth
- More measured pacing
- Avoidance of language patterns that read as overly young
- The avatar demographic in the Seedance prompt should be in the 40s or 50s rather than late 20s
  or early 30s
- The audio approach calibrates to calmer, more measured vocal performance rather than the
  high-energy delivery that drives TikTok engagement
- The CTA prompts substantive comment responses rather than emoji reactions or keyword drops
  (Facebook's algorithm weights substantive comment engagement heavily)

Caption length: 3 to 5x longer than equivalent Instagram or TikTok captions (300-600 characters).
The longer caption format includes more specific detail, more context, and direct invitation to
engage.

Voice rules: same as TikTok prompt above, with the additional calibration for measured pacing and
warmth.

Include the complete Seedance 2.0 generation prompt in brackets at the end with:
- Avatar in their 40s or 50s
- Calmer emotional arc, less peak-energy
- Same technical specifications (9:16, lighting, skin texture, anti-polish)

Output:
- The full script with each line numbered
- The Seedance 2.0 prompt in brackets (with older avatar demographic explicitly noted)
- The longer caption text (300-600 characters)
- Estimated runtime
```

## Prompt 5: Cross-Platform Parallel Generation Prompt

Use this when you want all 4 platform variants of the same content concept in one Claude session.
Saves 75% of the time vs running 4 sequential prompts.

```
Using the persona document, product brief, and structural reference loaded above, generate scripts
for all 4 platforms simultaneously based on this single concept:

CONCEPT ANGLE:
[Describe the specific concept being executed across all 4 platforms. Include: the specific pain
point being addressed, the specific mechanism being introduced, the specific proof point being
delivered, and the specific transformation being promised. This is the underlying strategic angle
that stays constant across platforms.]

Apply the platform-specific calibration variables for each platform:

TIKTOK (15-25 seconds):
- Specificity hook in first 2-3 seconds
- DM share CTA naming a specific person archetype
- High-contrast text overlay aesthetic
- [Trending audio overlay / Voiceover-only]: [pick one]

INSTAGRAM REELS (18-30 seconds):
- Same structural arc
- Save-driving CTA + comment funnel keyword (stacked)
- Stories-aesthetic text overlay
- Voiceover-only

YOUTUBE SHORTS (30-45 seconds):
- Same structural arc, slightly more education-tolerant pacing
- Integrated subscribe CTA at close
- Generate Title (≤60 chars), Description first 150 chars, longer description body, thumbnail concept
- Voiceover-only

FACEBOOK REELS (25-45 seconds):
- Same structural arc with calmer, warmer tone for older audience
- Substantive comment prompt CTA
- Avatar demographic shifted to 40s/50s
- Caption 3-5x longer than IG/TT
- Voiceover-only, measured pacing

For each platform, output:
- The full script (numbered lines)
- The Seedance 2.0 generation prompt in brackets (with platform-appropriate avatar demographic)
- Platform-specific metadata (caption for IG/FB, title+description+thumbnail for YT, audio
  guidance for TikTok)
- Estimated runtime

Voice rules for ALL 4 platforms:
- Pull verbatim phrases from the audience insight statement
- No em dashes
- No "obsessed", "game-changing", "transformational"
- No "It's not X, it's Y" structures
- Short sentences
- Read aloud test must pass
- The mechanism enters before the product
```

The output is 4 complete platform-specific scripts ready for production. A single 60-minute Claude session running this prompt 5-6 times produces 20-24 platform-specific scripts (5-6 concepts × 4 platforms).

## Prompt 6: Whole-Script Variation From a Winner (per platform)

When a script has performed strongly on any platform, generate 5-6 variations from the single winner.

This is the LITE variation pattern. For component-level variation that turns 1 winner into 1000+ combinations via hook + body + CTA component swapping, see [variation-from-winner-reel.md](variation-from-winner-reel.md). Use the lite pattern below for fast iteration; use the component-level pipeline for the strongest winners that deserve full multiplication.

```
The following script performed well based on the performance data attached:

[Paste the winning script in full, including the Seedance prompt and platform metadata]

Performance data:
- Platform: [TikTok / Instagram Reels / YouTube Shorts / Facebook Reels]
- Hook rate: [percentage]
- Hold rate: [percentage]
- CPA: [dollar amount]
- View count and reach: [numbers]
- Posting time and audio used: [if applicable]

Write 5 variations of this script for [platform name].

Each variation must:
- Maintain the format structure (same beat sequence, same duration target)
- Maintain the emotional register (same mood, same tonal arc)
- Maintain the overall narrative arc (same emotional shape)
- Preserve the closing structure (same CTA architecture)
- Preserve the duration

Each variation must change:
- The specific personal story details (different number, timeline, specific event)
- The visual pairing notes in the Seedance prompt (different scene, different framing, but same
  aesthetic baseline)
- The hook line wording (same structure, different specifics)
- The body content (different beats inside the same arc)

Each variation should target a slightly different segment within the broader persona than the
original. The original may have hit one specific pain point. Variations can hit adjacent pain
points using the same emotional shape.

For each variation, output:
- The variation number and a one-sentence note on which segment it targets
- The full script (numbered lines)
- The updated Seedance 2.0 generation prompt in brackets (with the changed visual pairing notes)
- Platform metadata (caption / title+description / audio guidance, updated as needed)

Voice rules: same as the master prompts (no em dashes, no banned phrases, customer-language
priority, read-aloud test).
```

The 5-6 variations preserve the performance signal (the structural and emotional elements that drove engagement) while exploring different audience segments within the broader persona. The algorithm sees enough variation between accounts (or posting windows) that nothing reads as duplicate.

## When to use which prompt

| Situation | Prompt to use |
|---|---|
| Need a single TikTok script | Prompt 1 |
| Need a single Instagram Reels script | Prompt 2 |
| Need a single YouTube Shorts script | Prompt 3 |
| Need a single Facebook Reels script | Prompt 4 |
| Need scripts for all 4 platforms from one concept | Prompt 5 (parallel generation) |
| A script has performed; want lite variations | Prompt 6 |
| A script has performed strongly; want component-level multiplication | [variation-from-winner-reel.md](variation-from-winner-reel.md) |

For weekly intelligence that decides WHICH content concepts get put through these prompts, see [../references/cross-platform-intelligence.md](../references/cross-platform-intelligence.md).

## Common failure modes

### Running each platform's prompt in a separate Claude session

Loses the cross-platform context. The brief gets paid for in tokens 4 times. Cross-platform pattern recognition does not happen because each session sees only one platform.

**Fix**: load the brief once, then run multiple prompts (or the parallel generation prompt) within the same session.

### Skipping the brief load

If the 3-input brief is not loaded, the master prompts produce generic scripts that read like marketing copy.

**Fix**: always load the brief BEFORE running any master prompt. The brief is the foundation; the master prompts are calibration on top.

### Treating Facebook Reels like Instagram Reels

The older Facebook audience requires materially different calibration (avatar demographic, pacing, caption length, CTA style). Reusing the Instagram prompt for Facebook produces underperforming Facebook content.

**Fix**: use Prompt 4 (Facebook-specific) for Facebook Reels generation. Do not adapt Instagram output.

### Skipping the Seedance prompt

Some operators run the master prompts and only use the script output, generating Seedance prompts manually. This wastes the calibration work and produces avatar/scene mismatches.

**Fix**: always include the Seedance prompt instruction in the master prompt. Use the generated Seedance prompt as the production input.

### Running the parallel generation prompt without specifying the concept angle

If the concept angle is fuzzy, the parallel generation produces 4 fuzzy scripts. The platform calibration cannot save a weak underlying concept.

**Fix**: lock the concept angle (specific pain, specific mechanism, specific proof, specific transformation) before running parallel generation. The concept angle is the constant; the platform calibration is the variable.

## Cross-references

- 3-input brief structure: [../references/cross-platform-brief-structure.md](../references/cross-platform-brief-structure.md)
- Platform calibration variables: [../references/platform-calibration-variables.md](../references/platform-calibration-variables.md)
- Cross-platform intelligence (weekly synthesis): [../references/cross-platform-intelligence.md](../references/cross-platform-intelligence.md)
- Component-level variation pipeline (for strongest winners): [variation-from-winner-reel.md](variation-from-winner-reel.md)
- Component-level variation references:
  - [../references/winner-variation-pipeline.md](../references/winner-variation-pipeline.md)
  - [../references/hook-variation-categories.md](../references/hook-variation-categories.md)
  - [../references/body-variation-framings.md](../references/body-variation-framings.md)
  - [../references/cta-variation-types.md](../references/cta-variation-types.md)
  - [../references/compatibility-matrix.md](../references/compatibility-matrix.md)
- Seedance consistency patterns (for the Seedance prompts in each script): [../references/seedance-consistency.md](../references/seedance-consistency.md)
- Direct-response voice rules: `skills/video-scriptwriter/references/direct-response-voice-system.md`
- Hook engineering (5 levers + scoring): `skills/video-scriptwriter/references/hook-engineering.md`
- Anti-AI script tells: `skills/video-scriptwriter/references/anti-ai-script-tells.md`
