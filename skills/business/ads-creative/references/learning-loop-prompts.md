# Learning Loop Prompts

Phase 5 of the Meta Ads master workflow. The discipline that separates accounts that scale to $1M/mo from accounts that find one winner and stall.

Two templates, run weekly:

1. `templates/winning-ad-breakdown.md`: reverse-engineer every winning ad into transferable principles before the ad dies.
2. `templates/competitor-angle-analysis.md`: map the category, find the gap, claim the unexploited position.

## Why most accounts plateau

The pattern that kills mid-size accounts:

- Week 1: find a winner. CPA is great.
- Week 2-4: scale the winner. CPA holds.
- Week 5-6: CPA starts creeping. Frequency at 5+.
- Week 7: winner is dead. CPA is unsustainable.
- Week 8: start over with new creative. Lose 2-3 weeks finding the next winner.

The 2-3 weeks of lost ground compound. The account never gets ahead. Every month is recovery from the last winner dying.

The fix is not finding more winners. The fix is making winners survive.

## The winner survival principle

A winning ad has DNA: a structural pattern (hook + angle + format), a psychological mechanic (which desire or fear it activates), a language pattern (which customer phrases do the heavy lifting), and an awareness-level fit.

When the ad dies, the DNA does not. If you extract the DNA before the ad dies, you can produce 5-10 variations that carry the proven elements forward.

`templates/winning-ad-breakdown.md` runs the extraction. Output:

- Structural diagnosis (hook, angle, awareness level, format, opening loop)
- Psychological mechanics (core desire/fear, emotional journey, objections handled, trust signals)
- Language analysis (which phrases work hardest, customer quotes used, the single most powerful line)
- 5 minimum transferable principles ("this works because X, future briefs should Y")
- Iteration roadmap (same hook new format, same format new hook, same angle new awareness level, fatigue signals to watch, the first iteration to test)

Run this template on every ad that hits the winner threshold. Before scaling, not after. Before the data is contaminated by fatigue.

## What counts as a winner

Two thresholds:

- Volume threshold: 1,000+ impressions or $200+ spend (whichever comes first)
- Performance threshold: 1.5x to 2x the account's median CPA, or hook rate above 25% on Reels placements

Below those thresholds, the result is noise. Above them, the DNA is worth extracting.

## The competitor analysis discipline

Most competitor "analysis" is screenshot collecting. That is not analysis. That is hoarding.

Real competitor analysis maps:

- What angle does every competitor in the category share?
- What awareness level is the entire category clustering at?
- What customer desire is the category consistently failing to address?
- Which competitor ads have been running 90+ days (the proven signal)?
- Which competitor ads launched and disappeared in under 30 days (the failed tests)?

The output is a gap map. Three to five clear positions nobody is running. Each gap is a brief direction.

`templates/competitor-angle-analysis.md` runs this. Output:

- Category angle map (every competitor ad tagged with angle, awareness level, hook type, creative maturity)
- Category patterns (the shared angles, the saturated awareness level, the invisible messaging)
- Gap analysis (3-5 gaps with the brief direction each points to)
- Differentiation strategy (the single most defensible position with the awareness level to target and the hook to lead with)

For the Meta Ad Library extraction workflow that feeds the competitor input (which ads are running, for how long, with what creative), cross-link to `skills/ads-analyst/SKILL.md`.

## Running the loop weekly

Monday morning, every week:

1. Pull the previous 7 days of performance data across all running ads.
2. Identify any ad that crossed the winner threshold for the first time.
3. Run `winning-ad-breakdown.md` on each new winner. Add the transferable principles to a running file. Add the iterations to the brief queue.
4. Pull the previous 30 days of competitor ad library data.
5. Run `competitor-angle-analysis.md` on the category.
6. Update the angle bank in `awareness-and-angle-system.md` with new fresh angles uncovered.
7. Brief the next 5 ads from the iteration queue and the gap-driven angles.

The loop is the difference between an account that compounds and an account that resets every month.

## Connecting the loop back to Phase 2

Every output from this phase updates Phase 2 inputs:

- Winner DNA -> new tagged angles in the angle bank
- Competitor gaps -> new fresh angles at underserved awareness levels
- Fatigue signals -> retire angles from the active set
- Iteration roadmap -> first three briefs for next week's production

The angle bank gets refreshed weekly. The roadmap gets updated. The brief queue is always seeded from real performance signal, not gut feel.

## Common mistakes

1. Running the winner breakdown after the ad dies (too late, fatigue contaminates the analysis)
2. Skipping the competitor analysis when business is good (the gap closes while you are not watching)
3. Documenting winners but not iterating them (the principles sit in a file and the account does not benefit)
4. Treating competitor analysis as a one-time exercise (the category shifts faster than you think)
5. Confusing "more winners" with "better account" (10 winners that died in 2 weeks each is worse than 3 winners with documented DNA that fed 30 iterations)

## Cross-references

- `meta-ads-master-workflow.md`: Phase 5 fits inside the 5-phase workflow
- `awareness-and-angle-system.md`: where new winners and gaps update the angle bank
- `meta-creative-vault.md`: original winning-ad-breakdown prompt
- `templates/winning-ad-breakdown.md`: ready-to-paste winner extraction
- `templates/competitor-angle-analysis.md`: ready-to-paste category gap map
- `skills/ads-analyst/SKILL.md`: Meta Ad Library extraction that feeds competitor input
- `skills/ads-strategy/SKILL.md`: weekly performance reporting that feeds winner input
