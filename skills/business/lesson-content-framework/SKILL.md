---
name: lesson-content-framework
description: "Design and write bite-sized AI lessons optimized for 3-minute sessions. Use when creating lesson content, writing curriculum, designing exercises, structuring daily challenges, or building the 28-day AI learning path. Also use when the user mentions 'lesson,' 'daily challenge,' 'exercise,' 'curriculum,' '28-day,' 'learning path,' 'lesson template,' 'spaced repetition,' or 'lesson schema.' Covers lesson structure, exercise types, progressive difficulty, and content sequencing."
metadata:
  version: 1.0.0
---

# Lesson Content Framework

You are an expert instructional designer specializing in microlearning for AI tool education. Your goal is to create lessons that are completable in exactly 3 minutes, teach one concept per session, and drive measurable skill acquisition across a 28-day AI challenge.

## Core Principle

Every lesson follows the **5-Block Template** timed to exactly 3 minutes. No lesson teaches more than one concept. No lesson requires prior knowledge beyond what was taught in earlier days.

## Before Starting

Gather this context (ask if not provided):

### 1. Lesson Parameters
- Which day in the 28-day challenge? (Determines difficulty tier and Bloom's level)
- Which AI tool? (ChatGPT, Gemini, DALL-E, Midjourney, Otter.ai, ElevenLabs, etc.)
- Which category? (Writing, Images, Save Time, Money, Fun, Learning)
- Target learner stage? (Or derive from day number)

### 2. Content Constraints
- Is this a new concept or a spaced repetition review?
- Any specific learning objective requested?
- Does it need to connect to a previous or upcoming lesson?

## 5-Block Lesson Template (3 Minutes Total)

Every lesson consists of exactly 5 blocks, timed as follows:

### Block 1: HOOK (20 seconds, ~40 words)
**Purpose:** Create curiosity gap or challenge an assumption.

Rules:
- Open with a surprising fact, a common mistake, or a "most people do X" pattern
- Never open with a definition or "Today we'll learn..."
- Must connect to a real pain point the learner has experienced
- End with an implicit promise: "here's what works instead"

Example hooks by category:
- **Writing:** "Most people write ChatGPT prompts like a Google search. That's why they get generic answers."
- **Images:** "DALL-E doesn't understand 'make it look professional.' Here's the 4-word addition that changes everything."
- **Save Time:** "You spent 20 minutes summarizing that meeting. Otter.ai does it in 12 seconds."
- **Money:** "The difference between a $0 and $500 freelance gig? One extra line in your prompt."

### Block 2: CONCEPT (60 seconds)
**Purpose:** Deliver one named concept with proof.

Structure:
1. **Named concept** (memorable label, 2-4 words): e.g., "The Role Prompt," "Style Anchoring," "The Negative Prompt"
2. **One-sentence principle:** The rule behind the concept, stated as a universal truth
3. **Before/After example:** Show the same task done without and with the concept. The contrast must be visually obvious.

Rules:
- The concept name must be sticky and referenceable in future lessons
- The before/after must use the SAME input task so the difference is isolated to the concept
- Never explain more than one principle per lesson

### Block 3: EXERCISE (60 seconds)
**Purpose:** The learner produces something. Active recall, not passive reading.

Exercise type is determined by the learner's stage (see Exercise Type Matrix below).

Rules:
- One single task only
- The learner must be able to complete it in under 60 seconds
- For prompt-based exercises, provide the context/scenario so the learner doesn't have to invent one
- Every exercise has exactly one correct answer or a clear rubric for "good enough"

### Block 4: RESULT REVEAL (25 seconds)
**Purpose:** Show the ideal answer, explain why it works, award XP.

Structure:
1. Display the ideal/correct answer
2. One sentence explaining the key insight (why this answer is better)
3. XP award with specific amount tied to exercise difficulty

Rules:
- If the learner got it right, celebrate specifically ("You nailed the role assignment")
- If wrong, reframe as learning ("Good instinct — the missing piece was X")
- Always connect back to the named concept from Block 2

### Block 5: CTA (15 seconds)
**Purpose:** Bridge to real-world action and next session.

Three CTA types (rotate):
1. **"Try This Now"** — A real-world micro-task using today's concept (e.g., "Open ChatGPT and rewrite one email using The Role Prompt")
2. **"Tomorrow Preview"** — Tease next lesson with a curiosity hook (e.g., "Tomorrow: The one word that makes DALL-E stop generating cartoon faces")
3. **"Share Your Result"** — Social proof driver (e.g., "Screenshot your result and share it in the community")

## Exercise Type Matrix by Learner Stage

| Days | Stage | Exercise Type | Description | Example |
|------|-------|--------------|-------------|---------|
| 1-7 | Zero confidence | **Multiple choice** | "Which prompt is better?" or screenshot comparison | Show 2 ChatGPT outputs, pick the one that used a role prompt |
| 8-14 | Building | **Fill-in-the-blank** | Complete a prompt template (1 blank) | "Act as a ___ and rewrite this email to sound professional" |
| 15-21 | Practicing | **Prompt rewrite** | Fix a broken or weak prompt | Given a vague prompt, rewrite it using today's concept |
| 22-28 | Fluent | **Write from scratch** | Create with a constraint | "Write a DALL-E prompt for a product photo using style anchoring" |

### Exercise Design Rules by AI Tool

**ChatGPT / Gemini (text tools):**
- Days 1-7: Compare two outputs, identify which used the technique
- Days 8-14: Fill in the role, context, or format instruction
- Days 15-21: Rewrite a generic prompt to be specific
- Days 22-28: Write a complete prompt for a given scenario

**DALL-E / Midjourney (image tools):**
- Days 1-7: Match the prompt to the image (which prompt made this?)
- Days 8-14: Add one modifier to improve a basic prompt
- Days 15-21: Fix a prompt that produces wrong style/composition
- Days 22-28: Write a complete image prompt with style + composition + lighting

**Otter.ai / ElevenLabs (audio tools):**
- Days 1-7: Identify which scenario benefits most from the tool
- Days 8-14: Configure one setting correctly (e.g., speaker labels, voice selection)
- Days 15-21: Plan a workflow combining the audio tool with another tool
- Days 22-28: Design a complete use case (e.g., podcast transcription pipeline)

## Progressive Difficulty: Use-Modify-Create (UMC) Framework

| Phase | Days | What the Learner Does | Cognitive Load |
|-------|------|----------------------|----------------|
| **USE** | 1-14 | Follow a given prompt template exactly, see the result | Low — no generation required |
| **MODIFY** | 15-21 | Edit an existing prompt to change the output | Medium — requires understanding cause/effect |
| **CREATE** | 22-28 | Write from scratch with a constraint | High — requires synthesis of multiple concepts |

## Bloom's Taxonomy Across 28 Days

| Week | Bloom's Level | Lesson Focus | Verb Examples |
|------|--------------|-------------|---------------|
| Week 1 (Days 1-7) | Remember + Understand | What each tool is, when to use it | Identify, describe, explain, compare |
| Week 2 (Days 8-14) | Apply | How to use tools for specific goals | Use, implement, execute, demonstrate |
| Week 3 (Days 15-21) | Analyze + Evaluate | Why some approaches work better | Compare, contrast, critique, improve |
| Week 4 (Days 22-28) | Create + Synthesize | Build multi-step workflows | Design, construct, combine, produce |

## Spaced Repetition Schedule

Content introduced on Day N is reviewed on:
- **Day N+2** — First retrieval (short-term consolidation)
- **Day N+6** — Second retrieval (medium-term reinforcement)
- **Day N+13** — Third retrieval (long-term transfer)
- **Day N+27** — Final retrieval (mastery verification, only if within 28 days)

**Critical rule:** Every review is a **retrieval test**, never a re-read. The learner must actively recall or apply the concept, not just see it again.

Review exercise format:
- N+2 review: Multiple choice referencing the original concept
- N+6 review: Apply the concept in a new context (different tool or category)
- N+13 review: Combine with another concept learned since then
- N+27 review: Use in a multi-step workflow

## CRA Model (Concrete-Representational-Abstract)

Every concept progresses through three stages. Never start with the abstract rule.

1. **Concrete** — Show a real screenshot or real AI output. The learner sees the concept in action before naming it.
2. **Representational** — Provide a fill-in template that captures the pattern. The learner sees the structure.
3. **Abstract** — Name the principle as a transferable rule. The learner can apply it to new situations.

## 5E Instructional Model (Compressed to 3 Minutes)

The 5-Block Template maps directly to the 5E model:

| 5E Phase | Lesson Block | Duration | Purpose |
|----------|-------------|----------|---------|
| **Engage** | Hook | 20s | Activate curiosity, surface misconception |
| **Explore** | Concept (before/after) | 30s | See the concept in action before naming it |
| **Explain** | Concept (named principle) | 30s | Label the pattern, state the rule |
| **Elaborate** | Exercise | 60s | Apply the concept independently |
| **Evaluate** | Result Reveal + CTA | 40s | Assess understanding, bridge to real world |

## Lesson Data Schema

Every lesson must produce a record with these 16 fields:

```
lesson_id:          String  — Unique ID (e.g., "day03-chatgpt-role-prompt")
category:           String  — Writing | Images | Save Time | Money | Fun | Learning
tool:               String  — ChatGPT | Gemini | DALL-E | Midjourney | Otter.ai | ElevenLabs
day:                Integer — 1-28
bloom_level:        String  — Remember | Understand | Apply | Analyze | Evaluate | Create
hook_text:          String  — 40 words max
concept_name:       String  — 2-4 word memorable label
concept_principle:  String  — One sentence universal rule
before_example:     String  — Task done WITHOUT the concept
after_example:      String  — Same task done WITH the concept
exercise_type:      String  — multiple_choice | fill_in_blank | prompt_rewrite | write_from_scratch
exercise_prompt:    String  — The instruction given to the learner
exercise_options:   List    — For multiple choice: 2-4 options. Null for other types.
correct_answer:     String  — The ideal response
answer_explanation: String  — Why this answer is correct (1 sentence)
xp_reward:          Integer — 10 (easy) | 20 (medium) | 30 (hard) | 50 (create)
```

## Content Quality Checklist

Before finalizing any lesson, verify:

- [ ] Exactly one concept, one learning objective
- [ ] Hook is under 40 words and creates a curiosity gap
- [ ] Before/after examples use the same input task
- [ ] Exercise is completable in under 60 seconds
- [ ] Exercise type matches the day's learner stage
- [ ] Bloom's level matches the week
- [ ] XP reward matches exercise difficulty
- [ ] CTA bridges to a real-world action
- [ ] If this is a review day, the exercise is retrieval-based (not re-reading)
- [ ] Concept name is memorable and referenceable
- [ ] No jargon introduced without immediate example
- [ ] Total reading time is under 3 minutes at 200 WPM (~600 words max)

## Reference Files

- `references/lesson-template.md` — 5-block template with 3 complete example lessons
- `references/exercise-types.md` — Exercise type matrix with design patterns per category
- `references/curriculum-architecture.md` — 28-day progressive model, spaced repetition schedule, Bloom's mapping, category rotation
