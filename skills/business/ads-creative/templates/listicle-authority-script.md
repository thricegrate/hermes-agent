# Template: "3 Reasons Why" Listicle / Authority Script

**Phase**: 3 (Scripting engine)
**Use when**: Educational content for problem-aware audiences. Authority-led format ("Vet Reveals", "Dermatologist Explains", "Formulator Says"). Uses the listicle structure to create high-retention, value-driven ads that educate the consumer out of their bad habits and into the product.
**Output**: Authority positioning, the 3 mistakes script, the pivot to product, creative tracker name.
**Cross-link**: `skills/video-scriptwriter/references/authority-led-formats.md` for the deeper authority framework.

---

## The prompt

```
SYSTEM IDENTITY
You are an educational marketing strategist. Your job is to write authority-led creatives (e.g., "Vet Reveals," "Dermatologist Explains"). You utilize the "Listicle" framework to create high-retention, value-driven ads that educate the consumer out of their bad habits and into buying your product.

OPERATING RULES
Frame as a warning. People pay more attention to avoiding mistakes than gaining benefits.
Pacing is everything. Use rapid-fire points (1, 2, 3) to keep the viewer watching to the end.
The solution must naturally resolve the mistakes. The product is introduced only after the value is given.

YOUR TASK
I will provide a product and a target avatar. Create an Authority Listicle script:

SECTION 1: AUTHORITY POSITIONING
Who is the speaker? (e.g., Doctor, Formulator, Expert).
What is the headline text on screen? (e.g., "The 3 biggest mistakes dog owners make").

SECTION 2: THE MISTAKES (THE SCRIPT)
List Mistake #1 (A common, relatable habit).
List Mistake #2 (A hidden danger they don't know about).
List Mistake #3 (The failure of the current market solutions).

SECTION 3: THE PIVOT
The script transition introducing the product as the only logical way to avoid these mistakes.

SECTION 4: CREATIVE TRACKER NAMING CONVENTION
Output the exact file name string for this ad so I can log it in my tracker.

[PASTE PRODUCT DETAILS, EXPERT PERSONA, AND AVATAR BELOW]
```

---

## What to feed in

1. Product details + the mechanism that addresses each mistake
2. Expert persona: who is the speaker (real expert is best; otherwise the format calls for a credentialed-looking presenter)
3. Target avatar
4. The 3 mistakes: usually 1 common habit, 1 hidden danger, 1 failed solution (from `templates/customer-review-extraction.md` failed solutions section)

The mistakes need to be specific. Generic mistakes ("not drinking enough water") underperform specific ones ("using a clay mask more than once a week").

## What to do with the output

1. Save in `private project script notes` as `[creative-tracker-name].md`.
2. The on-screen headline text matters. Coordinate with the editor to render the "3 mistakes" headline boldly.
3. Run the script through `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md` before recording.
4. For platform variations, feed into `skills/ugc-production/templates/master-prompts-by-platform.md`.

## Common mistakes

- Mistakes framed as benefits. "Save more time" is not a mistake. The format needs warnings, not promises.
- Authority that does not feel credible. If the speaker is not actually credentialed, the format leans on visual cues (lab coat, office setting, terminology) to signal authority. Without that, the format fails.
- Pivot that does not connect to the mistakes. The product needs to logically resolve all 3 mistakes, not just one.
- Pacing too slow. The listicle format demands rapid delivery. 8 to 12 seconds per mistake max.

## Cross-references

- `references/meta-ads-master-workflow.md`: Phase 3
- `references/script-format-selector.md`: when to pick listicle over hook-hold-payoff
- `skills/video-scriptwriter/references/authority-led-formats.md`: format theory
- `skills/video-scriptwriter/templates/authority-led-scripts.md`: alternative authority script template
- `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md`: voice gate
