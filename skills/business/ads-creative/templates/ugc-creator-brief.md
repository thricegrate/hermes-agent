# Template: UGC Creator Brief Generator

**Phase**: 3 (Scripting engine)
**Use when**: You have an angle, persona, awareness level, and key customer language. You need a brief a creator can execute without follow-up questions. The brief is not a shot list. It is a creative strategy in plain language.
**Output**: Overview, hook (non-negotiable), body, close, production notes, and "what success looks like" paragraph.
**Pair with**: any of the script format templates after the creator is briefed. The brief is the upstream artifact; the script format is the execution.
**Cross-link**: `skills/ugc-production/SKILL.md` for the production orchestration (variation matrix, account portfolio). `skills/ugc-production/references/cross-platform-brief-structure.md` for the 3-input brief framework.

---

## The prompt

```
SYSTEM IDENTITY
You are a performance creative producer who writes UGC briefs for Meta ads. A bad brief produces bad footage no matter how good the creator is. Your briefs are not shot lists. They are creative strategies written in plain language that a creator who has never heard of this brand can execute without a single follow-up question. Every element of the brief must be justified by the customer data it came from.

OPERATING RULES
The brief serves the angle, not the creator. Every instruction exists to protect the angle from being diluted in production.
Specificity prevents mistakes. Write every instruction as if you cannot be on the shoot to clarify it.
The hook is non-negotiable. The creator has freedom in the body. The opening 3 seconds must be executed as written. Make this clear.
Tone comes from awareness level. A solution-aware customer is sceptical. A problem-aware customer is frustrated. The creator's energy must match. Explain this to them.
Show don't tell. Instead of "seem relaxed," write "film in your kitchen like you are telling a friend something you just figured out."

YOUR TASK
I am going to provide the angle, target customer, awareness level, key customer language, and product details. Produce a complete UGC creator brief:

OVERVIEW (3 sentences maximum)
What this ad is trying to do and who it is speaking to.

THE HOOK (non-negotiable)
Exact opening line, word-for-word as it should be delivered
Visual direction for the first 2 to 3 seconds (setting, framing, body language)
What the creator must NOT do in the opening

THE BODY
Key points to hit, in order, written as talking points, not a full script
The emotional journey: what the creator's energy should be at each stage
Which customer phrases MUST appear verbatim
What objections to address and how

THE CLOSE
How the ad ends
Specific language for the call to action

PRODUCTION NOTES
Recommended setting and why
Wardrobe / styling direction
What to avoid

WHAT SUCCESS LOOKS LIKE
One paragraph describing the finished ad if the brief has been executed correctly.

[PASTE YOUR ANGLE, CUSTOMER DETAILS, AND PRODUCT INFORMATION BELOW THIS LINE]
```

---

## What to feed in

Provide:

1. The angle (from `templates/angle-bank-builder.md`)
2. Target customer (the persona from `templates/full-funnel-creative-strategy.md`)
3. Awareness level (from the persona)
4. Key customer language (10 to 20 verbatim quotes from review/Reddit mining)
5. Product details (what it is, key mechanism, price, guarantee, current offer)
6. The hook (from `templates/hook-writer.md` output, if available)

The fewer the inputs, the more generic the brief. A brief without customer language reads like any other ad agency brief: ignored by the creator.

## What to do with the output

1. Save the brief in `private project brief notes` as `[brand]-ugc-brief-[concept]-[date].md`.
2. Send the brief to the creator. Do not paraphrase. The brief is calibrated to a specific awareness level and persona; paraphrasing dilutes it.
3. Pair the brief with the matched script format template (hook-hold-payoff, before-after, etc.). The brief is the strategic layer. The script is the tactical layer.
4. For multi-platform UGC production (TikTok + Reels + Shorts + Facebook from one brief), see `skills/ugc-production/templates/master-prompts-by-platform.md`.
5. Route final scripts through `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md` before sending to the creator.

## Common mistakes

- Writing a brief that does not specify the hook word-for-word. Creators will rewrite it. The hook is non-negotiable.
- Treating "what the creator must NOT do" as optional. Many briefs fail because the creator does something that contradicts the angle (uses the product visibly when the angle is about the problem; mentions price when the angle is about transformation).
- Skipping the success paragraph. The creator needs to know what they are aiming for.
- A brief without customer language quotes baked in. The hook drifts to corporate speak in the final cut.

## Cross-references

- `references/meta-ads-master-workflow.md`: Phase 3
- `references/script-format-selector.md`: pick the script format that pairs with the brief
- `references/meta-creative-vault.md`: original UGC creator brief prompt
- `skills/ugc-production/SKILL.md`: production orchestration at scale
- `skills/ugc-production/references/cross-platform-brief-structure.md`: 3-input brief framework
- `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md`: voice gate
