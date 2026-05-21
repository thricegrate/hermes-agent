# Ad Batch Prompt Template

The Z-Image Turbo (LoRA) prompts for generating 10-12 before/after AI face/body images for an ad batch. Plus the variant matrix that produces variation across the 10-12 ads.

For the full ad creation workflow, see [../references/before-after-ad-workflow.md](../references/before-after-ad-workflow.md).

## When to use this template

You have:
- An app concept locked
- The "before" and "after" states defined for your viral feature
- Z-Image Turbo (LoRA) access at fal.ai
- A face-swap tool (SwapTok or equivalent)

You need 10-12 ad variants in roughly an hour. This template produces them.

## The variant matrix

Variation should happen across these axes. The action footage and the app reveal screenshot stay the same. Only these axes change.

| Axis | Variation count | What changes |
|---|---|---|
| Persona age | 2-3 | E.g., late 20s, mid-30s, mid-40s |
| Persona gender | 2 | Male, female |
| Persona aesthetic | 2 | E.g., professional, casual / lifestyle |
| Hook angle | 3 | Status, fear, curiosity (or whichever 3 fit your niche) |

A 4-axis × 2-3 options matrix produces 24-36 theoretical combinations. Pick the 10-12 that fit your specific audience best.

## Z-Image Turbo prompt structure

The prompt structure that works for face/body before/after generation:

### Base prompt template

```
[STATE] portrait of a [AGE] year old [GENDER] with [DESCRIPTORS], [SETTING],
[LIGHTING], [WARDROBE], [FRAMING], realistic skin texture with visible pores
and natural variation, organic phone-photo quality not studio quality, slight
candid feel, [9:16 portrait aspect ratio]
```

Where:

- `[STATE]` is "Before" or "After" (the transformation state)
- `[AGE]` is the persona age (e.g., 32, 41, 47)
- `[GENDER]` is the persona gender
- `[DESCRIPTORS]` are 2-3 specific physical features (hair color, build, ethnicity if relevant)
- `[SETTING]` is the environment (e.g., kitchen, bathroom, home office, sidewalk)
- `[LIGHTING]` is a dedicated clause (e.g., "soft warm window light from left, late morning quality")
- `[WARDROBE]` is what they are wearing (e.g., "casual gray t-shirt", "white button-up rolled up at sleeves")
- `[FRAMING]` is the camera angle (e.g., "front-facing selfie", "three-quarter angle")

### Before vs After difference

The key trick: the same person in BOTH states. The prompt structure stays identical EXCEPT for one phrase that differentiates the states.

Examples:

**Face rating app (before / after attractive)**

Before:
```
Casual portrait of a 38 year old man with brown hair and average build,
in a kitchen, soft warm morning light from window at left, gray t-shirt,
front-facing phone selfie, slightly tired expression, dark circles under eyes,
slightly unkempt hair, realistic skin texture with visible pores and natural
variation, organic phone-photo quality not studio quality, candid feel,
9:16 portrait aspect ratio
```

After:
```
Casual portrait of the same 38 year old man with brown hair and average build,
in a kitchen, soft warm morning light from window at left, gray t-shirt,
front-facing phone selfie, fresh and rested expression, clear skin, neat hair,
realistic skin texture with visible pores and natural variation, organic
phone-photo quality not studio quality, candid feel, 9:16 portrait aspect ratio
```

The differences are bolded (figuratively): expression, eye area, hair. Same person otherwise. Same setting, lighting, wardrobe, framing.

**Fitness app (before / after fit)**

Before:
```
Casual full-body shot of a 41 year old man with brown hair, slightly overweight
build, in a bathroom, soft warm morning light from window at left, athletic
shorts and gray t-shirt, mirror selfie, slightly slumped posture, realistic
skin texture, organic phone-photo quality not studio quality, candid feel,
9:16 portrait aspect ratio
```

After:
```
Casual full-body shot of the same 41 year old man with brown hair, athletic
build with visible muscle tone, in a bathroom, soft warm morning light from
window at left, athletic shorts and gray t-shirt, mirror selfie, confident
upright posture, realistic skin texture, organic phone-photo quality not
studio quality, candid feel, 9:16 portrait aspect ratio
```

Same person, same setting. Build and posture change.

**AI literacy app (before / after confident with AI)**

Before:
```
Casual portrait of a 44 year old woman with shoulder-length brown hair,
mid-career professional, in a home office at a desk, soft cool morning light
from window, casual button-up shirt, looking at a laptop with confused
expression, slight frown, hand on chin, realistic skin texture with visible
pores and natural variation, organic phone-photo quality not studio quality,
candid feel, 9:16 portrait aspect ratio
```

After:
```
Casual portrait of the same 44 year old woman with shoulder-length brown hair,
mid-career professional, in a home office at a desk, soft cool morning light
from window, casual button-up shirt, looking at a laptop with confident
expression, slight smile, leaning forward engaged, realistic skin texture with
visible pores and natural variation, organic phone-photo quality not studio
quality, candid feel, 9:16 portrait aspect ratio
```

Same person, same setting, same wardrobe. Expression and posture change.

## The 10-12 variant generation prompt

Use this as a single prompt to a Claude (or any LLM) to generate the full batch of Z-Image prompts.

```
I am producing a batch of 10-12 ad variants for an iOS app using Z-Image Turbo.

The app: [APP NAME] - [one-sentence description].

The viral feature reveal: [what the app shows the user].

The transformation: [BEFORE state] → [AFTER state].

The target audience: [persona description, e.g., "men 35-50 who feel out of shape"].

The variant matrix:
- 3 persona ages: [list 3 specific ages, e.g., 32, 41, 47]
- 2 persona genders: male, female
- 2 aesthetics: professional, casual lifestyle
- 3 hook angles: [list 3 specific angles, e.g., "fear of falling behind",
  "status / peer comparison", "specific scenario / 'POV'"]

Generate 10-12 distinct ad variants. For each variant, output:

VARIANT [N]:
- Persona: [age + gender + aesthetic]
- Hook angle: [which of the 3]
- Hook line (text overlay for first 2 seconds): [exact text]
- Z-Image BEFORE prompt: [full prompt using the structure: state, age, gender,
  descriptors, setting, lighting, wardrobe, framing, realism clauses,
  9:16 aspect ratio]
- Z-Image AFTER prompt: [same structure, with ONE clause changed to indicate
  the after state]
- Visual notes: [setting, props, anything specific]

Constraints:
- Each variant must use a different persona/hook combination
- The BEFORE and AFTER prompts in each variant must describe the SAME PERSON
  in the SAME SETTING with only the transformation state changing
- Use realistic skin texture clauses for every prompt (visible pores, natural
  variation, no filter quality)
- Use organic phone-photo quality clauses (not studio, not produced)
- Use 9:16 portrait aspect ratio for every prompt
- Hook lines must follow the project voice rules: no em dashes, no
  "obsessed", no "game-changing", no "transformational", short sentences,
  conversational tone

Output all 10-12 variants in one response.
```

## Hook angle examples by app category

The "hook angle" for each variant determines what emotion the ad triggers in the first 2 seconds. Pick 3 angles that fit your app and rotate across variants.

### For attractiveness / face rating apps

- Curiosity: "What is your face score out of 10?"
- Insecurity: "I did not realize how I had aged until I checked this"
- Peer comparison: "POV: your friend just showed you what they got"
- Surprise: "I was not ready for this score"

### For fitness / body apps

- Identity: "If you are over 35 and your body is not what it used to be..."
- Specific scenario: "POV: you finally figured out why nothing is working"
- Surprise: "I checked my body fat and the number was wild"
- Peer comparison: "My friend who never works out got this score and I was furious"

### For AI literacy / learning apps

- Status: "If you are over 40 and worried AI is leaving you behind..."
- Specific scenario: "I asked ChatGPT this and the answer was insane"
- Curiosity: "What is your AI literacy score?"
- Peer comparison: "My intern uses AI tools I have never even heard of"

### For skincare apps

- Insecurity: "If your skin has gotten worse since you turned 35..."
- Surprise: "I got my skin scanned and the results were brutal"
- Curiosity: "Look what this app says about your skin"
- Identity: "POV: you finally figured out why your skincare was not working"

## Worked example: 12 variants for a face rating app

Inputs:
- App name: FaceCheck
- Description: AI face rating with detailed breakdowns
- Viral feature: numerical score plus 3 sub-scores (jawline, symmetry, skin)
- Audience: men 35-50 worried about looking older

The 12 variants matrix:

| # | Age | Gender | Aesthetic | Hook angle | Hook line |
|---|---|---|---|---|---|
| 1 | 38 | M | Casual | Curiosity | "What is your face score out of 10?" |
| 2 | 38 | M | Professional | Status | "POV: your colleague got an 8 and you got a 5" |
| 3 | 41 | M | Casual | Peer comp | "My buddy showed me his score and I was destroyed" |
| 4 | 41 | M | Professional | Insecurity | "I did not realize I had aged this much" |
| 5 | 44 | M | Casual | Curiosity | "I checked my face score for the first time" |
| 6 | 44 | M | Professional | Status | "POV: you finally figured out why she stopped looking" |
| 7 | 35 | F | Casual | Curiosity | "What is your face score out of 10?" |
| 8 | 35 | F | Professional | Peer comp | "My friend got a 9 and I was furious" |
| 9 | 42 | F | Casual | Insecurity | "I did not realize I looked tired all the time" |
| 10 | 42 | F | Professional | Status | "POV: your wedding photos look better than you do now" |
| 11 | 47 | M | Casual | Surprise | "I was not ready for this score" |
| 12 | 47 | F | Casual | Insecurity | "If you are over 45 and your face has changed..." |

For each row, the Z-Image BEFORE and AFTER prompts get generated using the prompt structure at the top of this file.

The action footage (you taking a selfie) and the app reveal screenshot stay the same across all 12. The face is the variable. The hook is the variable. Everything else is constant.

This produces 12 ad variants in roughly an hour once the workflow is set up.

## After the batch is generated

1. Run all 12 BEFORE images and 12 AFTER images through Z-Image Turbo (24 generations)
2. Pass each face through SwapTok to merge onto your action footage (24 video clips)
3. Edit 12 ads in CapCut or TikTok Studio (12 edits, ~5 minutes each)
4. Upload 4-6 of the strongest to TikTok Smart+ campaign for testing
5. Hold the remaining 6-8 in reserve for the next batch as variants of the winner

## Cross-references

- Workflow that uses this template: [../references/before-after-ad-workflow.md](../references/before-after-ad-workflow.md)
- TikTok campaign management for the resulting ads: [../references/tiktok-smartplus-campaigns.md](../references/tiktok-smartplus-campaigns.md)
- Voice rules for hook lines: `skills/video-scriptwriter/references/direct-response-voice-system.md`
- Hook engineering (5 levers + scoring): `skills/video-scriptwriter/references/hook-engineering.md`
- Anti-AI script tells (especially relevant to keep the hook lines native): `skills/video-scriptwriter/references/anti-ai-script-tells.md`
