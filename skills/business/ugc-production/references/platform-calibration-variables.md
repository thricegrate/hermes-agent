# Platform Calibration Variables

Once the 3-input brief is loaded into Claude (see [cross-platform-brief-structure.md](cross-platform-brief-structure.md)), the platform-specific calibration variables produce different output for different platforms from the same underlying brief.

The 4 calibration variables:

1. Duration
2. CTA architecture
3. Caption length and style
4. Audio approach

Each variable has different optimal settings on each of the 4 target platforms (TikTok, Instagram Reels, YouTube Shorts, Facebook Reels).

## Why calibration matters

Format-specific calibration baked into the upstream prompt produces native-looking content for each platform. Calibration applied as afterthought edits produces content that feels imported from another platform, which underperforms.

The 4 variables together determine how a single content concept gets rendered for each platform. Same brief, same strategic angle, different platform-native execution.

## Variable 1: Duration

Each platform has different optimal content durations.

| Platform | Cold discovery | Warmer audience |
|---|---|---|
| TikTok video | 15-30 seconds | 30-60 seconds |
| Instagram Reels | 15-30 seconds | 30-45 seconds |
| YouTube Shorts | 30-45 seconds | 45-60 seconds (or longer via standard YouTube uploads) |
| Facebook Reels | 25-45 seconds | 45-60 seconds |

### Why durations differ

- **TikTok and Instagram Reels** sit in similar 15-30 second sweet spots because both platforms have similar fast-scroll dynamics
- **YouTube Shorts** runs longer comfortably because the platform's audience is more education-tolerant and the algorithm rewards completion of longer content
- **Facebook Reels** tolerates slightly longer content because the older audience demographic engages with longer durations more comfortably

### How to specify

In the master prompt, state the target duration as a range. Claude will calibrate the script length to fit cleanly within the range without padding or compression.

Example: "Duration 15 to 25 seconds." Claude produces a script that, at conversational pace (2.5-3 words per second), runs 38-75 words. That fits the range with breathing room.

## Variable 2: CTA Architecture

Each platform rewards different CTA structures because each platform's algorithm weights different engagement signals.

| Platform | Primary CTA architecture | Why |
|---|---|---|
| TikTok | Specific-person share prompts ("send this to the friend who...") | DM shares are the highest-weighted distribution signal on TikTok |
| Instagram Reels | Save-driving CTAs + comment funnel triggers | Instagram weights saves and substantive comments heavily |
| YouTube Shorts | Subscribe-driving CTAs (integrated, not aggressive) | Subscribe rate is YouTube's primary distribution signal |
| Facebook Reels | Substantive comment prompts (genuine response, not emoji) | Facebook's algorithm rewards real comment engagement |

### TikTok CTA examples

> "Send this to the friend who has tried every diet and given up."
> "Tag the person you keep telling about this exact problem."
> "Send this to whoever in your life still thinks they need 8 glasses of water."

The specific-person framing is critical. "Share this with friends" is generic and produces fewer DM shares than "send this to the friend who [specific behavior]."

### Instagram Reels CTA examples

Save-driving:
> "Save this for the next time you start over on Monday."
> "Save this for tomorrow morning before you walk into the kitchen."

Comment funnel:
> "Comment SKIN and I will send you the exact routine."
> "Drop a comment with your skin type and I will tell you which step to skip."

The Instagram CTA can stack both: "Save this for tomorrow morning AND comment ROUTINE for the full setup."

### YouTube Shorts CTA examples

> "Subscribe for the full series on this exact problem."
> "Hit subscribe if you want me to break down the science behind this."
> "If this clicked, subscribe so the algorithm keeps showing you this."

The subscribe prompt should feel natural rather than aggressive. Integrated into the closing rather than as a hard sales close.

### Facebook Reels CTA examples

> "What is the one thing you have tried that did not work? Drop it in the comments."
> "If you have been managing this for a while, share what worked when nothing else did."
> "Tell me your story in the comments. I read every one."

Facebook CTAs invite substantive comment responses rather than emoji reactions or keyword drops. The older audience engages more deeply with substantive prompts.

### How to specify in the prompt

State the CTA architecture explicitly:

```
CTA architecture: [TikTok / Instagram / YouTube / Facebook]
- TikTok: specific-person share prompt naming a specific archetype
- Instagram: save-driving prompt + comment funnel keyword (stacked)
- YouTube: integrated subscribe prompt at the close
- Facebook: substantive comment prompt asking for genuine response
```

Claude calibrates the CTA to match.

## Variable 3: Caption Length and Style

Caption requirements differ meaningfully across platforms.

| Platform | Caption length | Caption style |
|---|---|---|
| TikTok | Short, punchy (under 100 characters) | High contrast text overlays, bolder positioning, aggressive visual messaging |
| Instagram Reels | Short to medium (100-200 characters) | Instagram Stories text aesthetic: bold text on semi-transparent dark background, bottom third positioning |
| YouTube Shorts | Captions matter less; description handles SEO | Title (60 chars) + description first 150 chars + longer body |
| Facebook Reels | 3-5x longer than IG/TikTok (300-600 characters) | More specific detail, more context, direct invitation to engage |

### Why caption styles differ

- **TikTok** native aesthetic is aggressive visual messaging. The ad must look like a TikTok, not an Instagram post.
- **Instagram** has a more restrained Stories aesthetic. The text overlay style is calmer and more readable.
- **YouTube** has different metadata structure (title + description matter more than captions in the video itself).
- **Facebook** audience is older, reads more text, engages more deeply with longer copy. The longer caption format fits the platform's content patterns.

### How to specify

For TikTok and Instagram, specify the caption text + the text overlay styling notes. For YouTube, specify the title (≤60 chars), the description first 150 chars (above the fold), and the longer description body. For Facebook, specify the longer caption text with substantive detail.

## Variable 4: Audio Approach

Audio integration differs between platforms.

| Platform | Audio approach |
|---|---|
| TikTok | Trending audio matching applied at production. Claude script may need to leave space for trending audio overlay |
| Instagram Reels | Audio fit weighted less heavily; cleaner standalone voiceover acceptable |
| YouTube Shorts | Audio fit weighted less heavily; voiceover-driven content works well |
| Facebook Reels | Calmer, more measured vocal performance over high-energy delivery; trending audio less critical |

### What "leave space for trending audio" means

For TikTok specifically, the script can be structured as voiceover that pairs with trending audio underneath, OR as voiceover-only. The choice depends on the script angle:

- **Voiceover + trending audio**: the voiceover plays during the verbal beats; trending audio sits underneath and rises during silence beats. Best for scripts where the trending audio adds emotional context.
- **Voiceover-only (no trending audio)**: the voiceover carries the entire audio. Best for scripts that need precise emotional pacing without the trending audio's mood baked in.

For TikTok, specify which approach the Claude script targets. For the other 3 platforms, voiceover-only is the default.

### How to specify

```
Audio approach: [TikTok / IG / YT / FB]
- TikTok: voiceover [+ trending audio overlay / -only]
- Instagram: voiceover-only, calmer pacing
- YouTube: voiceover-only, slightly more measured
- Facebook: voiceover-only, calm and conversational tone matching older audience
```

## Optional Variable 5: Avatar Demographic Match

For all 4 platforms, the AI avatar (Seedance generation) demographic should match the audience insight statement. But the platform's audience demographics shift the default:

- **TikTok**: skews younger; avatars in late 20s to mid-30s common
- **Instagram Reels**: similar to TikTok; late 20s to early 40s
- **YouTube Shorts**: broader demographic; 20s through 50s all common
- **Facebook Reels**: skews older; avatars in their 40s or 50s match better than younger avatars

### Why this matters

A 25-year-old AI avatar on a Facebook Reels ad targeting 50+ users reads as a mismatch. The viewer disconnects.

A 50-year-old AI avatar on a TikTok ad targeting 25-year-olds also reads as a mismatch.

Match the avatar demographic to BOTH the audience insight statement AND the platform's audience skew.

### How to specify in the Seedance prompt

Include explicit age and demographic notes in the Seedance generation prompt:

> "[Character: woman in her late 40s, brown hair with grey at the temples, casual home environment, mid-career professional aesthetic]"

For TikTok variants targeting younger audience: "[Character: woman in her late 20s, casual lifestyle aesthetic]" instead.

## Putting it together: the calibration matrix

For each script generated, specify the 4 (or 5) variables in the prompt. Example for an Instagram Reels script:

```
Platform: Instagram Reels
Duration: 18-30 seconds
CTA architecture: save-driving + comment funnel keyword (stacked)
Caption length and style: medium (150 characters), Stories aesthetic, bottom-third positioning
Audio approach: voiceover-only, calmer pacing than TikTok
Avatar demographic: matches audience insight statement (early 30s woman, casual home environment)
```

Claude takes the brief plus this calibration matrix and produces an Instagram-native script.

For the master prompts that consume these variables, see [../templates/master-prompts-by-platform.md](../templates/master-prompts-by-platform.md).

## What stays constant across platforms

Even though calibration variables differ, these stay the same across all 4 platforms when generating from the same brief:

- The audience insight statement (loaded once)
- The product brief (loaded once)
- The structural reference (loaded once)
- The strategic angle of the specific concept (the underlying claim, mechanism, and emotional pull)
- The voice rules (no em-dashes, no banned phrases, customer-language priority)

The calibration variables flex around these constants. Different output, same strategic core.

## Cross-references

- Brief structure (the 3 inputs): [cross-platform-brief-structure.md](cross-platform-brief-structure.md)
- Master prompts that use these variables: [../templates/master-prompts-by-platform.md](../templates/master-prompts-by-platform.md)
- Cross-platform intelligence (weekly synthesis across platforms): [cross-platform-intelligence.md](cross-platform-intelligence.md)
- Seedance consistency (avatar generation patterns): [seedance-consistency.md](seedance-consistency.md)
- TikTok-specific trending audio workflow: see `skills/tiktok-slideshow/references/trending-audio-workflow.md` (covers slideshows but the audio matching logic transfers to TikTok video)
