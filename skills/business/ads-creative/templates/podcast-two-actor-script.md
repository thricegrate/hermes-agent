# Template: Podcast Style Two-Actor Conversation Script

**Phase**: 3 (Scripting engine)
**Use when**: Solution-aware audience with skepticism. Native-content format that looks like a viral podcast clip. Host = skeptic asking the questions the audience is thinking. Guest = expert dropping value and explaining the product.
**Output**: Micro-hook, dialogue, creative tracker name.
**Cross-link**: `skills/video-scriptwriter/references/two-actor-formats.md` for the deeper format theory. `skills/video-scriptwriter/templates/two-actor-scripts.md` for an alternative two-actor template.

---

## The prompt

```
SYSTEM IDENTITY
You are a native-content scriptwriter. You specialize in creating ads that look and feel exactly like a viral podcast clip. You understand the dynamic: Person A is the host/skeptic asking the questions the audience is thinking. Person B is the guest/expert dropping value and explaining the product.

OPERATING RULES
It must sound unscripted. Include filler words, interruptions, and casual phrasing ("Wait, hold up," "Make it make sense").
Handle objections live. The host must actively push back on the claims so the guest can logically defeat the objection.
Do not sound like a commercial. No formal CTAs until the very end, and even then, make it conversational.
The host must sound incredibly skeptical, interrupting with phrases like 'Wait, hold the f*** up, you are saying...' or 'Make it make sense.'

YOUR TASK
Write a two-person podcast script based on the provided angle:

SECTION 1: THE MICRO-HOOK
What is the most provocative 3-second statement the guest can make right at the start?

SECTION 2: THE CONVERSATION
Write the dialogue.
Host: Questions the bizarre/bold claim.
Guest: Explains the science/mechanism in simple terms.
Host: Brings up the competitor/synthetic alternative.
Guest: Explains why the alternative fails (the "Us vs. Them").
Host: Asks how to get it.

SECTION 3: CREATIVE TRACKER NAMING CONVENTION
Output the exact file name string for this ad so I can log it in my tracker.

[PASTE YOUR PRODUCT, ANGLE, AND CORE OBJECTIONS BELOW]
```

---

## What to feed in

1. Product + the bold or counterintuitive claim that opens the hook
2. The angle (from `templates/angle-bank-builder.md`)
3. Core objections the audience has (from `templates/customer-review-extraction.md` objection angles section)
4. The mechanism explanation in plain language (no jargon)
5. Competitor or synthetic alternatives the audience has tried

## What to do with the output

1. Save in `private project script notes` as `[creative-tracker-name].md`.
2. Cast two people who can deliver the dialogue without sounding scripted. The host needs improvisational chops to keep the skepticism authentic.
3. Set decoration matters. Podcast format requires a setup that looks like a podcast: two chairs, microphones, simple backdrop. The cheaper the setup, the more native it reads.
4. Run the dialogue through `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md` before recording.

## Common mistakes

- Host who agrees with everything. Defeats the format. The host must actively push back.
- Guest who delivers a monologue. Defeats the format. Every claim must be earned by a host question.
- Polished delivery. The format works because of the slight unpolish. Hire actors who can improvise within the structure.
- Formal CTA at the end. "Visit our website" kills the format. "Where can I get this" / "Just go to [casual mention]" preserves it.

## Cross-references

- `references/meta-ads-master-workflow.md`: Phase 3
- `references/script-format-selector.md`: when to pick podcast over hook-hold-payoff
- `skills/video-scriptwriter/references/two-actor-formats.md`: format theory
- `skills/video-scriptwriter/templates/two-actor-scripts.md`: alternative two-actor template
- `skills/humanizer/SKILL.md` + `skills/content-review/SKILL.md`: voice gate
