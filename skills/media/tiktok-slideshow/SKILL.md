---
name: tiktok-slideshow
description: "Create TikTok slideshows, short-form video scripts, and visual storytelling for social platforms."
  Use when the user wants to create TikTok slideshow content, viral slideshow scripts, swipe-through
  carousels for TikTok, multi-slide posts, or wants to add slideshows on top of existing TikTok video
  output. Triggers on: "TikTok slideshow", "viral slideshow", "slideshow content", "TikTok carousel",
  "swipe-through post", "slideshow script", "GPT Image 2 slideshow", "Nano Banana slideshow",
  "trending audio slideshow", "TikTok format alternative", "personal story slideshow",
  "ranked list slideshow", "realization slideshow", "controversial opinion slideshow",
  "routine breakdown slideshow", "slideshow for the product demo", "slideshow for build-in-public".
  Generates the full slideshow: format pick, script with paired image prompts, trending audio match,
  posting hint. Five formats supported: Personal Story, Ranked List, Realization, Controversial Opinion,
  Routine Breakdown. Tool-agnostic for image generation (NB2 or GPT Image 2). For TikTok video scripts
  (not slideshows), use video-scriptwriter. For organic social across platforms, use content-social.
---

# TikTok Slideshow

Produce TikTok slideshow content that captures the algorithmic acceleration window the platform is currently giving to swipe-through formats. Slideshows beat video on production economics and on engagement signals (saves, comments, swipe-through velocity) when the format is right for the content.

## When to use this skill

The user wants a slideshow, not a video. The format is right when:
- The content rewards swipe-through dynamics (curiosity gap pulls viewers slide to slide)
- The content is reference-worthy (people save it to come back to)
- The opinion is contrarian enough to drive comment debate
- Production capacity is tighter than what video would need
- The audience is on TikTok and the algorithmic push window is open

When the user wants a video script, route to `video-scriptwriter`. When they want multi-platform organic content, route to `content-social` (which links here for TikTok slideshow specifics).

## Prerequisites

Gather what's missing before writing:

- **Persona doc** -- target audience, real pain points, language patterns. For CC content, default to `private project coaching/session-6/` or audience profile docs.
- **Product or topic** -- what the slideshow is about. For CC, this is often an the product skill demo, a build-in-public moment, or a learn-AI app angle.
- **Transformation or insight** -- what the viewer gets after swiping through.
- **Image gen tool** -- default to Nano Banana 2 (project standard). Switch to GPT Image 2 only if the user asks for it or product text rendering is critical.

For CC examples and worked walkthroughs, see [references/cc-examples.md](references/cc-examples.md).

## The 5 formats at a glance

| Format | Hook pattern | Slide count | Anchor metric | Use when |
|---|---|---|---|---|
| Personal Story | Specific outcome + timeline | 6-7 | Swipe-through velocity | Transformation content, build-in-public, before/after |
| Ranked List | "What's #1?" reverse reveal | 5-7 | Swipe-through to final slide | Tool comparisons, recommendation roundups, curated picks |
| Realization | "I figured out why..." insight | 5-7 | Saves | Educational content, problem diagnosis, aha moments |
| Controversial Opinion | Contrarian statement + defense | 5-7 | Comments | Hot takes the audience will argue, niche orthodoxy challenges |
| Routine Breakdown | One step per slide | 5-6 | Saves | Workflows, processes, step-by-step systems |

Full structure, hook pattern, failure modes, and example hooks for each format: [references/slideshow-formats.md](references/slideshow-formats.md).

## Production workflow

Four steps. Run them in order.

### Step 1: Pick the format

Use the table above. If two formats fit, default to the one whose anchor metric matches the user's goal. Saves and comments compound differently. Saves keep distributing for weeks. Comments push initial reach.

### Step 2: Generate the script with paired image prompts

Run [templates/master-claude-prompt.md](templates/master-claude-prompt.md) with the persona, product, format choice, and aesthetic baseline. Output is a complete slideshow script with one image prompt per slide in brackets.

For format-specific skeletons with worked examples and slot-fill structure:
- [templates/personal-story.md](templates/personal-story.md)
- [templates/ranked-list.md](templates/ranked-list.md)
- [templates/realization.md](templates/realization.md)
- [templates/controversial-opinion.md](templates/controversial-opinion.md)
- [templates/routine-breakdown.md](templates/routine-breakdown.md)

### Step 3: Generate the slide images

Apply the universal image prompting principles. Same character ref + scene ref + aesthetic baseline across every slide. Skin texture clause. Anti-polish language. Lighting as a dedicated clause. Generate 6-8 variants for slides with humans and pick the strongest.

Universal disciplines: [references/image-prompting-principles.md](references/image-prompting-principles.md).

Tool-specific recipes:
- Nano Banana 2 (project default): [references/tool-recipe-nb2.md](references/tool-recipe-nb2.md). Pairs with `skills/nb2-image-gen/SKILL.md` for general NB2 prompt engineering.
- GPT Image 2: [references/tool-recipe-gpt-image-2.md](references/tool-recipe-gpt-image-2.md).

### Step 4: Match trending audio

Find a trending track in the niche, filter for emotional register match, assign to the slideshow before scheduling. 5-10 minutes per batch. The platform-specific distribution multiplier most operators skip.

Workflow: [references/trending-audio-workflow.md](references/trending-audio-workflow.md).

## Variations from winners

When a slideshow performs, do not start fresh. Run [templates/variation-from-winner.md](templates/variation-from-winner.md) to spin 5-6 variations that preserve the structural pattern and emotional register. One winner becomes 6 high-probability slideshows. The performance signal carries through because the elements that drove it (structure, register, narrative arc) stay intact.

## Voice rules (mandatory)

Every script, hook, and CTA the skill produces must comply with the project voice:

- **Coffee shop rule**: every line must sound like talking to a friend across a cafe table. Read it aloud. If it sounds performative or corporate, rewrite. See `SOUL.md`.
- **No em-dashes**: project-wide rule. See `rules/no-em-dashes.md`.
- **Short sentences**: one thought per line. Break long ideas into two short sentences.
- **Simple words**: "use" not "leverage", "set up" not "implement", "stuff" not "elements".
- **Voice reference**: read private voice-reference notes before writing if unsure.

**Final gate**: route every finished slideshow script through `humanizer` and `content-review` before delivery. This is non-negotiable per `CLAUDE.md` for any externally-published content.

## Output format

Hand the finished slideshow to the user in this shape:

```
# Slideshow: [Title or hook line]

**Format:** [Personal Story / Ranked List / Realization / Controversial Opinion / Routine Breakdown]
**Slide count:** [N]
**Audio:** [Track name + register match note]
**Posting hint:** [Suggested time of day or batch slot]

---

## Slide 1: [Hook]

**Text overlay:** [The exact words that appear on the slide]

**Image prompt:** [Full image gen prompt with character ref, scene ref, aesthetic baseline,
skin texture clause, lighting clause, 9:16 spec]

---

## Slide 2: [Beat name]

**Text overlay:** [...]

**Image prompt:** [...]

---

[... slides 3 through N ...]

---

## Slide N (final): [CTA]

**Text overlay:** [Low-friction CTA]

**Image prompt:** [...]
```

Always include audio + posting hint. Always include the per-slide image prompt block (not a single shared prompt). If the user wants the slideshow in batch (multiple slideshows in one ask), repeat the block per slideshow.

## Cross-references

- For AI UGC video (not slideshows) across all 4 platforms (TikTok video + Instagram Reels + YouTube Shorts + Facebook Reels) generated in parallel from one Claude session, see `skills/ugc-production/templates/master-prompts-by-platform.md`. That covers reels with platform-specific calibration; this skill covers TikTok slideshows specifically.
- Hook patterns: `skills/video-hook/references/video-hook-formulas-2025.md` (desire-based hooks for Personal Story and Realization), `skills/content-social/references/hook-formulas.md` (social hooks for Ranked List and Controversial Opinion).
- Image generation tools: `skills/nb2-image-gen/SKILL.md` (NB2 prompt engineering), `skills/ads-creative/references/generative-tools.md` (tool comparison).
- Voice gate: `skills/humanizer/SKILL.md`, `skills/content-review/SKILL.md`.
- Voice rules: `SOUL.md`, private voice-reference notes, `rules/no-em-dashes.md`.
- Multi-platform context: `skills/content-social/SKILL.md` (when slideshows are part of a broader content engine).
- Storytelling craft: `skills/storyteller/references/sheridan-framework.md` (when the slideshow leans into open-question narrative rather than neat-lesson structure).
