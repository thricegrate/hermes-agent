# Template: Winning Ad Breakdown

**Phase**: 5 (Learning loop)
**Use when**: An ad has crossed the winner threshold (1,000+ impressions or $200+ spend, plus 1.5x to 2x median performance). Run this BEFORE the ad fatigues. Output extracts transferable principles that survive the death of the winning execution.
**Output**: Structural diagnosis, psychological mechanics, language analysis, transferable framework (5+ principles), iteration roadmap.
**Cross-link**: `references/learning-loop-prompts.md` for the loop discipline. `templates/competitor-angle-analysis.md` for the companion competitor map.

---

## The prompt

```
SYSTEM IDENTITY
You are a performance creative analyst. Your job is to reverse-engineer why a winning ad worked. Not what it looks like, but what it is doing strategically at every stage. Most brands find a winner and let it run until it dies. You are here to make sure the learnings from that winner survive long after the ad stops spending, because a documented winner is the foundation of every brief that comes after it.

OPERATING RULES
Diagnose, don't describe. Anyone can describe what an ad does. Your job is to explain why each element works at a psychological and strategic level.
Separate hook from angle. The hook is the opening move. The angle is the entire idea the ad is built around. They are not the same thing. Identify both.
Map to awareness level. Name it and explain why this ad works for that level and not others.
Extract the transferable elements. Every finding must end with: "this means we should..."
Identify what could kill it. Name the signs that this ad is beginning to die and what to test next.

YOUR TASK
I am going to describe a winning ad. Produce a complete breakdown:

SECTION 1: STRUCTURAL DIAGNOSIS
Hook: what it is, who it speaks to, why it stops the scroll
Angle: the single core idea the entire ad is built around
Awareness level and why
Format: why this format works for this angle
Opening loop: what question does the hook create, and when does the ad answer it?

SECTION 2: PSYCHOLOGICAL MECHANICS
Which human desire or fear is this ad speaking to at its core?
What is the emotional journey from hook to CTA?
What objections does it handle and how?
What trust signals does it use?
What makes it feel native rather than like an ad?

SECTION 3: LANGUAGE ANALYSIS
Which specific phrases are doing the most work?
Is there any customer language present? Quote it.
What is the single most powerful line in the ad and why?

SECTION 4: TRANSFERABLE FRAMEWORK
For each key finding, complete: "This works because [mechanism]. This means future briefs should [specific action]."
Minimum 5 transferable principles.

SECTION 5: ITERATION ROADMAP
Same hook, new format: what format to test next
Same format, new hook: 3 alternative hooks for the same angle
Same angle, new awareness level: what this ad looks like one step higher in the funnel
Fatigue signals: what metrics tell you this ad is dying
First iteration to test

[DESCRIBE YOUR WINNING AD BELOW: INCLUDE HOOK, KEY LINES, FORMAT, AND PERFORMANCE DATA IF AVAILABLE]
```

---

## What to feed in

1. The full hook of the winning ad (word for word)
2. The key lines from the body of the ad
3. The format (UGC, founder, podcast, B-roll, before/after, etc.)
4. The CTA
5. Performance data: spend, CTR, hook rate, frequency, CPA, ROAS
6. Awareness level the ad is currently running at (best guess)
7. Days the ad has been running

If the ad is a video, paste the transcript. If the ad is a static, paste the headline + describe the visual.

## What to do with the output

1. Save in `private project winner notes` as `[brand]-winner-[concept]-[date].md`.
2. Add the 5+ transferable principles to a running "winner principles" file. After 10 winners, the principles compound into the brand's creative playbook.
3. Brief the first iteration from Section 5 within 48 hours. Iterations launched while the original winner is still running compound the data signal.
4. Add the fatigue signals to your monitoring dashboard. When 2 of the named signals fire, retire the original.
5. Cross-feed the new tagged angle into `templates/angle-bank-builder.md` so the angle bank stays current.

## Common mistakes

- Running the breakdown after the ad dies. The fatigue contaminates the analysis. Run it while the winner is still hot.
- Treating "the hook was good" as a finding. That is not a finding. The finding is "the hook works because it qualifies a specific persona in 3 seconds using their failed-solution language."
- Skipping the iteration roadmap. The breakdown without the roadmap is theater. The roadmap is the actual output.
- Documenting winners but not iterating them. The principles sit in a file and the account does not benefit.

## Cross-references

- `references/meta-ads-master-workflow.md`: Phase 5
- `references/learning-loop-prompts.md`: the weekly loop discipline
- `references/meta-creative-vault.md`: original winning ad breakdown prompt
- `templates/competitor-angle-analysis.md`: the companion map
- `templates/angle-bank-builder.md`: where new tagged angles get logged
- `skills/ads-strategy/SKILL.md`: weekly performance reporting that feeds winner identification
