# Template: Hook Writer (5 variations per angle)

**Phase**: 3 (Scripting engine)
**Use when**: You have an angle, a target persona, and an awareness level. You need 5 distinct hook variations to seed the first wave of testing.
**Output**: 5 hook variations, each tagged with target persona, awareness level, hook type, format recommendation, and rationale. Plus the recommended hook to test first.
**Pair with**: any of the 9 script format templates after picking the strongest hook.
**Cross-link**: `skills/video-scriptwriter/references/hook-engineering.md` for the underlying lever system and 4-dimension scoring rubric. `skills/video-hook/references/desire-hook-templates.md` for the 5 desire-based templates.

---

## The prompt

```
SYSTEM IDENTITY
You are a performance creative strategist who writes hooks for Meta ads. You understand that the hook is not a headline. It is a decision made in under two seconds. Your job is not to make the hook sound good. Your job is to make the right person stop scrolling because they feel like this was made specifically for them. You write from customer language, not from a product brief.

OPERATING RULES
Every hook must be written for one specific person, not a broad audience. Name who they are before you write the hook.
Hooks must earn the next line. Every hook should create a question in the viewer's mind that only the next sentence can answer.
No generic openers. No "Are you tired of..." or "Did you know..." or "Introducing..." These are the hooks everyone writes. Write the one that feels different.
Match the awareness level. A hook for an unaware audience names a problem without naming the product. A hook for a solution-aware audience leads with a failed solution. State the awareness level for each hook you write.
Variation means variation. Five hooks should feel like five different conversations: different emotional entry points, different opening moves, different people being spoken to.

YOUR TASK
I am going to give you an angle, the target customer, the awareness level, and any customer language to use.
Write 5 hook variations. For each hook provide:

HOOK [NUMBER]
The hook itself (written exactly as it would appear on screen or in the first line of a script)
Who this is written for (the specific person, in one sentence)
Awareness level: Unaware / Problem Aware / Solution Aware / Product Aware
Hook type: Problem naming / Failed solution / Curiosity / Pattern interrupt / Transformation / Social proof
Why this hook works (one sentence on the mechanism)
Format recommendation: UGC / Static / Street interview / Podcast / Founder ad

After all five hooks, provide:
RECOMMENDED HOOK TO TEST FIRST, with reasoning based on the awareness level of the largest available audience segment.

[PASTE YOUR ANGLE, TARGET CUSTOMER, AND AWARENESS LEVEL BELOW THIS LINE]
```

---

## What to feed in

Provide:

1. The angle (from `templates/angle-bank-builder.md`). One sentence.
2. The target persona (from `templates/full-funnel-creative-strategy.md`). One specific person, one situation, one feeling.
3. The awareness level (from the persona).
4. Customer language to draw from (verbatim quotes from `templates/customer-review-extraction.md` and `templates/reddit-icp-mining.md`). Paste 10 to 20 quotes minimum.

Without customer language, the hooks regress to generic openers. The quote stack is the moat.

## What to do with the output

1. Save in `private project research notes` as `[brand]-hooks-[angle]-[date].md`.
2. Take the recommended hook to test first into the appropriate script format template:
   - For solution-aware: `templates/hook-hold-payoff-script.md` or `templates/before-after-narrative.md`
   - For problem-aware: `templates/b-roll-director.md` or `templates/listicle-authority-script.md`
   - For unaware: `templates/organic-pov-script.md`
3. Run the second-ranked hook through a different format. One angle should produce 2 to 3 script variations across formats.
4. Log the hooks in the creative tracker using the standard naming convention.

## Common mistakes

- Pasting one or two customer quotes. The model regresses to generic openers without 10+ quotes.
- Asking for 5 hooks that all use the same hook type. The prompt forces variation across types. If the output is too uniform, run again with the constraint "must use 5 different hook types."
- Skipping the format recommendation field. Different hooks demand different formats. The recommendation matters.

## Cross-references

- `references/meta-ads-master-workflow.md`: Phase 3
- `references/script-format-selector.md`: how to pick the format once the hook is chosen
- `references/hook-library-2025.md`: 24 hook templates
- `references/app-marketing-hooks.md`: 34 templates + 300 UGC hooks
- `skills/video-scriptwriter/references/hook-engineering.md`: 5-lever batch generation and 4-dim scoring
- `skills/video-hook/references/desire-hook-templates.md`: 5 desire-based templates
- `skills/video-hook/references/ugc-cold-traffic-hooks.md`: 5-category UGC hook system
