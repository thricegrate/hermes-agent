# Master Claude Prompt for TikTok Slideshows

The reusable prompt that produces a complete slideshow script with paired image prompts in a single Claude call. Works for any of the 5 formats. Slot in the persona, product, format choice, and aesthetic baseline.

## When to use this template

Use this when you have:
- A persona document (audience, pain points, language)
- A product or topic
- A specific transformation, insight, or position
- A format choice (Personal Story, Ranked List, Realization, Controversial Opinion, Routine Breakdown)

Run this once to get the complete slideshow. If you do not have a clear format choice yet, read [references/slideshow-formats.md](../references/slideshow-formats.md) first and pick.

## The master prompt

Copy the prompt below. Fill in the bracketed slots. Run it as a single Claude call.

---

```
You are writing a TikTok slideshow script. The format is [FORMAT NAME: Personal Story / Ranked List
/ Realization / Controversial Opinion / Routine Breakdown].

The slideshow has [SLIDE COUNT: 5 / 6 / 7] slides total.

PERSONA:
[Paste the persona document. Include: who the audience is, age range, what they care about, their
specific pain points, the language they actually use, what they have already tried.]

PRODUCT OR TOPIC:
[Describe the product, topic, transformation, insight, or position. Include the specific outcome,
the specific timeline, the specific number, or the specific contrarian claim. Be concrete. Avoid
"helping people" and "improving their lives". Use the actual numbers and the actual specifics.]

THE TRANSFORMATION OR INSIGHT:
[What does the viewer get after swiping through? What changes for them? What do they realize?
What action will they take?]

VISUAL AESTHETIC BASELINE:
[Describe the consistent aesthetic across all slides. Default for CC content: "Warm interior
lighting, authentic phone selfie or candid lifestyle feel, soft natural framing, organic not
studio quality, casual everyday environments." Adapt for the slideshow's mood.]

CHARACTER DESCRIPTION (if a person appears in the slideshow):
[Describe the recurring character: age range, appearance, what they typically wear in this slideshow.
This will be used as a reference description across slides.]

SCENE DESCRIPTION (if the slideshow stays in one environment):
[Describe the recurring scene: location, key visual elements, time of day, lighting source.]

INSTRUCTIONS:

Write a complete slideshow script that follows the [FORMAT NAME] format structure:

For PERSONAL STORY:
- Slide 1 is the hook line that promises a specific personal outcome with a timeline
- Slides 2 through [N-1] walk through the discovery and the mechanism, each one a single short
  text overlay paired with a specific visual
- The final slide is a low-friction CTA

For RANKED LIST:
- Slide 1 establishes the list theme and what the audience is about to see
- Slides 2 through [N-1] present items in REVERSE order (5 through 2)
- The final slide reveals item 1

For REALIZATION:
- Slide 1 opens with a specific moment of insight
- Each subsequent slide deepens the realization with specific details, evidence, or progressive
  understanding
- The final slide either closes with a CTA or lands the insight

For CONTROVERSIAL OPINION:
- Slide 1 is a statement that contradicts conventional thinking in the niche
- Slides 2 through [N-1] defend the position with specific evidence, examples, or reasoning
- The final slide restates the position with conviction or calls out the discussion

For ROUTINE BREAKDOWN:
- Slide 1 establishes the routine and what it accomplishes
- Slides 2 through [N-1] walk through each step with specific instructions or details
- The final slide drives the action or provides additional context

For each slide, include:
1. The text overlay (the exact words that appear on the slide). Keep it short. One sentence
   when possible. Two short sentences max.
2. An image generation prompt in brackets describing the exact static image to generate. Include:
   - Scene direction (who, where, what they are doing, what they are wearing)
   - The lighting clause (source, direction, quality, time-of-day) as a dedicated element
   - The skin texture clause if a face is in frame ("realistic skin texture, visible pores around
     nose and cheeks, natural slight unevenness, no filter quality")
   - The anti-polish language ("phone framing, organic not studio quality, casual everyday
     environment")
   - The aesthetic baseline from above
   - Clean negative space note for text overlay placement (upper third or center)
   - 9:16 aspect ratio note

VOICE RULES (mandatory):
- Coffee shop rule: every line must sound like talking to a friend across a cafe table. No
  presentation language. No "leverage", "implement", "optimize". Use "use", "set up", "fix".
- No em-dashes anywhere.
- Short sentences. One thought per line. Break long ideas into two short sentences.
- Simple words. Specific numbers. Real specifics over abstractions.
- For CC content specifically, match the founder voice: blunt, self-deprecating, dry humor,
  English is a third language so simple word choice is authentic. Numbers over adjectives.

OUTPUT FORMAT:

# Slideshow: [Title or hook line]

**Format:** [FORMAT NAME]
**Slide count:** [N]
**Audio:** [Suggest the emotional register of the trending audio that should be assigned to this
slideshow. Audio matching workflow runs separately, but suggest the register here.]
**Posting hint:** [Suggested time of day or batch slot based on the format and content]

---

## Slide 1: [Beat name]

**Text overlay:** [Exact text that appears on the slide]

**Image prompt:** [Full prompt with scene direction, lighting clause, skin texture clause if face
in frame, anti-polish, aesthetic baseline, 9:16 spec, negative space note]

---

## Slide 2: [Beat name]

**Text overlay:** [...]

**Image prompt:** [...]

---

[... continue through Slide N ...]

---

After producing the slideshow, list the files I should generate with the image gen tool, in the
order they should be produced.
```

---

## Worked example

### Inputs

- **Format**: Personal Story
- **Slide count**: 6
- **Persona**: CC audience, 35-50+ Americans, want to learn AI, feel overwhelmed and do not know where to start, prefer free demos before paying
- **Product**: the product skill that drafts CC newsletter issues
- **Transformation**: Saved 2 hours per newsletter issue, drafted 4 issues per week
- **Visual aesthetic baseline**: Warm interior, authentic phone selfie feel, soft natural framing, casual home office environment
- **Character description**: Founder, mid-40s, casual t-shirt and hoodie, slightly tousled hair, glasses
- **Scene description**: Home office desk, laptop open, morning light from window at left

### Output (what the master prompt produces, abbreviated example)

```
# Slideshow: I built a bot that writes my newsletter for 215K subscribers

**Format:** Personal Story
**Slide count:** 6
**Audio:** Driving energetic track, fits achievement frame in slide 1 and slide 6
**Posting hint:** Tuesday 10am-12pm ET

---

## Slide 1: Hook

**Text overlay:** I built an AI bot in 4 hours that writes my newsletter for 215K subscribers.
They have not noticed.

**Image prompt:** Mirror selfie of a man in his mid-40s in casual t-shirt and hoodie, slightly
amused expression, holding his phone. Soft warm morning light from a window at left, casting natural
shadows, golden hour quality, no harsh highlights. Realistic skin texture, visible pores around
nose and cheeks, natural slight unevenness, no filter quality. Phone camera framing, organic not
studio quality, casual everyday home office environment. Clean negative space in upper third for
text overlay. 9:16 aspect ratio.

---

## Slide 2: The before

**Text overlay:** I write 4 newsletters a week. Each one used to take 2 hours.

**Image prompt:** Wide candid shot of the same home office desk from over the shoulder, laptop
open showing a draft document, cup of coffee, soft warm morning light from window at left. Phone
camera framing, organic not studio quality. Clean negative space in upper third for text overlay.
9:16 aspect ratio.

[... continues for slides 3-6 ...]
```

## How to adapt the prompt

If the user has a different mood, swap the aesthetic baseline. If the slideshow is in a different setting (gym, kitchen, outdoor), swap the scene description. If the character is different, swap the character description.

The structure of the prompt stays the same. The slot fills change.

## What to do with the output

1. Read the script. Voice-check it against the rules in [SKILL.md](../SKILL.md) (coffee shop rule, no em-dashes, short sentences, simple words).
2. Generate the slide images using the appropriate tool recipe ([tool-recipe-nb2.md](../references/tool-recipe-nb2.md) or [tool-recipe-gpt-image-2.md](../references/tool-recipe-gpt-image-2.md)).
3. Run the trending audio matching workflow ([trending-audio-workflow.md](../references/trending-audio-workflow.md)) to find the actual track.
4. Route the final script through `humanizer` and `content-review` before delivery.

## When to use a format-specific template instead

Use the format-specific templates in this folder when:
- You want a worked example for that specific format with the slot-fill skeleton spelled out
- You want format-specific failure modes called out
- You want a shorter prompt that focuses on the specific format only

The format-specific templates produce the same output. They are scoped narrower for cases where the format is already locked.
