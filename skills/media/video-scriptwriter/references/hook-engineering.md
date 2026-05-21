# Hook Engineering for Direct Response

The 5-lever hook framework + scoring system for direct-response ad scripts. Use this when generating, scoring, or iterating hooks for paid ads or organic short-form.

For the broader hook taxonomy across content types, see `skills/video-hook/SKILL.md`. This file is specific to direct-response ad work where hooks need to be generated in batches, scored systematically, and iterated based on the scoring data.

## What this workflow produces

From a single insight, this workflow generates:

- 10 hook variations
- 5 psychological lever categories (2 hooks per lever)
- A scoring framework (4 dimensions, /40 total)
- Top-3 ranked hooks
- Kill/rewrite recommendations for low-scoring hooks

## Best use case

This workflow works best when you already have:

- A strong insight
- Customer language (Reddit threads, sales calls, review mining)
- A defined persona
- Awareness-stage clarity

The stronger the insight, the stronger the hook output. Weak hooks come from vague inputs, not weak prompting.

## The 5 psychological levers

Every hook pulls on one of 5 levers. The 10-hook batch covers all 5 with 2 per lever.

### Lever 1: Curiosity gap

Create an information gap the brain is compelled to close.

**Pattern:** Specific moment + missing piece the viewer wants to know
**Example:** "Three weeks before my wife asked her sister for couples counseling advice, I started avoiding her in bed."

### Lever 2: Fear / loss aversion

Threat-avoidance trigger. The viewer feels at risk and needs to protect themselves or someone they care about.

**Pattern:** Specific consequence + implication that the viewer might already be experiencing it
**Example:** "I didn't realize my morning erections had been gone for eighteen months until my wife pointed it out, sideways."

### Lever 3: Contrarian

Challenges what the niche commonly believes. The hook is the position itself.

**Pattern:** Statement that contradicts conventional wisdom in the category
**Example:** "Most testosterone supplements never address SHBG. That's why they don't work."

### Lever 4: Social proof

Implies others are already in on something. Triggers the "I'm being left out" reflex.

**Pattern:** Specific peer behavior + implication that this is happening at scale
**Example:** "My wife stopped initiating before I admitted something was wrong. Talking to other guys, it's everywhere."

### Lever 5: Identity protection

Hooks that activate the viewer's sense of who they are or who they don't want to be.

**Pattern:** Specific identity-shaking moment that the viewer self-recognizes into
**Example:** "My daughter asked me to play tag at her birthday party. I made it 30 seconds."

## The scoring framework

Each hook scores from 1 to 10 across 4 dimensions. Total: /40.

### Stop-power (1-10)

Does the hook stop the scroll in the first second?

- **1-3**: Generic, no stop signal
- **4-6**: Has a specific element but easy to scroll past
- **7-8**: Strong specific element that pulls attention
- **9-10**: Pattern interrupt that stops attention cold

### Specificity (1-10)

Is the hook specific enough to feel real?

- **1-3**: Generic statements, no specific details
- **4-6**: Some specifics but rounded or convenient
- **7-8**: Specific moments, places, numbers
- **9-10**: Specifics so precise they could only have come from real experience

### Lever clarity (1-10)

Does the hook hit the lever it's tagged with cleanly?

- **1-3**: Hook tagged as one lever but reads as another
- **4-6**: Lever is there but diluted
- **7-8**: Lever clearly drives the hook
- **9-10**: Lever is the entire reason the hook works

### Natural cadence (1-10)

Does the hook sound like a real person talking?

- **1-3**: Reads as written marketing copy
- **4-6**: Mostly natural but with one or two written-not-spoken phrases
- **7-8**: Sounds spoken across most of the line
- **9-10**: Indistinguishable from a real person speaking aloud

### Reading the totals

- **35-40**: Top tier. Worth producing and testing.
- **30-34**: Strong. Iterate on the weakest dimension before producing.
- **25-29**: Borderline. Significant rewrite needed.
- **Below 25**: Kill or rewrite from scratch.

## Worked example

Hook #5 (Curiosity gap)

> "Three weeks before my wife asked her sister for couples counseling advice, I started avoiding her in bed."

| Dimension | Score | Why |
|---|---|---|
| Stop-power | 9 | "Three weeks before" creates immediate timeline curiosity. "couples counseling advice" specifies the high-stakes moment. |
| Specificity | 10 | Specific timeframe + specific person (wife's sister) + specific behavior (counseling advice) + specific avoidance behavior. Could not be invented. |
| Lever clarity | 8 | The curiosity gap is "what happened in those three weeks?" That's the lever. The hook does not get distracted by other levers. |
| Natural cadence | 9 | Sounds like a real person confessing. Slight rhythm of self-disclosure. No marketing language. |
| **Total** | **36/40** | Top-tier hook. Worth producing. |

### Why it works (qualitative)

- Uses trigger-event language ("three weeks before")
- Creates immediate curiosity (the gap is "what happened?")
- Feels emotionally real (the level of self-disclosure)
- No product mention
- High specificity (the wife's sister, couples counseling advice, the avoidance)

## Why the scoring layer matters

Most teams only generate hooks. Very few score them systematically, compare lever performance, or identify recurring winners.

Without scoring, teams default to: "This sounds good."

With scoring, you build:

- Repeatable selection criteria
- Stronger testing discipline
- Better creative iteration loops
- A persona-specific map of which levers win

## Common failure modes

### Hooks sound like ad copy

The hook reads as marketing language ("Discover the secret to..." "Transform your life with...")

**Fix:** Pull from Reddit / review / sales-call language only. If a customer would not say it in conversation, it is wrong for a hook.

### All hooks pull the same lever

10 hooks generated, 8 are curiosity gap variations. Lever testing is broken.

**Fix:** Each lever must appear at least twice. Force the spread across all 5.

### Hooks are too long

Hook lines over 15 words take more than 3 seconds to say. The viewer scrolls before the hook lands.

**Fix:** Read each hook aloud mentally. Cut anything over 3 seconds. 12-15 words maximum.

### Hooks feel vague

The hook lacks a specific behavior, trigger event, or moment.

**Fix:** Every hook must reference a specific behavior, trigger event, or moment. Generic feelings are not hooks.

## How this feeds the pipeline

### Top 3 hooks

Become 3 separate ad concepts. Each gets a full script written around it.

### Killed hooks

Logged for future reuse. A hook that scored 22/40 today might score 32/40 with a different persona or awareness stage.

### Highest-performing lever

Becomes the default opener pattern for that persona track. After enough data, you have a persona-specific lever map.

Over time:

- Persona-specific hook systems
- Lever-performance insights
- Faster iteration cycles
- Stronger opening frameworks

## Hook variation generator (preserving body)

When a script wins, you can generate 10 alternate first-3-second hooks that flow into the existing body.

### What stays locked

- The body of the script (everything after line 3)
- The persona language
- The tone of the body

### What varies

- The hook line (first 3 seconds, max 15 words)
- The lever the hook pulls on

The output: 10 alternate hooks across the 5 levers (2 per lever), each one flowing into line 4 of the existing script. Different levers unlock different audience pools, which means different ad-set targeting and different lookalike audiences.

For the actual generation prompt, see [../templates/hook-generator-and-scorer.md](../templates/hook-generator-and-scorer.md).

## Cross-references

- Voice rules: [direct-response-voice-system.md](direct-response-voice-system.md)
- Anti-AI script tells (relevant to hook quality): [anti-ai-script-tells.md](anti-ai-script-tells.md)
- Generation templates: [../templates/hook-generator-and-scorer.md](../templates/hook-generator-and-scorer.md)
- Broader hook taxonomy (different scope): `skills/video-hook/SKILL.md`
- UGC component-level hook variation (different scope): `skills/ugc-production/references/hook-variation-categories.md`
