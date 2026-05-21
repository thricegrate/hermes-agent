# Andromeda Algorithm Architecture

The algorithmic foundation that every modern Meta ad account lives inside. Most accounts plateau between $300K and $500K per month not because the creative is bad but because Andromeda reads all the creative as the same single ad.

This is the architecture-level guide. The creative-level workflow that builds on top of it lives in `meta-ads-master-workflow.md`. If you only have time for one foundational reference, read this one first.

## The 300-millisecond problem

When someone opens Instagram, Meta has roughly 300 milliseconds to decide what ad to serve. Less than a blink. Across billions of active ads at any moment.

A full auction across billions of ads in 300ms does not exist as a piece of engineering. Meta would melt the servers running it. So Meta split the system into two stages.

### Stage 1: Retrieval (Andromeda)

The gatekeeper. Scans billions of ads and narrows them down to roughly 1,000 candidates in milliseconds.

Uses:
- Semantic similarity between ads
- User intent (current behavioral cluster)
- Visual analysis (scene, actor, framing, palette)
- Social proof signals
- Behavioral clustering

### Stage 2: Ranking

The auction most media buyers already know. Among the ~1,000 retrieved candidates, the ranker calculates:
- eCPM
- Predicted CTR
- Conversion probability
- Bid competitiveness

Then selects the winner.

The implication: Andromeda decides whether your ad even gets a ticket to the auction. Targeting strategy, bid level, and creative quality only matter if you survive Stage 1.

## What an Entity ID actually is

Andromeda has to process billions of ads quickly. So it clusters ads using a semantic fingerprint.

It analyzes:
- Visuals (scene, actor, framing, color)
- Narration
- Copy
- Pacing
- Edit rhythm
- Scene composition
- Audio structure

If multiple ads score above a similarity threshold across those dimensions, Andromeda collapses them into one Entity ID. That single Entity ID gets one auction ticket.

If 50 ads sit inside one Entity ID, they are competing for one slot. Most of them never see daylight.

### The fake-diversity trap

The trap most accounts fall into: producing 50 ads that vary only the cosmetic surface.

Same actor + same setting + same edit rhythm + same framing + same emotional entry point, then swap:
- Hooks
- Captions
- Subtitles
- Colors
- Opening text overlays

Andromeda reads this as one creative with cosmetic variation. One Entity ID. One auction ticket.

The result:
- CPMs rise (the system has no fresh creative to deploy)
- Reach compresses (the same Entity ID hits the same users)
- Spend cannibalizes itself (multiple ads bid against each other)
- Scale stalls

The account "runs out of audience" but the real problem is the account has run out of Entity IDs.

## The hierarchical behavioral tree

Andromeda organizes ads into behavioral trees. Each user has a current position in the tree based on recent behavior.

Example tree for a fitness-interested woman, age 28:

```
Female, 28, fitness-interested
├── Fitness Products
│   ├── Athleisure
│   ├── Nutrition
│   ├── Supplements
│   ├── Yoga
│   ├── Running
│   └── Recovery
```

Each branch contains Entity IDs.

When Andromeda predicts current intent, it cuts entire branches from consideration for that impression. If the user is currently in a "Yoga" behavioral cluster, your "Recovery Supplement" branch may never reach the auction. Even if your ad is excellent.

The risk: if all your ads live on one branch because they share:
- Same benefit
- Same persona
- Same structure
- Same environment
- Same narrative style

then one branch cut removes your entire account from that auction opportunity.

The fix is not to spam more variants of the same branch. The fix is to operate on multiple branches at once so the account survives any single branch cut.

## The 4-dimension framework

To generate distinct Entity IDs, every batch of creatives needs variation across at least 2 of these 4 dimensions:

### 1. Format

The structural pattern of the ad. Examples:
- Podcast clip (two-actor)
- POV creator
- Pharmacist authority
- Street interview
- Static comparison
- Carousel
- Long-form yapper (3-4 min)
- Skit
- Walk-and-talk
- B-roll + voiceover
- Silent / text-only
- Before/after narrative

Format is usually the easiest dimension to vary first because the script structure changes drive everything downstream (setting, framing, edit rhythm).

### 2. Persona

Different customer life situations. Not demographics. Examples:
- First-time mom
- Exhausted founder
- Hormone-conscious woman in her 30s
- Men 40+ struggling with intimacy
- Fitness-focused recovery buyer
- Sleep-deprived shift worker

The persona changes who is on camera, what they wear, what setting feels native, what language they use.

### 3. Environment

Where the ad visually takes place. Examples:
- Kitchen
- Gym
- Studio
- Pharmacy
- Bathroom
- Supermarket
- Car
- Bedroom
- Outdoor / street
- Office / desk

Environment changes the scene composition, lighting, palette, and ambient audio. Andromeda's visual analysis weighs this heavily.

### 4. Pain / Benefit

The pain or desire entry point. Examples:
- Sleep quality
- Energy
- Relationship confidence
- Hormone balance
- Recovery
- Mental clarity
- Post-workout performance
- Skin clarity
- Digestion

Pain / benefit changes what the script names in the first 3 seconds, which is what Andromeda's semantic analysis reads as the ad's "topic."

## Batching for real diversity

Real diversity is not "5 versions of the same ad with different hooks." Real diversity is multiple batches that each vary at least 2 of the 4 dimensions.

Example: 4 batches that produce 4 different Entity IDs:

```
Batch 1
- Persona: busy moms
- Pain/benefit: morning energy
- Environment: kitchen
- Format: POV creator

Batch 2
- Persona: men 40+
- Pain/benefit: relationship confidence
- Environment: podcast setup
- Format: two-actor expert

Batch 3
- Persona: wellness-curious women
- Pain/benefit: hormone balance
- Environment: pharmacist studio
- Format: authority

Batch 4
- Persona: fitness-focused buyers
- Pain/benefit: post-workout recovery
- Environment: gym
- Format: street interview
```

Now you have:
- Multiple branches the account lives on
- Multiple semantic signatures
- Multiple Entity IDs
- Multiple auction tickets

When the user's behavioral cluster shifts (kitchen morning -> gym evening), at least one of your branches is still in consideration.

## The fake diversity audit

Run this filter on the existing account. The audit is fast and the result is uncomfortable but useful.

Strip away from every running ad:
- Hook variations
- Font changes
- Subtitle swaps
- Music swaps
- CTA tweaks

Mute every video. Watch them silently.

Ask: would these still look like different ads?

If the answer is no, the account has fake diversity. The 50 ads in the account are collapsing into 2 to 4 Entity IDs.

Then ask for each cluster:
- Do they target different pains?
- Different personas?
- Different environments?
- Different formats?
- Different emotional entry points?

If most answers are no, the account needs a structural rebuild starting at Batch 1 of a fresh 4-dimension framework.

For the ready-to-paste audit prompt, see `templates/fake-vs-real-diversity-audit.md`.

## The strategic shift: narrow targeting is dead

### The old playbook (pre-Andromeda)

- Narrow targeting
- Lookalikes
- Interest stacks
- Demographic refinement
- Hundreds of similar creatives

This worked when Meta's auction was simpler and creative diversity mattered less because targeting did the work.

### The new playbook (Andromeda-native)

- Broad targeting + high Entity ID diversity
- Let creative determine the audience

Andromeda already interprets the semantic meaning of every creative. When narrow targeting layers on top, the two systems conflict.

Example of the conflict:
- Your creative semantically reads as "yoga recovery"
- Your targeting says "running enthusiasts only"

The system either overrides the targeting, misplaces impressions, or suppresses delivery entirely. Either way, performance is unstable and unreadable.

Broad targeting removes the friction. The creative becomes the targeting layer. Andromeda places the right creative in front of the right behavioral cluster automatically. Your job is to ensure you have enough Entity IDs to claim space across multiple clusters.

## The 14-day operating cycle

Every 14 days:

### Step 1: Audit fake diversity

Count Entity IDs, not ads. Use `templates/fake-vs-real-diversity-audit.md`.

If the account has 100 ads but 4 Entity IDs, the account is constrained. The fix is not more ads. The fix is structural batching.

### Step 2: Build 10 to 15 structurally distinct concepts

Each concept varies at least 2 of the 4 dimensions (persona, format, environment, pain/benefit). Use `templates/entity-id-batch-builder.md`.

### Step 3: Run broad targeting

No interest stacks. No narrow lookalikes. Let Andromeda place the creative.

### Step 4: Review winning Entity IDs

Not winning hooks. Winning structures.

Which persona + format + environment + pain combination is producing the lowest CPA at the highest scale? That is the winning Entity ID structure.

### Step 5: Scale winners carefully

Produce variations of the winning structure while maintaining structural diversity. The variations must be structurally distinct enough to spawn new Entity IDs rather than collapse into the winning one. Vary at least 1 of the 4 dimensions per variation.

### Step 6: Add new branches continuously

New personas. New environments. New formats. New benefits. Every cycle expands the branches the account exists on inside the behavioral tree.

This is how the account compounds. Most accounts do not lose because the ads are bad. They lose because Andromeda thinks all the ads are the same.

## How Andromeda affects the creative process upstream

If the account architecture is broken at the Entity ID level, no creative quality improvement will fix it. The first task in any Meta ads engagement is the diversity audit. Then the structural rebuild. Then individual creative quality.

The implication for the creative workflow:

| Phase | What it does | Andromeda layer |
|---|---|---|
| Phase 1 (customer mining) | Surfaces personas, pain points, language | Provides inputs for the persona and pain/benefit dimensions |
| Phase 2 (angle bank) | Tagged angle library | Each angle should be tagged with its 4-dimension fingerprint, not just awareness level |
| Phase 3 (scripting engine) | 10 script formats | Format is one of the 4 dimensions; pick formats that produce structurally distinct outputs |
| Phase 4 (static + animation) | NB2 batching + AI animation | Environment and format dimensions; AI animation styles (Lego, Pixar, claymation) create distinct semantic signatures |
| Phase 5 (learning loop) | Winner breakdowns + competitor gaps | Read winners as Entity ID structures, not as individual ads |

The 5-phase Meta Ads master workflow assumes the Andromeda architecture underneath. Without the architectural foundation, the creative workflow produces 50 ads that collapse into 4 Entity IDs and never compound.

## What "good" looks like

A healthy Andromeda-proof account has:

- 8 to 12+ distinct Entity IDs at any time
- Coverage across at least 4 of the major branches in the behavioral tree (different personas + environments + benefits)
- Broad targeting (no interest stacks, no narrow lookalikes)
- A 14-day cycle that adds 2 to 4 new Entity IDs per cycle
- Performance reads at the Entity ID level, not the individual ad level
- A library of "winning structures" documented so iterations spawn new Entity IDs rather than recreate old ones

A broken account has:
- 50 to 200 ads collapsing into 2 to 4 Entity IDs
- 80% of spend concentrated on one branch
- Narrow lookalike targeting fighting the semantic targeting Andromeda already does
- "Iteration" that swaps hooks and CTAs without changing the 4 dimensions
- Performance that creeps without obvious cause (the cause is auction starvation)

## Common mistakes

1. Treating "100 ads" as a diversity metric. The metric is Entity IDs, not ads.
2. Running hook variation tests inside one Entity ID. You learn nothing about Andromeda's behavior because the auction does not care which hook won; it cares which Entity ID won.
3. Layering narrow targeting on top of broad creative. The semantic targeting Andromeda does already serves the role; narrow targeting creates conflict.
4. Scaling winning ads by producing 10 more versions of the same actor + setting + format. The new versions get absorbed into the winning Entity ID and the account does not grow.
5. Skipping the audit step in the 14-day cycle. Without the count, the team produces from feel and the account decays.

## Cross-references

- `meta-ads-master-workflow.md`: the 5-phase creative workflow that lives on top of this architecture
- `awareness-and-angle-system.md`: awareness levels are orthogonal to Entity IDs; both axes matter
- `script-format-selector.md`: format is one of the 4 dimensions; the decision tree there directly drives Entity ID diversity
- `static-and-animation-pipeline.md`: animation styles (Lego, Pixar, claymation) create distinct semantic signatures, useful for Entity ID expansion
- `learning-loop-prompts.md`: winner reverse-engineering should read winners as Entity ID structures
- `templates/fake-vs-real-diversity-audit.md`: ready-to-paste audit prompt
- `templates/entity-id-batch-builder.md`: ready-to-paste batch builder
- `skills/ads-strategy/SKILL.md`: targeting doctrine has shifted under Andromeda; see notes there
- `skills/ads-strategy/references/audience-targeting.md` + `retargeting-lookalike-playbook.md`: legacy targeting playbooks that need reading through the new doctrine
- `skills/ugc-production/SKILL.md`: the 14-day cycle complements the production orchestration
