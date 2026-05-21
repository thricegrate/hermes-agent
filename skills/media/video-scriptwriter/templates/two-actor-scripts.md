# Two-Actor Script Templates

Two prompts for two-actor formats:
- Prompt 3: Podcast clip script (Host + Expert)
- Prompt 4: Skit conversation script (Skeptic + Believer)

For when to use each format and the structural patterns, see [../references/two-actor-formats.md](../references/two-actor-formats.md).

For voice rules that apply across both formats, see [../references/direct-response-voice-system.md](../references/direct-response-voice-system.md).

## Prompt 3: Podcast Clip Script (Host + Expert)

Use this for 45-60 second clips where authority drives the conversion. Host is a curious layperson. Expert is the authority figure. Information unfolds through dialogue.

```
Write a 45 to 60 second podcast clip script.

Persona:
[persona]

Mechanism:
[mechanism story: the biological, psychological, or category-specific cause behind the problem]

Product:
[product + 1-line description]

Objection to handle:
[one-line objection: the most common pushback the audience has when they hear the mechanism]

Format:
Two-actor podcast clip.

Host:
curious layperson, asks the questions the audience would ask

Expert:
authority figure, explains the mechanism without sounding like a brochure

Structure:

1. Host poses the symptom or problem (2 lines)
2. Expert names the mechanism in unfamiliar language (3 lines)
3. Expert handles the objection (2 lines)
4. Expert references the solution category, then product name (2 lines)
5. Closing line lands the transformation

Output:
- HOOK (host's first line)
- Full script with HOST/EXPERT labels per line
- Estimated runtime
- Visual notes per line (camera angle, gesture, prop, expression cue)

Constraint:
Each line maximum 2 sentences. Read aloud. If the actor runs out of breath, cut it.

The mechanism enters before the product. The product cannot appear before line 8 (around second 35).

Voice rules:
- No em dashes
- No "It's not X, it's Y" structures
- No "Most guys / most women / most people" openers
- No "obsessed", "game-changing", "transformational"
- No three-word stacked closers
- No two-fragment contrast
- Use contractions, fragments, casual disagreement
- The expert explains difficult concepts simply, like talking to a friend at a bar

Pull verbatim phrases from customer research where possible. Mark any line that needs verbatim source material with [VERBATIM-NEEDED].
```

## Prompt 4: Skit Conversation Script (Skeptic + Believer)

Use this for 30-45 second skits in fast-scrolling environments (TikTok, Reels). Actor A dismisses the category. Actor B reveals the discovery. The conversation feels overheard, not performed.

```
Write a 30 to 45 second skit conversation script.

Persona:
[persona]

Insight:
[the discovery moment that converts the skeptic]

Product:
[product + 1-line description]

Format:
Two-actor skit.

Actor A:
skeptic, voices the audience's pushback

Actor B:
believer who discovered something, casual and a little smug

Structure:

1. Actor A dismisses the category
2. Actor B reveals the discovery
3. Actor A pushes back
4. Actor B responds with specifics
5. Actor A converts (small reaction, not a sales conversion)
6. Actor B references the product softly

Output:
- HOOK (Actor A's first line)
- Full script with A/B labels per line
- Visual notes (setting cue, gesture, expression, prop)
- Estimated runtime

Constraint:
Dialogue must feel overheard, not scripted.

Use:
- Contractions (you're, don't, can't, I'm)
- Interruptions (Actor A cuts off Actor B mid-sentence)
- Fragments (incomplete sentences, especially in dismissive Actor A lines)
- Casual disagreement ("come on", "yeah right", "wait what")
- Backtracking ("I mean, not really, but...")

Voice rules:
- No em dashes
- No "It's not X, it's Y" structures
- No "Most guys / most women / most people" openers
- No "obsessed", "game-changing", "transformational"
- The product enters as a soft reference, not a pitch
- Lines maximum 2 sentences
- Each line under 4 seconds when read aloud

Pull verbatim phrases from customer research where possible.
```

## Worked example: Podcast clip output

For a male hormone health product (mechanism: cortisol binding testosterone):

```
HOOK (HOST, 0:00-0:04):
"Why do guys in their 40s lose interest in their wives even when they still love them?"

EXPERT (0:04-0:08):
"It's usually not psychological. It's biological."

EXPERT (0:08-0:14):
"The body converts testosterone into estrogen through aromatase, and belly fat accelerates it."

HOST (0:14-0:18):
"But people just say 'take Viagra.'"

EXPERT (0:18-0:24):
"Viagra changes blood flow temporarily. The conversion still happens every day."

EXPERT (0:24-0:30):
"There's a category of supplements that actually addresses the conversion at the source."

EXPERT (0:30-0:35):
"The one I've been recommending is [Brand]."

HOST (0:35-0:40):
"And that actually works long-term?"

EXPERT (0:40-0:48):
"It changes the underlying biology. Most men feel the difference within six weeks."

CLOSING (EXPERT, 0:48-0:55):
"That's the part most guys never hear. The fix isn't in the bedroom. It's in the bloodstream."

VISUAL NOTES:
- Two-shot or split-screen with host and expert
- Mics visible (sells the podcast format)
- Studio backdrop, even if faked
- Expert in casual professional (button-up, no tie)
- Host in t-shirt or casual sweater
- Cuts to b-roll of testosterone/aromatase diagram during line 4 (the mechanism explanation)

ESTIMATED RUNTIME: 55 seconds.

NOTES:
- Mechanism enters at line 4 (second 8)
- Product enters at line 8 (second 32) which is 58% of runtime, in line with two-actor format rules
- Voice register stays calm and explanatory throughout
- No banned phrases, no em dashes
```

## Worked example: Skit conversation output

For a skincare product (mechanism: most collagen products do not survive digestion):

```
HOOK (ACTOR A, 0:00-0:03):
"Collagen supplements are a scam."

ACTOR B (0:03-0:08):
"Most are. But there's one that actually works because of how it's structured."

ACTOR A (0:08-0:11):
"Yeah right."

ACTOR B (0:11-0:18):
"My skin's been crazy for a month. I haven't changed anything else."

ACTOR A (0:18-0:21):
"Like, what kind of crazy?"

ACTOR B (0:21-0:28):
"Texture. Like the pores around my nose just... I don't know how to describe it."

ACTOR A (0:28-0:31):
"Wait, you're serious?"

ACTOR B (0:31-0:38):
"It's the bonded form. Most collagen breaks down in your stomach. This one doesn't."

ACTOR A (0:38-0:42):
"Send me the link."

ACTOR B (0:42-0:45):
"It's [Brand]. The one with the white packaging."

VISUAL NOTES:
- Setting: kitchen counter, both actors casual (sweatshirts, no makeup-look)
- Phone-camera framing (not professional)
- Actor A leaning on counter, scrolling phone
- Actor B making coffee
- Natural light from window

ESTIMATED RUNTIME: 45 seconds.

NOTES:
- Hook is dismissal of the category (Actor A's first line)
- Believer's discovery uses self-correction ("Texture. Like the pores around my nose just... I don't know how to describe it.")
- Skeptic's conversion is small ("Wait, you're serious?") not full ("OMG I need this!")
- Product reference is soft ("It's [Brand]. The one with the white packaging.")
- Mechanism (line 8: "It's the bonded form. Most collagen breaks down in your stomach.") enters before product reference
- Used contractions, fragment, casual disagreement
- No banned phrases, no em dashes
```

## Common failure modes when running these prompts

### The expert sounds like a brochure

The model defaults to clinical-sounding mechanism explanations.

**Fix:** Add to the prompt: "The expert explains the mechanism the way they would explain it to a friend at a bar, not the way a textbook explains it. Imagine the expert at a casual dinner."

### The skit feels staged

Both actors speak in complete polished sentences with no interruptions or fragments.

**Fix:** Add to the prompt: "Use at least 2 fragments per script. At least 1 self-correction. At least 1 interruption (one actor cuts the other off mid-sentence)."

### The product enters too early

The mechanism gets explained, then the product gets named in the next line, taking only 30 percent of runtime.

**Fix:** Add to the prompt: "The product cannot appear before line 8. Add an objection and an objection handle between the mechanism explanation and the product mention."

### The hook is a category statement

The host or Actor A opens with a generalization ("Most men in their 40s lose their drive.")

**Fix:** Replace with a specific question or specific dismissal. "Why do guys in their 40s lose interest..." or "Collagen supplements are a scam."

### The visual notes are missing

The model produces dialogue but no visual cues.

**Fix:** Add to the prompt: "Output visual notes after EACH line, not just at the end. Include camera angle, prop, gesture, or expression."

## Cross-references

- Format explanation (when to use, why it works): [../references/two-actor-formats.md](../references/two-actor-formats.md)
- Voice rules: [../references/direct-response-voice-system.md](../references/direct-response-voice-system.md)
- Anti-AI script tells (especially the dialogue tells): [../references/anti-ai-script-tells.md](../references/anti-ai-script-tells.md)
- Hook engineering (for the host's first line / Actor A's first line): [../references/hook-engineering.md](../references/hook-engineering.md)
- Script reviewer (run on the output before production): [script-reviewer.md](script-reviewer.md)
