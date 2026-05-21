---
name: nb2-image-gen
description: |
  Generate images using Nano Banana 2 (Gemini) for any purpose: product covers, thumbnails,
  social cards, banners, hero images, email headers, Open Graph cards. Not limited to ad templates.
  Two modes: prompt builder (construct optimized NB2 prompts) and direct generation (API call).
  Use when user asks to "generate an image", "create a cover", "make a thumbnail",
  "product image", "social card", "banner", "NB2", "Nano Banana", or needs any non-ad image.
---

# NB2 Image Gen

Generate any image using Nano Banana 2 (Gemini). Product covers, thumbnails, social cards, banners, hero images -- anything that's not a templated ad creative (use `ads-designer` for that).

## Model

**Nano Banana 2** (`gemini-3-pro-image-preview`)
- Best-in-class text rendering for AI image generation
- Supports extreme aspect ratios (1:8 to 8:1)
- Image grounding (web search for real-world references)
- Product image reference via `inlineData`

## Prerequisites

- `GEMINI_API_KEY` in environment
- Python 3.10+ with `google-genai`, `Pillow`, `python-dotenv`

## Quick Start

### Single image from prompt
```bash
python skills/nb2-image-gen/scripts/generate.py \
  --prompt "Dark tech product card with amber accents..." \
  --output cover.png \
  --aspect 16:9
```

### Batch from JSON
```bash
python skills/nb2-image-gen/scripts/generate.py \
  --batch prompts.json \
  --output ./covers/ \
  --count 2
```

### With reference image
```bash
python skills/nb2-image-gen/scripts/generate.py \
  --prompt "Redesign this as a dark premium card..." \
  --ref screenshot.png \
  --output redesigned.png
```

## Prompt Engineering for NB2

### The Formula

> "Create a [ASSET TYPE] in [STYLE] style. [COMPOSITION]. Text: '[EXACT TEXT]' in [PLACEMENT]. Aspect ratio [AR], high resolution."

### Rules

1. **1-2 sentences max.** Short, specific prompts beat long vague ones
2. **Asset type first:** product card, YouTube thumbnail, social banner, email header
3. **Text in quotes** with explicit placement: `bold white text "ALL ACCESS" top center`
4. **Contrast explicitly:** "high-contrast text against dark background"
5. **One font style** per image, minimal text
6. **Aspect ratio** in prompt: "16:9 landscape" / "4:5 vertical" / "1:1 square"
7. **Style/mood** explicitly: premium, dark, tech, minimal, warm, editorial
8. **Exclusions explicit:** "NO photos, NO people, NO logos, NO watermarks"

### What Works Well

- Dark backgrounds with glowing accent elements
- Geometric patterns, grids, abstract shapes
- Bold typography as design element
- Gradient overlays and light effects
- Clean minimal compositions with one focal point

### What to Avoid

- Conflicting instructions ("minimal but busy")
- Too many text elements (max 3-4 text blocks)
- Vague requests ("make it cool")
- Overloaded scenes without clear hierarchy

### Text Rendering Tips

- Spell out EXACTLY what text should appear, in quotes
- Describe font style: "bold sans-serif", "thin uppercase", "monospace"
- Specify color + size: "large white bold", "small gray caption"
- Placement: "centered", "top-right corner", "bottom bar"
- Fewer text elements = better rendering quality
- ALWAYS verify text in output -- NB2 sometimes garbles words

### Aspect Ratios

| Use Case | Ratio | Prompt Keyword |
|----------|-------|----------------|
| Product card / OG image | 16:9 | "16:9 landscape, 1200x630" |
| Social feed | 1:1 | "square 1:1" |
| Instagram / product | 4:5 | "4:5 vertical" |
| Story / mobile | 9:16 | "9:16 vertical" |
| YouTube thumbnail | 16:9 | "16:9 landscape, 1280x720" |
| Email header | 3:1 | "wide banner 600x200" |
| Web banner | 4:1 | "ultra-wide banner" |

## Batch JSON Format

```json
{
  "project": "the product Coach",
  "generated_at": "2026-03-25",
  "images": [
    {
      "id": "all-access-cover",
      "name": "All-Access Bundle Cover",
      "aspect_ratio": "16:9",
      "prompt": "Full prompt here...",
      "reference_images": []
    }
  ]
}
```

## Script: generate.py

### CLI Options

| Flag | Default | Description |
|------|---------|-------------|
| `--prompt` / `-p` | -- | Single prompt text |
| `--batch` / `-b` | -- | Path to JSON batch file |
| `--output` / `-o` | `./output/` | Output file or directory |
| `--ref` / `-r` | -- | Reference image(s) for the model |
| `--aspect` / `-a` | `1:1` | Aspect ratio (only for single prompt) |
| `--count` / `-n` | 1 | Variations per prompt |
| `--delay` / `-d` | 3.0 | Seconds between API calls |

### Output

Single mode: saves to the specified file path.
Batch mode: creates a folder per image with `image_v1.png` + `prompt.txt`.

## Integration

- `ads-designer`: Use that for templated ad creatives (40 formats). Use this for everything else.
- `website-brand-analysis`: Get brand colors/style for consistent prompts.
- `product-frontend`: Generate product covers for digital products.
- `newsletter-ad-creator`: Generate newsletter ad images.

## References

- `references/prompt-guide.md` -- Full NB2 prompting guide with examples
