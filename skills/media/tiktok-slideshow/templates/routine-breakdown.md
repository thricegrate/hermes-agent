# Routine Breakdown Slideshow Template

One step per slide. 5 to 6 slides. Anchor metric: saves.

For the universal format reference, see [references/slideshow-formats.md](../references/slideshow-formats.md).

## When this format wins

- Specific routines or workflows the audience would want to follow
- Skincare routines, fitness routines, morning routines, productivity systems
- the product workflow demos (the steps of a specific automation)
- Build-in-public process docs
- Anything where the audience would benefit from a saved reference

## Slot-fill skeleton

```
SLIDE 1 (THEME):
Format: Establishes the routine. Specific timeframe + specific outcome.
Slot: [The routine name with specific time or count] + [What it accomplishes].

SLIDE 2 (STEP 1):
Format: First step. One specific action.
Slot: [Step 1 action] + [Brief detail or why it matters].

SLIDE 3 (STEP 2):
Format: Second step. One specific action.
Slot: [Step 2 action] + [Brief detail].

SLIDE 4 (STEP 3):
Format: Third step. One specific action.
Slot: [Step 3 action] + [Brief detail].

SLIDE 5 (STEP 4 OR THE LAND):
Format: Fourth step OR the result if doing 4-step routine.
Slot: [Step 4] OR [The complete routine landed].

SLIDE 6 (CTA):
Format: Low-friction CTA.
Slot: [Save this for tomorrow morning / Comment keyword / Follow for more].
```

For 6-step routines, expand to 7 slides (theme + 6 steps + CTA). For 4-step routines, contract to 5 slides (theme + 4 steps with CTA on the last step).

## Worked example

A Routine Breakdown for an the product newsletter automation workflow:

```
# Slideshow: My exact 5-step workflow that ships a newsletter draft in 25 minutes

**Format:** Routine Breakdown
**Slide count:** 6
**Audio:** Driving energetic track building through the steps, fits the workflow frame
**Posting hint:** Saturday or Sunday morning ET (high save rate window)

---

## Slide 1: Theme

**Text overlay:** My exact 5-step workflow that ships a newsletter draft in 25 minutes. To 215K
subscribers.

**Image prompt:** [Wide shot of home office desk with laptop open, coffee cup, notebook with
visible handwritten notes, soft warm morning light from window at left. Phone camera framing,
organic not studio quality, casual home office. Clean negative space in upper third for text
overlay. 9:16 aspect ratio.]

---

## Slide 2: Step 1

**Text overlay:** Step 1. Voice memo for 90 seconds. Speak the topic and the angle. Do not write
anything yet.

**Image prompt:** [Close-up of a phone in hand showing a voice memo recording in progress (red
record button visible), soft warm morning light. Realistic skin texture on visible hand. Phone
camera framing, organic not studio quality. Clean negative space in upper third for text overlay.
9:16 aspect ratio.]

---

## Slide 3: Step 2

**Text overlay:** Step 2. Run the voice memo through transcription. The bot reads the transcript
plus 5 example issues.

**Image prompt:** [Close-up of laptop screen showing a transcription tool with text appearing,
hand on trackpad. Soft warm morning light from window at left. Realistic skin texture on visible
hand. Phone camera framing, organic not studio quality. Clean negative space in upper third for
text overlay. 9:16 aspect ratio.]

---

## Slide 4: Step 3

**Text overlay:** Step 3. The bot drafts in my voice. Output is rough but in the right tone.

**Image prompt:** [Over-the-shoulder shot of laptop showing a draft document with text being
generated, founder watching focused. Soft warm morning light. Realistic skin texture on visible
hand and shoulder. Phone camera framing, organic not studio quality. Clean negative space in
upper third for text overlay. 9:16 aspect ratio.]

---

## Slide 5: Step 4

**Text overlay:** Step 4. I edit. 15 minutes max. Cut weak sentences, fix the hook, sharpen the
CTA.

**Image prompt:** [Close-up of laptop screen showing a document with edits visible (track changes
or strikethrough), founder typing. Soft warm late morning light from window at left. Realistic
skin texture on visible hand. Phone camera framing, organic not studio quality. Clean negative
space in upper third for text overlay. 9:16 aspect ratio.]

---

## Slide 6: Step 5 + CTA

**Text overlay:** Step 5. Subject line gets 3 variants tested. Done. Comment NEWSLETTER for the
full bot setup.

**Image prompt:** [Mirror selfie of founder, mid-40s, satisfied confident expression, holding
phone. Soft warm late morning light from window at left, golden hour quality. Realistic skin
texture, visible pores, natural unevenness, no filter quality. Phone camera framing, organic
not studio quality. Clean negative space in upper third for text overlay. 9:16 aspect ratio.]

---

After producing the slideshow, generate the 6 images using NB2:
01-theme.png, 02-step1.png, 03-step2.png, 04-step3.png, 05-step4.png, 06-step5-cta.png
```

## Failure modes specific to Routine Breakdown

### Vague steps

"Be consistent" is not a step. "Voice memo for 90 seconds" is. Each step needs a specific action the audience can do. If the step is not specific enough to do tomorrow morning, rewrite it.

### Too many steps on one slide

The format works because each step gets one slide of attention. If you cram 3 steps on slide 2, the format breaks. The viewer cannot read the slide fast enough during the swipe. One step per slide. Always.

### The routine is not actionable

If the routine is motivational framing without specifics ("wake up early, take care of yourself, work hard"), it does not earn saves. The audience saves the slideshow because they want to do the routine. Saved-but-vague does not get done.

### The viewer cannot tell what to do first

If step 1 is unclear or step 1 depends on something the audience does not have, the routine breaks before they start. Test step 1 in your head: could a stranger reading slide 2 do this thing tomorrow with what they already have? If no, fix step 1.

### Specific timeframe missing from the theme

"My morning routine" is a weaker theme than "The exact 5-step morning routine I run at 6am every weekday". The specific timeframe creates the curiosity gap and signals the routine is concrete, not aspirational.

### CTA is generic

"Follow for more" is weaker than "Save this for tomorrow morning" or "Comment ROUTINE for the full setup with timestamps". The CTA should match the format's anchor metric (saves), so prompts that call for saving work especially well here.

## The Claude prompt for spinning a fresh Routine Breakdown slideshow

```
Write a TikTok Routine Breakdown slideshow with 6 slides (theme + 4-5 steps + CTA on the last
slide).

PERSONA: [Paste persona]

THE ROUTINE THEME: [Specific timeframe + specific outcome. Examples: "The exact 5-step morning
routine I run at 6am every weekday", "How I write 3 newsletter issues in 2 hours using AI", "The
4-step skincare routine that fixed my acne in 6 weeks".]

THE 4 OR 5 STEPS, IN ORDER:
- Step 1: [Specific action] + [Brief detail or why it matters]
- Step 2: [Specific action] + [Brief detail]
- Step 3: [Specific action] + [Brief detail]
- Step 4: [Specific action] + [Brief detail]
- Step 5 (optional): [Specific action] + [Brief detail]

CTA: [Comment keyword for the full routine, save this for tomorrow morning, or follow for more.]

VISUAL AESTHETIC BASELINE: [Default for CC: warm interior, authentic phone selfie feel, soft
natural framing, organic not studio quality, casual home environment. Routine slides often mix
selfie shots (theme + CTA) with action shots (steps in progress). Action shots can be over-the-
shoulder or close-up of the action.]

CHARACTER: [Description of the recurring person.]

SCENE: [Description of the recurring environment, often the same throughout if the routine
happens in one place.]

For each slide, output:
1. Beat name (Theme / Step 1 / Step 2 / Step 3 / Step 4 / Step 5 + CTA)
2. Text overlay (the exact words appearing on the slide)
3. Image prompt (full prompt with scene direction matching whether this slide is selfie or action,
   lighting clause, skin texture clause if face or hand in frame, anti-polish language, aesthetic
   baseline, clean negative space for text overlay, 9:16 aspect ratio)

Voice rules: coffee shop rule, no em-dashes, short sentences, simple words. The voice should be
direct and concrete. Specific actions over abstractions. Specific timeframes over vague phrases.
CC voice: blunt, practical, no fluff.
```

Run this. Voice-check. Generate images. Match audio. Route through humanizer and content-review
before delivery.
