---
name: newsletter-ad-creator
description: |
  Create high-converting newsletter ad banner images using proven HubSpot-style layouts.
  Interviews the user about their product, offer, and audience, then generates Nano Banana Pro
  (Gemini) image prompts matching 6 tested newsletter ad templates. Use when user asks to
  "create newsletter ads", "design email banner", "newsletter ad creative",
  "sponsor ad for newsletter", "email ad image", or "newsletter banner".
---

# Newsletter Ad Creator

Generate newsletter banner ad images that match proven high-performing patterns from HubSpot-style campaigns. Specialized for inline email ads that drive lead magnet downloads, ebook signups, and free tool registrations.

## Model

**Nano Banana Pro** (`gemini-3-pro-image-preview`) via the same API workflow as `ads-designer`.

## Prerequisites

- `GEMINI_API_KEY` in environment
- Product/offer details from user
- Read `references/style-guide.md` for visual patterns
- Read `references/prompt-library.md` for prompt templates

## Aspect Ratios (Newsletter Banners)

| Ratio | Use Case | Prompt Keyword |
|-------|----------|----------------|
| 16:9 | Standard newsletter banner (recommended) | "16:9 landscape image" |
| 2:1 | Wide newsletter banner | "2:1 wide landscape image" |
| 3:2 | Compact newsletter banner | "3:2 landscape image" |

**Default to 16:9** unless user specifies otherwise.

## Workflow

### Step 1: Interview (5 Questions)

Ask these 5 questions before generating anything:

**Q1. What are you promoting?**
Options: ebook, guide, tool, course, templates, report, playbook, checklist, webinar, other
> This determines the mockup type (ebook cover, laptop screen, document pages, etc.)

**Q2. What's the headline?**
Ask if they have one or want you to write it. If writing, follow the copy formula:
`[Action Verb] + [Quantified Value] + [Benefit]`
Power words: Unlock, Supercharge, Transform, Enhance, Master, Cut, Discover

**Q3. What's the subtitle or supporting line?**
1-2 sentence benefit expansion or "Free [format]: [specific promise]"

**Q4. Which layout style?**
Present the 6 options below, or offer "auto-pick based on product type":

| # | Style | Best For | Look |
|---|-------|----------|------|
| 1 | Clean Ebook | Ebooks, guides, reports | Cream background, bold headline left, 3D ebook mockup right |
| 2 | Dark Authority | Tools, courses, premium offers | Dark navy, white text, device mockup, coral accents |
| 3 | Bold Product | Template packs, prompt bundles | Cream base, bold headline, angled ebook + geometric shapes |
| 4 | YouTube Thumbnail | Reports, viral content, bold claims | Full-bleed dark background, ALL CAPS, collage + stickers |
| 5 | Split Diagonal | Prompt collections, multi-asset offers | Diagonal two-tone split, serif headline, stacked screenshots |
| 6 | Warm Minimal | Playbooks, guides, courses | Light cream, lots of whitespace, floating screenshots |

**Q5. Color preference?**
Options:
- Warm/Orange: cream background + orange (#FF6B35) accents
- Dark/Navy: navy (#1B2838) background + coral/white accents
- Minimal/Cream: off-white background + subtle orange highlights
- Bold/Dark: textured dark background + red/yellow accents
- Custom: user provides hex codes

### Step 2: Auto-Pick Logic

If user selects "auto-pick", use this mapping:

| Product Type | Recommended Layout | Recommended Colors |
|---|---|---|
| Ebook, guide, report | Clean Ebook (#1) | Warm/Orange |
| Tool, software, SaaS | Dark Authority (#2) | Dark/Navy |
| Templates, prompts, swipe files | Bold Product (#3) | Warm/Orange |
| Annual report, data, research | YouTube Thumbnail (#4) | Bold/Dark |
| Multi-asset bundle, collection | Split Diagonal (#5) | Dark/Navy |
| Playbook, course, masterclass | Warm Minimal (#6) | Minimal/Cream |

### Step 3: Generate Prompts

1. Load `references/prompt-library.md`
2. Select the 2 templates matching the chosen layout
3. Fill placeholders:
   - `{HEADLINE}` = user's headline
   - `{SUBTITLE}` = user's subtitle
   - `{PRODUCT_TYPE}` = ebook/guide/tool/etc.
   - `{PRIMARY_COLOR}` = hex from color selection
   - `{ACCENT_COLOR}` = complementary accent
   - `{ASPECT_RATIO}` = 16:9 unless specified
4. Present 2-3 prompt variants to user
5. Let them pick or request modifications

### Step 4: Generate Image

Run the Gemini API call:

```bash
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [{
        "text": "PROMPT_HERE"
      }]
    }],
    "generationConfig": {
      "responseModalities": ["image", "text"]
    }
  }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | base64 -d > output.png
```

Save to: `~/clawd/output/{project}-newsletter-ad-{layout}-v{N}.png`

### Step 5: Review

**ALWAYS review before delivering.** Check:
- [ ] Headline text renders correctly (no garbled words)
- [ ] Subtitle text is accurate
- [ ] No hallucinated logos or brand names
- [ ] Layout matches the selected template style
- [ ] Color scheme is correct
- [ ] Mockup type matches the product (ebook = 3D book, tool = laptop, etc.)
- [ ] Aspect ratio is correct for newsletter banner

Use `Read` tool to view the generated image.

### Step 6: Iterate or Deliver

If issues found:
- Simplify prompt (fewer text elements)
- Be more explicit about exclusions
- Adjust mockup description
- Regenerate

When approved, deliver with caption describing the layout and dimensions.

## Copy Rules

- NEVER use em dashes in headlines or subtitles
- Use numbers in headlines when possible (100+, 200, 50, 1000+)
- Keep headlines under 10 words
- Keep subtitles under 20 words
- Structure: `[Action Verb] + [Quantified Value] + [Benefit]`

## Integration

This skill works with:
- `ads-designer`: Shares the same Gemini API workflow and prompt conventions
- `newsletter-monetizer`: Creates ad creatives for newsletter sponsorship packages
- `newsletter-writer`: Banner ads can promote lead magnets within newsletter issues
- `marketing-ads`: Can provide creative briefs that feed into this skill
- `creative-director`: Can orchestrate newsletter ad creation as part of larger campaigns

## Output

Save images to:
```
~/clawd/output/{project}-newsletter-ad-{layout}-v{N}.png
```

Examples:
- `cyber-corsairs-newsletter-ad-clean-ebook-v1.png`
- `alfagap-newsletter-ad-dark-authority-v2.png`
- `ai-health-lab-newsletter-ad-youtube-thumb-v1.png`
