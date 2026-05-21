---
name: remotion
description: |
  Programmatic video creation using React compositions. Build intros, social clips,
  captioned videos, data visualizations, and text animations -- all rendered to MP4.
  Use when user asks to "create a video", "render a composition", "make an intro",
  "generate a social clip", "add animated captions", "make a chart animation",
  "build a video from scratch", or "create video content".
metadata:
  tags: remotion, video, react, animation, composition, social-clip, captions, dataviz
---

# Remotion Video Creation

Create videos programmatically from parameterized React compositions rendered to MP4.
For editing existing footage (silence removal, jump cuts), use `video-editor` skill instead.

## Available Compositions

| Composition | Format | What it does |
|-------------|--------|--------------|
| `TextOverlay` | 1920x1080 | Animated text on solid/gradient bg (fadeIn, slideUp, typewriter, spring, scaleIn) |
| `IntroOutro` | 1920x1080 | Brand intro/outro with logo, tagline, optional CTA |
| `SocialClipVertical` | 1080x1920 | Vertical clip for Reels/Shorts/TikTok with text overlay |
| `SocialClipSquare` | 1080x1080 | Square clip for Instagram/LinkedIn with text overlay |
| `CaptionedVideo` | 1920x1080 | Video with word-by-word animated captions (TikTok style) |
| `DataViz` | 1920x1080 | Animated vertical bar chart |
| `DataVizHorizontal` | 1920x1080 | Animated horizontal bar chart |
| `Transition3DDemo` | 1920x1080 | 3D rotation effect (easeOut, 1s) |
| `Transition3DSpring` | 1920x1080 | 3D rotation effect (spring physics, 1.5s) |
| `Transition3DSubtle` | 1920x1080 | 3D rotation effect (subtle, 0.67s) |

## Quick Start

```bash
# Install dependencies (first time)
cd skills/remotion && npm install

# Preview all compositions in Remotion Studio
npm run studio

# Render a composition to MP4
npx ts-node scripts/render.ts --comp TextOverlay \
  --props '{"text":"My Newsletter","bgColor":"#1a1a2e","textColor":"#e94560"}' \
  --out out/intro.mp4

# Render with quality options
npx ts-node scripts/render.ts --comp DataViz \
  --props '{"title":"Growth","data":[{"label":"Q1","value":50000},{"label":"Q2","value":120000}]}' \
  --codec h264 --crf 18 --out out/chart.mp4
```

## Creating New Compositions

1. Create `.tsx` file in `src/` with Zod schema for props
2. Register in `src/Root.tsx` with `<Composition>` and `schema` prop
3. Preview in Studio (`npm run studio`)
4. Render via `scripts/render.ts`

See `directives/create-video.md` for full guide with examples.

## Integration Points

| Skill | How |
|-------|-----|
| `video-editor` | Complementary: video-editor cuts existing footage, remotion creates new content |
| `video-scriptwriter` | Script output -> SocialClip or CaptionedVideo props |
| `youtube-producer` | IntroOutro compositions for channel branding |
| `newsletter-writer` | DataViz compositions for newsletter stat graphics |

## Remotion Knowledge Base

37 rule files for Remotion domain knowledge. Load on demand when writing compositions:

**Core:** [compositions](rules/compositions.md), [sequencing](rules/sequencing.md), [timing](rules/timing.md), [animations](rules/animations.md), [parameters](rules/parameters.md), [calculate-metadata](rules/calculate-metadata.md), [trimming](rules/trimming.md)

**Media:** [assets](rules/assets.md), [audio](rules/audio.md), [videos](rules/videos.md), [images](rules/images.md), [gifs](rules/gifs.md), [fonts](rules/fonts.md)

**Text & Captions:** [text-animations](rules/text-animations.md), [subtitles](rules/subtitles.md), [display-captions](rules/display-captions.md), [import-srt-captions](rules/import-srt-captions.md), [transcribe-captions](rules/transcribe-captions.md), [measuring-text](rules/measuring-text.md)

**Effects:** [transitions](rules/transitions.md), [3d](rules/3d.md), [light-leaks](rules/light-leaks.md), [audio-visualization](rules/audio-visualization.md), [lottie](rules/lottie.md), [transparent-videos](rules/transparent-videos.md)

**Advanced:** [ffmpeg](rules/ffmpeg.md), [charts](rules/charts.md), [maps](rules/maps.md), [voiceover](rules/voiceover.md), [sfx](rules/sfx.md), [tailwind](rules/tailwind.md), [can-decode](rules/can-decode.md), [extract-frames](rules/extract-frames.md), [get-audio-duration](rules/get-audio-duration.md), [get-video-dimensions](rules/get-video-dimensions.md), [get-video-duration](rules/get-video-duration.md), [measuring-dom-nodes](rules/measuring-dom-nodes.md)

## Dependencies

- Node.js 18+, npm
- `cd skills/remotion && npm install`
