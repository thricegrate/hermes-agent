# Before/After AI Ad Workflow

The highest-converting ad format for iOS apps right now is dead simple: before / after. Show someone BEFORE using the app. Show the result AFTER. That is the entire ad.

This file covers the 4-step workflow that produces 10-12 ad variants in roughly an hour using AI tools, with no UGC creators, no contracts, no back-and-forth.

## Why before/after wins for iOS apps

The before/after format works specifically because:

- The "reveal" IS the ad. The viewer sees the transformation in 2 seconds.
- It triggers the core human desire (insecurity → relief) without explaining the app
- It works on mute (most TikTok scrolling is silent)
- It produces a comment-bait moment naturally (people argue about the result)
- It can be produced at scale by one person with no cast or crew

For face rating apps, show someone getting their score. For fitness apps, show the body scan. For food apps, show the calorie breakdown. The reveal IS the ad.

The viewer does not care about the app. They care about the RESULT.

## What NOT to do in the ad

The single biggest mistake founders make is "showing off the app." Showing the UI, the features, the screens. Nobody cares.

Show the result. Show the transformation. Show the reveal.

The app appears as the silent agent that produces the result. The result is the hero.

## The 4-step workflow

### Step 1: Record yourself doing the "action"

Pick up your phone. Record yourself doing whatever the user does in the app:

- For a face rating app: record yourself taking a selfie
- For a body scanner: record yourself standing in front of the camera
- For a food app: record yourself pointing the camera at a plate
- For a height predictor: record yourself entering numbers

The recording does not need to be high quality. Phone camera, natural light, real environment. 5-10 seconds is enough.

This is the "action" footage. You will paste AI-generated faces over it in step 3.

### Step 2: Generate "before" and "after" face/body images with Z-Image

Use Z-Image Turbo (LoRA) on fal.ai to generate the before and after images. URL: https://fal.ai/models/fal-ai/z-image/base/lora/requests

For each ad variant, generate one "before" image and one "after" image. The two images are the same person, with the difference being whatever your app promises:

- Face rating: "before" is an average-looking face, "after" is a more attractive version of the same face
- Fitness: "before" is overweight, "after" is fit
- Skincare: "before" is bad skin, "after" is clear skin
- Glow up: "before" is dull, "after" is glowing

The two images need to look like the same PERSON, just at different states. This is what Z-Image Turbo (LoRA) handles well: same identity, different conditions.

For prompts, see [../templates/ad-batch-prompt.md](../templates/ad-batch-prompt.md).

### Step 3: Use SwapTok to merge the AI face onto your video

SwapTok takes the AI-generated face image and pastes it onto the action footage from step 1. The result is two videos:

- Video 1: your action footage with the "before" AI face
- Video 2: your action footage with the "after" AI face

(Note: SwapTok is the founder's own tool, purpose-built for this exact workflow. Any face-swap tool that produces clean output works. Heygen, Runway, and others have similar capabilities.)

The two videos should look identical EXCEPT for the face. Same lighting, same framing, same motion. The difference is the AI face transformation.

### Step 4: Edit in CapCut or TikTok Studio

Open CapCut or TikTok Studio (free). Build the ad:

1. Drop in Video 1 (before AI face)
2. Add a cut to Video 2 (after AI face)
3. Add screenshots of the app's reveal screen between the two
4. Add trending music (TikTok Studio has built-in trending audio)
5. Add text overlays for the hook (first 2 seconds) and the comment-bait (anywhere in the ad)
6. Export at 9:16 portrait

The edit should be roughly:
- 0-2 seconds: hook (text overlay or first line of action)
- 2-5 seconds: before footage
- 5-7 seconds: app reveal screenshot
- 7-9 seconds: after footage
- 9-11 seconds: result + soft CTA

Total runtime: 9-15 seconds for the standard format.

## Producing 10-12 variants per hour

The reason this workflow scales is that steps 2-3 happen in parallel.

Once you have one batch of action footage from step 1, you can generate 10-12 different AI faces in step 2 (one batch run on Z-Image with different personas), run all of them through SwapTok in step 3, and edit them all in step 4.

Each variant differs in:
- The AI persona (different age, ethnicity, gender)
- The hook text overlay
- The trending audio

The action footage and the app reveal screenshots stay the same.

This is what produces 10-12 variants in roughly an hour. The workflow is mechanical once set up.

## Ad creative rules

The format is simple. Execution still matters. Apply these rules across every variant.

### Keep ads rough and native-looking

The ad must look like a TikTok, not a polished commercial. The moment a viewer thinks "this is an ad," they have lost interest.

What rough and native looks like:
- Phone camera framing (not DSLR)
- Natural lighting (not studio)
- Slight handheld movement (not stabilized)
- Casual settings (bedroom, kitchen, bathroom, sidewalk)
- Trending audio (not licensed music)
- Text overlays in TikTok's default fonts (not custom branding)

Polished ads look like ads. Rough ads look like content. Content gets watched.

### Hook in the first 2 seconds

The hook must trigger the desire or insecurity in the first 2 seconds. After 2 seconds, the viewer has either kept watching or scrolled.

Hook formats that work:
- "What is your face score out of 10?"
- "I tried the app everyone is talking about"
- "POV: you finally figured out why nothing was working"
- "If you are over 30 and your face looks tired..."

For deeper hook engineering, see `skills/video-scriptwriter/references/hook-engineering.md` (the 5-lever framework + scoring system).

### Show the viral feature

The "reveal" moment from the app must appear in the ad. The viewer needs to see what the app produces. If the ad shows only the before/after and never shows the app's reveal screen, conversion drops.

Recommended placement: after the "before" beat, before the "after" beat. The viewer sees the app working its magic.

### Trigger the insecurity

Every ad targets a specific insecurity:
- Face rating: "Am I attractive?"
- Fitness: "Am I in shape?"
- Skincare: "Is my skin getting worse?"
- Glow up: "Have I let myself go?"

The hook and the imagery should reinforce the insecurity. The viewer feels seen. The viewer wants to know their result. The viewer downloads.

### Comment bait everything

TikTok's algorithm pushes videos with high engagement. Comments rank higher than likes for distribution.

Hide something in the ad that makes people comment. The classic example: a frame in the ad that includes "men kissing" or some other reaction-bait content. The audience comments to argue, complain, or ask about it. Comments = engagement = cheaper reach. The algorithm cannot tell the difference between positive and negative comments.

Other comment-bait patterns:
- A controversial face score that people argue about
- A "wrong" answer in the app that people correct
- A subtle visual error people point out
- An ambiguous prediction people debate

Comments are the multiplier on every other ad metric. Build them into the ad on purpose.

### Delete negative comments that hurt ROI

Some negative comments help (engagement). Some hurt (purchase signal). Delete:

- "It costs money": kills purchase intent for other viewers
- "It is just AI generated": kills credibility
- "It is a scam": kills trust

Keep:
- Arguments about the result
- People debating the comments
- Reactions to the comment-bait
- Anything that drives more comments

A 10-minute daily comment review keeps the comment section in the right shape.

## What gets a winning ad killed

Two things kill an otherwise-winning ad before it scales:

### 1. Music that gets removed

Trending audio occasionally gets pulled by TikTok for licensing reasons. When the audio disappears, the ad loses 80% of its momentum.

Track which audio is being used. If a winning ad's audio gets pulled, swap the audio to another trending track immediately. Do not just let the ad run silently.

### 2. The TikTok pixel breaking

If the campaign is scaled too fast (>+30% per 3 days) or the campaign settings change mid-flight, the TikTok pixel can lose optimization.

When this happens, CPA spikes and the ad stops converting. The fix is usually waiting 24-48 hours for the pixel to recalibrate.

Avoid the issue by following the scaling rules in [tiktok-smartplus-campaigns.md](tiktok-smartplus-campaigns.md).

## Ad formats beyond before/after

Before/after is the default. When you need variation:

- **POV ("you")**: "POV: you finally figured out you have not been hot since 2019"
- **Reveal-only**: just the app's reveal moment with a hook ("Look what this app gave me")
- **Reaction**: a person reacting to their result on camera
- **Side-by-side compare**: two friends getting their results compared

All four still target the same emotional core. They just trade the before/after structure for a different reveal mechanic.

For deeper ad creative theory and the full direct-response system, see `skills/video-scriptwriter/references/direct-response-voice-system.md` and adjacent files.

## Cross-references

- Variant generation prompt: [../templates/ad-batch-prompt.md](../templates/ad-batch-prompt.md)
- TikTok campaign management for these ads: [tiktok-smartplus-campaigns.md](tiktok-smartplus-campaigns.md)
- Component-level variation at scale (1 winner becomes 1000+ variants): `skills/ugc-production/templates/variation-from-winner-reel.md`
- Hook engineering: `skills/video-scriptwriter/references/hook-engineering.md`
- Direct-response voice rules: `skills/video-scriptwriter/references/direct-response-voice-system.md`
- Anti-AI ad tells (especially relevant to keep ads native-looking): `skills/video-scriptwriter/references/anti-ai-script-tells.md`
- Broader ads creative skill: `skills/ads-creative/SKILL.md`
