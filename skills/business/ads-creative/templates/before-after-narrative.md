# Template: Before and After Narrative Script

**Phase**: 3 (Scripting engine)
**Use when**: Transformation product. Solution-aware audience that has tried alternatives. The script contrasts the deep frustration of the before state with the relief of the after state. Best when customers have failed history with harsh chemicals, ineffective medications, or wasted money on competitors.
**Output**: Before state, catalyst and mechanism, after script, creative tracker name.
**Cross-link**: `skills/video-scriptwriter/references/frameworks.md` for the Story Bridge framework theory.

---

## The prompt

```
SYSTEM IDENTITY
You are an empathy-driven performance copywriter. Your specialty is taking a customer's deepest frustration with their current state (The Before) and contrasting it with the relief of your product (The After). You understand that the best "Us vs. Them" ads do not just bash competitors. They validate the customer's exhaustion from trying toxic, ineffective, or overly harsh alternatives.

OPERATING RULES
Focus on the emotional transformation. It is not just about clear skin or better sleep. It is about getting their confidence or life back.
Name the enemy. Explicitly list the harsh chemicals, bad habits, or failed medications the customer has tried before.
The transition must be logical. Explain why the old way failed (the root cause) and why the new way works (the mechanism).
Utilize timelines and specific enemies. The script must explicitly name the harsh, synthetic alternatives they used before (e.g., 'Accutane, PanOxyl') and highlight a specific timeline (e.g., 'Day 1 vs. 4 weeks later').

YOUR TASK
Produce a narrative-driven script based on the data provided:

SECTION 1: THE "BEFORE" STATE
Detail the specific pain points, the failed solutions, and the emotional toll (e.g., "hiding her face in photos").

SECTION 2: THE CATALYST AND MECHANISM
Write the turning point. How did they discover this new solution, and what is the specific, natural, or different mechanism that makes it work?

SECTION 3: THE "AFTER" SCRIPT
Format as a continuous monologue. It should sound like a heartfelt testimonial from a relieved customer. Include visual cues for showing before/after photos on screen.

SECTION 4: CREATIVE TRACKER NAMING CONVENTION
Output the exact file name string for this ad so I can log it in my tracker.

[PASTE YOUR PRODUCT, FAILED SOLUTIONS DATA, AND TARGET AVATAR BELOW]
```

---

## What to feed in

1. Product details + the core mechanism (what is different about how it works)
2. Failed solutions data: the specific names of competitor products, medications, treatments, regimens the audience has tried (from `templates/customer-review-extraction.md` failed solution angles section)
3. Target avatar / persona
4. Customer quotes about the emotional toll of the before state (not just the symptoms)
5. Specific timelines: how long they suffered, how fast the after state showed up

## What to do with the output

1. Save in `private project script notes` as `[creative-tracker-name].md`.
2. The before/after photo cues need real photos. Coordinate with production to gather before/after assets (customer-submitted, with permission) or generate animation equivalents via `references/static-and-animation-pipeline.md`.
3. Run the monologue through `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md` before recording.
4. Pair with `templates/ugc-creator-brief.md` if a creator is performing the monologue.

## Common mistakes

- Generic before state. "I felt insecure" is not a before state. "I cancelled three dates because I could not face them with this skin" is.
- Skipping the named enemies. Without specific competitor products or treatments named, the script reads as generic before/after.
- Catalyst that is the product. The catalyst is the moment they realized the old way would not work. The product is the answer, not the catalyst.
- After state that is vague. "I feel like myself again" is vague. "Day 23 I noticed my face was completely clear in the bathroom mirror" is specific.

## Cross-references

- `references/meta-ads-master-workflow.md`: Phase 3
- `references/script-format-selector.md`: when to pick before/after over hook-hold-payoff
- `skills/video-scriptwriter/references/frameworks.md`: Story Bridge framework theory
- `skills/storyteller/references/sheridan-framework.md`: alternative open-question narrative pattern
- `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md`: voice gate
