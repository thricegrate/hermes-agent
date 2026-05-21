# Silent / Text-Only Script Format

The cheapest format to produce. Often the highest-volume test format on Meta. No voiceover, no talking head. Background visual + text overlays carry everything.

When the format is calibrated, silent ads outperform produced UGC at a fraction of the cost. When it is uncalibrated, they look like screensavers.

## When this format wins

- High-volume top-of-funnel testing (cheap to produce 20 to 50 variations per week)
- Captions-off feeds (Reels, TikTok with sound off in public spaces)
- Visually demonstrable products (textures, applications, before/after, satisfying actions)
- Brands without a founder face or creator pipeline
- Saturated categories where everyone is using talking heads
- Pre-validating headlines and claims before investing in produced video

## When this format loses

- Products that need explanation (mechanism is invisible without narration)
- Story-driven angles (silent format does not carry narrative arcs)
- High-consideration purchases where audience needs trust signals
- Brands that lack distinctive visual assets

## The three layers

A silent ad has three layers:

1. **Visual bedrock**: the continuous background action that runs the full duration of the ad. Must be satisfying, pattern-interrupt strange, or product-demonstrative. The viewer should be able to watch the bedrock alone with no text and still feel pulled to keep watching.

2. **Text overlay sequence**: 5 to 7 cards of text that take the viewer from hook to CTA. One bold claim per card. 2 to 3 seconds per card.

3. **Audio (optional)**: trending audio track on TikTok/Reels for organic-feel placements. For paid Meta placements, silence often works without audio. Never add a voiceover.

## Visual bedrock selection

The bedrock is the difference between an ad that holds and an ad that scrolls past. Three categories:

### ASMR-style satisfying

- Product application (cream into skin, oil onto wood, foam dispensing)
- Texture demonstrations (powder mixing, ingredient pouring, fabric folding)
- Slow-motion product reveals
- Close-up packaging interactions (opening, scooping, dispensing)

### Pattern-interrupt strange

- Extreme close-ups of unexpected surfaces
- Anatomical or scientific visualizations
- Unusual hands-on demonstrations (applying product to fruit, glass, paper)
- Time-lapse transformations

### Product-demonstrative

- Before/after side-by-side
- Comparison demonstrations (your product vs competitor)
- Mechanism visualizations (how it works on a model or surface)
- Real-world use case (the product being used in the moment of need)

The bedrock should loop seamlessly. The viewer should not be able to tell where the video starts and ends.

## Text timing model

The pacing rule: 2 to 3 seconds per card. Below 2 seconds, the viewer cannot finish reading. Above 3 seconds, the viewer scrolls.

Standard 15 to 20 second sequence:

| Time | Card type | Example |
|---|---|---|
| 0:00 to 0:02 | Hook (bold claim) | "13 years of pain. Gone in 2 days." |
| 0:02 to 0:05 | Problem amplification | "I tried everything." |
| 0:05 to 0:08 | Failed solutions | "Accutane. PanOxyl. Retinoids. Nothing worked." |
| 0:08 to 0:12 | Mechanism | "Until I tried this." |
| 0:12 to 0:15 | Outcome | "Day 14: skin completely clear." |
| 0:15 to 0:18 | Guarantee | "Free 30-day return. No questions." |
| 0:18 to 0:20 | CTA | "Link below." |

The card sequence is the script. Every card must earn its place. Anything that does not advance from hook to CTA gets cut.

## Text styling rules

- High contrast: white text on darker visual, or black text on lighter visual. Never low-contrast.
- Bold or extra-bold weight. Light fonts disappear at thumb-scroll speed.
- Centered or upper-third placement. Lower-third gets cut off by platform UI in some placements.
- One bold claim per card. If it needs two lines, split into two cards.
- Use the platform's native text tool (TikTok native, Reels native). Third-party caption tools look corporate.

## Audio strategy

Three options:

1. **Trending audio (organic feel)**: best for TikTok-style placements. Pick audio that matches the emotional register of the script. A frustrated-then-relieved arc needs different audio than a transformation-driven arc.

2. **Silence (paid Meta default)**: defaults to silent in 80%+ of Reels viewer sessions. No audio strategy needed; the visual carries it.

3. **Ambient sound or minimal music**: low-volume ambient music. Adds production value without competing with the text. Avoid lyrics.

Never add a voiceover. The format is silent by design. A voiceover defeats the cost economics and the visual focus.

## Production economics

Silent ads cost a fraction of produced UGC:

- Live filming: phone footage + 30 minutes of editing per ad. ~$20 in editor time.
- AI-generated bedrock: NB2 anchor frame + Kling animation. ~$3 per 15-second ad.
- Stock-modified bedrock: existing brand footage with new text overlays. ~$5 in editor time per ad.

The economics let you test 20 to 50 variations per week. Volume is the input that the algorithm rewards.

## Common failure modes

- Too much text per card. Viewers cannot read it in 2 seconds. Always cap at one bold claim.
- Bedrock that does not earn the text. Generic product shots fail. The visual needs to be either ASMR-satisfying or pattern-interrupt strange.
- Skipping the guarantee. The format under-converts at the bottom of the funnel without risk reversal.
- Card sequence that drifts from hook to CTA. Every card must advance the arc.
- Adding voiceover "just in case." Defeats the format.

## Variations from one bedrock

The format multiplies easily. From one bedrock (say, an ASMR application of skincare cream), generate:

- Version A: problem-aware text sequence (failed solutions named)
- Version B: solution-aware text sequence (mechanism explained)
- Version C: product-aware text sequence (guarantee-led)
- Version D: most-aware text sequence (offer + urgency)

One bedrock + 4 text sequences = 4 ads at 4 awareness levels. The angle bank multiplies.

For the ready-to-paste prompt that produces a silent ad brief, see `skills/ads-creative/templates/silent-text-only-script.md`.

## Cross-references

- `skills/ads-creative/templates/silent-text-only-script.md`: ready-to-paste prompt
- `skills/ads-creative/references/script-format-selector.md`: when to pick silent over voiceover formats
- `skills/ads-creative/references/static-and-animation-pipeline.md`: AI-generated bedrock workflow (NB2 + Kling)
- `skills/ads-creative/references/static-headline-formulas.md`: headline copy patterns for the text overlays
- `references/hook-engineering.md`: hook-card writing principles
- `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md`: voice gate for text card copy
