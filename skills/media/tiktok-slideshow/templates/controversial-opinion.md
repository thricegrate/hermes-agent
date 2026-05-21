# Controversial Opinion Slideshow Template

Defensible contrarian statement + evidence. 5 to 7 slides. Anchor metric: comments.

For the universal format reference, see [references/slideshow-formats.md](../references/slideshow-formats.md).

## When this format wins

- Hot takes the audience will argue (substantively, not just rage)
- Niche orthodoxy challenges where you have credible evidence
- Anti-conventional positions that are defensible across 5 slides
- the product contrarian takes ("Most AI skills are useless. Here is why.")
- Industry hype critiques where you have real data

## Slot-fill skeleton

```
SLIDE 1 (THE POSITION):
Format: Contrarian statement, no hedge. The hook is the position itself.
Slot: [The contrarian statement, stated decisively].

SLIDE 2 (WHY EVERYONE BELIEVES THE OPPOSITE):
Format: Acknowledge the standard view. Show you understand why people believe it.
Slot: [The standard position] + [The reason it sounds correct].

SLIDE 3 (THE CRACK IN THE STANDARD VIEW):
Format: The first piece of evidence that breaks the standard view.
Slot: [Specific evidence] + [Why this contradicts the standard view].

SLIDE 4 (THE STRONGER EVIDENCE):
Format: The second piece of evidence. Often the most concrete data point.
Slot: [Specific data point or example] + [Why it strengthens the contrarian position].

SLIDE 5 (THE IMPLICATION):
Format: What the contrarian position means for the audience.
Slot: [What changes if the position is correct] + [What the audience should do differently].

SLIDE 6 (THE LAND):
Format: Restate the position with conviction. Either CTA or call out the discussion.
Slot: [The position restated] + [Comment keyword / Call to debate / Reflective close].

SLIDE 7 (CTA): [Use only if going to 7 slides; otherwise CTA is on slide 6]
```

## Worked example

A Controversial Opinion slideshow for AI hype:

```
# Slideshow: Most AI skills you see online are useless

**Format:** Controversial Opinion
**Slide count:** 6
**Audio:** Sharp confrontational track in the tech niche, fits the contrarian frame
**Posting hint:** Tuesday or Wednesday 11am-2pm ET (peak comment activity)

---

## Slide 1: The position

**Text overlay:** Most AI skills you see online are useless.

**Image prompt:** [Direct-to-camera waist-up shot of founder, mid-40s, confident expression,
slight half-smile that says "I am ready for this argument". Soft warm interior light from window
at left, late morning quality, casual t-shirt or hoodie. Realistic skin texture, visible pores,
natural unevenness, no filter quality. Phone-held framing, organic not studio quality. Clean
negative space in upper third for text overlay. 9:16 aspect ratio.]

---

## Slide 2: Why everyone believes the opposite

**Text overlay:** People see a 30-second demo and think the skill is real. The demo is the
product they are selling.

**Image prompt:** [Same setting, slight angle change, founder gesturing with hand. Soft warm
interior light. Realistic skin texture on hand and face. Phone camera framing, organic not studio
quality, candid lifestyle feel. Clean negative space in upper third for text overlay. 9:16 aspect
ratio.]

---

## Slide 3: The first crack

**Text overlay:** I tested over 100 AI skills in the last year. Maybe 5 actually saved me time
across 30 days of real use.

**Image prompt:** [Close-up of laptop screen showing a notes document with a long list of
crossed-off items, soft warm interior light, slightly out of focus to emphasize the volume.
Phone camera framing, organic not studio quality. Clean negative space in upper third for text
overlay. 9:16 aspect ratio.]

---

## Slide 4: The stronger evidence

**Text overlay:** The 5 that worked were boring. They handled ONE specific repetitive task. They
did not try to do everything.

**Image prompt:** [Wide shot of founder at desk, looking at laptop with focused expression, hand
on chin. Soft warm interior light from window at left. Realistic skin texture on hand and face.
Phone camera framing, organic not studio quality. Clean negative space in upper third for text
overlay. 9:16 aspect ratio.]

---

## Slide 5: The implication

**Text overlay:** If a skill claims to do 10 things, it does zero of them well. Pick boring single
purpose ones.

**Image prompt:** [Over-the-shoulder shot of founder typing at laptop, soft warm interior light
from window at left. Realistic skin texture on visible hand. Phone camera framing, organic not
studio quality. Clean negative space in upper third for text overlay. 9:16 aspect ratio.]

---

## Slide 6: The land

**Text overlay:** I am not saying AI is overhyped. I am saying most of what gets posted as AI
content is. Different problem.

**Image prompt:** [Direct-to-camera shot of founder, calm confident expression, slight nod, eye
contact with camera. Soft warm interior light from window at left, late morning quality. Realistic
skin texture, visible pores, natural unevenness, no filter quality. Phone-held framing, organic
not studio quality. Clean negative space in upper third for text overlay. 9:16 aspect ratio.]

---

After producing the slideshow, generate the 6 images using NB2:
01-position.png, 02-standard-view.png, 03-first-crack.png, 04-stronger-evidence.png,
05-implication.png, 06-land.png
```

## Failure modes specific to Controversial Opinion

### Gratuitously contrarian

Posting controversial opinions just for engagement gets short-term comment volume but long-term audience erosion. The viewer reads the rage-bait pattern and the credibility drops. The controversy needs to be backed by actual reasoning that produces value for viewers who engage with it.

### Cannot defend across 5 slides

If you cannot defend the position with specific evidence across 5 slides, the position is not strong enough to post. Either find better evidence or pick a different position.

### Hedged hook

"I think maybe the 8-glass rule is sometimes wrong" is not a Controversial Opinion. "The 8-glass water rule is wrong" is. The format requires conviction. Hedging kills the swipe-through pull.

### Position is not actually controversial

If 80% of the niche already agrees with the position, it is not controversial. The format works because the position challenges what most viewers believe. If the position is consensus, pick a different one or pick a different format.

### Slides 2-5 do not actually defend

If the defense slides are vague ("the standard view is wrong because..."), the slideshow loses credibility halfway through. Each defense slide needs ONE specific piece of evidence: a number, an example, an observation, a counter-case.

### The land is also a CTA but with no conviction

Slide 6 should land the position with conviction OR call out the discussion. Either works. What does not work is hedging at the end ("but maybe I am wrong, comment what you think"). The audience came for the opinion. Land it.

## The Claude prompt for spinning a fresh Controversial Opinion slideshow

```
Write a TikTok Controversial Opinion slideshow with 6 slides.

PERSONA: [Paste persona]

THE POSITION: [The contrarian statement, stated decisively. No hedge. Examples: "Most AI skills
are useless." "Cardio is misleading you." "Skipping breakfast is the best thing for your energy."]

WHY THE STANDARD VIEW EXISTS: [Why people usually believe the opposite. Acknowledge it. Show you
understand the conventional position.]

THE FIRST CRACK: [The first specific piece of evidence that breaks the standard view.]

THE STRONGER EVIDENCE: [The second specific piece of evidence. Often the most concrete data point
or example.]

THE IMPLICATION: [What changes if the position is correct. What the audience should do differently.]

THE LAND: [Restate the position with conviction. Either CTA or close.]

VISUAL AESTHETIC BASELINE: [Default for CC: warm interior, authentic phone selfie feel, soft
natural framing, organic not studio quality. For Controversial Opinion specifically, more
direct-to-camera framing works well. Subject is more confrontational on camera.]

CHARACTER: [Description of the recurring person.]

SCENE: [Description of the recurring environment.]

For each slide, output:
1. Beat name (The position / Why everyone believes the opposite / The first crack / The stronger
   evidence / The implication / The land)
2. Text overlay (the exact words appearing on the slide)
3. Image prompt (full prompt with scene direction emphasizing direct-to-camera framing where
   appropriate, lighting clause, skin texture clause, anti-polish language, aesthetic baseline,
   clean negative space for text overlay, 9:16 aspect ratio)

Voice rules: coffee shop rule, no em-dashes, short sentences, simple words. The voice should be
direct and confident. No hedging. Specific evidence over vague claims. CC voice: blunt, dry humor,
willing to call out hype. The position must be defensible, not gratuitous.
```

Run this. Voice-check carefully (Controversial Opinion is the format most likely to slip into
ragebait or generic complaint). Generate images. Match audio. Route through humanizer and
content-review before delivery.
