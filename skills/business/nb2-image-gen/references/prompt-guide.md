# Nano Banana 2 Prompt Guide

Compiled from Google Cloud, Google DeepMind, and community best practices.

## Core Principle

NB2 is a thinking model. It understands intent, physics, and composition. Don't write prompts like search queries. Write like you're art-directing a designer: clear, specific, concise.

## The Formula

```
Create a [ASSET TYPE] about [SUBJECT] in a [STYLE/MOOD] style.
Show [COMPOSITION/SCENE] with [LIGHTING/ANGLE].
Text: '[EXACT TEXT]' in [FONT STYLE] at [PLACEMENT].
Aspect ratio [AR], high resolution.
```

One to two sentences. That's it.

## What Makes Strong Prompts

- Asset type first (product card, banner, thumbnail, infographic)
- Exact target audience or context
- Mood/style explicitly stated (dark tech, warm editorial, minimal)
- Composition and camera angle defined
- Aspect ratio upfront
- 1-2 sentences maximum

## What Makes Weak Prompts

- Vague ("make a cool image")
- Conflicting ("super minimal but very busy")
- Overloaded scenes without focal point
- Forgetting aspect ratio
- Too many text elements

## Text Rendering

NB2 has strong text rendering but it's not perfect. Rules:

1. Put EXACT text in quotation marks
2. Describe placement: "bold white text '50% OFF' in the top-right corner"
3. Mention contrast: "high-contrast text against dark background"
4. One font style per image
5. Keep text brief (3-5 words per text block max)
6. Max 3-4 text blocks per image
7. ALWAYS verify output -- zoom in and check spelling

## Aspect Ratios

NB2 supports extreme ratios (1:8 to 8:1).

| Ratio | Use |
|-------|-----|
| 16:9 | Product cards, OG images, YouTube thumbnails, web banners |
| 1:1 | Social feed, profile images |
| 4:5 | Instagram feed, product shots |
| 9:16 | Stories, mobile screens |
| 3:1 | Email headers |
| 4:1+ | Ultra-wide web banners |

## Style Keywords That Work

### Dark/Tech
dark background, glowing elements, neon accents, grid pattern, neural network, constellation, terminal aesthetic, deep navy, ambient glow

### Premium/Luxury
minimal, clean, metallic accents, subtle gradients, sophisticated typography, muted palette, editorial, museum quality

### Warm/Organic
golden hour lighting, warm tones, natural textures, handcrafted feel, paper grain, soft shadows

### Bold/Impact
high contrast, saturated colors, large typography, geometric shapes, split composition, dynamic angles

## Product Cover Prompts (Examples)

### Dark Tech Product Card
```
Create a premium digital product cover card in dark tech style. Deep navy background with subtle glowing grid of small amber dots connected by thin lines. Bold white text "PRODUCT NAME" centered. Smaller gray subtitle below. Amber accent color for highlights and price badge. Minimal, no photos, no people. 16:9 landscape, high resolution.
```

### Clean SaaS Card
```
Create a clean SaaS product card on white background. Soft blue-purple gradient accent in top-left corner. Bold dark text "Product Name" with light gray tagline below. Small feature icons in a row. Rounded corners feel. Modern, minimal. 16:9 landscape.
```

### Course/Digital Product
```
Create a course cover image with dark gradient background transitioning from deep purple to black. Gold accent text "COURSE TITLE" in bold sans-serif, centered. Subtle geometric pattern behind text. Small author name in thin white font below. Premium, aspirational feel. 16:9 landscape.
```

## Image Grounding

NB2 can search the web to understand real-world subjects before generating. Works for:
- Specific locations (landmarks, buildings)
- Exact animal species/breeds
- Botanical subjects
- Does NOT work for specific people (blocked)

## Cost

- ~$0.04/image (Gemini Flash Image)
- ~$0.24/4K image (Nano Banana Pro)

## Thinking Mode

Keep disabled by default. Enable only when:
- Model produces nonsensical results
- Complex infographics
- Combining image grounding with spatial reasoning

## Sources

- Google Cloud: Ultimate Prompting Guide for Nano Banana
- Google DeepMind: How to Create Effective Image Prompts
- DEV.to: Getting the Most Out of Nano-Banana 2
- InVideo: Nano Banana 2 Ultimate Prompt Guide
