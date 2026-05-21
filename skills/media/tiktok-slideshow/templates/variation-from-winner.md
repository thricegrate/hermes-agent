# Variation From Winner Template

When a slideshow performs, do not start fresh. Spin 5 to 6 variations from the winner. Each variation preserves the structural pattern, the emotional register, and the narrative arc. The performance signal carries through because the elements that drove engagement remain intact.

One winner becomes 6 high-probability slideshows.

## When to use this template

Use this when a slideshow has performed strongly. Strong performance looks like:

- Save rate above the account's baseline
- Comment volume above baseline
- Swipe-through completion rate above baseline (most viewers reaching the final slide)
- Distribution lift visible in the analytics within 24 to 48 hours

If the slideshow performed at or below baseline, do not vary it. Pick a different format or angle. Variation only multiplies winners. Multiplying losers just produces more losers.

## What gets preserved across variations

The variations keep the elements that drove the original performance:

- **Format structure** (Personal Story / Ranked List / Realization / Controversial Opinion / Routine Breakdown)
- **Slide count** (if the original was 6 slides, variations are 6 slides)
- **Emotional register** (if the original was driving and energetic, variations stay in that register)
- **Narrative arc** (the beats land in the same emotional shape)
- **Closer line structure** (if the CTA was a comment-keyword on slide 6, variations keep that)

## What gets changed across variations

The variations change the elements that target a different segment within the broader persona:

- **Specific personal story details** (different number, different timeline, different mechanism)
- **Visual pairing** (different scene, different framing, different mood within the same baseline)
- **Hook line wording** (same structure, different specifics)
- **Slide 2-5 content** (different beats inside the same arc)

## The variation prompt

```
The following slideshow performed strongly:

[Paste the winning slideshow script in full, including text overlays and image prompts.]

PERFORMANCE DATA (if available):
- Save rate: [number]
- Comment count: [number]
- Swipe-through completion: [percentage]
- View count: [number]
- Posting time: [day, time]
- Audio used: [track name + register note]

Write 5 variations of this slideshow. Each variation must:

1. Maintain the format structure (same number of slides, same beat sequence)
2. Maintain the emotional register (same mood and pacing)
3. Maintain the narrative arc (same emotional shape across the slides)
4. Preserve the closer line structure (if the original ended with a comment-keyword CTA, variations
   keep a comment-keyword CTA)

Each variation must change:

1. The specific personal story details (different number, timeline, or mechanism)
2. The visual pairing notes (different scene, framing, or mood within the same aesthetic baseline)
3. The hook line wording (same structure, different specifics)
4. The body slides 2 through [N-1] content (different beats inside the same arc)

Each variation should target a slightly different segment within the broader persona than the
original. The original may have hit one specific pain point. Variations can hit adjacent pain
points using the same emotional shape.

For each variation, output:

# Variation [N]: [Title]

**Targeting:** [Which segment of the broader persona this variation aims at, and how it differs
from the original]

**Changes from original:** [Brief note on what got swapped]

---

## Slide 1: [Beat name]

**Text overlay:** [...]

**Image prompt:** [...]

---

## Slide 2: [Beat name]

**Text overlay:** [...]

**Image prompt:** [...]

---

[... continue for all slides ...]

VOICE RULES (mandatory):
- Coffee shop rule: every line must sound like talking to a friend across a cafe table
- No em-dashes anywhere
- Short sentences. One thought per line.
- Simple words. Specific numbers. Real specifics.
- Match the original's voice intensity exactly. If the original was casual, variations are casual.
  If the original was confrontational, variations are confrontational.
```

## Worked example

Original winning slideshow: "I built a bot that writes my newsletter for 215K subscribers" (Personal Story, 6 slides, driving energetic audio, performed at 3x baseline saves).

5 variations targeting different segments of the broader CC audience:

### Variation 1: Targeting the "I want to start a newsletter" segment

Same format. Same arc. Different specific story.

```
SLIDE 1 HOOK: I built a bot that wrote my first newsletter for me. It got 1,200 opens.
[Same arc through slides 2-5]
SLIDE 6 CTA: Comment NEWSLETTER and I will send you the bot.
```

### Variation 2: Targeting the "I have a newsletter but it is shrinking" segment

Same format. Same arc. Different specific story.

```
SLIDE 1 HOOK: My newsletter open rate dropped 8 points in 6 months. I built a bot that fixed it.
[Same arc through slides 2-5, with slide 5 proof being open rate recovery]
SLIDE 6 CTA: Comment NEWSLETTER and I will send you the bot.
```

### Variation 3: Targeting the "I write content for clients" segment

```
SLIDE 1 HOOK: I built a bot that writes content for 3 clients. They have not noticed.
[Same arc, different proof points]
SLIDE 6 CTA: Comment CLIENT and I will send you the bot.
```

### Variation 4: Targeting the "I am skeptical of AI for writing" segment

```
SLIDE 1 HOOK: I did not trust AI to write in my voice. Then I tested it. 215K subscribers cannot
tell.
[Same arc, but slide 2-3 lean into the skepticism]
SLIDE 6 CTA: Comment NEWSLETTER and I will send you the bot.
```

### Variation 5: Targeting the "I want to know how the the product works" segment

```
SLIDE 1 HOOK: I built a bot in 4 hours. Now my newsletter writes itself.
[Same arc, but slides 3-4 lean more into the "how" mechanism]
SLIDE 6 CTA: Comment the product and I will send you the setup.
```

Each variation is a slightly different angle on the same winning structure. The algorithm sees enough variation between accounts (or posting windows) that nothing reads as duplicate content. The underlying performance pattern that earned the original distribution carries through.

## Failure modes when generating variations

### Variations are too similar

If 5 variations all target the same segment with minor wording changes, the variations cannibalize each other. Each variation should target a different segment within the broader persona.

### Variations break the arc

If variation 3's slide 4 is a different emotional beat from the original's slide 4, the variation has changed the arc. The arc is what made the original perform. Keep the arc, vary the specifics.

### Variations dilute the voice

The original was successful because of its voice intensity. If variations soften the voice, they lose the signal. Match the voice exactly.

### Variations switch formats

If the original was a Personal Story and variation 4 ends up looking like a Realization, the variation is no longer a variation. It is a new piece. The format structure must stay constant.

### Generating 5 variations all at once

Sometimes the model produces 5 variations that are all weak because they all hedge in the same way. If the first 2 or 3 variations are good but the rest feel forced, stop and use the strong ones. 3 strong variations beat 5 mediocre ones.

## Cross-references

- For format-specific variation logic, see the format's template (e.g., [personal-story.md](personal-story.md), [ranked-list.md](ranked-list.md))
- For the broader rationale on why variation-from-winners outperforms fresh ideation, see the strategic context covered in [SKILL.md](../SKILL.md)
- Voice gate before delivery: `skills/humanizer/SKILL.md`, `skills/content-review/SKILL.md`
- **Reel parallel (UGC video, not slideshows)**: For the component-level Winner Variation Pipeline that turns 1 winning AI UGC reel into 1,000+ tested combinations through hook + body + CTA component swapping with compatibility filtering and an 8-week compounding loop, see `skills/ugc-production/templates/variation-from-winner-reel.md` and `skills/ugc-production/references/winner-variation-pipeline.md`. The slideshow workflow above is the format-specific cousin of that pipeline. Use the slideshow template for swipe-through carousels, the reel template for AI avatar video.
