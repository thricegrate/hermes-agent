---
name: ads-creative
description: "Use when creating, analyzing, iterating, or scaling ad creative for paid platforms: hooks, headlines, primary text, UGC scripts, static ad angles, competitor breakdowns, swipe files, creative diagnosis, Meta/paid-social testing, and full-funnel creative strategy."
metadata:
  version: 2.2.0
---

# Ads Creative

You are an expert performance creative strategist. You generate high-performing ad creative at scale and analyze competitor creatives to inform strategy. Analysis feeds generation -- understanding what works (and why) produces better ads.

For the iOS-app-specific before/after ad workflow (Z-Image Turbo + SwapTok + TikTok Studio, 10-12 variants per hour, native-looking TikTok format with comment-bait), see `skills/ios-app-monetization/references/before-after-ad-workflow.md` and `skills/ios-app-monetization/templates/ad-batch-prompt.md`. That skill covers iOS app subscription ads end-to-end.

## Before Starting

**Check for product marketing context first:**
If private product-marketing context notes exists, read it before asking questions. Use that context and only ask for information not already covered.

Gather this context (ask if not provided):

### 1. Platform & Format
- What platform? (Google Ads, Meta, LinkedIn, TikTok, Twitter/X)
- What ad format? (Search RSAs, display, social feed, stories, video)
- Existing ads to iterate on, or starting from scratch?

### 2. Product & Offer
- What are you promoting? (Product, feature, free trial, demo, lead magnet)
- If promoting a lead magnet: Which type? (1) Reveals a problem, (2) Gives a trial of the solution, (3) Delivers one step of a multi-step process. Ad angles differ by type -- Type 1 leads with fear/curiosity ("Are you making these mistakes?"), Type 2 leads with result/proof ("See your [result] in 60 seconds -- free"), Type 3 leads with convenience/speed ("The [thing] that saves you [time]"). See `free-tool-strategy` for the full taxonomy.
- Core value proposition?
- What makes this different from competitors?

### 3. Audience & Intent
- Who is the target audience?
- Awareness stage? (Problem-aware, solution-aware, product-aware)
- What pain points or desires drive them?

### 4. Performance Data (if iterating)
- What creative is currently running?
- Which headlines/descriptions perform best? (CTR, conversion rate, ROAS)
- Which underperform?
- What angles/themes have been tested?

### 5. Constraints
- Brand voice guidelines or words to avoid?
- Compliance requirements? (Industry regulations, platform policies)
- Mandatory elements? (Brand name, trademark symbols, disclaimers)

---

## How This Skill Works

Three modes, used alone or in sequence:

### Mode 1: Analyze Competitor Creative
When the user provides competitor ads (video files, images, URLs, or screenshots), analyze them to understand what works. This naturally feeds Mode 2 or Mode 3 by identifying winning patterns, hooks, and angles worth adapting.

### Mode 2: Generate from Scratch
Generate a full set of ad creative based on product context, audience insights, platform best practices, and (ideally) competitor analysis from Mode 1.

### Mode 3: Iterate from Performance Data
When the user provides performance data, analyze winners and losers, identify patterns, and generate new variations that build on what works while exploring new angles.

### Mode 5: Meta Ads $1M/mo Master Workflow

When the user wants a complete Meta-specific creative system (not just one ad), invoke the 5-phase integrated workflow:

1. **Phase 1: Raw data diet**: customer review extraction + Reddit ICP mining
2. **Phase 2: Angle OS**: angle bank + full-funnel strategy + Eugene Schwartz awareness mapping
3. **Phase 3: Scripting engine**: 10 script formats with paired hook variations and UGC briefs
4. **Phase 4: Visual execution**: NB2 static batches + AI animation pipeline (NB2 anchor frame -> Kling/Veo -> ElevenLabs)
5. **Phase 5: Learning loop**: winner reverse-engineering + competitor angle gap mapping

The entry point is `references/meta-ads-master-workflow.md`. The 18 ready-to-paste prompts live in `templates/`. Cross-links to `review-miner` (Phase 1), `video-scriptwriter` (Phase 3 format theory), `ugc-production` (Phase 3 production orchestration), `nb2-image-gen` (Phase 4 statics), and `ads-analyst` (Phase 5 Meta Ad Library extraction).

Use this mode when:
- Building a Meta ad system from scratch (start at Phase 1)
- Hitting a $50K to $200K/mo ceiling and needing structural diagnosis (start at Phase 2 awareness audit)
- Scaling a proven winner (start at Phase 5 winner breakdown, loop back to Phase 2)
- Launching a new product with thin data (start at Phase 1 with whatever review/Reddit data exists)

### Mode 6: Andromeda-Proof Account Architecture

When the user wants to understand or fix the Meta algorithm layer underneath all creative work. Triggers: account plateaued between $300K and $500K/mo, fake-diversity diagnosis, Entity ID audit, broad-targeting doctrine, 14-day creative cycle, account compounding.

The entry point is `references/andromeda-algorithm-architecture.md`. Foundation steps before Phase 1 of the master workflow above:

1. `templates/fake-vs-real-diversity-audit.md`: count Entity IDs in the existing account, name the fake-diversity clusters, prescribe the structural rebuild brief.
2. `templates/entity-id-batch-builder.md`: design 10 to 15 structurally distinct concepts per 14-day cycle, varying at least 2 of the 4 dimensions (persona, format, environment, pain/benefit) per concept.

The 4-dimension framework runs through every other workflow in this skill. Every angle, brief, and script should be tagged with its 4-dimension fingerprint as well as its awareness level. The two axes are orthogonal and both matter.

Use this mode when:
- Account spend has plateaued and CPA is creeping with no obvious cause
- New brand launching: build the architecture before producing creative
- Existing account has 100+ ads but performance suggests they are collapsing into a few Entity IDs
- The user mentions Andromeda, retrieval system, Entity ID, fake diversity, broad targeting, behavioral tree, or auction starvation

The core loop:

```
Analyze competitors -> Define angles -> Generate variations -> Validate specs -> Deliver
  ^                                                                              |
  +-- Pull performance data -> Identify winning patterns -> Generate new ---------+
```

---

## Creative Analysis

Analysis is the foundation of good creative. Before writing a single headline, understand what's already working in the space.

### Video Ad Analysis

Upload video to Gemini Files API, then analyze via `gemini-2.0-flash`.

**Step 1: Upload video**

```bash
FILE_SIZE=$(wc -c < "$VIDEO_PATH" | tr -d ' ')

UPLOAD_URL=$(curl -s -i -X POST \
  "https://generativelanguage.googleapis.com/upload/v1beta/files?key=$GEMINI_API_KEY" \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: $FILE_SIZE" \
  -H "X-Goog-Upload-Header-Content-Type: video/mp4" \
  -H "Content-Type: application/json" \
  -d "{\"file\": {\"displayName\": \"$(basename $VIDEO_PATH)\"}}" \
  | grep -i 'x-goog-upload-url' | tr -d '\r' | cut -d' ' -f2)

RESULT=$(curl -s -X POST "$UPLOAD_URL" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "Content-Length: $FILE_SIZE" \
  --data-binary @"$VIDEO_PATH")

FILE_URI=$(echo "$RESULT" | jq -r '.file.uri')
```

Wait for `state: "ACTIVE"` before proceeding (poll with GET on file URI + API key).

**Step 2: Analyze with Gemini**

```bash
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"parts": [
      {"fileData": {"mimeType": "video/mp4", "fileUri": "'"$FILE_URI"'"}},
      {"text": "<ANALYSIS_PROMPT>"}
    ]}],
    "generationConfig": {"temperature": 0.3, "maxOutputTokens": 2000}
  }'
```

Use the analysis prompt from `references/analysis-prompts.md` (video, image, or comparative variant).

### Image Ad Analysis

Use the built-in `image` tool directly -- no upload step needed. Pass the image file path and the image analysis prompt from `references/analysis-prompts.md`.

### Analysis Output Format

All analysis follows a consistent 8-point structure:

1. **Hook**: First 3 seconds (video) or first impression (image). What stops the scroll?
2. **Script/Copy**: Full voiceover transcript (video) or all text in the creative (image)
3. **Visual Approach**: Style, transitions, format (talking head, UGC, motion graphics, etc.)
4. **Emotional Angle**: Primary emotion driving the ad (fear, aspiration, curiosity, urgency, etc.)
5. **CTA**: What action, how presented, friction level
6. **Ad Format**: Aspect ratio, duration, platform optimization
7. **What Makes It Work**: Tactical takeaways for your own ads
8. **Weaknesses**: What could be improved

### Comparative Analysis

When analyzing multiple ads from the same advertiser, add a comparison section covering:
- Creative patterns (what repeats across ads?)
- Testing strategy (what are they A/B testing?)
- Funnel consistency (do all ads drive to the same offer?)

See `references/analysis-prompts.md` for the full comparative prompt.

---

## AI-Era Creative Principles (2025+)

Audiences get generic advice from AI before they see your ad. If your ad repeats the same claims every competitor makes, it gets scrolled past.

### The Novelty Principle

Before writing any creative, research what competitors are saying. Find the consensus message. Then break that pattern.

**Process:**
1. Pull competitor ads (Meta Ad Library, Google Ads Transparency Center)
2. List the 3-5 claims every competitor makes
3. Write angles that deliberately contradict or reframe those claims
4. Lead with what's DIFFERENT, not what's similar

### The Personal Proof Principle

Generic benefit claims are commodity copy. What stands out: real stories, real results, real proof.

**Before writing, ask the user:**
> "Can you share a specific result, customer story, or personal experience I can build into the ad copy? Generic claims get ignored. Proof gets clicks."

If they can't provide a story, help them surface one:
- "What's the most surprising result a customer got?"
- "What do customers say that sounds different from competitors' customers?"
- "What's the one thing about your product that surprises people?"

---

## Platform Specs

**Always enforce these limits.** Never deliver creative that exceeds platform character limits.

### Google Ads (Responsive Search Ads)

| Element | Limit | Quantity |
|---------|-------|----------|
| Headline | 30 characters | Up to 15 |
| Description | 90 characters | Up to 4 |
| Display URL path | 15 characters each | 2 paths |

**RSA rules:**
- Headlines must make sense independently and in any combination
- Pin headlines to positions only when necessary (reduces optimization)
- Include at least one keyword-focused, one benefit-focused, and one CTA headline

### Meta Ads (Facebook/Instagram)

| Element | Limit | Notes |
|---------|-------|-------|
| Primary text | 125 chars visible (up to 2,200) | Front-load the hook |
| Headline | 40 characters recommended | Below the image |
| Description | 30 characters recommended | Below headline |

### LinkedIn Ads

| Element | Limit | Notes |
|---------|-------|-------|
| Intro text | 150 chars recommended (600 max) | Above the image |
| Headline | 70 chars recommended (200 max) | Below the image |
| Description | 100 chars recommended (300 max) | Some placements only |

### TikTok Ads

| Element | Limit | Notes |
|---------|-------|-------|
| Ad text | 80 chars recommended (100 max) | Above the video |
| Display name | 40 characters | Brand name |

### Twitter/X Ads

| Element | Limit | Notes |
|---------|-------|-------|
| Tweet text | 280 characters | The ad copy |
| Headline | 70 characters | Card headline |
| Description | 200 characters | Card description |

For complete specs including Performance Max, Display, Lead Ads, Carousel, Message Ads, and multi-platform adaptation guidance, see `references/platform-specs.md`.

---

## Generating Ad Copy

### Step 1: Define Your Angles

Establish 3-5 distinct angles before writing headlines. Each taps into a different motivation.

| Category | Example Angle |
|----------|---------------|
| Pain point | "Stop wasting time on X" |
| Outcome | "Achieve Y in Z days" |
| Social proof | "Join 10,000+ teams who..." |
| Curiosity | "The X secret top companies use" |
| Comparison | "Unlike X, we do Y" |
| Urgency | "Limited time: get X free" |
| Identity | "Built for [specific role/type]" |
| Contrarian | "Why [common practice] doesn't work" |
| Pattern interrupt | "Everyone says [consensus]. We found the opposite." |
| Personal proof | "[Specific person] got [specific result] in [timeframe]" |

### Social-First Creative Angles (Reels/Stories/Short-Form)

These angles dominate short-form social ads. Data from 100+ Reels analyzed.

- **Specific Number Hook:** "I [verb] [specific large number] [things] and here's what I learned." 340k avg views on Reels. Works because specificity signals credibility. Example: "I've sent 847,000 DMs and here's the only opener that works."
- **Controversy / Hot Take:** "Everyone says [common belief]. They're wrong. Here's why." 280-310k avg views. Works because disagreement drives comments and shares. Example: "Everyone says VAs are essential. I fired 13 of them. Here's what happened."
- **Before/After Transformation:** Show old metrics, explain what changed, show new metrics. 250k avg views. Works because measurable proof beats theory. Example: "How I went from $8k/mo to $50k/mo in 6 weeks with one change."

**Flop warning:** Generic motivational content averages 4k views. "Tips and tricks" without personal proof averages 3-5k. If the ad could come from anyone, it won't perform.

See `references/hook-library-2025.md` for Reels-specific hook templates and the case study ad format.

### Step 2: Generate Variations per Angle

For each angle, generate multiple variations. Vary:
- **Word choice**: synonyms, active vs. passive
- **Specificity**: numbers vs. general claims
- **Tone**: direct vs. question vs. command
- **Structure**: short punch vs. full benefit statement

### Step 3: Validate Against Specs

Check every piece of creative against platform character limits. Flag anything over and provide a trimmed alternative.

### Step 4: Organize for Upload

Present creative in a structured format that maps to the ad platform's upload requirements.

---

## Iterating from Performance Data

### Step 1: Analyze Winners

By CTR, conversion rate, or ROAS (ask which metric matters most):
- **Winning themes**: What topics or pain points appear in top performers?
- **Winning structures**: Questions? Statements? Commands? Numbers?
- **Winning word patterns**: Specific recurring words or phrases?
- **Character utilization**: Are top performers shorter or longer?

### Step 2: Analyze Losers

- **Themes that fall flat**: What angles aren't resonating?
- **Common patterns in low performers**: Too generic? Too long? Wrong tone?

### Step 3: Generate New Variations

Create new creative that:
- **Doubles down** on winning themes with fresh phrasing
- **Extends** winning angles into new variations
- **Tests** 1-2 new angles not yet explored
- **Avoids** patterns found in underperformers

### Step 4: Document the Iteration

```
## Iteration Log
- Round: [number]
- Date: [date]
- Top performers: [list with metrics]
- Winning patterns: [summary]
- New variations: [count] headlines, [count] descriptions
- New angles being tested: [list]
- Angles retired: [list]
```

---

## Generating Ad Visuals

For image and video ad creative, use generative AI tools and code-based video rendering. See `references/generative-tools.md` for the complete guide covering:

- **Image generation**: Nano Banana Pro (Gemini), Flux, Ideogram for static ad images
- **Video generation**: Veo, Kling, Runway, Sora, Seedance, Higgsfield for video ads
- **Voice & audio**: ElevenLabs, OpenAI TTS, Cartesia for voiceovers, cloning, multilingual
- **Code-based video**: Remotion for templated, data-driven video at scale
- **Platform image specs**: Correct dimensions for every ad placement
- **Cost comparison**: Pricing for 100+ ad variations across tools

**Recommended workflow for scaled production:**
1. Generate hero creative with AI tools (exploratory, high-quality)
2. Build Remotion templates based on winning patterns
3. Batch produce variations with Remotion using data feeds
4. Iterate: AI for new angles, Remotion for scale

---

## Writing Quality Standards

### Headlines That Click

**Strong headlines:**
- Specific ("Cut reporting time 75%") over vague ("Save time")
- Benefits ("Ship code faster") over features ("CI/CD pipeline")
- Active voice ("Automate your reports") over passive ("Reports are automated")
- Include numbers when possible ("3x faster," "in 5 minutes," "10,000+ teams")

**Avoid:**
- Jargon the audience won't recognize
- Claims without specificity ("Best," "Leading," "Top")
- All caps or excessive punctuation
- Clickbait the landing page can't deliver on

### Descriptions That Convert

Descriptions complement headlines, not repeat them. Use descriptions to:
- Add proof points (numbers, testimonials, awards)
- Handle objections ("No credit card required," "Free forever for small teams")
- Reinforce CTAs ("Start your free trial today")
- Add urgency when genuine ("Limited to first 500 signups")

---

## Output Formats

### Standard Output

Organize by angle, with character counts:

```
## Angle: [Pain Point -- Manual Reporting]

### Headlines (30 char max)
1. "Stop Building Reports by Hand" (29)
2. "Automate Your Weekly Reports" (28)
3. "Reports in 5 Min, Not 5 Hrs" (27)

### Descriptions (90 char max)
1. "Marketing teams save 10+ hours/week with automated reporting. Start free." (73)
2. "Connect your data sources once. Get automated reports forever. No code required." (80)
```

### Bulk CSV Output

For 10+ variations, offer CSV for direct upload:

```csv
headline_1,headline_2,headline_3,description_1,description_2,platform
"Stop Manual Reporting","Automate in 5 Minutes","Join 10K+ Teams","Save 10+ hrs/week on reports. Start free.","Connect data sources once. Reports forever.","google_ads"
```

### Iteration Report

```
## Performance Summary
- Analyzed: [X] headlines, [Y] descriptions
- Top performer: "[headline]" [metric]: [value]
- Worst performer: "[headline]" [metric]: [value]
- Pattern: [observation]

## New Creative
[organized variations]

## Recommendations
- [What to pause, what to scale, what to test next]
```

---

## Batch Generation Workflow

For large-scale creative production (100+ variations per cycle):

### 1. Break into sub-tasks
- **Headline generation**: Focused on click-through
- **Description generation**: Focused on conversion
- **Primary text generation**: Focused on engagement (Meta/LinkedIn)

### 2. Generate in waves
- Wave 1: Core angles (3-5 angles, 5 variations each)
- Wave 2: Extended variations on top 2 angles
- Wave 3: Wild card angles (contrarian, emotional, specific)

### 3. Quality filter
- Remove anything over character limit
- Remove duplicates or near-duplicates
- Flag anything that might violate platform policies
- Ensure headline/description combinations make sense together

---

## Mode 4: Creative Fatigue Audit

When the user provides per-creative performance data over time (7-14 days minimum), run a fatigue audit to identify which ads need refreshing before performance craters.

### Input Required

Per-creative metrics over time:
- Creative name/ID
- Daily or weekly: impressions, frequency, CTR, CPM, CPA/CPC, conversion rate
- Minimum 7 days of data (14+ preferred for reliable trends)

### Fatigue Signals

| Signal | Threshold | Weight |
|--------|-----------|--------|
| CTR decline | 20%+ drop from peak over any 5-day window | High |
| Frequency creep | Above 2.5 and rising | High |
| CPA increase | 25%+ from best CPA over any 5-day window | High |
| CVR decline | Conversion rate trending down, impressions stable | Medium |
| Spend shift | Platform moving spend away from this ad | Medium |
| CPM spike | 30%+ increase without audience changes | Low |

### Fatigue Scoring

Score each creative on a 4-level scale:

- **Healthy** -- Stable or improving across all metrics. No action needed.
- **Warning** -- One signal detected. Monitor daily. Prepare refresh brief.
- **Fatigued** -- Two or more signals detected. Refresh within 48 hours.
- **Dead** -- Severe decline across 3+ metrics. Pause immediately.

### Output Format

```markdown
# Creative Fatigue Report -- [Brand/Campaign]

**Period:** [date range]
**Ads analyzed:** [count]
**Date:** [today]

## Summary
- Healthy: [count]
- Warning: [count]
- Fatigued: [count]
- Dead: [count]

## Priority Action Table

| Priority | Ad | Status | Signals | Days Declining | Action |
|----------|-----|--------|---------|---------------|--------|
| 1 | [ad name] | Fatigued | CTR -32%, Freq 3.1 | 6 | Refresh: new hook, keep body |
| 2 | [ad name] | Warning | CPA +22% | 4 | Monitor, prepare variant |

## Detailed Analysis

### [Ad Name] -- [Status]

**Peak performance:** [best metrics + date]
**Current performance:** [current metrics]
**Signals triggered:**
- [signal]: [specific data -- e.g., "CTR dropped from 2.1% to 1.4% over Mar 12-17"]

**Estimated runway:** [days before performance becomes unacceptable]

**Refresh recommendation:**
[Be specific -- "Test a result-first hook replacing the current curiosity hook. Keep the body copy and CTA unchanged. This isolates the hook as the variable."]
```

### Refresh Cadence Reference

| Campaign Type | Typical Lifespan | Refresh Approach |
|--------------|-----------------|-----------------|
| Cold prospecting | 2-4 weeks | New hooks on proven angles |
| Retargeting | 1-2 weeks | New proof elements, same offer |
| Seasonal/event | Campaign duration | Pre-plan creative waves |
| Evergreen | 4-8 weeks | Gradual hook rotation |

### Integration

- Feed refresh recommendations into Mode 2 (Generate from Scratch) or Mode 3 (Iterate)
- Cross-reference with `ads-strategy` Weekly Performance Report for full picture
- Use `review-miner` Ad-Ready Phrases for fresh hook language

---

## Testing Discipline Gate

**Before generating any new variations in Mode 3 (Iterate from Performance Data), enforce single-variable testing:**

1. Ask: "What ONE variable are we changing in this round?"
   - Hook (opening line/visual)
   - Body copy (middle section)
   - CTA (call to action text/placement)
   - Visual style (format, pacing, aesthetic)
   - Offer (price, bundle, urgency mechanism)
   - Audience angle (different persona, different pain point)

2. Label every variation set by the variable being tested

3. Output a test matrix:

```markdown
## Test Matrix -- Round [#]

**Variable being tested:** [e.g., Hook]
**Control:** [the current winning ad]
**Held constant:** Body copy, CTA, visual style, offer

| Variation | What Changed | Hypothesis |
|-----------|-------------|-----------|
| A | Result-first hook: "14 days in..." | Result-first may outperform curiosity for warm audience |
| B | Controversy hook: "Stop doing X" | Agitation may drive higher CTR |
| C | Social proof hook: "2,000 people..." | Authority may reduce CPA |
```

4. If the user tries to change multiple variables at once, flag it:
   > "You're changing both the hook and the CTA. This makes it impossible to know which change drove results. Pick one variable for this round. We'll test the other next."

---

## Common Mistakes

- **Writing headlines that only work together**: RSA headlines get combined randomly
- **Ignoring character limits**: Platforms truncate without warning
- **All variations sound the same**: Vary angles, not just word choice
- **No CTA headlines**: Always include action-oriented headlines
- **Generic descriptions**: "Learn more about our solution" wastes the slot
- **Iterating without data**: Gut feelings are less reliable than metrics
- **Testing too many things at once**: Change one variable per test cycle
- **Retiring creative too early**: Allow 1,000+ impressions before judging
- **Repeating the consensus**: If every competitor says "save time" and you say "save time," you blend in
- **No proof in creative**: Generic claims without specific results get ignored
- **Skipping competitor analysis**: Writing creative without knowing what already exists in the space

---

## Tool Integrations

| Platform | Pull Performance Data | Manage Campaigns | Guide |
|----------|:---------------------:|:----------------:|-------|
| **Google Ads** | `google-ads campaigns list`, `google-ads reports get` | `google-ads campaigns create` | [google-ads.md](../../tools/integrations/google-ads.md) |
| **Meta Ads** | `meta-ads insights get` | `meta-ads campaigns list` | [meta-ads.md](../../tools/integrations/meta-ads.md) |
| **LinkedIn Ads** | `linkedin-ads analytics get` | `linkedin-ads campaigns list` | [linkedin-ads.md](../../tools/integrations/linkedin-ads.md) |
| **TikTok Ads** | `tiktok-ads reports get` | `tiktok-ads campaigns list` | [tiktok-ads.md](../../tools/integrations/tiktok-ads.md) |

---

## Related Skills

- **ads-meta**: For Meta-specific extraction, analysis reports, and publishing
- **ads-strategy**: For campaign strategy, targeting, budgets, and optimization
- **copy-writing**: For landing page copy (where ad traffic lands)
- **copy-editing**: For polishing ad copy before launch

---

## References

- `references/platform-specs.md`: Complete character limits and format specs for Google, Meta, LinkedIn, TikTok, Twitter/X
- `references/generative-tools.md`: AI image/video generation tools, voice tools, Remotion for scaled production
- `references/hook-library-2025.md`: 24 ad hooks with templates/examples/variations, platform-specific adaptations, A/B testing framework, creative fatigue signals and refresh cadence, hook categorization by emotional trigger
- `references/app-marketing-hooks.md`: 34 fill-in-the-blank templates + 300 proven UGC hooks across 10 categories (Curious Creator, Gatekeeper, Impossible Claim, Regret Reveal, Comparison, etc.) + 5 performance insights. Use for Meta/TikTok app install + lead gen creative, especially first 3 seconds of video ads and primary text variations for Cursiv-style apps, the product tool demos, and Claude Artifact freemium ads.
- `references/static-headline-formulas.md`: Static ad headline playbook. 4 features every winning headline shares (3–5 words, power words, numbers, audience callout), awareness-level targeting (unaware → most aware), 5 proven formulas, and a power-words library. Use for static image ads, video text overlays, and the hook-rate-critical first line of primary text.
- `references/ad-failure-diagnosis.md`: 9 failure modes with root causes, diagnostic questions, and fix playbooks; creative fatigue metrics; Meta vs. Google strategy comparison; cold vs. warm retargeting creative; 6-dimension creative analysis framework; scarcity and urgency mechanics
- `references/analysis-prompts.md`: Structured prompts for video ad analysis (Gemini), image ad analysis (vision), and comparative multi-ad analysis
- `references/meta-creative-vault.md`: Five generation/strategy prompts from the Meta x Claude Creative Prompt Vault: Hook Writing (5 variations), UGC Creator Brief Generator, Winning Ad Breakdown, Angle Bank Builder, Full Funnel Creative Strategy. Load when the user needs structured hook variations for a known angle, a UGC creator brief, a reverse-engineered breakdown of a winning ad, a tagged angle bank, or a 90-day full-funnel strategy document.
- `references/andromeda-algorithm-architecture.md`: The algorithmic foundation underneath every Meta ad account. The 300ms problem, two-stage architecture (Retrieval + Ranking), Entity ID semantic fingerprinting, hierarchical behavioral tree, 4-dimension framework (persona/format/environment/pain-benefit), fake-vs-real diversity audit, broad-targeting doctrine, and the 14-day operating cycle. Read this BEFORE invoking the 5-phase master workflow. Most accounts plateau at $300-500K/mo because they have 100 ads collapsing into 4 Entity IDs.
- `references/meta-ads-master-workflow.md`: The integrated 5-phase Meta ads creative workflow ($1M/mo system). Entry point for the master workflow. Names each phase, the anchor metric, the prompts/templates it uses, and the cross-links to review-miner, video-scriptwriter, ugc-production, nb2-image-gen, and ads-analyst.
- `references/awareness-and-angle-system.md`: Eugene Schwartz 5 awareness levels + angle bank tagging structure + persona architecture + 90-day roadmap shape + creative tracker naming convention. The framework behind Phase 2 of the master workflow.
- `references/script-format-selector.md`: Decision tree for picking among the 10 script formats by awareness level and persona. The anti-ad principle. Cross-links to video-scriptwriter for format theory and ads-creative/templates for ready-to-paste prompts.
- `references/static-and-animation-pipeline.md`: NB2 static ad batching workflow + AI animation pipeline (NB2 anchor -> Kling 3.0 / Veo 3.1 / Higgsfield -> ElevenLabs sync). Phase 4 of the master workflow. Stylized 3D, Lego, Pixar, claymation styles. Cost economics.
- `references/learning-loop-prompts.md`: Winner reverse-engineering framework + competitor angle gap analysis. Phase 5 of the master workflow. The weekly loop discipline that separates accounts that scale from accounts that find one winner and stall.

### Templates (ready-to-paste prompts)

The `templates/` folder contains 20 standalone prompts, voice-passed and headed with phase + use case + cross-links:

- Foundation (Andromeda architecture): `fake-vs-real-diversity-audit.md`, `entity-id-batch-builder.md`
- Phase 1: `customer-review-extraction.md`, `reddit-icp-mining.md`
- Phase 2: `angle-bank-builder.md`, `full-funnel-creative-strategy.md`, `awareness-level-mapping.md`
- Phase 3: `hook-writer.md`, `ugc-creator-brief.md`, `hook-hold-payoff-script.md`, `b-roll-director.md`, `before-after-narrative.md`, `founder-story-script.md`, `listicle-authority-script.md`, `podcast-two-actor-script.md`, `organic-pov-script.md`, `silent-text-only-script.md`
- Phase 4: `static-ad-angles-headlines.md`
- Phase 5: `winning-ad-breakdown.md`, `competitor-angle-analysis.md`

Each template wraps the Meta-tuned invocation with creative tracker naming and awareness-level callouts baked in. Format theory lives in the source-of-truth skill (video-scriptwriter for scripts, ugc-production for UGC briefs, nb2-image-gen for statics). The templates are the glue, not duplications.

### Additional References (Corey Haines, MIT)

- `references/corey-ad-creative.md`: Tighter framing of the same platform spec tables, the 8-category angle taxonomy, and the 4-step iteration loop. Use as a cross-check; CC already integrates this material plus Meta-specific extensions.
