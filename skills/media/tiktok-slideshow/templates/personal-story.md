# Personal Story Slideshow Template

The format that opens with a specific personal outcome and walks through the discovery and the mechanism. 6 to 7 slides. Anchor metric: swipe-through velocity.

For the universal format reference, see [references/slideshow-formats.md](../references/slideshow-formats.md).

## When this format wins

- Transformation content (before/after with a specific timeline)
- Build-in-public moments
- the product skill demos with a clear result
- Coaching pivot story arcs
- Anything where the curiosity gap is "how did you get from A to B?"

## Slot-fill skeleton

```
SLIDE 1 (HOOK):
Format: [Specific outcome] in [specific timeline] doing [specific thing or because of specific change].
Slot: [Outcome] + [Timeline] + [Mechanism teaser].

SLIDE 2 (THE BEFORE):
Format: Background. Where you started. The pain or the problem before.
Slot: [The before-state described concretely with a number or specific detail].

SLIDE 3 (THE DISCOVERY):
Format: The moment something changed. The thing you noticed, tried, or stumbled into.
Slot: [The trigger event] + [Why it mattered].

SLIDE 4 (THE MECHANISM):
Format: How it works. What you actually did. The specific action or system.
Slot: [The mechanism explained in 1-2 short sentences].

SLIDE 5 (THE PROOF OR MID-RESULT):
Format: The evidence it worked. Numbers, observations, things that changed.
Slot: [The specific proof point with numbers if possible].

SLIDE 6 (THE LAND OR FINAL RESULT):
Format: Where you are now. The full result, not just the early signal.
Slot: [The complete outcome stated with conviction].

SLIDE 7 (CTA): [Use only if going to 7 slides; otherwise CTA is on slide 6]
Format: Low-friction call to action.
Slot: [Comment keyword / Bio link / Save this / etc.]
```

## Worked example

A worked Personal Story slideshow for an the product newsletter automation skill demo:

```
# Slideshow: Newsletter bot saved me 8 hours a week

**Format:** Personal Story
**Slide count:** 6
**Audio:** Driving energetic, fits the achievement frame
**Posting hint:** Tuesday 10am-12pm ET

---

## Slide 1: Hook

**Text overlay:** I built an AI bot in 4 hours that writes my newsletter for 215K subscribers.
They have not noticed.

**Image prompt:** [Mirror selfie of founder, mid-40s, casual t-shirt, slightly amused expression,
holding phone. Soft warm morning light from window at left, golden hour quality. Realistic skin
texture, visible pores around nose and cheeks, natural slight unevenness, no filter quality. Phone
camera framing, organic not studio quality, casual home office environment. Clean negative space
in upper third for text overlay. 9:16 aspect ratio.]

---

## Slide 2: The before

**Text overlay:** I write 4 newsletters a week. Each one used to take 2 hours.

**Image prompt:** [Wide candid shot of home office desk over the shoulder, laptop open showing a
draft document, cup of coffee. Soft warm morning light from window at left. Phone camera framing,
organic not studio quality. Clean negative space in upper third for text overlay. 9:16 aspect
ratio.]

---

## Slide 3: The discovery

**Text overlay:** The trick was not better prompts. The bot needed to learn my voice first.

**Image prompt:** [Close-up of laptop screen showing 5 example newsletter issues open in a
text editor, soft warm morning light from window at left. Realistic textures on the desk, natural
phone-photo quality. Clean negative space in upper third for text overlay. 9:16 aspect ratio.]

---

## Slide 4: The mechanism

**Text overlay:** I gave it 5 example issues and a voice memo about the topic. It drafts in
my voice now.

**Image prompt:** [Over-the-shoulder shot of founder typing at laptop, mid-40s, hoodie, focused
expression. Soft warm morning light from window at left, natural shadows, late morning quality.
Realistic skin texture on visible hand and arm. Phone camera framing, organic not studio quality.
Clean negative space in upper third for text overlay. 9:16 aspect ratio.]

---

## Slide 5: The proof

**Text overlay:** Total time per issue: 25 minutes instead of 2 hours. Open rate is the same.

**Image prompt:** [Close-up of a notebook or sticky note with handwritten numbers (25 min, 2 hr,
36% OR), placed on the desk near a coffee cup. Soft warm morning light, natural shadows, organic
phone-photo quality. Clean negative space in upper third for text overlay. 9:16 aspect ratio.]

---

## Slide 6: The land + CTA

**Text overlay:** I built it in 4 hours. Comment NEWSLETTER and I will send you the setup.

**Image prompt:** [Mirror selfie of founder, slightly different angle from slide 1, calmer
confident expression, holding phone. Soft warm afternoon light from window at left, late afternoon
quality. Realistic skin texture, visible pores, natural unevenness, no filter quality. Phone camera
framing, organic not studio quality. Clean negative space in upper third for text overlay. 9:16
aspect ratio.]

---

After producing the slideshow, generate the 6 images in this order using NB2:
01-hook.png, 02-before.png, 03-discovery.png, 04-mechanism.png, 05-proof.png, 06-cta.png
```

## Failure modes specific to Personal Story

### The hook has no number or no timeline

"I changed my health this year" is not a Personal Story hook. "I lost 23 pounds in 11 weeks" is. The number creates the curiosity gap. Without it, the slideshow has no swipe-through pull.

### Slide 2 is advice instead of a beat

If slide 2 reads as "here is how you should think about [topic]", the format breaks. The viewer is along for YOUR ride. Slide 2 is YOUR before-state, not a prescription for theirs.

### Slides 3-5 do not progress

The mechanism slides need to actually move forward. Each slide reveals something the prior slide did not. If slide 4 is just rephrasing slide 3, cut one of them.

### The proof slide has no specific evidence

"It really worked" is not proof. "25 minutes instead of 2 hours" is. "I saved tons of time" is not proof. "I got 3 hours back per week" is. Numbers, observations, things that can be checked.

### CTA is too high-friction

"Sign up at my website using the link in my bio and create an account and start your trial" is too much friction for slide 6. "Comment NEWSLETTER" or "Bio link" or "Save this" is right.

## The Claude prompt for spinning a fresh Personal Story slideshow

```
Write a TikTok Personal Story slideshow with 6 slides.

PERSONA: [Paste persona]

OUTCOME I WANT TO SHARE: [The specific transformation, with a specific number AND a specific
timeline.]

THE BEFORE: [Where I started, described concretely.]

THE DISCOVERY: [The moment something changed. What I noticed, tried, or stumbled into.]

THE MECHANISM: [How it actually works. What I did.]

THE PROOF: [The specific evidence. Numbers if possible.]

THE LAND: [Where I am now.]

CTA: [Comment keyword, bio link, save this, or other low-friction action.]

VISUAL AESTHETIC BASELINE: [Default for CC: warm interior, authentic phone selfie feel, soft
natural framing, organic not studio quality, casual home environment.]

CHARACTER: [Description of the recurring person if applicable.]

SCENE: [Description of the recurring environment if applicable.]

For each slide, output:
1. Beat name (Hook / The before / The discovery / The mechanism / The proof / The land + CTA)
2. Text overlay (the exact words appearing on the slide)
3. Image prompt (full prompt with scene direction, lighting clause, skin texture clause if face
   in frame, anti-polish language, aesthetic baseline, clean negative space note for text overlay,
   9:16 aspect ratio note)

Voice rules: coffee shop rule (sounds like talking to a friend across a cafe table), no em-dashes,
short sentences (one thought per line), simple words ("use" not "leverage"), specific numbers
over adjectives. For CC voice, blunt and self-deprecating, English is a third language so simple
word choice is authentic.
```

Run this. Voice-check the output. Generate images. Match audio. Route through humanizer and content-review before delivery.
