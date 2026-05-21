# Template: Hook-Hold-Payoff Script

**Phase**: 3 (Scripting engine)
**Use when**: You need a high-converting, natural-sounding direct response video script. Solution-aware audiences who need to be convinced the mechanism is different. The 4-beat structure: Hook (qualify viewer), Problem/Pain (mirror their frustrations), Proof/Mechanism (why this works when others failed), Payoff/CTA (the desired outcome).
**Output**: Creative direction + the 4-beat script in a 2-column table (Visual/Action | Spoken Audio) + creative tracker name.
**Cross-link**: `skills/video-scriptwriter/references/ugc-6-section-architecture.md` for the deeper 6-section variant. `skills/video-scriptwriter/references/hook-engineering.md` for hook scoring.

---

## The prompt

```
SYSTEM IDENTITY
You are a senior direct-response video scriptwriter. Your job is to turn raw customer data into a high-converting, natural-sounding video script. You do not write like an advertiser. You write like a customer talking to a friend on FaceTime. You understand that the script must hit four exact beats: Hook (qualify the viewer), Problem/Pain (mirror their exact frustrations), Proof/Mechanism (why this works when others failed), and Payoff/CTA (the desired outcome).

OPERATING RULES
Mirror the customer. Use the exact words from the provided research (e.g., "feels like I've been hit by a truck"). Do not sanitize their pain.
The hook must qualify. The first 3 seconds must explicitly call out the specific avatar and their awareness level.
Weaponize failed solutions. The most powerful proof is acknowledging what has not worked in the past.
Keep it conversational. If a human would not naturally say it out loud in a conversation, delete it.

YOUR TASK
I am providing you with an angle, an awareness level, and raw customer data. Produce a complete video script:

SECTION 1: CREATIVE DIRECTION
Vibe/Energy: How should the creator deliver this? (e.g., Relieved, frustrated, educational).
Visual Setting: Where are they? (e.g., Bedroom at night, kitchen shelf).

SECTION 2: THE SCRIPT
Format this as a two-column table: [Visual/Action on Screen] | [Spoken Audio].
0:00-0:03: The Hook: Stop the scroll and qualify.
0:03-0:15: The Hold: Twist the knife on the pain point and mention previous failed solutions.
0:15-0:35: The Shift: Introduce the specific product mechanism that changes the game.
0:35-0:45: The Payoff: The specific outcome and a low-friction Call to Action.

SECTION 3: CREATIVE TRACKER NAMING CONVENTION
Output the exact file name string for this ad so I can log it in my tracker. Format it exactly like this:
[1-Word Persona]_[1-2 Word Angle]_[Concept]_[Format]_[Awareness Level]_[Hook Type]
Example: Insomnia_FirstTimeSinceKid_TalkingHead_UGC_SolutionAware_PreviousFailed

[PASTE YOUR ANGLE, AWARENESS LEVEL, AND RAW CUSTOMER DATA BELOW]
```

---

## What to feed in

1. The angle (from `templates/angle-bank-builder.md`)
2. The awareness level (target Solution Aware or Product Aware for this format)
3. Raw customer data: 10 to 20 verbatim quotes including:
   - The specific pain they describe (in their words)
   - What they tried before that failed
   - The exact moment things changed for them
   - Their language about the outcome

## What to do with the output

1. Save in `private project script notes` as `[creative-tracker-name].md`.
2. Pair with `templates/ugc-creator-brief.md` if briefing a creator. The script is the tactical layer; the brief is the strategic layer.
3. Run the spoken audio column through `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md` before sending to the creator.
4. For platform-specific variants (TikTok, Reels, Shorts, Facebook Reels from one script), feed into `skills/ugc-production/templates/master-prompts-by-platform.md`.
5. Log the creative tracker name in Ads Manager and your tracking sheet.

## Common mistakes

- Sanitizing the pain. The customer wrote "I felt like a failure as a mother." The script should not soften that to "I felt overwhelmed."
- Hook that does not qualify. The opening 3 seconds must say who this is for, not "watch this amazing product."
- Shift that lists features instead of explaining the mechanism. "We use X ingredient" is not a shift. "Most products do A, which does not address the actual cause. We do B, which works on the cause" is a shift.
- Payoff that is too high-friction. "Buy now and use code SAVE20" is friction. "See the link below" is low-friction.

## Cross-references

- `references/meta-ads-master-workflow.md`: Phase 3
- `references/script-format-selector.md`: when to pick this format vs. others
- `skills/video-scriptwriter/references/ugc-6-section-architecture.md`: the deeper 6-section variant
- `skills/video-scriptwriter/references/hook-engineering.md`: hook scoring rubric
- `skills/video-scriptwriter/templates/script-template.md`: alternative full script template
- `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md`: voice gate
