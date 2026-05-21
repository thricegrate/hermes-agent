# Voice Optimization for UGC Authenticity

The voice is the element that most consistently fails the authenticity test with audiences who have exposure to synthetic content. Production quality, avatar realism, and backgrounds can all be engineered to pass the human perception filter. The voice is what trips it up.

---

## Why AI Voices Sound "Off"

The specific qualities in genuine human speech that synthesis hasn't fully replicated:

1. **Micro-variations in pace and rhythm** that reflect internal cognitive processing. A real person varies pace based on emotional content and cognitive accessibility of what they're saying.
2. **Breath-pattern variation** that reflects genuine emotional engagement. Real speakers breathe differently when enthusiastic vs. explaining something complex vs. making a serious point.
3. **Slight tension before significant words** that real speakers produce when they know what they're about to say matters. This creates a prosodic emphasis pattern distinct from synthesized emphasis.
4. **Genuine self-correction patterns** that reflect real cognition. Real people occasionally start a sentence construction and choose a slightly different one. This micro-disfluency signals genuine thought.

---

## The 5-Step Voice Fix

### Step 1: Always Use Speech-to-Speech Over Text-to-Speech

**Use `speech_to_speech.py`, NOT `text_to_speech.py` for all UGC content.**

Text-to-speech generates delivery optimized for accuracy and consistency, which means it lacks the specific imperfections that signal genuine human speech.

Speech-to-speech records a human reading the script with genuine emotional delivery and maps that performance onto the AI voice model. The output preserves pace variations, emphasis patterns, micro-pauses, and emotional register while applying the voice model's characteristics.

**Recording protocol:**
- Quiet environment with a dedicated USB microphone (not laptop audio)
- Read the script as if telling a close friend about something that genuinely helped you
- Do NOT start and stop between sentences -- record in continuous takes to preserve natural rhythm
- Do 3-4 takes per script. Use the take that feels most naturally delivered, not the most technically accurate
- The recording doesn't need to be perfect. It needs to be genuine.

```bash
# Record source audio, then convert
python skills/elevenlabs/scripts/speech_to_speech.py \
    --input source_recording.mp3 \
    --voice "Liam" \
    --output .tmp/ugc-voiceover.mp3
```

### Step 2: ElevenLabs Parameter Presets for UGC

The default settings (stability 0.5, similarity 0.75) produce delivery that's too smooth and consistent for UGC. These presets produce more natural-sounding output:

```bash
python skills/elevenlabs/scripts/speech_to_speech.py \
    --input source.mp3 \
    --voice "Liam" \
    --stability 0.35 \
    --similarity 0.50 \
    --output .tmp/ugc-output.mp3
```

**UGC Preset Explained:**
- **Stability: 0.35** (default 0.5) -- Lower stability = more vocal variation = more human. Settings above 0.6 produce the too-smooth delivery that registers as synthetic.
- **Similarity: 0.50** (default 0.75) -- Moderate style exaggeration preserves emotional character while preventing flat, neutral delivery.
- **Speaker boost: ON** -- Improves naturalness of prosodic patterns, particularly in hook and transformation sections where emotional authenticity matters most.

**If the result is too variable** (breaks in delivery, inconsistent tone), increase stability to 0.40-0.45 before going higher.

### Step 3: Micro-Pause Markup in Scripts

Before generating voice-over, insert `[PAUSE]` markers at 3 key points in the script where a genuine human speaker would pause:

1. **Before the product name** in Section 4 (Solution Introduction) -- a brief pause before naming the product signals the speaker is remembering rather than reciting
2. **After the most emotionally significant pain statement** in Section 2 (Pain Acknowledgment) -- a pause after the pain peak signals emotional connection with the memory
3. **Before the CTA** in Section 6 -- a pause signals the speaker is making a genuine offer rather than delivering a scripted directive

**In ElevenLabs:** Pauses are inserted as brief SSML tags in text input, or as genuine pauses in the source recording for speech-to-speech. Target duration: 0.3-0.6 seconds (long enough to feel natural, short enough to avoid dead air).

**Script markup example:**
```
"...and honestly at this point you're just tired."
[PAUSE]
"What I didn't understand was that..."
```

### Step 4: Audio Cleaning Without Over-Processing

The most common error is removing TOO MUCH in the cleanup process. Operators who silence every breath, remove every micro-pause, and normalize volume to perfectly consistent levels are eliminating the authenticity signals the speech-to-speech workflow was designed to preserve.

**Correct protocol:**
- Remove only silences exceeding 0.8 seconds between sections
- **Do NOT remove breath sounds between sentences** -- these are authenticity signals
- Normalize volume to a consistent level but **preserve dynamic range** within the voice-over. Do NOT compress to remove energy variation between sections.
- Remove any clipping, distortion, or background noise noticeable on mobile speakers

```bash
# Use isolate_audio.py with CONSERVATIVE settings
python skills/elevenlabs/scripts/isolate_audio.py \
    --input .tmp/ugc-output.mp3 \
    --output .tmp/ugc-clean.mp3
```

**After cleaning, listen on mobile speakers** (not studio monitors). Mobile is where 90%+ of UGC is consumed. If it sounds clean enough on phone speakers, it's done.

### Step 5: The 3-Second Authenticity Test

Before deploying ANY new voice model across a production batch:

1. Play the first 3 seconds to someone who is not involved in the production process
2. Ask: "Does that sound like a real person or does it sound like AI?"
3. If they hesitate or say AI, regenerate with adjusted settings or a different voice model
4. Do NOT deploy a voice that fails this test regardless of time invested

This test is not scientific but it is reliable. The human auditory system is more sensitive to synthetic speech patterns than any technical metric.

---

## Voice Model Selection for UGC

Not all ElevenLabs voices perform equally well for UGC. Best performers for cold-traffic UGC:

| Voice | Style | UGC Fit | Best For |
|-------|-------|---------|----------|
| Liam | Energetic, social media creator | Excellent | Fitness, lifestyle, consumer products |
| Chris | Charming, down-to-earth | Excellent | SaaS, productivity, professional tools |
| Jessica | Playful, bright, warm | Excellent | Beauty, wellness, parenting |
| Eric | Smooth, trustworthy | Good | Finance, coaching, high-ticket |
| Sarah | Mature, reassuring | Good | Health, education, transformation |

**For custom/cloned voices:** Clone from 60+ seconds of natural conversational speech (not polished recordings). The imperfections in casual speech transfer better to UGC-style output.

---

## Production Batch Workflow

For 20-25 UGC voice-overs per production cycle:

1. Record all source audio in Block 1 (creative decisions block) -- one continuous recording session
2. Split into individual script recordings
3. Batch-submit all to speech_to_speech.py in Block 2 -- run sequentially, not manually waiting
4. Review first 3 seconds of each output (3-second test)
5. Regenerate any that fail the test with adjusted stability/similarity
6. Light audio cleanup per Step 4 protocol
7. Feed cleaned audio into jogg-ai for video generation (Block 3)

---

## Quick Reference: UGC vs Standard Settings

| Parameter | Standard (newsletters, narration) | UGC (cold traffic reels) |
|-----------|-----------------------------------|--------------------------|
| Method | text_to_speech.py | speech_to_speech.py |
| Stability | 0.50 | 0.35 |
| Similarity | 0.75 | 0.50 |
| Speaker Boost | Off | On |
| Breath removal | Yes | No (keep breaths) |
| Volume normalization | Flat | Preserve dynamic range |
| Quality test | Technical accuracy | 3-second authenticity test |
