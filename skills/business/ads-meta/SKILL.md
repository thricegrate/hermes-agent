---
name: ads-meta
description: "Full Meta Ads pipeline: extract competitor creatives from Meta Ad Library, analyze them into strategy reports, and publish campaigns via the Marketing API. Use when the user wants to download Meta/Facebook ads, build swipe files, generate ad strategy reports, create Meta ad campaigns, or publish ads. Triggers: 'Meta ads,' 'Facebook ads,' 'Ad Library,' 'extract competitor ads,' 'download Meta ads,' 'swipe file,' 'ad strategy report,' 'publish to Meta,' 'create Meta campaign,' 'Meta ads analysis,' 'competitor ads Facebook,' 'ad library extraction.' Formerly: meta-ads-extractor, meta-ads-analyser, meta-ads-publisher."
metadata:
  version: 2.0.0
---

# Ads Meta

Full Meta Ads pipeline: extract competitor creatives from the Ad Library, analyze them into professional strategy reports, and publish your own campaigns via the Marketing API. Three stages that work independently or as a connected flow.

```
Extract (Ad Library) --> Analyze (Strategy Report) --> Publish (Marketing API)
```

---

## Stage 1: Extract

Pull ad creative assets (images, videos, landing page URLs) from Meta's Ad Library via browser automation.

### Prerequisites

- Browser tool (Playwright or similar)
- `curl` for downloading assets

### 1. Get the Correct Ad Library Page ID

The Ad Library uses a **delegate_page ID**, NOT the profile ID from meta tags. This is the #1 source of errors.

```
Navigate to: https://www.facebook.com/<page-username>/
Extract via JS: document.documentElement.innerHTML.match(/"delegate_page":\{[^}]*"id":"(\d+)"/)
Fallback (if no delegate_page): use fb://profile/<id> from al:android:url meta tag
```

The delegate_page ID is what `view_all_page_id` expects. See `references/dom-selectors.md` for details on both ID types.

### 2. Open the Ad Library with Filters

```
https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&is_targeted_country=false&media_type=image_and_meme&search_type=page&view_all_page_id={PAGE_ID}
```

Key filter values:
- `active_status`: `active` | `inactive` | `all`
- `media_type`: `image_and_meme` | `video` | `all` (omit for all)
- `country`: `ALL` | `US` | `DE` etc.

### 3. Extract Media URLs from DOM

Run the extraction JS from `references/dom-selectors.md` via browser evaluate. Returns JSON with image and video URLs.

**Extraction is instant (no network cost).** The JS extracts ALL URLs from the page. Then download only the specific assets requested. Page sort order matches DOM order: `images[0]` / `videos[0]` = highest impressions.

**Image selectors:** `img` elements with `fbcdn.net` src containing `s600x600` (ad thumbnails).
**Video selectors:** `video` elements with `fbcdn.net` src (direct .mp4 URLs).
**Video posters:** `video[poster]` attributes (full-res thumbnail frames).

### 4. Extract CTA Destination URLs

Each ad card has a CTA button linking to the advertiser's landing page:

```javascript
(() => {
  const ctas = [...document.querySelectorAll('a')]
    .filter(a => a.textContent.trim().match(/^(Learn More|Shop Now|Sign Up|Download|Get Offer|Book Now|Apply Now|Contact Us|Subscribe|Watch More|See More)$/i))
    .map(a => ({ text: a.textContent.trim(), url: a.href }))
    .filter(c => c.url && !c.url.includes('facebook.com/ads/library'));
  return JSON.stringify(ctas);
})()
```

These URLs can be passed to the **design-analysis** skill for offer/funnel analysis.

### 5. Download Assets & Capture Dimensions

All fbcdn.net URLs work with direct `curl` -- no authentication needed.

```bash
curl -sL -o "output.jpg" "https://scontent-xxx.xx.fbcdn.net/v/..."
curl -sL -o "output.mp4" "https://video-xxx.xx.fbcdn.net/v/..."
```

For batch downloads, use `scripts/extract-and-download.sh`:
```bash
bash scripts/extract-and-download.sh urls.json output-dir advertiser-slug
```

### 6. Extract Aspect Ratios

After downloading, determine aspect ratio:

**Images:**
```bash
sips -g pixelWidth -g pixelHeight image.jpg  # macOS
```

**Videos:**
```bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 video.mp4
```

**Common Meta ad aspect ratios:**

| Ratio | Dimensions | Use Case |
|-------|------------|----------|
| 1:1 | 1080x1080 | Feed (universal) |
| 4:5 | 1080x1350 | Feed (recommended) |
| 9:16 | 1080x1920 | Stories, Reels |
| 16:9 | 1920x1080 | Video, landscape |
| 1.91:1 | 1200x628 | Link ads |

Save metadata to JSON alongside assets. See `references/dom-selectors.md` for full metadata format.

### 7. Scroll for More Results

The Ad Library lazy-loads ~20 ads initially. Scroll down and wait, then re-extract. The JS deduplicates automatically.

### Naming Convention

```
{advertiser-slug}-{type}-{nn}.{ext}
```
Examples: `hbs-online-image-01.jpg`, `iman-gadzhi-video-03.mp4`

### Known Limitations

- Image resolution capped at 600x600 (server-enforced). Sufficient for analysis.
- Videos are full quality.
- Rate limiting: 1-2s delay between downloads for large batches.
- URL expiry: fbcdn.net URLs contain auth tokens that expire. Download promptly.

---

## Stage 2: Analyze

Generate a professional ad strategy analysis report from extracted assets.

### Prerequisites

- Extracted ad assets from Stage 1 (images, videos, landing page screenshots)
- Assets folder typically at:
```
~/clawd/output/meta-ads/{advertiser-slug}/
```

### Analysis Process

#### 1. Analyze Each Creative

For each ad, identify:
- **Aspect Ratio**: Dimensions and ratio (1:1, 4:5, 9:16, 16:9)
- **Duration**: For videos, length in seconds
- **Hook**: Opening line/visual that stops the scroll
- **Script/Copy**: Key messaging and value proposition
- **Visual Flow**: Sequence of scenes/elements (video)
- **Emotion**: Primary emotional trigger (curiosity, fear, aspiration, etc.)
- **CTA**: Call to action and friction level
- **Strengths**: What works well
- **Weaknesses/Gaps**: What could be improved

Use vision model for images, Gemini for video analysis.

#### 2. Analyze Landing Pages

For each landing page:
- **Headline**: Primary value proposition
- **Strategy**: Key conversion elements (social proof, urgency, etc.)
- **Conversion Flow**: Path from landing to purchase/signup
- **Strengths / Gaps**: What converts well and what's missing

#### 3. Map Funnels

Group ads by destination landing page. Each funnel = landing page + all ads driving to it.

Typical funnel types:
- **TOFU**: Awareness, lead magnets, quizzes, free content
- **BOFU**: Direct offer, application, purchase

#### 4. Identify Strategy Patterns

Look for:
- Credibility stacking (logos, credentials, social proof)
- Price anchoring
- Native creative (ads that don't look like ads)
- Identity-driven copy
- Testing patterns (variants of same creative)

### Output: HTML Report

Generate a self-contained HTML report using `templates/report-template.html`.

**Report structure:**
1. Header (advertiser, stats, date)
2. Strategy Overview (acquisition strategy, funnel flow, creative testing patterns, key takeaways)
3. Funnel Sections (one per landing page, with landing page card + ad cards grid)
4. Footer (source, date)

**Styling:** Clean, doc-like. White background, simple typography. Inline playable media. Mobile-friendly grid. Badges for quick scanning (TOFU/BOFU, Video/Image, Variant, aspect ratio).

### Delivery

1. Generate HTML file in the assets folder:
   ```
   ~/clawd/output/meta-ads/{advertiser-slug}/{slug}-analysis.html
   ```
2. Zip the entire folder (HTML + all media)
3. Send via Telegram with caption

The HTML uses relative paths to media files. Always deliver as a zip so it opens locally with all assets.

---

## Stage 3: Publish

Create and publish campaigns to Meta Ads Manager via the Marketing API. All ads are created as PAUSED for manual review.

### Prerequisites

- Meta Marketing API token (system user with ads_management permission)
- Ad Account ID, Facebook Page ID
- Payment method on ad account

**Credentials in private environment configuration:**
```
META_AD_ACCOUNT_ID=act_your_account_id
META_PAGE_ID=your_facebook_page_id
META_ACCESS_TOKEN=your_access_token
```

### Pre-Publish Holistic Review (MANDATORY)

Before creating ANY ads, review the full picture:

- Ad copy matches creative visuals
- Landing page URL is correct for each ad
- CTA matches the funnel stage (TOFU/MOFU/BOFU)
- Targeting makes sense for the offer
- Budget is appropriate for test/scale phase
- All ads in set are thematically consistent
- No typos or broken links
- DSA compliance fields filled (EU targeting)
- Image dimensions correct (1:1, 4:5, etc.)
- Video placeholders have complete copy

**Present summary to user and wait for confirmation before proceeding.**

### Create Campaign

```bash
curl -X POST "https://graph.facebook.com/v21.0/act_{AD_ACCOUNT}/campaigns" \
  -d "name=Campaign Name" \
  -d "objective=OUTCOME_TRAFFIC" \
  -d "status=PAUSED" \
  -d "special_ad_categories=[]" \
  -d "access_token=$TOKEN"
```

**Objectives:**
- `OUTCOME_AWARENESS`: Brand awareness
- `OUTCOME_TRAFFIC`: Website traffic
- `OUTCOME_ENGAGEMENT`: Post engagement
- `OUTCOME_LEADS`: Lead generation
- `OUTCOME_SALES`: Conversions

### Create Ad Set

```bash
curl -X POST "https://graph.facebook.com/v21.0/act_{AD_ACCOUNT}/adsets" \
  -d "name=Ad Set Name" \
  -d "campaign_id={CAMPAIGN_ID}" \
  -d "status=PAUSED" \
  -d "billing_event=IMPRESSIONS" \
  -d "optimization_goal=LINK_CLICKS" \
  -d "bid_strategy=LOWEST_COST_WITHOUT_CAP" \
  -d "daily_budget=2000" \
  -d 'targeting={"geo_locations":{"countries":["DE","AT","CH"]},"age_min":25,"age_max":55,"targeting_automation":{"advantage_audience":0}}' \
  -d "dsa_beneficiary=Company Name" \
  -d "dsa_payor=Company Name" \
  -d "access_token=$TOKEN"
```

**Required for EU targeting:** `dsa_beneficiary`, `dsa_payor`, `targeting_automation.advantage_audience` (0 = off, 1 = on).

### Upload Images

```bash
curl -X POST "https://graph.facebook.com/v21.0/act_{AD_ACCOUNT}/adimages" \
  -F "filename=@/path/to/image.png" \
  -F "access_token=$TOKEN"
```

Returns `image_hash` for use in ad creative.

### Create Ads

**Single Image Ad:**
```bash
curl -X POST "https://graph.facebook.com/v21.0/act_{AD_ACCOUNT}/ads" \
  -d "name=Ad Name" \
  -d "adset_id={ADSET_ID}" \
  -d "status=PAUSED" \
  -d 'creative={"object_story_spec":{"page_id":"{PAGE_ID}","link_data":{"image_hash":"{HASH}","link":"https://...","message":"Ad copy here","call_to_action":{"type":"LEARN_MORE"}}}}' \
  -d "access_token=$TOKEN"
```

**Carousel Ad:**
```bash
curl -X POST "https://graph.facebook.com/v21.0/act_{AD_ACCOUNT}/ads" \
  -d "name=Carousel Ad" \
  -d "adset_id={ADSET_ID}" \
  -d "status=PAUSED" \
  -d 'creative={"object_story_spec":{"page_id":"{PAGE_ID}","link_data":{"message":"Main copy","link":"https://...","child_attachments":[{"link":"...","image_hash":"...","name":"Slide title","description":"Slide desc"}],"multi_share_optimized":true}}}' \
  -d "access_token=$TOKEN"
```

**Video Ad (placeholder -- copy only, no video):**
```bash
curl -X POST "https://graph.facebook.com/v21.0/act_{AD_ACCOUNT}/ads" \
  -d "name=VIDEO PLACEHOLDER - Name" \
  -d "adset_id={ADSET_ID}" \
  -d "status=PAUSED" \
  -d 'creative={"object_story_spec":{"page_id":"{PAGE_ID}","link_data":{"link":"https://...","message":"Video script as ad copy","name":"Headline","description":"Subhead","call_to_action":{"type":"LEARN_MORE"}}}}' \
  -d "access_token=$TOKEN"
```

### CTA Types

| Type | Use Case |
|------|----------|
| LEARN_MORE | General info, tutorials |
| SIGN_UP | Email capture, courses |
| DOWNLOAD | Lead magnets, PDFs |
| GET_OFFER | Promotions, discounts |
| BOOK_NOW | Consultations, calls |
| CONTACT_US | B2B inquiries |
| SHOP_NOW | E-commerce |
| WATCH_MORE | Video content |

### Post-Publish Confirmation

After creating all ads, provide summary with campaign/ad set/ad IDs, statuses, and Ads Manager link:
```
https://www.facebook.com/adsmanager/manage/ads?act={AD_ACCOUNT}
```

**Next steps for user:** Review in Ads Manager, upload videos for placeholders, set to ACTIVE when ready.

### Common Errors

| Error | Solution |
|-------|----------|
| No Payment Method | Add credit card to ad account |
| App in Development Mode | Switch app to Live mode |
| DSA fields required | Add dsa_beneficiary and dsa_payor |
| Advantage Audience required | Add targeting_automation.advantage_audience |
| Invalid image dimensions | Use 1:1, 4:5, or 9:16 aspect ratios |

---

## Safety Rules

1. **Always create as PAUSED**: Never auto-activate ads
2. **Always do holistic review**: Check copy / creative match before publishing
3. **Always confirm with user**: Before creating, after creating
4. **Always provide Ads Manager link**: For manual review
5. **Never modify active ads**: Only paused/draft

---

## Example Workflow

```
User: Analyze EricPartaker's Meta ads and create a similar campaign for us

1. EXTRACT: Get Page ID, open Ad Library, extract media URLs, download assets
2. ANALYZE: Analyze each creative + landing pages, map funnels, generate HTML report
3. GENERATE: Use ads-creative skill to create new copy inspired by analysis
4. PUBLISH: Create campaign, ad set, and ads as PAUSED
5. DELIVER: Send analysis report + Ads Manager link to user
```

---

## Integration Pipeline

```
ads-meta (extract) --> ads-creative (analyze + generate copy) --> ads-meta (publish)
                   --> design-analysis (landing page audits)
```

---

## Related Skills

- **ads-creative**: For cross-platform ad copy generation, competitor creative analysis, hooks, and iteration
- **ads-strategy**: For campaign strategy, targeting, budgets, and optimization
- **design-analysis**: For deeper landing page audits

---

## References

- `references/dom-selectors.md`: CSS selectors, URL patterns, JS extraction code, Page ID extraction, CDN patterns, scroll/pagination
- `templates/report-template.html`: Full HTML/CSS template for strategy analysis reports
- `scripts/extract-and-download.sh`: Batch download script for extracted asset URLs
