# Cross-Platform Brief Structure: The 3 Inputs

The foundational brief structure for any AI UGC script generation session. Without these 3 inputs, no amount of platform-specific calibration produces strong output.

The 3 inputs feed every Claude session, regardless of which platform the output targets. They are the upstream variables. The platform calibration (see [platform-calibration-variables.md](platform-calibration-variables.md)) is the downstream adjustment.

## Why a unified brief matters

Most operators feed Claude a product brief and ask for "a TikTok script," then take that same script and try to adapt it for Instagram Reels, YouTube Shorts, and Facebook Reels with minor edits.

The result is content that performs reasonably on the original platform and underperforms on every other platform because the format-specific calibration was never built into the upstream prompt.

The fix is the unified 3-input brief. Each input is platform-agnostic. The same brief drives content generation across all 4 platforms. Calibration variables adjust output downstream.

## Input 1: The Audience Insight Statement

A vivid emotional portrait of the target persona built from real customer review language, comment section analysis from competitor content, and direct feedback from existing buyers.

This is NOT a demographic description. "Women 25 to 45 interested in skincare" produces generic scripts that read like marketing.

The audience insight statement captures:

- Specific pain points the audience has lived
- Specific language patterns they actually use
- Specific emotional states they experience in their own words
- Specific failed alternatives they have already tried
- Specific weight or burden they carry from the unsolved problem

### Worked example

**Bad (demographic)**:
> "Women 25 to 45 interested in skincare."

**Good (audience insight)**:
> "Women in their late 20s to early 40s who have been managing persistent hormonal acne for at least a year, have tried multiple serum routines, have been to a dermatologist at least once, are spending $80 to $150 per month on skincare without seeing the results that justify the spend, and are carrying the specific emotional weight of someone who has done everything 'right' and still wakes up disappointed by what they see in the mirror."

The level of specificity gives Claude the emotional context to write scripts that sound like real human conversation rather than marketing copy.

### How to source this input

The audience insight statement comes from real audience research, not from imagination:

- **Reddit threads** in subreddits the audience uses (r/SkincareAddiction, r/Acne, etc.)
- **Comment sections** on competitor content (especially TikTok comments on viral pieces in the niche)
- **Sales call transcripts** if available
- **Customer review mining** from the product's own reviews + competitor reviews
- **Direct survey or interview** with existing buyers

Pull verbatim phrases. The audience insight statement should include actual language patterns, not paraphrases.

For deeper persona work, route to `skills/niche-finder/SKILL.md` (the 5-Layer Persona Depth Profile that feeds this input).

## Input 2: The Product Brief

The product brief includes:

1. **The unique mechanism**: what the product does that other products do not
2. **Specific proof points** from real customers, including timelines and before-and-after language
3. **The price point and offer structure**

### The unique mechanism articulation

This matters most. Generic mechanism descriptions produce generic scripts.

**Bad**:
> "Our serum hydrates and brightens."

**Good**:
> "The serum addresses hormonal acne through a specific ingredient combination that targets the underlying cause rather than masking the symptoms."

The mechanism articulation gives Claude something specific to anchor the messaging around. Without it, Claude defaults to category-level claims that any competitor could make.

### Specific proof points

Every claim in the script needs a specific anchor. Real timelines, real numbers, real before-and-after language pulled from actual customer reviews.

**Bad**:
> "Customers see results fast."

**Good**:
> "Customers report visible reduction in active breakouts within 18 to 21 days, with most users seeing the full transformation between weeks 6 and 8."

The specific timeframes and numbers give the script credibility. Vague proof points produce vague scripts.

### Price point and offer structure

Include:
- The retail price
- Whether there is a subscription or one-time purchase
- Any current offers (bundle, trial, money-back)
- The platform where the offer lives (own site, Amazon, retail)

This anchors the CTA in the script. A $29 product needs different CTA energy than a $199 product. A subscription needs different framing than a one-time purchase.

## Input 3: The Structural Reference

An annotated transcript from a high-performing competitor reel that has been running 30+ days in the same vertical, with structural labels marking:

- Hook
- Pain section
- Mechanism bridge
- Product introduction
- Proof element
- CTA

### Why 30+ days of active spend matters

30+ days is market validation. The competitor's structure has already been tested against a real audience and proven to work. We can use that structure as a blueprint while writing entirely original language around the client's specific product and audience.

Without the structural reference, Claude generates scripts based on its training data assumptions about what AI UGC scripts should look like, which produces output that is directionally correct but not calibrated to what the current algorithm is rewarding.

### How to source the structural reference

1. **Identify a competitor reel** in the same vertical that has been running for 30+ days (visible in TikTok Creative Center or via tools like Foreplay.co, AdLibrary, etc.)
2. **Transcribe it** using a transcription tool (Otter, Descript, Whisper)
3. **Annotate the transcript** with structural labels at each beat:
   - "[HOOK]" at the first 2-3 seconds
   - "[PAIN]" at the section that establishes the audience pain
   - "[MECHANISM BRIDGE]" at the section that explains why other solutions fail
   - "[PRODUCT INTRODUCTION]" at the section that names or shows the product
   - "[PROOF]" at the section that delivers evidence
   - "[CTA]" at the closing call-to-action

The annotated transcript is the structural blueprint. Claude can replicate the proven structure with completely different language and product context.

### What the structural reference is NOT

- It is not the script you want Claude to write
- It is not a competitor whose copy you want to copy verbatim (that gets flagged for plagiarism and is creatively limiting)
- It is not a 5-day-old reel (insufficient market validation)

It is a structural blueprint. The structure has been validated. The language gets written fresh.

## Loading the 3 inputs into Claude

The 3 inputs go into the Claude session BEFORE any platform-specific prompting. The structure:

```
SYSTEM CONTEXT (loaded once per session):

# AUDIENCE INSIGHT STATEMENT
[Paste the full audience insight statement, verbatim phrases included]

# PRODUCT BRIEF
- Unique mechanism: [specific articulation]
- Specific proof points: [list of real proof points with timelines and numbers]
- Price point and offer: [retail price + offer structure]

# STRUCTURAL REFERENCE
[Paste the annotated competitor transcript with structural labels]

---

You will now generate AI UGC scripts using these 3 inputs as the foundation. Platform-specific
calibration variables will be specified for each script generation request.
```

Once loaded, the same Claude session can produce scripts for all 4 platforms, generate variations from winners, and run cross-platform analysis without reloading the brief.

## What changes between sessions and what stays constant

### Stays constant across all sessions for a product/audience pair

- Audience insight statement
- Product brief
- Structural reference

These get refreshed only when the audience evolves, the product evolves, or a new structural winner emerges that materially differs from the current reference.

### Changes per session

- Platform calibration variables (see [platform-calibration-variables.md](platform-calibration-variables.md))
- Specific concept angle (within the brief, what specific angle is being tested this week)
- Variation generation requests (when winners need to be multiplied)

## Common mistakes

### Demographic substitution

Treating "women 25-45 in skincare" as the audience insight statement. This produces generic scripts. The audience insight statement requires the emotional and behavioral specificity that demographics never capture.

### Mechanism without specificity

"Our product is unique" or "Our formulation is proprietary" is not a unique mechanism. The mechanism articulation needs to name what the product does and why it works, in language a non-marketer can understand.

### Structural reference from a 5-day-old reel

The reel needs 30+ days of active spend behind it to count as market validation. Pulling structure from a reel that just launched is gambling on whether it will sustain, not learning from validated content.

### Skipping the structural reference entirely

Without the structural reference, Claude defaults to its training data's notion of "AI UGC scripts." That output is directionally correct but generic. The structural reference is what calibrates Claude to current algorithmic dynamics.

### Loading inputs every session instead of once

Re-pasting the same brief every Claude session wastes tokens and breaks context continuity. Load the brief once at session start, then run multiple generation requests within that session.

## How this connects to the rest of the skill

The 3-input brief is the upstream of every UGC content workflow:

- **Daily production**: feeds the platform-specific calibration ([platform-calibration-variables.md](platform-calibration-variables.md)) and the master prompts ([../templates/master-prompts-by-platform.md](../templates/master-prompts-by-platform.md))
- **Variation generation**: feeds whole-script variations of winners (see master-prompts template) and component-level variations ([variation-from-winner-reel.md](../templates/variation-from-winner-reel.md))
- **Weekly intelligence**: the brief itself gets updated based on weekly cross-platform synthesis ([cross-platform-intelligence.md](cross-platform-intelligence.md))

## Cross-references

- Platform calibration variables (downstream of the brief): [platform-calibration-variables.md](platform-calibration-variables.md)
- Cross-platform intelligence (where the brief gets updated): [cross-platform-intelligence.md](cross-platform-intelligence.md)
- Master prompts that consume the brief: [../templates/master-prompts-by-platform.md](../templates/master-prompts-by-platform.md)
- Persona depth profile (deeper audience research that feeds Input 1): `skills/niche-finder/SKILL.md`
- Component-level variation (deeper variation pipeline that uses the brief): [winner-variation-pipeline.md](winner-variation-pipeline.md)
