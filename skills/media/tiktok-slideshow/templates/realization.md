# Realization Slideshow Template

Insight moment + progressive deepening. 5 to 7 slides. Anchor metric: saves.

For the universal format reference, see [references/slideshow-formats.md](../references/slideshow-formats.md).

## When this format wins

- Educational content with a specific aha moment
- Problem diagnosis (the audience knows the symptom, you name the cause)
- Aha moment framings that resonate with audiences stuck on a problem
- the product audience-misread story (the coaching pivot)
- Anti-conventional thinking with a "I just realized why..." angle

## Slot-fill skeleton

```
SLIDE 1 (THE MOMENT):
Format: First-person insight statement. The realization itself, stated clearly.
Slot: "I realized why [specific problem] / I figured out why [specific outcome] / I noticed [specific
pattern]."

SLIDE 2 (THE STANDARD ASSUMPTION):
Format: What people usually think. The assumption the realization breaks.
Slot: [The conventional explanation] + [Why it does not actually fit the symptom].

SLIDE 3 (THE ACTUAL CAUSE):
Format: The real reason. The mechanism the realization names.
Slot: [The actual cause] + [Why this fits the evidence better].

SLIDE 4 (THE EVIDENCE):
Format: The proof or pattern that makes the realization stick.
Slot: [Specific evidence, observation, or pattern] + [Why it confirms the new explanation].

SLIDE 5 (WHAT TO DO):
Format: The practical implication of the realization.
Slot: [The action that follows from the new understanding] + [Why this works].

SLIDE 6 (THE CLOSE):
Format: Either CTA or closing reflection that lands the realization.
Slot: [Comment keyword / Save this for the next time you face the symptom / Reflective close].

SLIDE 7 (CTA): [Use only if going to 7 slides; otherwise CTA is on slide 6]
```

## Worked example

A Realization slideshow for the coaching pivot story (CC content):

```
# Slideshow: Why most people give up on learning AI in 2 weeks

**Format:** Realization
**Slide count:** 6
**Audio:** Reflective slow track building toward driving in the last beat
**Posting hint:** Saturday 9am ET (high save rate window)

---

## Slide 1: The moment

**Text overlay:** I just realized why most people give up on learning AI in the first 2 weeks.

**Image prompt:** [Three-quarter close-up of founder, mid-40s, looking thoughtful, gaze slightly
off-camera. Soft warm afternoon light from window at left, late afternoon quality. Realistic skin
texture, visible pores, natural unevenness, no filter quality. Phone camera framing, candid
lifestyle feel, not posed. Clean negative space in upper third for text overlay. 9:16 aspect
ratio.]

---

## Slide 2: The standard assumption

**Text overlay:** Everyone says it is the time commitment. Or the tools. They are wrong.

**Image prompt:** [Same setting, slight angle change, founder looking at notebook with pen.
Soft warm afternoon light. Realistic skin texture on visible hand. Phone camera framing, organic
not studio quality. Clean negative space in upper third for text overlay. 9:16 aspect ratio.]

---

## Slide 3: The actual cause

**Text overlay:** It is the gap between knowing what to do and actually doing it. Mahabharat has
a name for this.

**Image prompt:** [Close-up of an open notebook with handwritten notes, words "Duryodhana" and
"knowing vs doing" visible. Same desk, soft warm afternoon light. Phone camera framing, organic
not studio quality. Clean negative space in upper third for text overlay. 9:16 aspect ratio.]

---

## Slide 4: The evidence

**Text overlay:** I sent 62,000 emails about learning AI. 50 people clicked. They knew. They did
not do.

**Image prompt:** [Close-up of laptop screen showing analytics dashboard with low click numbers,
slightly out of focus to emphasize the number. Soft warm afternoon light. Phone camera framing,
organic not studio quality. Clean negative space in upper third for text overlay. 9:16 aspect
ratio.]

---

## Slide 5: What to do

**Text overlay:** Reading another article does not close the gap. Doing one specific thing with
the AI in front of you does.

**Image prompt:** [Over-the-shoulder shot of founder typing into a small AI app on laptop,
focused expression. Soft warm late afternoon light from window at left, golden hour quality.
Realistic skin texture on visible hand and arm. Phone camera framing, organic not studio quality.
Clean negative space in upper third for text overlay. 9:16 aspect ratio.]

---

## Slide 6: Close + CTA

**Text overlay:** I built a free 5-minute app that walks you through ONE specific thing. Comment
LEARN.

**Image prompt:** [Mirror selfie of founder, calm confident expression, holding phone. Soft warm
golden hour light from window at left, late afternoon quality. Realistic skin texture, visible
pores, natural unevenness, no filter quality. Phone camera framing, organic not studio quality.
Clean negative space in upper third for text overlay. 9:16 aspect ratio.]

---

After producing the slideshow, generate the 6 images using NB2:
01-moment.png, 02-assumption.png, 03-cause.png, 04-evidence.png, 05-action.png, 06-close-cta.png
```

## Failure modes specific to Realization

### The realization is obvious

If the audience already agrees with the realization before slide 2, the slideshow has no insight value. They will not save it. They will not comment. They will scroll. The realization needs to be something that lands as "oh, I had not thought of it that way".

### The realization is generic

"I realized hard work pays off" is not a Realization. "I realized why my React app was slow" is. The realization needs to be specific to a problem the audience recognizes from their own life.

### Slides do not progress the realization

Each slide needs to deepen the insight. Slide 2 names the standard assumption. Slide 3 names the actual cause. Slide 4 brings the evidence. Slide 5 names the action. If slide 4 is just slide 3 rephrased, cut one of them.

### The "what to do" slide is missing

A realization without an action implication does not earn saves. The audience saves the slideshow because they want to apply the realization. Slide 5 (or whatever the action slide is) gives them something to do with the insight. Without it, the slideshow is interesting but not save-worthy.

### The voice is preachy

If the realization slides read as "let me explain to you what is really going on", the format breaks. The format works best when the founder is figuring it out alongside the viewer, not lecturing them. Voice should be reflective, not authoritative.

## The Claude prompt for spinning a fresh Realization slideshow

```
Write a TikTok Realization slideshow with 6 slides.

PERSONA: [Paste persona]

THE REALIZATION: [The first-person insight. Be specific. "I realized why [specific problem]" or
"I figured out why [specific outcome]" or "I noticed [specific pattern]."]

THE STANDARD ASSUMPTION: [What people usually think about this problem or topic. The assumption
the realization breaks.]

THE ACTUAL CAUSE: [The real reason. The mechanism the realization names.]

THE EVIDENCE: [The proof or pattern that makes the realization stick. Specific data, observation,
or pattern.]

THE ACTION THAT FOLLOWS: [The practical implication. What the audience should do given the new
understanding.]

CLOSE: [CTA or reflective close that lands the realization.]

VISUAL AESTHETIC BASELINE: [Default for CC: warm interior, authentic phone selfie feel, soft
natural framing, organic not studio quality, casual home environment. For Realization specifically,
slightly more pensive lighting works well: late afternoon, golden hour, soft.]

CHARACTER: [Description of the recurring person.]

SCENE: [Description of the recurring environment, often the same setting throughout.]

For each slide, output:
1. Beat name (The moment / The standard assumption / The actual cause / The evidence / What to do
   / Close + CTA)
2. Text overlay (the exact words appearing on the slide)
3. Image prompt (full prompt with scene direction, lighting clause favoring late afternoon or
   golden hour for the reflective tone, skin texture clause if face in frame, anti-polish language,
   aesthetic baseline, clean negative space for text overlay, 9:16 aspect ratio)

Voice rules: coffee shop rule, no em-dashes, short sentences, simple words. The voice should be
reflective rather than authoritative. The founder is figuring it out alongside the viewer. CC
voice: blunt but thoughtful, self-deprecating where authentic.
```

Run this. Voice-check. Generate images. Match audio. Route through humanizer and content-review before delivery.
