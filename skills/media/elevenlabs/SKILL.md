---
name: elevenlabs
description: |
  Integrates ElevenLabs for text-to-speech, speech-to-text, voice cloning, audio production,
  sound effects, and audio isolation via Python SDK scripts. Use when user wants to generate speech,
  clone voices, transcribe audio, create sound effects, or convert voices.
  Triggers: "elevenlabs", "text to speech", "voice clone", "generate audio", "transcribe",
  "sound effects", "voice over", "narration", "TTS", "speech to text".
metadata:
  version: 2.0.0
  tags: audio, voice, tts, stt, speech, clone, sound-effects, elevenlabs
---

# ElevenLabs Python SDK Integration

Generate speech, clone voices, transcribe audio, create sound effects, and isolate audio directly from Claude Code via Python SDK scripts.

## Prerequisites

- ElevenLabs account with API key (free tier: 10K characters/month)
- `elevenlabs` Python package (`pip install elevenlabs`)
- `python-dotenv` for env loading
- API key set in `.env` as `ELEVENLABS_API_KEY`

## Scripts

All scripts live in `skills/elevenlabs/scripts/` and are run with:

```
python skills/elevenlabs/scripts/<script>.py [options]
```

### text_to_speech.py -- Convert text to speech

```bash
# From text
python skills/elevenlabs/scripts/text_to_speech.py --text "Hello world" --voice Adam --output .tmp/hello.mp3

# From file
python skills/elevenlabs/scripts/text_to_speech.py --file script.txt --voice Brian --model eleven_multilingual_v2

# All options
python skills/elevenlabs/scripts/text_to_speech.py \
    --text "Your text here" \
    --voice "Adam"                      # Voice name or ID \
    --model eleven_multilingual_v2      # Model ID \
    --output .tmp/output.mp3            # Output path \
    --stability 0.5                     # 0.0-1.0 \
    --similarity 0.75                   # 0.0-1.0 \
    --speed 1.0                         # 0.5-2.0
```

### speech_to_text.py -- Transcribe audio

```bash
python skills/elevenlabs/scripts/speech_to_text.py --input recording.mp3
python skills/elevenlabs/scripts/speech_to_text.py --input recording.mp3 --output transcript.txt --diarize --language en
```

### speech_to_speech.py -- Voice conversion

```bash
python skills/elevenlabs/scripts/speech_to_speech.py --input source.mp3 --voice Brian --output .tmp/converted.mp3
```

### voice_clone.py -- Clone a voice from samples

```bash
python skills/elevenlabs/scripts/voice_clone.py --name "My Voice" --files sample1.mp3 sample2.mp3
```

### sound_effects.py -- Generate sound effects

```bash
python skills/elevenlabs/scripts/sound_effects.py --prompt "rain on a tin roof" --duration 5 --output .tmp/rain.mp3
```

### isolate_audio.py -- Remove background noise

```bash
python skills/elevenlabs/scripts/isolate_audio.py --input noisy_recording.mp3 --output .tmp/clean.mp3
```

### list_voices.py -- Browse available voices

```bash
python skills/elevenlabs/scripts/list_voices.py
python skills/elevenlabs/scripts/list_voices.py --gender male --accent american
```

### check_subscription.py -- Monitor credit usage

```bash
python skills/elevenlabs/scripts/check_subscription.py
```

## Voice Reference

Popular built-in voices (use `--voice Name`):

| Name | Style | Gender | Accent |
|------|-------|--------|--------|
| Adam | Dominant, Firm | Male | American |
| Brian | Deep, Resonant, Comforting | Male | American |
| Chris | Charming, Down-to-Earth | Male | American |
| Daniel | Steady Broadcaster | Male | British |
| George | Warm, Captivating Storyteller | Male | British |
| Charlie | Deep, Confident, Energetic | Male | Australian |
| Liam | Energetic, Social Media Creator | Male | American |
| Eric | Smooth, Trustworthy | Male | American |
| Sarah | Mature, Reassuring, Confident | Female | American |
| Alice | Clear, Engaging Educator | Female | British |
| Lily | Velvety Actress | Female | British |
| Jessica | Playful, Bright, Warm | Female | American |
| River | Relaxed, Neutral, Informative | Neutral | American |

Run `list_voices.py` for the full list including custom/cloned voices.

## Models

| Model | Best For | Languages | Latency |
|-------|----------|-----------|---------|
| eleven_multilingual_v2 | Natural quality, long-form (default) | 29 | Standard |
| eleven_flash_v2_5 | Low latency, cost-effective | 32 | ~75ms |
| eleven_turbo_v2_5 | Balanced quality and speed | 32 | ~250ms |
| eleven_english_sts_v2 | Speech-to-speech conversion | English | Standard |
| scribe_v1 | Speech-to-text transcription | 90+ | Standard |

## Usage Patterns

### Voice Cloning Workflow

1. Record clean audio samples (30s minimum, clear speech, no background noise)
2. `voice_clone.py --name "My Voice" --files sample1.mp3 sample2.mp3`
3. `list_voices.py` to find your cloned voice ID
4. `text_to_speech.py --voice <voice_id>` for all future generations

### Newsletter Audio Edition

1. Write newsletter content with `newsletter-writer` skill
2. `text_to_speech.py --file newsletter.txt --voice Adam` to create audio version
3. Output in `.tmp/` for review before publishing

### Video Voiceover

1. Write script with `video-scriptwriter` skill
2. `text_to_speech.py --file script.txt --voice Brian --output .tmp/narration.mp3`
3. Feed audio into `video-editor` or `remotion` pipeline

### Sound Design

1. `sound_effects.py --prompt "epic cinematic whoosh" --output .tmp/whoosh.mp3`
2. `sound_effects.py --prompt "gentle rain" --duration 10 --output .tmp/rain.mp3`
3. `isolate_audio.py --input recording.mp3` to clean up recordings

### UGC Voice Production

For AI-generated UGC content (reels, TikTok, avatar videos), use speech-to-speech with optimized settings for natural-sounding delivery. The default TTS settings produce delivery that sounds too polished for UGC.

1. Record yourself reading the script naturally (like telling a friend, not performing)
2. Convert using speech-to-speech with UGC presets:
```bash
python skills/elevenlabs/scripts/speech_to_speech.py \
    --input source_recording.mp3 \
    --voice "Liam" \
    --stability 0.35 \
    --similarity 0.50 \
    --output .tmp/ugc-voiceover.mp3
```
3. Keep breath sounds (authenticity signals). Only remove silences >0.8s.
4. Run the 3-second authenticity test: play first 3 seconds to someone uninvolved, ask "real person or AI?"

**Full workflow, parameter guide, voice model selection, and batch production protocol:** See `references/voice-optimization-ugc.md`

### Transcription

1. `speech_to_text.py --input meeting.mp3 --output transcript.txt --diarize`
2. Use transcript for content repurposing, subtitles, or notes

## Integration Points

- **video-scriptwriter**: Write scripts, then voice them with `text_to_speech.py` (standard) or `speech_to_speech.py` (UGC -- see `references/voice-optimization-ugc.md`)
- **video-editor / remotion**: Generate narration audio for video compositions
- **newsletter-writer / newsletter-publisher**: Create audio editions of newsletters
- **notebooklm**: NotebookLM generates audio overviews; ElevenLabs provides custom voice control

## Credit Awareness

- Every TTS, voice clone, SFX, and isolation operation uses credits
- Run `check_subscription.py` before large batches to check remaining characters
- Free tier: 10,000 characters/month
- Flash models cost ~50% less than standard models

## Output

All generated files default to `.tmp/` directory. Override with `--output` flag.
