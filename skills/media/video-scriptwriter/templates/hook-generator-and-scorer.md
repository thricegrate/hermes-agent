# Hook Generator and Scorer

Three prompts in one template:
1. Generate 10 hooks across 5 psychological levers
2. Score the hooks across 4 dimensions
3. Generate hook variations from a winning script (preserving the body)

For the framework explanation (5 levers, scoring rubric, failure modes), see [../references/hook-engineering.md](../references/hook-engineering.md).

For voice rules that apply across all hooks, see [../references/direct-response-voice-system.md](../references/direct-response-voice-system.md).

## Before you run any of these prompts

Confirm you have:
- One insight (one-sentence crystallization of what the audience needs to know)
- One persona (who they are, where they are in their life, what they have tried)
- One awareness stage (Unaware / Problem Aware / Solution Aware / Product Aware / Most Aware)
- One format type (video or static)
- Optional but recommended: brand voice document, winning ad examples, Reddit/review/sales-call language

The stronger the insight, the stronger the hook output. Weak hooks come from vague inputs, not weak prompting.

## Prompt 1: Hook Generator

Use this when you need 10 hook variations from a single insight.

```
Generate 10 hook variations for this concept.

Persona:
[persona, e.g. "men 38-55 noticing their wife pulling away in bed"]

Awareness stage:
[Unaware / Problem Aware / Solution Aware / Product Aware / Most Aware]

Insight:
[one-sentence insight]

Format:
[video / static]

Output the 10 hooks across 5 psychological levers (2 per lever):

1. Curiosity gap
2. Fear / loss aversion
3. Contrarian
4. Social proof
5. Identity protection

For each hook, output:
- The hook line (max 15 words)
- The lever
- One sentence explaining why it stops the scroll

Constraint:
Hooks must sound natural.
No marketing language.
No em dashes.
No "obsessed."
No "game-changing."
No "transformational."
No "It's not X, it's Y" structures.
No "Most guys / most women / most people" openers.

Pull verbatim phrases from customer research. If you do not have verbatim source material, mark the hook as [VERBATIM-NEEDED] and continue.

Awareness stage adjustment:
- Unaware: lead with symptom
- Problem Aware: lead with consequence
- Solution Aware: lead with mechanism
- Product Aware: lead with category positioning
- Most Aware: lead with offer specificity
```

## Prompt 2: Hook Scorer

Use this after Prompt 1 to rank the 10 hooks and identify which ones to produce.

```
Score these 10 hooks against the target persona:

[paste hooks from Prompt 1]

Persona:
[same persona from Prompt 1]

Score each hook from 1 to 10 across:

1. Stop-power: does the hook stop the scroll in the first second?
2. Specificity: is the hook specific enough to feel real?
3. Lever clarity: does the hook hit the lever it is tagged with cleanly?
4. Natural cadence: does the hook sound like a real person talking?

Scoring scale per dimension:
- 1-3: weak
- 4-6: borderline
- 7-8: strong
- 9-10: top tier

Output:
- Each hook with all 4 scores plus total /40
- Rank the top 3 and explain why each one works
- Flag anything below 25/40 for rewrite or deletion
- For rewrite candidates (25-29), suggest the specific fix (e.g., "Cut to 12 words", "Add specific detail in second clause", "Replace 'amazing' with the actual sensory detail")

Show your work. Reference the dimension definitions when explaining a score.
```

## Prompt 10 (variation generator): Hook Variations from a Winning Script

Use this when a script has performed well and you want 10 alternate hooks that preserve the body.

```
Generate 10 hook variations for this winning script.

Winning script:
[paste full script with line numbers]

Performance data:
- Hook rate: [percentage]
- Hold rate: [percentage by section]
- CTR: [percentage]
- Distribution: [reach + view count]

Persona:
[persona]

The body of the script stays unchanged. Generate 10 alternate first-3-second hooks that:
- Use the 5 psychological levers (2 hooks per lever)
- Match the script's tone exactly
- Flow naturally into line 4
- Preserve persona language (the verbatim customer phrases already in the script)

Levers:
1. Curiosity
2. Fear / loss aversion
3. Contrarian
4. Social proof
5. Identity protection

Constraint:
Each hook must be 15 words or fewer.
Each hook must read aloud in 3 seconds or less.
No em dashes, no banned phrases (obsessed, game-changing, transformational, "it's not X it's Y", "most guys/women/people" openers).

For each hook variation, output:
- The hook line
- The lever used
- Why it unlocks a different audience pool (which segment of the broader persona this hook pulls in that the original does not)
- Predicted entity-ID separation: yes/no + explanation (whether the algorithm will treat this as a different creative entity)

After all 10 hooks, recommend the top 3 to produce first based on which audience pools they unlock and how distinct they are from the original.
```

## Worked example output (compressed)

Inputs:
- Persona: married men 40-55, college-educated, $120k+ household, "high-functioning" but privately experiencing 6-18 months of declining bedroom performance
- Awareness stage: Problem Aware (they know something is wrong, do not know the cause)
- Insight: "Most men reframe declining sex life as stress or aging when the actual cause is biological"
- Format: video

### Prompt 1 output (Curiosity gap, 2 hooks):

**Hook 1A.** "I didn't realize my morning erections had been gone for eighteen months until my wife pointed it out, sideways."
- Lever: Curiosity gap
- Why: Specific timeframe + sideways reference creates information gap. Viewer wants to know what the wife said and what was happening before.

**Hook 1B.** "Three weeks before my wife asked her sister for couples counseling advice, I started avoiding her in bed."
- Lever: Curiosity gap
- Why: Trigger event (wife asking sister for counseling) + specific avoidance behavior. Viewer wants to know what happened in those three weeks.

### Prompt 2 output (for Hook 1B):

| Dimension | Score | Why |
|---|---|---|
| Stop-power | 9 | "Three weeks before" + "couples counseling advice" = high-stakes timeline curiosity |
| Specificity | 10 | Specific timeframe, specific person (wife's sister), specific behavior |
| Lever clarity | 8 | The curiosity gap drives the whole hook. No distraction from other levers. |
| Natural cadence | 9 | Sounds like real self-disclosure. No marketing language. |
| **Total** | **36/40** | Top tier. Produce. |

### Prompt 10 output (variations from a winning script):

**Hook A1.** "I didn't realize my morning erections had been gone for eighteen months until my wife pointed it out, sideways."
- Lever: Curiosity
- Why it unlocks a different pool: Original hook leads with the relational symptom (wife pulling away). This one leads with the physiological symptom most men in this persona have not consciously tracked. Pulls in the man who has not yet had the bedroom-avoidance moment but is one Google search away.
- Predicted entity-ID separation: Yes. Different ad-set targeting will surface this to men in "men's health symptoms" interest clusters rather than "marriage / relationship" clusters. Meta will read this as a different creative entity within ~48 hours of spend.

## Common failure modes when running these prompts

### The model produces hooks that score themselves high

The model is incentivized to validate its own output. Run Prompt 2 in a separate context if possible, or explicitly instruct the model to score hookishly (a 9/10 should be rare).

### The model uses banned phrases despite the constraint

Run a Ctrl+F (or grep) on the output for em dashes, "obsessed", "game-changing", "transformational", "It's not", "Most guys/women/people". If any appear, regenerate or fix manually.

### All hooks pull the same lever

If the model produces 7 curiosity gap hooks and 3 fear hooks, the constraint did not hold. Re-prompt explicitly: "Each lever must appear exactly twice. Force the spread."

### Variations from a winner do not actually flow into line 4

The variations need to be tested by reading hook + line 4 aloud. If there is a tonal break, the hook is wrong. Add to the prompt: "Read each new hook plus line 4 of the original script aloud. The transition must feel natural."

## Cross-references

- Framework explanation (5 levers, scoring): [../references/hook-engineering.md](../references/hook-engineering.md)
- Voice rules: [../references/direct-response-voice-system.md](../references/direct-response-voice-system.md)
- Anti-AI patterns to flag: [../references/anti-ai-script-tells.md](../references/anti-ai-script-tells.md)
- Script reviewer (run on the chosen hook + body): [script-reviewer.md](script-reviewer.md)
