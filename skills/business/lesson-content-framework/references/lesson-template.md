# 5-Block Lesson Template

## Template Structure

```
┌─────────────────────────────────────────┐
│ BLOCK 1: HOOK (20 seconds, ~40 words)   │
│ Pattern: Surprise / Misconception / Gap │
│ Never: "Today we'll learn..."           │
├─────────────────────────────────────────┤
│ BLOCK 2: CONCEPT (60 seconds)           │
│ 1. Named concept (2-4 words)            │
│ 2. One-sentence principle               │
│ 3. Before/After example (same task)     │
├─────────────────────────────────────────┤
│ BLOCK 3: EXERCISE (60 seconds)          │
│ Type: Based on learner stage            │
│ One task, one answer, < 60 seconds      │
├─────────────────────────────────────────┤
│ BLOCK 4: RESULT REVEAL (25 seconds)     │
│ Ideal answer + why + XP award           │
├─────────────────────────────────────────┤
│ BLOCK 5: CTA (15 seconds)              │
│ Try Now / Tomorrow Preview / Share       │
└─────────────────────────────────────────┘
```

---

## Example Lesson 1: ChatGPT / Writing (Day 3)

**Lesson ID:** `day03-chatgpt-role-prompt`
**Category:** Writing
**Tool:** ChatGPT
**Bloom's Level:** Understand
**Exercise Type:** Multiple choice (Days 1-7)

### Block 1: HOOK

> Most people write ChatGPT prompts like a Google search. That's why they get generic answers that sound like a Wikipedia article. There's a 5-word fix that changes everything.

*Word count: 32 | Read time: ~10 seconds*

### Block 2: CONCEPT

**Concept name:** The Role Prompt

**Principle:** When you assign ChatGPT a specific professional role, it activates domain-specific vocabulary, tone, and reasoning patterns that generic prompts never trigger.

**Before example:**
> **Prompt:** "Write an email asking for a deadline extension"
>
> **Output:** "Dear [Recipient], I am writing to request an extension on the deadline for [project]. Due to unforeseen circumstances, I would appreciate additional time to complete the work. Please let me know if this is possible. Thank you for your understanding."

**After example:**
> **Prompt:** "Act as a senior project manager. Write an email asking for a deadline extension"
>
> **Output:** "Hi Sarah, Quick flag on the Henderson deliverable — we hit a dependency blocker with the vendor API integration on Tuesday that pushed our critical path out by 3 days. I've already re-sequenced the remaining tasks to minimize impact. Requesting we move the deadline from Friday 3/14 to Wednesday 3/19. I can walk through the updated timeline on our 2pm sync. The quality bar stays the same — just need the runway."

*Read time: ~45 seconds*

### Block 3: EXERCISE

> **Which of these emails was written with a role prompt?**
>
> **Email A:** "I wanted to reach out regarding the upcoming deadline. Unfortunately, I need more time to complete the project. I apologize for any inconvenience this may cause and hope we can find a suitable arrangement."
>
> **Email B:** "Flagging a timeline risk on the Q2 campaign assets — the client's brand guidelines revision landed 4 days late, which compressed our design sprint. Recommending we push the internal review from Thursday to Monday. Creative quality won't take a hit. Happy to align on this in standup."

*Completion time: ~15 seconds*

### Block 4: RESULT REVEAL

> **Correct: Email B**
>
> Notice the specifics — "Q2 campaign assets," "4 days late," "Thursday to Monday." The Role Prompt made ChatGPT think like a project manager: concrete details, proactive solution, professional shorthand.
>
> **+10 XP**

### Block 5: CTA

> **Try this now:** Open ChatGPT and rewrite your last work email by starting with "Act as a [your job title]." Compare the two versions. The difference is immediate.

---

## Example Lesson 2: DALL-E / Images (Day 12)

**Lesson ID:** `day12-dalle-style-anchoring`
**Category:** Images
**Tool:** DALL-E
**Bloom's Level:** Apply
**Exercise Type:** Fill-in-the-blank (Days 8-14)

### Block 1: HOOK

> You type "a professional logo" into DALL-E and get clip art from 2003. The problem isn't DALL-E — it's that "professional" means nothing to an image model. Four extra words fix this permanently.

*Word count: 36 | Read time: ~12 seconds*

### Block 2: CONCEPT

**Concept name:** Style Anchoring

**Principle:** Image AI models produce dramatically better results when you anchor the visual style to a specific medium, era, or artistic reference instead of using subjective adjectives.

**Before example:**
> **Prompt:** "A professional coffee shop logo"
>
> **Result:** Generic clip-art style coffee cup with steam lines, default sans-serif font, looks like a free template from 2010.

**After example:**
> **Prompt:** "A coffee shop logo, minimal flat vector style, Scandinavian design, muted earth tones"
>
> **Result:** Clean geometric coffee cup icon, limited color palette (clay, cream, sage), balanced white space, looks like a real brand identity from a Copenhagen design studio.

*Read time: ~40 seconds*

### Block 3: EXERCISE

> **Complete this DALL-E prompt by filling in the style anchor:**
>
> You want a hero image for a tech startup's landing page. The brand is modern, clean, and premium.
>
> "A workspace with a laptop and coffee, __________ style, cool blue and white palette"
>
> Fill in the blank with a specific style anchor (medium + reference).

*Completion time: ~30 seconds*

### Block 4: RESULT REVEAL

> **Strong answers:**
> - "editorial photography, Apple product shoot" style
> - "minimal 3D render, Dribbble trending" style
> - "architectural photography, natural lighting" style
>
> **Weak answers:** "professional," "modern," "high quality" — these are subjective adjectives, not style anchors.
>
> The key: a style anchor names a **specific visual tradition** the model can reference. "Apple product shoot" gives DALL-E thousands of reference points. "Professional" gives it none.
>
> **+20 XP**

### Block 5: CTA

> **Tomorrow:** You'll learn The Negative Prompt — how telling DALL-E what NOT to include is sometimes more powerful than describing what you want. It's the difference between "a realistic portrait" and actually getting one.

---

## Example Lesson 3: Otter.ai / Save Time (Day 8)

**Lesson ID:** `day08-otter-speaker-labels`
**Category:** Save Time
**Tool:** Otter.ai
**Bloom's Level:** Apply
**Exercise Type:** Fill-in-the-blank (Days 8-14)

### Block 1: HOOK

> You recorded a 45-minute team meeting. Otter.ai transcribed it. But now you're scrolling through a wall of text with no idea who said what. One setting — turned off by default — makes transcripts actually usable.

*Word count: 38 | Read time: ~12 seconds*

### Block 2: CONCEPT

**Concept name:** Speaker Intelligence

**Principle:** Enabling speaker identification before recording transforms an unreadable transcript wall into a searchable, attributable meeting record where every statement is tied to its owner.

**Before example:**
> **Default Otter transcript:**
> "So I think we should push the launch to next week. Yeah that makes sense. But what about the press embargo? We already sent the press release. OK let's keep the original date then. Wait I disagree, the demo isn't ready..."
>
> *Result: 12 minutes scrolling to find who committed to what.*

**After example:**
> **With Speaker Intelligence enabled:**
> "**Sarah (PM):** I think we should push the launch to next week.
> **Dev (Engineering):** Yeah that makes sense.
> **Lisa (Marketing):** But what about the press embargo? We already sent the press release.
> **Sarah (PM):** OK let's keep the original date then.
> **Dev (Engineering):** Wait, I disagree — the demo isn't ready..."
>
> *Result: Search "Sarah" to find every decision the PM made. 30 seconds.*

*Read time: ~45 seconds*

### Block 3: EXERCISE

> **Complete this Otter.ai setup for a client meeting:**
>
> You're about to join a Zoom call with 3 people from a client's team. You want the transcript to show who said what.
>
> Step 1: Open Otter settings before the meeting
> Step 2: Enable __________
> Step 3: When prompted after the recording starts, __________ so Otter can distinguish voices
>
> Fill in both blanks.

*Completion time: ~30 seconds*

### Block 4: RESULT REVEAL

> **Correct answers:**
> - Blank 1: **Speaker identification** (or "Speaker labels")
> - Blank 2: **Name each speaker when they first talk** (or "Assign names to detected voices" / "Label each voice sample")
>
> The key insight: Speaker identification works best when you name speakers in the first 2 minutes while voices are fresh. If you wait until after the meeting, Otter has to guess, and accuracy drops from ~95% to ~70%.
>
> **+20 XP**

### Block 5: CTA

> **Try this now:** Before your next meeting, open Otter.ai, go to Settings, and enable Speaker Identification. When the meeting starts, tap each speaker's name as they first talk. Your transcript will go from a text wall to a searchable record.

---

## Writing Checklist for Each Block

### Hook Checklist
- [ ] Under 40 words
- [ ] Opens with surprise, misconception, or pain point
- [ ] Does NOT start with "Today we'll learn" or "In this lesson"
- [ ] Creates a curiosity gap that Block 2 resolves

### Concept Checklist
- [ ] Concept has a 2-4 word memorable name
- [ ] Principle is one sentence, stated as a universal truth
- [ ] Before/after uses the SAME task
- [ ] The improvement is visually obvious without explanation

### Exercise Checklist
- [ ] One task only
- [ ] Completable in under 60 seconds
- [ ] Type matches the learner's day range
- [ ] Context/scenario is provided (learner doesn't invent it)
- [ ] Has one clear correct answer or rubric

### Result Reveal Checklist
- [ ] Shows the ideal answer
- [ ] Explains WHY in one sentence
- [ ] References the named concept from Block 2
- [ ] Includes specific XP amount

### CTA Checklist
- [ ] Bridges to real-world action OR previews tomorrow
- [ ] Is specific enough to act on immediately
- [ ] Under 40 words

---

## Lesson Delivery Features (from Coursiv)

### Reading Mode Controls
Every lesson has accessibility controls in the header:
- **AA button** — 3 text size options (small/medium/large)
- **Bold toggle** — toggle all body text to bold
- **Paragraph size selector** — 3 spacing options (compact/normal/spacious)
- These persist per user session via local storage

### Audio Narration
- Every lesson has a "Listen" button alongside "Read"
- Speaker icon in header toggles audio playback
- Audio is text-to-speech (use ElevenLabs API)
- Useful for commute/exercise learning

### Difficulty Rating
After completing each lesson, user rates difficulty:
- 5-point scale: 1 "Too easy" ← → 3 "Just right" ← → 5 "Too difficult"
- Displayed as 5 clickable buttons below "You rock!" celebration
- Data feeds back into content team to calibrate lesson difficulty
- Store in Firestore per lesson per user

### Lesson Completion Celebration
- Green star badge with white checkmark (large, centered)
- "You rock!" heading
- Personalized subtitle: "Welcome to the 2026 28-Day AI Challenge! Can't wait to see you at the top!"
- Difficulty rating prompt
- Blue "Continue" button

### In-Lesson Quiz Questions
Some lessons include quiz questions between content blocks:
- Radio button options (3-4 choices)
- "Submit" button (disabled until selection)
- After submit: correct answer highlighted, explanation shown
- Quiz completion transitions to "Finish lesson" button

### Bookmark/Flag
- Small bookmark icon in lesson content
- Users can save specific lessons for later review
- Saved lessons appear in profile or library section

### Report an Issue
- Accessible from lesson view
- 5 checkbox options: "The spelling or grammar is incorrect", "Outdated content", "Translation error", "Incorrect answer", "Something else went wrong"
- Submit button (disabled until at least one selected)
