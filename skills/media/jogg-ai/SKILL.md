---
name: jogg-ai
description: |
  Create AI avatar videos, product marketing videos, and custom photo avatars via Jogg AI API.
  Browse avatars, voices, visual styles, and music. Supports async workflows with polling.
  Use when user wants to create talking head videos, product demos, UGC-style ads, or
  custom AI avatars. Triggers: "jogg", "avatar video", "talking head video", "product video",
  "ai video", "ugc video", "create avatar", "video ad with avatar".
metadata:
  version: 1.0.0
  tags: video, avatar, ai-video, product-video, ugc, marketing, jogg
---

# Jogg AI Video Creator

Create AI avatar videos, product marketing videos, and custom photo avatars via Jogg AI API v2.

## Prerequisites

- Python 3.10+
- `requests` and `python-dotenv` packages
- `JOGG_AI_API_KEY` set in `.env`

## Scripts

Run all scripts with: `python skills/jogg-ai/scripts/<script>.py [options]`

---

### Browsing Resources (run first to find IDs)

#### list_avatars.py -- Browse 300+ public avatars
```bash
python skills/jogg-ai/scripts/list_avatars.py --page-size 10
python skills/jogg-ai/scripts/list_avatars.py --gender female --style professional --age adult
python skills/jogg-ai/scripts/list_avatars.py --aspect-ratio portrait --scene business
python skills/jogg-ai/scripts/list_avatars.py --ethnicity east_asian --page 2
```
Filters: `--aspect-ratio`, `--style` (professional/social), `--gender`, `--age` (adult/senior/young_adult), `--scene` (lifestyle/outdoors/business/studio/health_fitness/education/news), `--ethnicity`

#### list_voices.py -- Browse voices (40+ languages)
```bash
python skills/jogg-ai/scripts/list_voices.py --language english --gender female
python skills/jogg-ai/scripts/list_voices.py --age young --page-size 30
python skills/jogg-ai/scripts/list_voices.py --use-case narrative_story
```
Filters: `--gender`, `--language`, `--age` (young/middle_aged/old), `--use-case`

#### list_styles.py -- Browse 50+ visual style templates
```bash
python skills/jogg-ai/scripts/list_styles.py
```
Visual styles are used in product videos to control the video's look and layout.

#### list_music.py -- Browse background music
```bash
python skills/jogg-ai/scripts/list_music.py --page-size 30
```

---

### Creating Videos

#### create_avatar_video.py -- Create talking avatar video
The primary video creation tool. Give an avatar a script and it generates a video.

```bash
# Basic: avatar speaks your script
python skills/jogg-ai/scripts/create_avatar_video.py \
  --avatar-id 123 --voice-id "en-US-ChristopherNeural" \
  --script "Welcome to our channel! Today we'll cover the top AI tools." \
  --aspect-ratio portrait --poll

# From script file
python skills/jogg-ai/scripts/create_avatar_video.py \
  --avatar-id 123 --voice-id "en-US-JennyNeural" \
  --script-file .tmp/my_script.txt --caption --poll --download

# With custom audio (no voice-id needed)
python skills/jogg-ai/scripts/create_avatar_video.py \
  --avatar-id 123 --audio-url "https://example.com/narration.mp3" \
  --screen-style 2 --poll

# Custom photo avatar (avatar-type 1)
python skills/jogg-ai/scripts/create_avatar_video.py \
  --avatar-id 456 --avatar-type 1 --voice-id "en-US-GuyNeural" \
  --script "Custom avatar speaking!" --poll --download
```

Key args:
- `--avatar-id` + `--avatar-type` (0=public, 1=custom)
- `--script` / `--script-file` / `--audio-url` (mutually exclusive)
- `--voice-id` (required with script, not with audio-url)
- `--screen-style` (1=full, 2=split, 3=picture-in-picture)
- `--caption` enables subtitles
- `--poll` waits for completion, `--download` saves the file

#### create_product.py -- Create product entry
First step for product marketing videos. Jogg AI crawls the URL to extract info.

```bash
# From product URL (Jogg crawls the page)
python skills/jogg-ai/scripts/create_product.py \
  --url "https://example.com/product-page"

# Manual entry
python skills/jogg-ai/scripts/create_product.py \
  --name "AI Newsletter Playbook" \
  --description "Step-by-step guide to building a profitable AI newsletter" \
  --target-audience "Content creators and newsletter operators"

# With media
python skills/jogg-ai/scripts/create_product.py \
  --name "My Product" --description "Description here" \
  --media "https://example.com/img1.jpg" "https://example.com/img2.jpg"
```

#### create_product_video.py -- Create product marketing video
Uses a product entry to generate a full marketing video with AI script, avatar, and visuals.

```bash
# Basic product video
python skills/jogg-ai/scripts/create_product_video.py \
  --product-id "prod_abc123" --length 30 --poll

# Full customization
python skills/jogg-ai/scripts/create_product_video.py \
  --product-id "prod_abc123" \
  --aspect-ratio portrait --length 60 \
  --script-style "Discovery" --avatar-id 123 \
  --voice-id "en-US-JennyNeural" \
  --caption --poll --download

# With custom script (overrides AI generation)
python skills/jogg-ai/scripts/create_product_video.py \
  --product-id "prod_abc123" --length 30 \
  --override-script "Have you seen this? It changed everything for me..." \
  --poll
```

---

### Custom Avatars

#### generate_photo_avatar.py -- Generate custom photo avatar
Two-stage pipeline: generate photo, then optionally add motion.

```bash
# Generate photo only
python skills/jogg-ai/scripts/generate_photo_avatar.py \
  --gender Female --age "Young adult" --avatar-style Professional \
  --ethnicity "East Asian" --poll

# Full pipeline: photo + motion
python skills/jogg-ai/scripts/generate_photo_avatar.py \
  --gender Male --age Adult --avatar-style Professional \
  --appearance "Clean shaven, dark hair, wearing a navy suit" \
  --background "Modern office with city view" \
  --add-motion --name "Alex" --voice-id "en-US-GuyNeural" --poll

# From reference photo
python skills/jogg-ai/scripts/generate_photo_avatar.py \
  --image-url "https://example.com/portrait.jpg" \
  --gender Male --age Adult --avatar-style Social \
  --add-motion --name "Custom Avatar" --voice-id "en-US-ChristopherNeural" --poll
```

Credits: Photo = 0.2 credits (4 images). Motion 2.0 = 2 credits.

---

### Utilities

#### check_status.py -- Universal status checker
Check any async job or poll until done. Works with all job types.

```bash
# One-shot check
python skills/jogg-ai/scripts/check_status.py --type avatar-video --id "video_123"
python skills/jogg-ai/scripts/check_status.py --type product-video --id "pvid_456"
python skills/jogg-ai/scripts/check_status.py --type photo-avatar --id "photo_789"
python skills/jogg-ai/scripts/check_status.py --type motion --id "motion_abc"

# Poll + download
python skills/jogg-ai/scripts/check_status.py --type avatar-video --id "video_123" \
  --poll --download --output ".tmp/my_video.mp4"
```

Types: `avatar-video`, `product-video`, `photo-avatar`, `motion`

#### upload_asset.py -- Upload media files
Upload images, videos, or audio for use in other scripts.

```bash
python skills/jogg-ai/scripts/upload_asset.py --file photo.jpg
python skills/jogg-ai/scripts/upload_asset.py --file narration.mp3
python skills/jogg-ai/scripts/upload_asset.py --file product.mp4 --content-type video/mp4
```

Returns an `asset_url` for use as `--image-url` or `--audio-url` in other scripts.

---

## Async Workflow Pattern

All video and avatar creation is async:

1. **Create** -- POST returns a job ID immediately
2. **Poll** -- GET the status endpoint until `completed` or `failed`
3. **Download** -- Use the `video_url` from the completed response

Every creation script supports `--poll` to handle steps 2-3 automatically.
Without `--poll`, scripts print the job ID for manual checking via `check_status.py`.

### Processing Times
| Job Type | Time |
|----------|------|
| Photo avatar | 2-5 min |
| Motion | 2-3 min |
| Avatar video | 2-5 min |
| Product video | 5-10 min |

---

## Common Workflows

### 1. Quick Avatar Video (simplest)
```bash
# Find avatar and voice
python skills/jogg-ai/scripts/list_avatars.py --gender female --style professional --page-size 5
python skills/jogg-ai/scripts/list_voices.py --gender female --language english --page-size 5

# Create video
python skills/jogg-ai/scripts/create_avatar_video.py \
  --avatar-id <ID> --voice-id <VOICE_ID> \
  --script "Your script here" --aspect-ratio portrait --poll --download
```

### 2. Product Marketing Video
```bash
# Create product from URL
python skills/jogg-ai/scripts/create_product.py --url "https://example.com/product"

# Generate video
python skills/jogg-ai/scripts/create_product_video.py \
  --product-id <PRODUCT_ID> --length 30 --script-style "Discovery" --poll --download
```

### 3. Custom Avatar Pipeline
```bash
# Upload photo (optional)
python skills/jogg-ai/scripts/upload_asset.py --file portrait.jpg

# Generate avatar with motion
python skills/jogg-ai/scripts/generate_photo_avatar.py \
  --image-url <ASSET_URL> --gender Male --age Adult \
  --add-motion --name "Brand Avatar" --voice-id <VOICE_ID> --poll

# Use in videos
python skills/jogg-ai/scripts/create_avatar_video.py \
  --avatar-id <AVATAR_ID> --avatar-type 1 \
  --voice-id <VOICE_ID> --script "Hello from your custom avatar!" --poll --download
```

### 4. Batch Product Ads
```bash
# Create product once
python skills/jogg-ai/scripts/create_product.py --url "https://example.com/product"

# Generate multiple variations
for style in "Storytime" "Discovery" "Data"; do
  python skills/jogg-ai/scripts/create_product_video.py \
    --product-id <ID> --script-style "$style" --length 30 --poll
done
```

---

## Script Styles (for product videos)

| Style | Best For | Tone |
|-------|----------|------|
| Storytime | Narrative product stories | Engaging, story-driven |
| Discovery | "I just found this" UGC | Exciting, exploratory |
| Don't Worry | Problem-solution format | Reassuring, helpful |
| Data | Stats-driven products | Factual, informative |
| Top 3 reasons | Feature-rich products | Clear, structured |
| Light marketing | General promotion | Friendly, soft sell |

## Aspect Ratios

| Ratio | Use Case |
|-------|----------|
| portrait (9:16) | TikTok, Reels, Shorts |
| landscape (16:9) | YouTube, website embeds |
| square (1:1) | Instagram feed, LinkedIn |

## Integration Points

- **video-scriptwriter** -- Write video scripts, then use with `create_avatar_video.py`
- **elevenlabs** -- Generate custom audio, use `--audio-url` in avatar videos
- **ads-meta** -- Create video ads, then publish to Meta
- **ads-designer** -- Pair static ads with Jogg AI video variants
