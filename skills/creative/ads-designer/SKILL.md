---
name: ads-designer
description: |
  Generate image ad creatives using Nano Banana 2 (Gemini) or Higgsfield.
  40 static ad templates covering every format: headline, offer, testimonial, us-vs-them,
  before/after, negative marketing, press, stat surround, UGC, comparison grid, and more.
  Three modes: single-ad, batch prompts (manual), or automated batch generation (Python script).
  Mode 3 passes real product photos as reference images so the model matches actual packaging.
  Use when user asks to "design an ad", "create ad images", "generate static ads",
  "batch ad generation", "make Meta ad creatives", "Nano Banana ads", or "automated ads".
---

# Ad Designer

Generate professional static ad creatives for Meta/social campaigns using AI image generation. 40 proven ad templates with single-ad, batch prompt, and fully automated generation modes.

**Brand consistency via DESIGN.md.** When generating an ad library for a brand that already has a `DESIGN.md`, read it and pass the colors, typography, and component tokens as constraints to the image generation prompts. This keeps the entire ad library on-brand without per-ad babysitting. If the brand has no DESIGN.md, recommend creating one via `skills/design-md/SKILL.md` before scaling the ad library past 10 creatives.

## Model

**Nano Banana 2** (`gemini-3-pro-image-preview`)
- State-of-the-art image generation and editing
- Strong text rendering for ad copy (product labels, headlines)
- Supports multiple aspect ratios
- Also available through **Higgsfield** ($50/mo) for faster generation and better UI

## Prerequisites

- `GEMINI_API_KEY` in environment (for direct API)
- Brand guidelines: ideally from `website-brand-analysis` (with Image Generation Prompt Modifier)
- Product images (1-3 images recommended)
- Creative brief OR batch mode selection

## Three Modes

### Mode 1: Single Ad
Traditional workflow. Receive brief, construct prompt, generate one image, review, deliver.

### Mode 2: Batch Prompts (Manual)
Generate brand-specific prompts for all 40 templates in one shot. Output is markdown with ready-to-paste prompts for Higgsfield or direct API.

### Mode 3: Automated Batch Generation (Recommended)
Fully automated pipeline. Generates JSON prompts, fires them to Gemini API via Python script, passes product photos as reference images, downloads results, and builds an HTML gallery. One command, walk away, review a gallery.

**Mode 3 is the primary workflow for scaled ad production.**

---

## Aspect Ratios

Set aspect ratio in the platform UI (Higgsfield) or in the prompt (direct API).

| Ratio | Dimensions | Use Case | Prompt Keyword |
|-------|------------|----------|----------------|
| 1:1 | 1080x1080 | Feed (universal) | "square image" |
| 4:5 | 1080x1350 | Feed (recommended) | "4:5 vertical image" |
| 9:16 | 1080x1920 | Stories/Reels | "9:16 vertical image" |
| 16:9 | 1920x1080 | Landscape | "16:9 landscape image" |

**Default to 1:1** unless brief specifies otherwise.

---

## 40 Ad Templates

Organized by category. Full prompt templates in `references/template-prompts-original.md` (verbatim) and `references/template-prompts-adapted.md` (integrated with our pipeline). Quick-reference catalog in `references/ad-format-catalog.md`.

### Copy-Forward (6)
| # | Format | Funnel | Ratio |
|---|--------|--------|-------|
| 1 | Headline | TOFU/MOFU | 4:5 |
| 2 | Offer/Promotion | MOFU/BOFU | 9:16 |
| 5 | Bullet-Points | MOFU | 4:5 |
| 21 | Bold Statement / Reaction | TOFU | 1:1 |
| 23 | Long-Form Manifesto | MOFU | 4:5 |
| 30 | Hero Statement + Icon Bar | MOFU | 1:1 |

### Social Proof (7)
| # | Format | Funnel | Ratio |
|---|--------|--------|-------|
| 3 | Testimonials | MOFU | 9:16 |
| 6 | Social Proof Stack | MOFU/BOFU | 4:5 |
| 11 | Pull-Quote Review Card | MOFU | 1:1/4:5 |
| 15 | Social Comment Screenshot | TOFU/MOFU | 1:1 |
| 16 | Curiosity Gap Hook Quote | TOFU | 1:1 |
| 17 | Verified Review Card | MOFU | 1:1 |
| 19 | Highlighted Testimonial | MOFU/BOFU | 1:1 |

### Comparison (4)
| # | Format | Funnel | Ratio |
|---|--------|--------|-------|
| 7 | Us vs Them | MOFU | 4:5 |
| 8 | Before & After (UGC) | TOFU/MOFU | 9:16 |
| 25 | Us vs Them Color Split | MOFU | 1:1 |
| 31 | Comparison Grid | MOFU/BOFU | 1:1 |

### Data/Authority (7)
| # | Format | Funnel | Ratio |
|---|--------|--------|-------|
| 4 | Features/Benefits Point-Out | MOFU | 4:5 |
| 10 | Press/Editorial | TOFU/MOFU | 4:5 |
| 13 | Stat Surround (Product) | MOFU | 1:1 |
| 18 | Stat Surround (Lifestyle) | MOFU | 1:1 |
| 20 | Advertorial Content Card | TOFU | 4:5 |
| 26 | Stat Callout (Lifestyle) | TOFU/MOFU | 4:5 |
| 28 | Feature Arrow Callout | MOFU | 1:1 |

### Product Showcase (6)
| # | Format | Funnel | Ratio |
|---|--------|--------|-------|
| 12 | Lifestyle + Colorway Array | TOFU | 1:1 |
| 14 | Bundle Showcase + Benefit Bar | MOFU/BOFU | 1:1 |
| 22 | Flavor Story / "Tastes Like" | TOFU/MOFU | 1:1 |
| 27 | Benefit Checklist Showcase | MOFU | 1:1 |
| 35 | Hero Product + Stat Bar | MOFU | 1:1 |
| 37 | Hero + Icon Bar + Promo | BOFU | 1:1 |

### Native/Organic (5)
| # | Format | Funnel | Ratio |
|---|--------|--------|-------|
| 9 | Negative Marketing (Bait) | TOFU | 4:5 |
| 33 | Faux Press Screenshot | TOFU | 4:5 |
| 34 | Faux iPhone Notes | TOFU | 9:16 |
| 36 | Whiteboard Before/After | TOFU/MOFU | 1:1 |
| 40 | Post-It Note (Ugly) | TOFU | 1:1 |

### Hybrid (5)
| # | Format | Funnel | Ratio |
|---|--------|--------|-------|
| 24 | Product + Comment Callout | MOFU | 1:1 |
| 29 | UGC + Viral Post Overlay | TOFU | 4:5 |
| 32 | UGC Story Callout Bubbles | TOFU | 9:16 |
| 38 | UGC + Product + Review Split | MOFU | 1:1 |
| 39 | Curiosity Gap Scroll-Stopper | TOFU | 4:5 |

---

## Workflow: Single Ad Mode

### 1. Receive Brief

Get creative brief with:
- Ad template number (1-40) or concept description
- Exact copy/text (or let `review-miner` / `copy-writing` provide it)
- Target aspect ratio
- Brand Modifier paragraph (from `website-brand-analysis`)
- Product images (if any)

### 2. Construct Prompt

Load the appropriate template from `references/template-prompts-adapted.md`. Fill in:
- `{BRAND_MODIFIER}` with the Image Generation Prompt Modifier from brand analysis
- All bracketed placeholders with brand-specific details
- Copy from `review-miner` output where noted

### 3. Generate Image

**Direct API:**
```bash
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [{
        "text": "YOUR_PROMPT_HERE"
      }]
    }],
    "generationConfig": {
      "responseModalities": ["image", "text"]
    }
  }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | base64 -d > output.png
```

**Higgsfield:** Paste prompt directly into Higgsfield UI. Set aspect ratio in settings.

### 4. Review Before Sending

**ALWAYS review generated images before sending to user.**

Check for:
- [ ] Text is correct (no garbled words)
- [ ] No hallucinated logos or brand names
- [ ] Product label/packaging rendered accurately
- [ ] No unexpected elements
- [ ] Aspect ratio looks correct
- [ ] Overall quality is acceptable

### 5. Iterate if Needed

If image has issues:
- Simplify the prompt (fewer instructions)
- Be more explicit about exclusions
- Try regenerating (Nano Banana 2 is very consistent but results vary)

### 6. Deliver

Save and send:
```
~/clawd/output/{project}-{ad-type}-v{N}.png
```

---

## Workflow: Batch Mode (Primary)

The Nano Banana 2 scaled production workflow. Two steps.

### Step 1: Brand DNA

Run `website-brand-analysis` on the target brand URL. Ensure the output includes the **Image Generation Prompt Modifier** (50-75 word paragraph).

If the user already has brand guidelines, extract/write the Image Generation Prompt Modifier manually:
```
Use [primary color #hex] as primary, [secondary #hex] as accent. Typography: [weight] [style]
sans-serif in [color] for headlines, [weight] for body. Photography: [lighting], [angle], [mood].
Background: [color/texture]. Product shots: [style]. Overall aesthetic: [2-3 adjectives].
```

### Step 2: Generate All Prompts

Input:
- Brand DNA / Image Generation Prompt Modifier
- Product images (attach 1-3)
- Template selection: "all 40" or specific numbers (e.g., "1, 7, 13, 15, 21, 40")

Process:
1. Load `references/template-prompts-adapted.md`
2. For each selected template, fill all placeholders with brand-specific details
3. Prepend the Brand Modifier to each prompt
4. If `review-miner` output is available, inject mined copy into relevant templates

Output: A single markdown document with all prompts numbered, each self-contained and ready to paste.

```markdown
# [BRAND] Ad Prompts - Batch Generation

## Brand Modifier
[The 50-75 word paragraph]

---

## Prompt 1: Headline
[Complete, ready-to-paste prompt]

---

## Prompt 7: Us vs Them
[Complete, ready-to-paste prompt]

...
```

### Step 3: Execute

- **DIY:** Paste each prompt into Higgsfield or Nano Banana 2 directly
- **VA handoff:** Send the document to a VA who queues all prompts in Higgsfield
- **API batch:** Loop through prompts programmatically via Gemini API

---

## Workflow: Automated Batch Mode (Mode 3)

The fully automated pipeline. Brand DNA to finished gallery, no copy-pasting.

### Why Product Image Reference Matters

When you pass real product photos alongside the text prompt, Nano Banana 2 matches your actual packaging in the output. Without references, it guesses what the product looks like. With references, it reproduces your real wrapper, label placement, and colors. This is the difference between "generic protein bar" and "your exact product."

The Gemini API handles this natively via `inlineData` -- product images go in the `contents` array alongside the text prompt. No special "edit endpoint" needed.

### Step 1: Brand DNA

Same as Mode 2. Run `website-brand-analysis` to get the Image Generation Prompt Modifier.

### Step 2: Product Images

Drop 1-3 product photos into a folder:
- Front of packaging (required)
- Angled shot (recommended)
- Lifestyle shot (optional, helps with context templates)

Higher resolution = better results. The script resizes to 800x800 max for the API.

### Step 3: Generate JSON Prompts

Instead of markdown output (Mode 2), generate a `prompts.json` file:

```json
{
  "brand": "Brand Name",
  "product": "Product Name",
  "brand_modifier": "The 50-75 word Image Generation Prompt Modifier",
  "generated_at": "2026-03-13T10:00:00",
  "prompts": [
    {
      "template_number": 1,
      "template_name": "headline",
      "category": "copy-forward",
      "funnel_stage": "TOFU/MOFU",
      "aspect_ratio": "4:5",
      "needs_product_images": true,
      "prompt": "Full completed prompt with brand modifier baked in...",
      "notes": "Copy upgrade suggestions"
    }
  ]
}
```

Process:
1. Load `references/template-prompts-adapted.md`
2. Fill all placeholders with brand-specific details
3. Prepend Brand Modifier to each prompt
4. Set `needs_product_images` based on template metadata tag
5. Output as JSON

### Step 4: Run the Generation Script

```bash
# Full batch -- all 40 templates
python skills/ads-designer/scripts/generate_ads.py \
  --prompts prompts.json \
  --product-images product-front.png product-angle.png

# Specific templates only (test run)
python skills/ads-designer/scripts/generate_ads.py \
  --prompts prompts.json \
  --product-images ./product-images/ \
  --templates 1,7,15,21,40

# Multiple variations per template
python skills/ads-designer/scripts/generate_ads.py \
  --prompts prompts.json \
  --product-images ./product-images/ \
  --count 3 \
  --output ./my-brand-ads/
```

**CLI options:**

| Flag | Default | Description |
|------|---------|-------------|
| `--prompts` / `-p` | required | Path to JSON prompts file |
| `--product-images` / `-i` | none | Product image files or directories |
| `--output` / `-o` | `./output/` | Output directory |
| `--count` / `-n` | 1 | Variations per template |
| `--delay` / `-d` | 3.0 | Seconds between API calls (rate limiting) |
| `--templates` / `-t` | all | Comma-separated template numbers |

### Step 5: Review Gallery

The script auto-generates `gallery.html` in the output directory. Open it in a browser to:
- Browse all generated ads grouped by template
- Filter by category (Copy-Forward, Social Proof, etc.)
- Click to enlarge any image
- View the prompt used for each template

You can also regenerate the gallery manually:
```bash
python skills/ads-designer/scripts/generate_gallery.py --input ./output/
```

### Output Structure

```
output/
├── 01_headline/
│   ├── ad_v1.png
│   └── prompt.txt
├── 07_us_vs_them/
│   ├── ad_v1.png
│   └── prompt.txt
├── ...
├── results.json          # Generation log (success/fail per prompt)
└── gallery.html          # Visual gallery
```

### Cost Estimates

| Scope | Images | Estimated Cost |
|-------|--------|---------------|
| 5-template test run | 5 | ~$0.20-1.20 |
| Full 40-template run | 40 | ~$1.60-9.60 |
| Full run, 3 variations each | 120 | ~$4.80-28.80 |

Pricing depends on output resolution. Gemini API charges per image generation call.

### Troubleshooting

| Issue | Fix |
|-------|-----|
| Rate limit errors | Increase `--delay` to 5-10 seconds |
| Timeout | Script retries once automatically. If persistent, run failed templates separately |
| Product not matching | Use higher-res product photos. Front-facing shots work best |
| Text garbled | Simplify the prompt. Fewer text elements = better rendering |
| API key error | Set `GEMINI_API_KEY` or `NANO_BANANA_API_KEY` in environment |

---

## Prompt Engineering

### Critical Rules

1. **Be explicit about exclusions:**
   ```
   NO logos. NO brand names. NO company names. NO watermarks. NO additional text.
   ```

2. **Specify exact text:**
   ```
   The ONLY text on the image should be exactly: [your text here]
   ```

3. **Keep prompts focused:**
   - Don't overload with too many instructions
   - Separate layout from content from style

4. **Product consistency:**
   - Attach 1-3 product images as reference
   - Nano Banana 2 is very good at reproducing product labels and packaging
   - Specify "Use the attached images as brand reference" at the start

5. **Aspect ratio in prompt (direct API) or settings (Higgsfield):**
   ```
   Generate a square 1:1 image...
   ```

### Common Issues & Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| Hallucinated logos | Model fills "empty" space | Add "NO logos. NO brand names." explicitly |
| Garbled text | Too many text instructions | Simplify, use fewer lines |
| Wrong aspect ratio | Not specified clearly | Start prompt with "Generate a square/4:5/etc image" |
| Extra decorations | Over-specified design | Add "no decorations, no borders, no frames" |
| Generic stock look | Vague prompt | Add specific style cues (warm lighting, minimal, etc.) |
| Bad product label | Poor reference image | Use higher-quality product images, specify label details |

---

## Expanding the Template Library

To add new ad formats beyond the 40:

1. Find an ad creative you want to replicate
2. Give Claude the image and say: "Give me the standardized Nano Banana 2 prompt for this that I can use for any brand"
3. Claude generates a template with [PLACEHOLDER] variables
4. Add to `references/template-prompts-original.md` and create an adapted version
5. Update `references/ad-format-catalog.md`

This is how the original 40 were built -- Claude reverse-engineers the prompt from the output.

---

## Integration

This skill works with:
- `website-brand-analysis`: Provides brand guidelines + Image Generation Prompt Modifier
- `review-miner`: Provides customer-sourced copy for ad templates
- `copy-writing`: Headline formulas and CTA guidelines
- `ads-creative`: Hook library for headline inspiration
- `creative-director`: Orchestrates asset creation across campaigns
- `ads-strategy`: Campaign planning determines which templates to prioritize
- `ads-meta`: Publishes generated creatives to Meta Ads

## Output

Save images to:
```
~/clawd/output/{project}-{ad-type}-v{N}.png
```

Save batch prompt documents to:
```
~/clawd/output/{brand}-batch-prompts.md
```

## References

- `references/template-prompts-original.md` -- 40 original Nano Banana 2 templates (verbatim)
- `references/template-prompts-adapted.md` -- 40 templates adapted to our pipeline (with `Product images` metadata)
- `references/ad-format-catalog.md` -- Quick-reference catalog with categories, funnel stages, product type recommendations
- `scripts/generate_ads.py` -- Automated batch generation script (Mode 3)
- `scripts/generate_gallery.py` -- HTML gallery generator for reviewing batch output
- `references/corey-image-generation.md` -- additional framework from coreyhaines31/marketingskills (MIT): image model selection (Gemini/Flux/Ideogram/GPT Image/Midjourney), OG image guidance, optimization, prompt structure formula
