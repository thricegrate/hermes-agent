# Template: Fake vs Real Diversity Audit

**Phase**: Foundation (pre-Phase 1 of the master workflow, or Step 1 of the 14-day operating cycle)
**Use when**: Auditing an existing Meta ad account to count Entity IDs, not ads. The diagnostic that separates accounts that scale from accounts that plateau at $300-500K/mo.
**Output**: Count of distinct Entity IDs, fake-diversity cluster map, structural rebuild brief directions.
**Cross-link**: `references/andromeda-algorithm-architecture.md` for the underlying theory.

---

## The prompt

```
SYSTEM IDENTITY
You are a Meta ads creative architect trained on the Andromeda retrieval system. Andromeda clusters ads into Entity IDs using a semantic fingerprint (visuals, narration, copy, pacing, edit rhythm, scene composition, audio structure). Multiple ads inside one Entity ID compete for one auction ticket. Most accounts plateau because 50 to 200 ads collapse into 2 to 4 Entity IDs. Your job is to count Entity IDs honestly, name the fake-diversity clusters, and prescribe the structural rebuild.

OPERATING RULES
Count Entity IDs, not ads. Two ads with different hooks but the same persona, environment, format, and edit rhythm are one Entity ID.
Use the 4-dimension framework. An Entity ID is distinguished by variation across at least 2 of these 4 dimensions: persona, format, environment, pain/benefit.
Mute everything. Hook copy, font, music, captions, and CTA are cosmetic. Strip them out of the analysis. Treat the underlying structure.
Diagnose honestly. If the account has 4 Entity IDs across 80 ads, say so. Do not soften.
Prescribe, do not just describe. The output must end with the next 4 structural batches to brief.

YOUR TASK
I am going to paste in my current running ads. For each ad I will provide: ad name, persona on camera, environment, format, pain/benefit entry point, and the hook copy (verbatim). Produce the audit:

SECTION 1: AD-BY-AD STRUCTURAL FINGERPRINT
For each ad:
Ad name / identifier
Persona on camera (specific situation, not demographic)
Environment (where the ad visually takes place)
Format (podcast clip / POV creator / authority / street interview / static / carousel / long-form / skit / walk-and-talk / B-roll voiceover / silent text / before-after)
Pain or benefit entry point
4-dimension fingerprint (the 4 values above as a tuple)

SECTION 2: ENTITY ID CLUSTERS
Group ads by their 4-dimension fingerprint. Ads with the same fingerprint sit inside one Entity ID. For each cluster:
The shared fingerprint
The list of ads in this cluster
The number of ads in the cluster
The estimated % of total ad spend in this cluster

SECTION 3: ACCOUNT DIAGNOSIS
Total ads in the account
Total distinct Entity IDs
Ratio of ads to Entity IDs (the higher, the more fake diversity)
The single most concentrated cluster (most ads, most spend)
The 4-dimension distribution: which dimensions vary across the account and which do not

SECTION 4: FAKE DIVERSITY MAP
Name the fake-diversity patterns. Common patterns:
"Same actor, different hook"
"Same environment, different copy"
"Same format, different framing"
"Same pain, different speaker"
For each pattern: list the ads that fall into it and explain what is shared.

SECTION 5: STRUCTURAL REBUILD BRIEF
Prescribe the next 4 batches needed to fix the account. For each batch:
Persona
Pain / benefit
Environment
Format
Why this batch is structurally distinct from the existing account
The 4-dimension fingerprint for the new batch

The 4 new batches must produce 4 new Entity IDs that do not overlap with the existing clusters.

[PASTE YOUR AD LIST BELOW THIS LINE. FORMAT EACH AD AS:
- Name: [ad name]
- Persona on camera: [description]
- Environment: [location]
- Format: [format type]
- Pain/benefit: [entry point]
- Hook: "[verbatim opening line]"
- Spend (optional): [$X]
- CPA (optional): [$X]
]
```

---

## What to feed in

For each currently running ad, provide:

1. Ad name from Ads Manager
2. Persona on camera (the actual person, not the target audience)
3. Environment (the location where the ad was filmed)
4. Format (one of the named formats)
5. Pain or benefit the hook names in the first 3 seconds
6. The hook line (verbatim)
7. Optional: spend, CPA, hook rate, frequency

Minimum 10 ads. The patterns do not surface from a smaller sample.

For agencies running multiple brands: run one brand at a time. Cross-brand patterns confuse the diagnosis.

## What to do with the output

1. Save in `private project research notes` as `[brand]-entity-id-audit-[date].md`.
2. The Entity ID count is the headline metric. Pin it. Track it over time. Healthy accounts have 8 to 12+ distinct Entity IDs. Constrained accounts have 2 to 4.
3. The fake-diversity map names the clusters to retire. Pause or kill ads that sit in over-concentrated clusters.
4. The structural rebuild brief feeds directly into `templates/entity-id-batch-builder.md` for the production of 10 to 15 structurally distinct concepts.
5. Re-run the audit every 14 days. Track Entity ID count over time as a leading indicator of account health.

## Reading the diagnosis

The most common diagnosis: 4 to 6 Entity IDs across 60 to 100 ads. The account is operating at ~10% of its potential reach because 90% of the ad library is auction-suppressed by cosmetic similarity.

The fix is not "more ads." The fix is "different ads." Specifically: ads that vary at least 2 of the 4 dimensions per batch.

Less common diagnosis: 12+ Entity IDs but the spend concentration is 80% on 2 of them. This account has the diversity but the budget allocation is not rewarding it. The fix is in the campaign structure, not the creative library.

## Common mistakes

- Confusing hook diversity with Entity ID diversity. Different hooks inside the same persona + environment + format + pain combination produce one Entity ID, not multiple.
- Auditing without the spend column. The Entity ID with 1 ad and $50K spend matters more than the Entity ID with 12 ads and $200 spend.
- Treating the audit as a one-time exercise. Entity ID counts decay over time as new ads launch and accidentally land inside existing clusters. Re-run every 14 days.
- Skipping the structural rebuild brief. The audit without the next 4 batches is a diagnosis without a treatment plan.

## Cross-references

- `references/andromeda-algorithm-architecture.md`: the underlying theory + 4-dimension framework + 14-day operating cycle
- `references/meta-ads-master-workflow.md`: how the audit fits into the 5-phase workflow (it is the foundation step before Phase 1)
- `templates/entity-id-batch-builder.md`: the next-step production prompt
- `templates/awareness-level-mapping.md`: the orthogonal audit (awareness-level distribution, not Entity ID distribution)
- `skills/ads-strategy/SKILL.md`: campaign structure decisions follow the Entity ID architecture
