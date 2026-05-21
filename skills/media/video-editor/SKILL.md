---
name: video-editor
description: >
  Edit raw screen recording and talking-head videos. Removes repeated takes, false starts,
  silence, filler, and [MUSIC] tags to produce a clean final cut. Optionally adds 3D swivel
  teaser transitions and generates YouTube metadata (chapters + summary). Use when the user
  provides a raw/unedited MP4 video file and wants it edited down. Triggers on: "edit this video",
  "cut this video", providing a raw MP4 for editing, or any request to remove bad takes
  from a recording.
---

# Video Editor

Edit raw recordings by transcribing, reviewing the transcript as an LLM editor,
and applying cuts with ffmpeg. Optionally add swivel teasers and YouTube metadata.

## Pipeline

```
MP4 --> Transcribe (5 providers) --> Format --> LLM Editorial Review --> Refine (ffmpeg or Silero VAD)
    --> Apply Cuts (single-pass, hw-accelerated) --> [Optional: Insert Teaser]
    --> [Optional: Generate Metadata] --> Edited MP4 + EDL
```

---

## Core Pipeline

### Step 1: Transcribe

```bash
python3 <skill_dir>/scripts/transcribe_assemblyai.py <input.mp4> --api-key <key>
```

Requires `ASSEMBLYAI_API_KEY` env var or `--api-key` flag.
Uses AssemblyAI `universal-3-pro` model with English language.
Word-level timestamps are returned by default.
Outputs `<basename>_transcript.json`.

**Alternative providers:**

| Provider | Script | Accuracy | Setup |
|----------|--------|----------|-------|
| AssemblyAI (recommended) | `transcribe_assemblyai.py` | 74ms avg | `ASSEMBLYAI_API_KEY` |
| Deepgram | `transcribe_deepgram.py` | 135ms avg | `DEEPGRAM_API_KEY` |
| Azure | `transcribe_azure.py` | 106ms avg | `AZURE_SPEECH_API_KEY` |
| Google | `transcribe_google.py` | 181ms avg | Service account + GCS |
| Whisper (local) | `transcribe_whisper.py` | N/A | `pip install faster-whisper` |

Whisper runs locally with no API key. Good for quick edits or offline use:
```bash
python3 <skill_dir>/scripts/transcribe_whisper.py <input.mp4> --model base
```

### Step 2: Format for review

```bash
python3 <skill_dir>/scripts/format_transcript.py <transcript.json> -o <formatted.txt>
```

Outputs timestamped lines like:
```
[00:08.16 - 00:12.34] Okay, so we have a lot of Cloud Code updates...
[00:12.50 - 00:18.90] Okay, so we have a whole bunch of Cloud Code updates to go...
```

### Step 3: Editorial review (you, the LLM)

Read the formatted transcript top to bottom. A ~24min raw recording produces ~300 lines,
easily reviewable in one pass. Apply these editing rules:

**Last take wins.** When the speaker repeats the same line or phrase multiple times (retakes),
keep only the LAST complete take. Earlier attempts are always cut. Retakes are easy to spot:
consecutive lines starting with the same few words (e.g., 8 lines all starting "First of all,
one of the biggest..."). Always pick the last one that completes the full thought.

**Cut false starts.** Any sentence that trails off mid-thought ending with "--" or just stops
and restarts is cut. Keep only the completed version. A line ending with "--" is almost always
a false start -- look for the completed version in the lines that follow. **Exception:** if a
false start contains a useful phrase that the clean retake omits (e.g., "model system card"),
extract that phrase as a micro-segment (even 1-2s) and place it before the clean retake.

**Remove all non-speech.** Every `[MUSIC]`, `[NOISE]`, `[APPLAUSE]`, or similar tag is removed entirely.

**Remove dead air.** Gaps and silence between takes are cut. The final video should flow
continuously from one kept segment to the next. **Also cut silence WITHIN segments** -- if a kept
segment has a 500ms+ internal pause (breath, hesitation, dead air), split it into two
segments with the silence removed. Review every segment >5s and look for gaps in the
transcript timestamps. Even short segments can contain splittable pauses.

**Trim filler and stumbles.** Remove standalone filler ("uh", "um", "like", "you know") when they
appear as hesitations. Also surgically remove mid-sentence stumbles by ending a segment before
the stumble and starting a new segment after the correction. Don't keep stumbles just because
splitting feels awkward -- the cut always works better than the stumble in the final video.

**Preserve the speaker's intent.** The final edit should read as if the speaker said everything
correctly on the first try. Maintain the logical flow and ordering of topics.

**When in doubt, keep the later version.** If two takes are roughly equal quality, prefer the later one.

**Merge adjacent segments.** When two kept segments are very close together (gap < 300ms),
merge them into one segment rather than creating a cut. This avoids micro-glitches.

### Output format

Produce an EDL (edit decision list) as JSON:

```json
{
  "segments": [
    {"start_ms": 68100, "end_ms": 82700},
    {"start_ms": 121300, "end_ms": 160400}
  ]
}
```

Each segment is a portion of the ORIGINAL video to keep. Segments must be in chronological order
and non-overlapping.

**Padding:** Add ~200ms padding before each segment start (to catch speech onset that
precedes the transcript timestamp). Do NOT over-pad -- 400ms was found to be too much,
causing the user to trim most starts back. Add ~200ms after each segment end.
AssemblyAI `start` timestamps mark when a word becomes recognizable (~200-300ms after
the speaker begins the sound), so the start padding compensates for this.

Write the EDL to `<basename>_edl.json`.

### Step 3.5: Refine EDL

Two options:

**Option A: ffmpeg silencedetect (zero dependencies)**
```bash
python3 <skill_dir>/scripts/refine_edl.py <input.mp4> <edl.json> [-o <refined_edl.json>]
```
Uses ffmpeg `silencedetect` to extend boundaries and split at internal pauses.
Options: `--noise-db -35`, `--min-pause-ms 500`, `--extend-ms 300`, `--dry-run`

**Option B: Silero neural VAD (more accurate, requires torch)**
```bash
python3 <skill_dir>/scripts/detect_speech_silero.py <input.mp4> -o <edl.json>
```
Uses Silero neural network for speech detection. Better at distinguishing speech from noise.
Options: `--min-silence 0.5`, `--min-speech 0.25`, `--padding 100`, `--merge-gap 0.3`

### Step 4: Apply edits

```bash
python3 <skill_dir>/scripts/apply_edits.py <input.mp4> <edl.json> -o <output_edited.mp4>
```

**Default: single-pass mode.** Uses ffmpeg trim+concat filter -- reads input once, faster for many segments.
Uses platform-aware hardware encoding (NVIDIA h264_nvenc on Windows, videotoolbox on macOS, libx264 fallback).

Options:
- `--normalize` -- apply audio normalization (highpass 80Hz + loudnorm I=-16:TP=-1.5:LRA=11)
- `--legacy` -- use segment-by-segment mode (safer fallback, slower)

### Step 5: Generate Premiere Pro EDL

```bash
python3 <skill_dir>/scripts/generate_edl.py <edl.json> <input.mp4> -o <output.edl>
```

Generates a CMX 3600 `.edl` file importable by Premiere Pro, DaVinci Resolve, and any NLE.
Auto-detects frame rate from the source MP4 via ffprobe.

---

## Optional Features (merged from video-edit-2)

### Swivel Teaser Insertion

Insert a fast-forward 3D rotating preview of future content as an early hook:

```bash
python3 <skill_dir>/scripts/insert_teaser.py <input.mp4> <output.mp4>
python3 <skill_dir>/scripts/insert_teaser.py <input.mp4> <output.mp4> --bg-image bg.png
```

| Argument | Default | Description |
|----------|---------|-------------|
| `--insert-at` | 3 | Where to insert teaser (seconds) |
| `--duration` | 5 | Teaser duration (seconds) |
| `--teaser-start` | 60 | Where to sample content from (seconds) |
| `--bg-color` | #2d3436 | Background color (hex) |
| `--bg-image` | none | Background image for 3D effect |

Timeline result: `[0-3s intro] [3-8s swivel teaser @ up to 100x] [8s+ original content]`
Audio plays continuously throughout.

**Requires:** Node.js + Remotion (`cd scripts/video_effects && npm install`)

### YouTube Metadata Generation

Generate Claude-powered YouTube summary + chapter timestamps:

```bash
python3 <skill_dir>/scripts/generate_metadata.py <formatted.txt> --title "My Video" --edl <edl.json>
```

- Uses Claude to generate 2-4 sentence summary + 5-15 chapter timestamps
- Chapter timestamps are automatically adjusted for removed content
- Outputs `<basename>_metadata.txt` with TITLE/SUMMARY/CHAPTERS sections
- Also generates 3-5 title suggestions using the 3 Drivers of Attention framework (Curiosity, Desire, Fear)
- Includes a thumbnail concept brief (composition, key elements, suggested color palette)

**Requires:** `pip install anthropic` + `ANTHROPIC_API_KEY` env var

---

## Hardware Encoding

The pipeline auto-detects the best encoder for your platform:

| Platform | Primary | Fallback |
|----------|---------|----------|
| Windows (NVIDIA) | h264_nvenc | libx264 |
| Windows (AMD) | h264_amf | libx264 |
| macOS | h264_videotoolbox | libx264 |
| Linux | h264_nvenc (if available) | libx264 |

Encoder detection is handled by `encoder_utils.py` and shared across all scripts.

---

## Handling large transcripts

If the formatted transcript is too long for a single pass (>2000 lines), process it in sections:

1. Read the first ~500 lines, produce keep-segments for that portion.
2. Continue reading the next ~500 lines, noting the overlap context.
3. Merge all segments into one EDL at the end.

In practice: a 24min raw recording = ~3400 words = ~300 formatted lines (one pass).
A 2-hour recording would be ~2500 lines (may need 4-5 passes).

## Quality check

After generating the EDL, run a sanity check:
- Total kept duration should be 30-40% of original for typical recordings with many retakes.
- No segment should be shorter than 500ms (likely a mistake).
- No gap between the end of one segment and start of the next should be < 50ms (merge them).
- Review any segment longer than 5 seconds -- it may contain an internal pause to split out.
- Typical result: ~60-75 segments for a 20-25min raw recording (after splitting internal pauses).
- Prefer under-clipping to over-clipping. It's easier for the user to trim excess than to extend clipped speech.

## Learnings from corrected edits

### Edit 1: 24min recording (58 -> 71 segments)
- **0 segments removed** -- content selection (what to keep) was 100% correct.
- **12 segments split** -- the biggest correction. Long segments (10-20s) contained 1-2s
  internal pauses that should have been cut. Always split segments at internal silence gaps.
- **1 segment added** -- a brief 1s segment was missed.
- **Start trim avg +200ms** -- 400ms start padding was too much; ~200ms is the sweet spot.
- **End trim avg -100ms** -- end padding was slightly tight; increased to ~200ms for safety.
- Final result: 8.5min from 24.4min raw (35% kept).

### Edit 2: 7min recording (12 -> 19 segments)
- **0 segments removed** -- content selection again 100% correct.
- **5 segments split** -- segments of 33s, 18s, 14s, 35s, and even 5.8s were all split.
  User splits at ANY internal pause, not just long ones. Check every segment >5s.
- **1 micro-segment added** -- user rescued "model system card" (1.3s) from a line
  discarded as a false start. When a false start contains useful context that the clean
  retake omits, extract that phrase as a micro-segment.
- **Stumble surgically removed** -- user cut "struggles to solve like new and" by ending
  one segment before the stumble and starting the next after it. Don't keep stumbles/filler
  just because splitting feels awkward -- the cut works better than the stumble.
- **Starts avg ~150ms later** -- 200ms start padding is slightly generous.
- **Ends avg ~150ms earlier** -- 200ms end padding is also slightly generous.
- **Prefer under-clipping** -- user explicitly prefers too-long segments over clipped speech.
  Easier to trim excess in Premiere than to extend a clipped word.
- Final result: 2.5min from 7min raw (35% kept).

### Edit 3: 23min recording (49 -> 101 segments after refine, user corrected to tighter edit)
- **Content selection correct** -- all topics the user kept were also in the automated edit.
- **Redundant meta-commentary kept** -- "shifting your mindset from HOW to WHAT" (lines 109-111)
  was kept but user cut it. The entire video already demonstrates this through examples.
  Rule: if a segment explicitly narrates the point the video is already making through examples,
  it's redundant. Prefer showing (examples) over telling (meta-commentary).
- **Same sentence kept twice** -- two identical sentences 2s apart (lines 97 vs 98) both kept.
  Rule: apply "last take wins" not just to adjacent lines but within a ~30s window.
  Scan for same-idea restatements that aren't immediately consecutive.
- **Short emotional beat over-cut** -- "And honestly, I get really surprised" (line 59, 2s) was
  cut as filler. User kept it as a transition. Rule: short (1-3s) emotional reactions or
  transitions should be kept even if they seem minor. They humanize the content and bridge
  sections. Only cut if stammered/repeated.
- **Intermediate false-start takes kept** -- between two attempts at the same example (lines
  159-175 vs 182-212), the middle attempt was partially included. Rule: when the speaker
  attempts the same example multiple times with significant gaps, identify ALL attempts and
  pick only the final most complete one. Cut everything in between.
- **Closing section under-compressed** -- speaker fatigue in the final 20% produces the most
  restarts. The automated edit kept 4+ restart attempts of "frees you up" / "bottleneck moved."
  User kept only the 2 cleanest. Rule: apply extra scrutiny to the final 20% of a recording.
  For conclusion sections, identify the single cleanest statement of each point.
- **Opening: don't layer takes** -- automated edit combined lines 17-18 AND 24-29 for the opener.
  User picked only 24-29 as one clean take. Rule: for the video opening, pick ONE definitive
  take. Never combine material from two different opening attempts.
- Final result: user's edit was 8.2min from 23.4min raw (35% kept).

### Voice activity detection
Use VAD (voice activity detection) to verify segment boundaries. Transcript timestamps alone
can clip speech onset/offset. After determining segment boundaries from the transcript, use
VAD on the source audio to confirm that no speech is being clipped at the start or end of
each segment. If VAD detects speech energy at a segment boundary, extend the segment to
include it. This prevents the most common user correction: extending starts/ends where
speech was clipped.

## Transcription provider benchmark

See [BENCHMARK.md](BENCHMARK.md) for the full 4-way comparison (AssemblyAI, Deepgram, Azure, Google)
tested against 71 hand-corrected segments.

## Premiere Pro import

After generating the `.edl` file with `generate_edl.py`:

1. Open Premiere Pro
2. File > Import (Cmd+I / Ctrl+I)
3. Select the `.edl` file
4. When prompted, choose the matching frame rate (30fps for most screen recordings)
5. A new sequence appears in the Project panel
6. Right-click any offline clip > Link Media > navigate to the original MP4
7. All 58+ cuts are now on the timeline -- scrub through to review and tweak

The EDL also works in DaVinci Resolve (File > Import Timeline > EDL) and most other NLEs.

## Dependencies

**Core pipeline (zero external Python deps):**
- Python 3.10+
- ffmpeg + ffprobe
- AssemblyAI API key (or other transcription provider)

**Optional features:**

| Feature | Install | Env var |
|---------|---------|---------|
| Silero VAD | `pip install torch` | -- |
| Whisper transcription | `pip install faster-whisper` | -- |
| YouTube metadata | `pip install anthropic` | `ANTHROPIC_API_KEY` |
| Swivel teaser | Node.js + `cd scripts/video_effects && npm install` | -- |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Cuts feel abrupt | Use `--padding 200` on detect_speech_silero.py |
| Too much cut | Use `--min-silence 1.0` |
| Too little cut | Use `--min-speech 0.1` |
| Slow encoding | Check hardware encoder: `python3 scripts/encoder_utils.py` |
| Single-pass fails | Use `--legacy` flag on apply_edits.py |
| Swivel blank frames | Ensure enough frames extracted (300 for 5s teaser) |

---

## Additional Tools (merged from remotion execution)

### Neural VAD Jump Cut (recommended for quick edits)

For quick silence removal without the full transcribe-review pipeline:

```bash
# Parallel version (5-10x faster, recommended)
python3 <skill_dir>/scripts/jump_cut_vad_parallel.py <input.mp4> <output.mp4> --enhance-audio

# Single-threaded version
python3 <skill_dir>/scripts/jump_cut_vad.py <input.mp4> <output.mp4> --enhance-audio

# Single-pass (low memory)
python3 <skill_dir>/scripts/jump_cut_vad_singlepass.py <input.mp4> <output.mp4>
```

Uses Silero neural VAD for speech detection. Supports "cut cut" restart phrase detection,
audio enhancement (EQ, compression, loudnorm -16 LUFS), and LUT color grading.

See `directives/jump_cut_vad.md` for full parameter guide.

### 3D Transition Effects

```bash
# Create standalone 3D rotation preview
python3 <skill_dir>/scripts/pan_3d_transition.py <input.mp4> <output.mp4>

# Insert swivel teaser into existing video
python3 <skill_dir>/scripts/insert_3d_transition.py <input.mp4> <output.mp4> --bg-image bg.png
```

See `directives/pan_3d_transition.md` for effect parameters.

### Thumbnail Face-Swap (Gemini AI)

```bash
# From YouTube URL
python3 <skill_dir>/scripts/recreate_thumbnails.py --url "https://youtube.com/..."

# Analyze reference photos for face direction
python3 <skill_dir>/scripts/analyze_face_directions.py
```

Requires `GEMINI_API_KEY`. See `directives/recreate_thumbnails.md`.

---

## Thumbnail Strategy

For the full thumbnail composition framework (face psychology, color science, text rules, layout patterns), see `skills/youtube-strategist/references/packaging-data.md`.

### 10 Iconic Thumbnail Types

Use as a selection guide when designing thumbnails:

1. **Big Bold Colorful**: saturated backgrounds, large subject, high energy
2. **Raw**: minimal editing, authentic/unfiltered look
3. **Before/After**: split frame showing transformation
4. **Products**: hero product shot, clean layout
5. **Numbers**: large numerals as focal point (dollar amounts, stats, counts)
6. **Scary**: dark tones, tension, warning energy
7. **Reactions**: exaggerated facial expressions, emotional response
8. **Nostalgic**: vintage feel, throwback aesthetic
9. **Quotes**: bold text quote as centerpiece
10. **Comments**: screenshot-style social proof from real comments

### QA Checks (every thumbnail)

- **Squint test**: still readable when you squint at it
- **Dark mode check**: looks good on dark backgrounds (80% of users browse in dark mode)
- **Glance test**: understood in 0.5 seconds or less
- **3 elements max**: no more than three visual elements competing for attention

### A/B Testing Workflow

- **YouTube native**: Test and Compare feature. Optimize for watch time per impression, not CTR alone
- **TubeBuddy**: alternative testing tool if native A/B is unavailable

### Color Guidance

- Cyan thumbnails average +36% more views
- Green, yellow, and orange also perform well
- Brightness sweet spot: 100-110
- High contrast between subject and background is critical

### Face Guidance

- Multiple faces outperform single face (+35-50% CTR)
- Sad faces average 2.3M views per video
- Surprise expression: +49% CTR
- Strong emotion always beats neutral expression

### Text in Thumbnails

- Only add text if it provides new information beyond the title
- Keep under 10 characters
- Text should occupy less than 7% of thumbnail area

---

## Metadata Optimization

### Title Optimization

- Front-load the hook in the first 5-6 words (30-40 characters)
- Keep total length under 50 characters ideal
- Use active verbs and power words (SHOCKING, BRUTAL, TERRIFYING)
- Negative framing averages +22% more views than positive framing

### Description

- First line: strong CTA or primary link
- Follow with 1-2 paragraphs of natural, keyword-rich summary
- No keyword spam. Tags do nothing; skip them entirely

### Chapters

Always include chapters. They help discovery, improve viewer experience, and boost retention. Name each chapter as a mini-hook that creates curiosity about that section.

### Title Suggestions (when generating metadata)

Provide 3-5 title options using the 3 Drivers framework:
- **Curiosity** (61% of top titles): create an information gap
- **Desire** (46%): sell the outcome
- **Fear** (40%): threat avoidance

Stack multiple drivers per title for maximum impact.

### Thumbnail Concept Brief (when generating metadata)

Include a brief thumbnail concept with every metadata generation:
- Composition layout (subject placement, background)
- Key visual elements (max 3)
- Suggested color palette based on color guidance above

---

### Cross-Niche Outlier Detection

```bash
# TubeLab API (recommended, 5 credits per query)
python3 <skill_dir>/scripts/scrape_cross_niche_tubelab.py

# yt-dlp (legacy, unreliable)
python3 <skill_dir>/scripts/scrape_cross_niche_outliers.py
```

See `directives/cross_niche_outliers.md`.

### Simple Video Edit (FFmpeg + Auphonic YouTube upload)

```bash
python3 <skill_dir>/scripts/simple_video_edit.py <input.mp4> --title "My Video"
```

FFmpeg-based silence removal + Whisper transcription + Claude metadata + Auphonic upload.

### Recommended Workflow

See `directives/smart_video_edit.md` for the recommended full editing workflow combining
neural VAD silence removal with 3D swivel teasers.

---

## Related Skills

- **youtube-strategist**: Pre-production strategy, outlier research, and packaging optimization
- **youtube-producer**: Video scripting and retention planning
