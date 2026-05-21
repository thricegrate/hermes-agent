# Video Creation Directive

## Render a composition

```bash
cd skills/remotion
npx ts-node scripts/render.ts --comp <ID> --props '<JSON>' --out out/<name>.mp4
```

## Available compositions

| ID | Best for | Key props |
|----|----------|-----------|
| `TextOverlay` | Quote cards, title screens | text, subtitle, animation, bgColor |
| `IntroOutro` | YouTube intros, branding | logoSrc, title, subtitle, style, showCta |
| `SocialClipVertical` | Reels, Shorts, TikTok | overlayText, bgVideoSrc/bgImageSrc |
| `SocialClipSquare` | Instagram, LinkedIn | overlayText, bgVideoSrc/bgImageSrc |
| `CaptionedVideo` | Videos with captions | videoSrc, captions (word+timing), activeColor |
| `DataViz` | Stats, bar charts | data (label+value), chartType, title |
| `DataVizHorizontal` | Horizontal bar charts | Same as DataViz with chartType: "horizontalBar" |

## Examples

**YouTube intro:**
```bash
npx ts-node scripts/render.ts --comp IntroOutro \
  --props '{"title":"My Newsletter","subtitle":"Weekly AI Newsletter","style":"bold"}' \
  --out out/intro.mp4
```

**Social quote card (vertical):**
```bash
npx ts-node scripts/render.ts --comp SocialClipVertical \
  --props '{"overlayText":"AI will not replace you. A person using AI will.","bgColor":"#0f172a"}' \
  --out out/quote-reel.mp4
```

**Growth chart:**
```bash
npx ts-node scripts/render.ts --comp DataViz \
  --props '{"title":"Subscribers","data":[{"label":"Q1","value":50000},{"label":"Q2","value":120000},{"label":"Q3","value":215000}]}' \
  --out out/growth.mp4
```

## Integration with other skills

- **video-scriptwriter** output -> `SocialClip` or `CaptionedVideo` props
- **newsletter-writer** stats -> `DataViz` props
- **youtube-producer** branding -> `IntroOutro` props
- **video-editor** -> Edit raw footage first, then overlay Remotion compositions
