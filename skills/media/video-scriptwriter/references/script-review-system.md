# Script Review System

How to review a direct-response ad script before it goes to production. The reviewer's job is to catch structural, voice, and pacing issues before filming, when fixing them is cheap.

For the reviewer prompt, see [../templates/script-reviewer.md](../templates/script-reviewer.md).

## Why the review step matters

Most weak ads are not terrible concepts. They are structurally flawed executions.

Common examples:
- Product enters too early
- Pacing dies mid-script
- Hook does not match body
- Authority tone breaks
- Lines sound written instead of spoken

These issues are expensive because they only become obvious after production. A 4-minute yapper that loses retention at the 1:30 mark because the mechanism reveal lands flat costs the same to produce as one that works. The review step catches these issues at the script stage, which is where they are cheap to fix.

## What the reviewer should actually do

A good reviewer behaves like:

- A creative director (catches voice and tone issues)
- A pacing editor (catches retention risks)
- A direct-response strategist (catches structural problems)

A bad reviewer behaves like:

- A motivational copywriting coach ("This needs more energy!")

Specificity matters. The whole point of review is precision.

### Weak feedback

> "Needs stronger flow."
> "The hook could be punchier."
> "Tighten the middle section."

### Strong feedback

> "Line 7 is 31 words. Viewer attention drops before the mechanism reveal at 1:45."
> "Line 4 ('It's not stress, it's biology') is a banned reframe construction. Replace with: 'Stress isn't the cause. Cortisol is.' or just: 'The cause is cortisol.'"
> "Mechanism reveal at 1:45 uses 'transformational' which is on the banned list. Replace with the specific behavioral change."

The reviewer references exact line numbers. Quotes the offending text. Provides the fix.

## What the reviewer checks

The review covers three categories: voice violations, structural weaknesses, pacing.

### Category 1: Voice violations

Run a check for each of these. Flag every instance with line number and quote.

**Banned phrases:**
- Em dashes (any em dash anywhere in the script)
- "I'm obsessed"
- "Game-changing"
- "Transformational"
- "It's not X, it's Y" structures (and every variant)
- "Most guys / most women / most people" as script openers
- More than 2-3 colons total in the script
- Parallel rhythm triplets (three-word stacked closers)
- Two-fragment contrast (matched short fragments separated by a period)

**Voice tells:**
- Any sentence the writer would not naturally say in conversation
- Any line where the voice register shifts (especially at mechanism reveal and CTA)
- Any line that sounds like it has invisible italics on it for emphasis
- Stage-direction adjectives the creator would not say out loud
- "Imagine if" hypotheticals
- Wisdom-bestowing closers
- Therapist reframes ("what was really happening was...")

### Category 2: Structural weaknesses

**Hook quality (first 3 seconds):**
- Is the hook a moment or a claim? Moments win, claims lose.
- Is the hook 12 words or fewer?
- Does the hook reference a specific behavior, trigger event, or moment?
- Does the hook sound like real customer language (Reddit, sales calls, reviews)?

**Mechanism / villain timing:**
- For long-form: villain reveal between 1:45 and 2:15
- For two-actor: mechanism in the second actor's lines, before line 6
- For authority-led: mechanism after credibility is established (in-studio: line 2-3; street interview: after the reveal)
- Is the mechanism specific? Does it name biology, psychology, or category-specific cause?

**Product reveal timing:**
- For long-form (3-4 min): product enters at 75-85 percent of runtime (around 3:00-3:25)
- For two-actor (45-60 sec): product enters in the last 30 percent
- For authority-led (30-45 sec): product enters as a narrow recommendation in the last beat
- For POV (30-90 sec): product enters in the discovery moment, naturally

If the product appears earlier than the rule for that format, flag it as a structural failure.

**Close strength:**
- Does the close land the transformation or just stop the script?
- Does the CTA sound like the same person who said the hook?
- Is there urgency theater? ("Limited time only", "while supplies last") If yes, flag.

### Category 3: Pacing

**Lines longer than 4 seconds:**
- Count the words in each line
- A 4-second line is roughly 12-14 words at conversational pace
- Lines over 14 words: flag and recommend a cut

**Energy drops:**
- Any section where 3 or more lines in a row are similar length and similar register
- Real conversation has rhythm variation
- Flag sections that feel monotone

**Scroll-risk sections:**
- Any 5-second window where nothing pulls the viewer forward
- The viewer needs a reason to keep watching every 5-7 seconds
- Flag sections where the reason is missing

## Review output format

The reviewer output structure:

```
## Voice violations

### Line 4: "It's not stress, it's biology."
**Violation:** Banned "It's not X, it's Y" reframe construction.
**Fix:** Replace with: "Stress isn't the cause. Cortisol is." Or simpler: "The cause is cortisol."

### Line 12: "—" (em dash)
**Violation:** Em dash detected.
**Fix:** Replace with comma, period, or rewrite as two sentences.

### Line 18: "transformational change"
**Violation:** Banned word "transformational".
**Fix:** Replace with the specific behavioral change. Example: "I started waking up before my alarm again."

## Structural weaknesses

### Hook (line 1): "Most men over 40 lose interest..."
**Issue:** Demographic opener. Banned. Reads as infomercial.
**Fix:** Replace with a specific scene. Example: "I was 43 and my wife stopped reaching for me at night."

### Product reveal at line 14 (estimated 1:50 of 3:00 script)
**Issue:** Product enters at 60 percent of runtime. Long-form rule is 75-85 percent.
**Fix:** Move product reveal to line 22-25. Expand mechanism explanation in lines 14-22. The villain reveal at line 12 is strong; let it breathe.

## Pacing issues

### Line 7: 31 words
**Issue:** Line is over 4 seconds. Viewer attention drops before mechanism reveal at line 14.
**Fix:** Cut to 14 words. Example: "[Original line]" → "[Suggested cut]"

### Lines 18-22: monotone
**Issue:** Five consecutive lines at 12-14 words. No rhythm variation.
**Fix:** Cut line 19 or merge with line 20. Add a 4-word fragment in the middle.

## Production-ready: NO
**Reason:** 3 voice violations, 1 structural failure (product reveal timing), 2 pacing issues. Estimated 30 minutes to fix and re-review.
```

The reviewer ends with a binary production-ready YES/NO and a reason.

## Specific phrases to flag

The reviewer should run a Ctrl+F (or equivalent) for these specific patterns and flag every instance:

- `—` (em dash)
- `It's not` (and `isn't` followed by negation reframe)
- `Most ` (especially as line opener)
- `obsessed`
- `game-changing` / `game changing`
- `transformational`
- `: ` (colons; flag if more than 3 in the script)
- Three-word phrases at end of paragraphs (potential mic drops)

## Pacing math

Word count to time conversion at conversational pace:
- 2.5-3 words per second for natural delivery
- 60-second script = 150-180 words
- 90-second script = 225-270 words
- 4-second line maximum = 12-14 words
- 3-second line (hook target) = 9-12 words

If the total word count exceeds the format's runtime allowance, the script needs cuts before review.

## Common reviewer mistakes

### Vague feedback

"Improve the flow" tells the writer nothing. Always reference exact lines.

### Subjective preference

"I would phrase this differently" is not feedback. Either the line violates a rule or it does not. Either it has a structural problem or it does not. Personal taste is not the reviewer's job.

### Over-flagging

If the reviewer flags 50 issues, the writer ignores all of them. Limit to the highest-leverage issues. A script with 3 critical issues fixed is better than a script with 20 minor issues marked.

### Under-flagging

Some reviewers approve scripts that have voice violations because the script "feels good overall." The voice violations are not subjective. They are banned. Flag them.

### Skipping the production-ready verdict

The reviewer must end with YES or NO. "Looks good with some changes" is not a verdict. Production-ready means production-ready.

## When to skip review

Two cases:

1. **Quick iteration on a known winner.** When generating hook variations from a winning script (using the hook variation generator), the body is already validated. Only the new hooks need review, not the whole script.

2. **Internal-only content.** Build-in-public scripts, behind-the-scenes content, or organic short-form where the script is more of a guide than a final piece. Apply voice rules but skip the full structural review.

For everything else, the review step is mandatory.

## Cross-references

- Voice rules: [direct-response-voice-system.md](direct-response-voice-system.md)
- Anti-AI script tells (the patterns the reviewer flags): [anti-ai-script-tells.md](anti-ai-script-tells.md)
- Reviewer prompt: [../templates/script-reviewer.md](../templates/script-reviewer.md)
- Hook engineering (review the hook against the 4-dimension scoring): [hook-engineering.md](hook-engineering.md)
- Format-specific structural rules:
  - [two-actor-formats.md](two-actor-formats.md)
  - [authority-led-formats.md](authority-led-formats.md)
  - [long-form-formats.md](long-form-formats.md)
- Voice gate before delivery: `skills/humanizer/SKILL.md`, `skills/content-review/SKILL.md`
