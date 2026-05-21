# Script Reviewer Template

Prompt 9: review a direct-response ad script for production readiness.

For the review methodology (what good vs bad reviews look like, what to flag), see [../references/script-review-system.md](../references/script-review-system.md).

For voice rules being checked, see [../references/direct-response-voice-system.md](../references/direct-response-voice-system.md).

For the anti-AI script tells being checked, see [../references/anti-ai-script-tells.md](../references/anti-ai-script-tells.md).

## When to use this template

Run this on every direct-response ad script before sending to a creator or queueing for production. The review takes 5-10 minutes and catches issues that would otherwise become obvious only after filming.

The two cases where review can be skipped:
- Quick iteration on a known winner (only the new hook needs review, not the whole script)
- Internal-only content (build-in-public, organic short-form where the script is more guide than final piece)

For everything else, review is mandatory.

## The reviewer prompt

```
Review this script for production readiness.

[paste full script with line numbers]

Format:
[podcast / skit / authority / yapper / POV]

Persona:
[persona]

Awareness stage:
[Unaware / Problem Aware / Solution Aware / Product Aware / Most Aware]

Estimated runtime:
[runtime in seconds or minutes]

Run the review across three categories.

==========================
CATEGORY 1: VOICE VIOLATIONS
==========================

Search for and flag every instance of:

Banned phrases:
- Em dashes (any em dash anywhere)
- "I'm obsessed"
- "Game-changing"
- "Transformational"
- "It's not X, it's Y" structures (every variant)
- "Most guys / most women / most people" as line openers
- More than 2-3 colons total in the script
- Parallel rhythm triplets (three-word stacked closers)
- Two-fragment contrast (matched short fragments separated by a period)

Voice tells:
- Any sentence the writer would not naturally say in conversation
- Any line where the voice register shifts (especially at mechanism reveal and CTA)
- Any line that sounds like it has invisible italics on it for emphasis
- Stage-direction adjectives the creator would not say out loud
- "Imagine if" hypotheticals
- Wisdom-bestowing closers
- Therapist reframes ("what was really happening was...")

For each violation, output:
- Line number
- Quoted text
- Violation type
- Specific fix (rewritten line, not just "rewrite this")

==========================
CATEGORY 2: STRUCTURAL WEAKNESSES
==========================

Hook quality (first 3 seconds):
- Is the hook a moment or a claim? (Moments win, claims lose)
- Is the hook 12 words or fewer?
- Does the hook reference a specific behavior, trigger event, or moment?
- Does the hook sound like real customer language?

Mechanism / villain timing:
- For long-form (3-4 min): villain reveal between 1:45 and 2:15
- For two-actor (45-60 sec): mechanism in second actor's lines, before line 6
- For authority-led (30-45 sec): mechanism after credibility (in-studio: line 2-3; street interview: after the reveal)
- Is the mechanism specific? Does it name biology, psychology, or category-specific cause?

Product reveal timing:
- For long-form: product enters at 75-85% of runtime
- For two-actor: product enters in last 30% of runtime
- For authority-led: product enters as narrow recommendation in last beat
- For POV: product enters in discovery moment, naturally

Close strength:
- Does the close land the transformation or just stop the script?
- Does the CTA sound like the same person who said the hook?
- Is there urgency theater? (Limited time, while supplies last) Flag if yes.

For each structural issue, output:
- Line number or timestamp
- Issue description
- Specific fix

==========================
CATEGORY 3: PACING
==========================

Lines longer than 4 seconds:
- Count words per line
- Flag any line over 14 words
- Suggest a specific cut

Energy drops:
- Flag any section where 3+ lines in a row are similar length and similar register
- Real conversation has rhythm variation

Scroll-risk sections:
- Flag any 5-second window where nothing pulls the viewer forward
- The viewer needs a reason to keep watching every 5-7 seconds

For each pacing issue, output:
- Line number or timestamp
- Issue
- Specific fix (with rewritten line if applicable)

==========================
OUTPUT FORMAT
==========================

## Voice violations
[List each violation with line number, quote, type, and fix]

## Structural weaknesses
[List each issue with line number / timestamp, issue, and fix]

## Pacing issues
[List each issue with line number, issue, and fix]

## Production-ready: YES or NO
[Reason: 1-2 sentences. If NO, summary of the most critical issues to address.]

==========================
CONSTRAINT ON FEEDBACK QUALITY
==========================

Be specific. Always reference exact line numbers. Quote the offending text. Provide rewritten lines, not vague directions.

DO NOT say:
- "Improve the flow"
- "The hook could be punchier"
- "Tighten the middle section"
- "Sounds a bit AI"

DO say:
- "Line 7 is 31 words. Cut to 14. Suggested rewrite: '[specific rewrite]'."
- "Line 4 ('It's not stress, it's biology') is a banned reframe construction. Replace with: 'The cause is cortisol.'"
- "Mechanism reveal at line 14 (timestamp 1:50) uses 'transformational' which is on the banned list. Replace with the specific behavioral change: 'I started waking up before my alarm again.'"

If the feedback could apply to any script, it is not specific enough. The whole point of review is precision.

==========================
ON OVER-FLAGGING AND UNDER-FLAGGING
==========================

If you flag more than 15 issues, the writer will ignore all of them. Limit to the highest-leverage issues. A script with 3 critical issues fixed is better than a script with 20 minor issues marked.

If you flag fewer than 3 issues on a script that is not yet production-ready, you missed something. Re-read the script with the banned phrases list and the structural rules in mind.

The verdict (Production-ready: YES or NO) must be binary. "Looks good with some changes" is not a verdict.
```

## Worked example: review output

Reviewing a 4-minute long-form yapper script for a male hormone health product:

```
## Voice violations

### Line 4 (timestamp 0:08): "It's not stress, it's biology."
**Violation:** Banned "It's not X, it's Y" reframe construction.
**Fix:** "The cause is biological. Cortisol binds testosterone in the blood."

### Line 18 (timestamp 1:32): "transformational change in my marriage"
**Violation:** Banned word "transformational".
**Fix:** Replace with the specific behavioral change. "My wife started reaching for me at night again. That hadn't happened in 18 months."

### Line 22 (timestamp 1:55): em dash detected
**Violation:** Em dash.
**Fix:** Replace with comma or rewrite as two sentences.

### Line 31 (timestamp 3:30): "Most guys never figure this out."
**Violation:** "Most guys" demographic generalization.
**Fix:** Replace with a specific scene or scrap. "I almost didn't figure it out either. Eighteen months in and I was still telling myself it was stress."

## Structural weaknesses

### Hook (line 1, timestamp 0:00): "Most men over 40 lose interest in their wives even when they still love them."
**Issue:** Demographic opener. Banned. Reads as infomercial.
**Fix:** Replace with a specific scene. Example: "I was 43 and my wife stopped reaching for me at night."

### Product reveal at line 25 (estimated timestamp 2:50)
**Issue:** Product enters at 70% of runtime. Long-form rule is 75-85%.
**Fix:** Move product reveal to line 28-30 (timestamp 3:10-3:25). Expand mechanism explanation in lines 22-25. The villain reveal at line 20 (cortisol binding) is strong; let it breathe.

### CTA (line 45, timestamp 3:55): "Click below to change your life."
**Issue:** Generic transformation language. Voice register shifts to marketer.
**Fix:** Match the hook's voice. "Link below if you're seeing the same pattern. I'd start with the bloodwork before you do anything."

## Pacing issues

### Line 7 (timestamp 0:20): 31 words
**Issue:** Line is over 4 seconds. Viewer attention drops before the pain validation builds.
**Fix:** Cut to 14 words. Original: "[long line]". Suggested: "I told myself she was tired. We had a third kid. The math made sense at the time."

### Lines 18-22 (timestamp 1:32-2:00): all 12-15 words, similar register
**Issue:** Five consecutive lines without rhythm variation. Energy flatlines before mechanism reveal.
**Fix:** Cut line 19 or merge with line 20. Add a 4-word fragment in the middle: "I was 43. Married 17 years."

## Production-ready: NO

**Reason:** 4 voice violations (em dash, "It's not X, it's Y", banned word, demographic opener), 3 structural failures (hook is a category statement, product reveal at 70% instead of 75-85%, CTA breaks character), 2 pacing issues. Estimated 20-30 minutes to fix and re-review.
```

## Common failure modes when running this prompt

### The reviewer flags everything

Reviewer outputs 30+ issues, half of which are minor stylistic preferences. Writer ignores all feedback.

**Fix:** Add to the prompt: "Limit to the 10-15 highest-leverage issues. Skip minor stylistic preferences. Focus on banned phrases, structural failures, and lines that fail the read-aloud test."

### The reviewer hedges on the verdict

Output ends with "Looks production-ready with some changes" instead of YES/NO.

**Fix:** Add to the prompt: "The verdict must be binary. Production-ready: YES or NO. No hedging. If the script needs changes, the verdict is NO."

### The reviewer gives vague fixes

Issues are flagged but the fix is "rewrite this line" without a specific rewrite.

**Fix:** Add to the prompt: "Every fix must include the rewritten line, not just a direction to rewrite. If you cannot suggest a specific rewrite, the issue may not be a real issue."

### The reviewer misses banned phrases

The script contains "transformational" or "It's not X, it's Y" but the reviewer does not flag it.

**Fix:** Run the script through Ctrl+F (or grep) before the review. Pre-flag banned phrases. Then run the review prompt. The reviewer should confirm and explain, not be the only check.

### The reviewer over-praises

The output spends 80% of words on what works and 20% on issues. The writer reads it as a green light when the script has problems.

**Fix:** Add to the prompt: "Skip the praise section entirely. The output is a list of issues and the verdict. The writer does not need to be told what works. They need to know what to fix."

## How this connects to the rest of the workflow

The reviewer fits between script generation and production:

1. Generate hook (Prompt 1) → Score hooks (Prompt 2) → Pick top 3
2. Generate full script for top hook (Prompts 3-8 depending on format)
3. **Run script reviewer (Prompt 9)** ← this template
4. Apply fixes
5. Re-run reviewer if more than 5 fixes were made
6. Send to production

The reviewer also runs after hook variations (Prompt 10). The new hook gets reviewed against the existing body to confirm tonal continuity.

## Cross-references

- Review methodology: [../references/script-review-system.md](../references/script-review-system.md)
- Voice rules: [../references/direct-response-voice-system.md](../references/direct-response-voice-system.md)
- Anti-AI script tells (the patterns being flagged): [../references/anti-ai-script-tells.md](../references/anti-ai-script-tells.md)
- Format-specific structural rules:
  - [../references/two-actor-formats.md](../references/two-actor-formats.md)
  - [../references/authority-led-formats.md](../references/authority-led-formats.md)
  - [../references/long-form-formats.md](../references/long-form-formats.md)
- Hook engineering (review the hook against 4-dim scoring): [../references/hook-engineering.md](../references/hook-engineering.md)
- Script generation templates:
  - [hook-generator-and-scorer.md](hook-generator-and-scorer.md)
  - [two-actor-scripts.md](two-actor-scripts.md)
  - [authority-led-scripts.md](authority-led-scripts.md)
  - [long-form-scripts.md](long-form-scripts.md)
- Final voice gate before delivery: `skills/humanizer/SKILL.md`, `skills/content-review/SKILL.md`
