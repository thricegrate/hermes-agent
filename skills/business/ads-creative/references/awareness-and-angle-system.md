# Awareness and Angle System

The framework that organizes Phase 2 of the Meta Ads master workflow. Eugene Schwartz's 5 awareness levels, the angle bank structure, persona architecture, and the 90-day creative roadmap shape.

For the historical theory deeper than this file goes, see `hormozi-goated-ads.md` (which adapts Schwartz). For the templates that operationalize this framework, see the templates folder.

## The 5 awareness levels

| Level | What the customer knows | What they need to hear | Hook entry |
|---|---|---|---|
| Unaware | No problem named | Name the problem in their words | Lifestyle moment, POV, pattern interrupt |
| Problem Aware | Has the problem, no solution named | Validate the frustration, mention the failed solutions they have tried | Failed solution open, pain-point amplification |
| Solution Aware | Knows a category of solutions exists, has not picked one | Differentiate the mechanism | "Here is why [common solution] does not work" |
| Product Aware | Knows your product exists, has not bought | Handle the objection that is stopping them | Risk reversal, social proof at scale, guarantee |
| Most Aware | Knows the product, ready to buy | Push the offer over the line | Urgency, scarcity, exclusive offer |

Source: Eugene Schwartz, *Breakthrough Advertising*. Adapted in `hormozi-goated-ads.md`.

## Why awareness mapping matters

The single biggest reason ad accounts cap out: every ad lives at one awareness level (usually product-aware). When the audience at that level is exhausted, frequency climbs, CPA creeps, and there is no relief. Adding more ads at the same level does not help. The relief comes from creative one level higher.

A healthy Meta ad account has at least 2 fresh angles at every awareness level at all times. The top of the funnel feeds the middle. The middle feeds the bottom.

## Awareness levels and Andromeda Entity IDs are orthogonal axes

Awareness level is one axis. The Andromeda 4-dimension framework (persona, format, environment, pain/benefit) is another. Both matter, and they are not the same dimension.

Two ads can target the same awareness level (both solution-aware) and still produce different Entity IDs because their personas, environments, and formats differ. Two ads can produce the same Entity ID (same persona + format + environment + pain) while targeting different awareness levels through hook variation only.

The healthy account distributes across both axes:

- Across the 5 awareness levels (Unaware -> Most Aware)
- Across at least 8 to 12 distinct Entity IDs

When tagging an angle in the angle bank, include both:

- Awareness level (Unaware / Problem Aware / Solution Aware / Product Aware / Most Aware)
- 4-dimension fingerprint (persona + format + environment + pain/benefit)

For the Andromeda layer in depth, see `andromeda-algorithm-architecture.md`.

## The angle bank structure

An angle is not a hook. An angle is the single core idea the entire ad is built around. The hook is the opening move of one specific execution. A good angle can produce 50 different hooks.

Every angle in the bank gets tagged:

- **Angle name**: short internal label (not a hook)
- **Source**: direct customer quote
- **Core idea**: one sentence
- **Target persona**: one specific person in one specific situation (not a demographic)
- **Awareness level**: which of the 5 levels this angle speaks to
- **Emotional trigger**: frustration, guilt, relief, embarrassment, pride, aspiration, fear, other
- **Best-fit script formats**: which of the 10 formats serve this angle
- **Hook direction**: one example hook
- **Creative priority**: high / medium / low
- **Status**: fresh (not yet tested) / active (running) / fatigued (needs resting)

`templates/angle-bank-builder.md` produces this tagged library from Phase 1 customer data.

## Persona architecture

A persona is not a demographic. "Women 35-45, household income $75K+" is not a persona. It is a media-buying instruction.

A persona is one specific person in one specific situation with one specific feeling. For example: "Maria, 39, two kids, has spent $400 on three different acne products in the last year, all of them stung her skin, now she stares at the mirror at 11pm scrolling Reddit threads about hormonal acne."

Most Meta ad accounts need 3 to 5 distinct personas. Each persona maps to one awareness level cluster. The angle bank serves the personas, not the demographics.

`templates/full-funnel-creative-strategy.md` produces the persona architecture for a brand.

## The 90-day creative roadmap

Phase 1 (Weeks 1 to 4): Foundation. Test the priority angles first. Generate the minimum viable creative volume per awareness level. Look for signal, not winners.

Phase 2 (Weeks 5 to 8): Validation. Read the Phase 1 data. Scale what is working. Kill what is not. Brief the second wave with refined angles.

Phase 3 (Weeks 9 to 12): Compounding. Iterate winners into new formats and hooks. Port proven angles to new personas. By the end of Phase 3 the account should have a self-feeding creative library where every dollar spent generates signal that makes the next brief better.

`templates/full-funnel-creative-strategy.md` produces the full 90-day roadmap with phase-specific priorities.

## Creative tracker naming convention

Every ad gets a name that sorts by every dimension. Use this format:

`[Persona]_[Angle]_[Concept]_[Format]_[AwarenessLevel]_[HookType]`

Example: `Insomnia_FirstTimeSinceKid_TalkingHead_UGC_SolutionAware_PreviousFailed`

After 30 days of spend, the tracker lets you rank ads by every dimension simultaneously. The format is the same dimension you tested. The awareness level is the same level you targeted. The hook type is the same emotional trigger. Pivots become legible.

Every template in `ads-creative/templates/` ends with this naming convention so the user pastes the file name directly into their tracker.

## The frequency diagnostic

Frequency is a health metric, not a vanity stat. Read it as follows:

- Frequency 2.0 to 4.0: healthy distribution at the current awareness level
- Frequency above 5.0: audience at this level is exhausted, expand to the next level up
- Frequency below 2.0: not enough impressions to read signal, give it more time

When frequency climbs above 5.0 at a specific awareness level and CPA simultaneously creeps, the diagnosis is almost always that the audience at that level is exhausted. The fix is not new creative at the same level. The fix is new creative one level up.

## Common mistakes

1. Treating "awareness level" as a copy variable instead of an audience variable
2. Trying to make one ad speak to all 5 levels (none of them feel addressed)
3. Building an angle bank without source quotes (the language drifts back to corporate speak)
4. Persona descriptions that are actually demographic descriptions
5. The 90-day roadmap that has no kill criteria (everything stays "in test" forever)

## Cross-references

- `meta-ads-master-workflow.md`: the 5-phase orchestration this fits inside
- `hormozi-goated-ads.md`: Schwartz pyramid theory in depth
- `static-headline-formulas.md`: awareness-level targeting for static headlines
- `meta-creative-vault.md`: original angle bank and full-funnel prompts
- `templates/angle-bank-builder.md`, `templates/full-funnel-creative-strategy.md`, `templates/awareness-level-mapping.md`: the three templates that operationalize this framework
