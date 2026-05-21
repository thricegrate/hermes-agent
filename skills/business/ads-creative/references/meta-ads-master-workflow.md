# Meta Ads $1M/mo Master Workflow

The integrated 5-phase creative system that turns raw customer data into a Meta ad account capable of scaling past seven figures monthly. Used when the brand needs a system, not a one-off ad.

Most ad accounts cap out because every ad speaks to one awareness level. The audience at that level runs out. Frequency climbs. CPA creeps. The fix is almost never a new ad. The fix is a new awareness level. This workflow builds a creative library that lives across all 5 levels at once, fed by real customer language, and refreshed weekly from performance signal.

## Foundation: Andromeda architecture

Before invoking any phase below, read `andromeda-algorithm-architecture.md`. The 5-phase workflow assumes the Andromeda retrieval system underneath every account it touches. Without that foundation, the workflow produces 50 ads that Andromeda collapses into 4 Entity IDs, and the account never compounds.

Two foundation steps run before Phase 1:

1. Run `templates/fake-vs-real-diversity-audit.md` on the existing account to count Entity IDs, not ads.
2. Run `templates/entity-id-batch-builder.md` to design 10 to 15 structurally distinct concepts that the upcoming phases will produce.

The 4-dimension framework (persona, format, environment, pain/benefit) is the operating discipline that runs through every phase below. Each concept in the angle bank should be tagged with its 4-dimension fingerprint, not just its awareness level.

## The 5 phases

| Phase | What it produces | Anchor metric | Primary templates |
|---|---|---|---|
| 1. Raw data diet | Customer language library (reviews + Reddit) | Quote count per pain point | `customer-review-extraction.md`, `reddit-icp-mining.md` |
| 2. Angle OS | Tagged angle bank + funnel map + awareness audit | Angles per awareness level | `angle-bank-builder.md`, `full-funnel-creative-strategy.md`, `awareness-level-mapping.md` |
| 3. Scripting engine | 10 script formats per winning angle | Format diversity per persona | `hook-writer.md` + 9 format templates |
| 4. Visual execution | Static ad batches + AI animation pipeline | Visual variations per concept | `static-ad-angles-headlines.md` + `static-and-animation-pipeline.md` |
| 5. Learning loop | Winner breakdowns + competitor gap maps | Transferable principles documented | `winning-ad-breakdown.md`, `competitor-angle-analysis.md` |

Every phase feeds the next. Skip Phase 1 and Phase 2 is built on guesses. Skip Phase 5 and winning ads die without their lessons surviving.

## Phase 1: Raw data diet

AI cannot guess what your market wants. It has to extract it.

Generic product descriptions in produce generic ads that fatigue in three days. The opening move is mining the unfiltered language customers use when nobody is selling to them.

Two sources, two prompts:

1. Customer reviews (Amazon, Shopify, app store, post-purchase surveys). The customers who already bought. Their language is product-aware and solution-aware. Best for bottom and middle funnel.

2. Reddit threads. The customers who have not bought yet. Their language is unaware and problem-aware. Best for top of funnel.

Templates:
- `templates/customer-review-extraction.md` produces a 5-section angle bank from reviews: raw language index, pain point angles, transformation angles, failed solution angles, objection angles.
- `templates/reddit-icp-mining.md` produces a 5-section map from Reddit: pain point map with frequency tags, failed solution library, emotional language extraction, community dialect, weak-signal flags.

For Amazon/Shopify review mining workflow specifically (scraping, deduping, tagging), see `skills/review-miner/SKILL.md`. For Reddit-specific workflow (subreddit selection, thread filtering, dialect calibration), see `skills/review-miner/references/reddit-icp-mining.md`.

Move to Phase 2 when you have at least 15 quoted pain points and 5 failed solutions in customer language, not yours.

## Phase 2: Angle OS

Data is useless without structure. 80% of ad accounts fail because every ad is product-aware. When that audience exhausts, there is nowhere to go.

The Angle OS is a library of validated creative directions, each tagged by:
- Target persona (one specific person, not a demographic)
- Awareness level (Eugene Schwartz 5-level pyramid)
- Emotional trigger (frustration, guilt, relief, embarrassment, pride, aspiration, fear)
- Best-fit script formats
- Creative priority (high / medium / low)
- Status (fresh / active / fatigued)

Three templates run in order:

1. `templates/awareness-level-mapping.md`: audit the current account against Eugene Schwartz's 5 awareness levels. Names the gaps.
2. `templates/angle-bank-builder.md`: turns Phase 1 customer language into a tagged angle library that fills those gaps.
3. `templates/full-funnel-creative-strategy.md`: maps the angle bank to a 90-day creative roadmap with persona architecture, funnel-stage formats, and the first three briefs to ship.

The frameworks behind these templates (Schwartz awareness pyramid, Hormozi awareness model) live in `awareness-and-angle-system.md` and the existing `hormozi-goated-ads.md`. Read those for the theory before invoking the templates.

Move to Phase 3 when the angle bank has at least 2 fresh angles per awareness level and the 90-day roadmap is documented.

## Phase 3: Scripting engine

Polished ads are dead. The native feed format wins. Every script in this phase is written to look like organic content, not advertising.

10 script formats. Pick by awareness level and persona. The decision tree lives in `script-format-selector.md`. Quick reference:

| Format | Best for awareness level | Best for | Template |
|---|---|---|---|
| Hook-Hold-Payoff | Solution Aware | Direct response, qualified audiences | `templates/hook-hold-payoff-script.md` |
| B-Roll + Voiceover | Problem Aware | Visual products, scrollable feeds | `templates/b-roll-director.md` |
| Before & After | Solution Aware | Transformation products | `templates/before-after-narrative.md` |
| Founder Story | Most Aware | Mission-driven, repeat buyers | `templates/founder-story-script.md` |
| Listicle / Authority | Problem Aware | Educational, expert positioning | `templates/listicle-authority-script.md` |
| Podcast Two-Actor | Solution Aware | Skeptical audiences, complex products | `templates/podcast-two-actor-script.md` |
| Organic POV | Unaware to Problem Aware | Top of funnel, lifestyle products | `templates/organic-pov-script.md` |
| Silent / Text-Only | Any | High-volume testing, captions-off feeds | `templates/silent-text-only-script.md` |
| Hook Writer | Any (5 variations per angle) | First-pass hook batch | `templates/hook-writer.md` |
| UGC Creator Brief | Any | Brief a creator without dilution | `templates/ugc-creator-brief.md` |

The format theory (what makes each format work, fail modes, voice patterns) lives in `skills/video-scriptwriter/references/`. The templates in `ads-creative/templates/` are the Meta-tuned invocations with creative tracker naming and awareness-level callouts baked in.

Move to Phase 4 when you have at least 1 script per awareness level ready to shoot.

## Phase 4: Visual execution

Two pillars:

### Static ad scaling

Customer review quotes become headline candidates. NB2 (Nano Banana 2) batches generate 10+ visual variations per concept. The `static-ad-angles-headlines.md` template produces 3 distinct static ad concepts per request (benefit-extreme, policy/guarantee, anti-solution). Each maps to a proven direct-response layout.

The full pipeline: review quotes -> headline candidates -> NB2 generation -> creative tracker logging. Detail in `static-and-animation-pipeline.md`.

### AI animation pipeline

Hyper-realistic AI humans look fake. Stylized 3D animations (Lego, Pixar, scientific graphic, claymation) bypass the consumer's ad blocker because we read them as entertainment.

The pipeline:
1. Script the animated narrative (Claude)
2. Generate anchor frame in NB2 (use as reference for all subsequent shots to keep visual consistency)
3. Animate base images in Kling 3.0 / Veo 3.1 / Higgsfield
4. Generate voiceover and audio in ElevenLabs, sync to final cut

Full workflow with prompt patterns: `static-and-animation-pipeline.md`. Cross-links to `skills/nb2-image-gen/SKILL.md` for NB2 prompting and `references/generative-tools.md` for tool selection.

Move to Phase 5 once Phase 4 creative has been live for at least 7 days with measurable spend.

## Phase 5: Learning loop

Most brands find a winning ad, scale it, watch it die, restart from scratch. The accounts that scale past $1M/mo extract the DNA of every winner and compound it across new formats.

Two templates:

1. `templates/winning-ad-breakdown.md`: reverse-engineers a winning ad into structural diagnosis, psychological mechanics, language analysis, transferable framework, and iteration roadmap. Output: 5 transferable principles + the next 3 iterations to test.

2. `templates/competitor-angle-analysis.md`: maps the category. What angle does every competitor share? What awareness level is everybody clustering at? What customer desires is the category consistently failing to address? Output: 3-5 unexploited gaps + the single most defensible position for your brand.

Run both weekly on Monday. Update the angle bank with new winners. Retire angles flagged as fatigued in `templates/winning-ad-breakdown.md` step 5. Then loop back to Phase 2 with refreshed inputs.

For the Meta Ad Library extraction workflow that feeds `competitor-angle-analysis.md`, see `skills/ads-analyst/SKILL.md`.

## When to invoke this workflow

- User wants to build a Meta ad creative system from scratch (start at Phase 1)
- User has scaled to $50-200K/mo and is hitting a ceiling (start at Phase 2 awareness audit)
- User has a winning ad they want to compound (start at Phase 5 winner breakdown, then loop back to Phase 2)
- User is launching a new product (start at Phase 1 with whatever review data exists, even if synthetic)

## Voice gate

Every script, hook, and headline produced by this workflow runs through `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md` before publication. No em-dashes. No banned marketing phrases. Coffee shop rule.

The templates themselves are voice-passed seed prompts. Output from those prompts is not automatically voice-compliant. The humanizer step is mandatory for any externally-published copy.

## Cross-references

- `references/andromeda-algorithm-architecture.md`: the algorithmic foundation underneath the entire workflow (Entity IDs, 4-dimension framework, behavioral tree, 14-day cycle, broad-targeting doctrine)
- `references/awareness-and-angle-system.md`: Schwartz 5-level pyramid, angle bank theory, persona architecture
- `references/script-format-selector.md`: decision tree for picking among the 10 script formats
- `references/static-and-animation-pipeline.md`: NB2 static workflow + Kling/Veo/ElevenLabs animation pipeline
- `references/learning-loop-prompts.md`: winner breakdown framework + competitor gap analysis
- `references/meta-creative-vault.md`: the original 5 Meta x Claude generation prompts (this workflow extends and structures them)
- `references/hormozi-goated-ads.md`: awareness pyramid foundation
- `references/hook-library-2025.md`: 24 hook templates
- `references/app-marketing-hooks.md`: 34 templates + 300 UGC hooks across 10 categories
- `references/static-headline-formulas.md`: 5 static ad formulas
- `skills/review-miner/SKILL.md`: review mining workflow that feeds Phase 1
- `skills/video-scriptwriter/SKILL.md`: format theory for Phase 3 scripts
- `skills/ugc-production/SKILL.md`: UGC production orchestration (the brief in Phase 3 is one input to that system)
- `skills/nb2-image-gen/SKILL.md`: NB2 prompting for Phase 4 statics
- `skills/ads-analyst/SKILL.md`: Meta Ad Library extraction for Phase 5 competitor analysis
