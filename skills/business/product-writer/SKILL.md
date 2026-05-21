---
name: product-writer
description: Writes the actual lesson content for a low-ticket digital product module by module. Use when user wants to write course content, create lesson material, draft module text, or produce educational content for their digital product.
---

# Product Writer

## Prerequisites

- A complete curriculum outline (from `product-architect` or user-provided)
- Must include: module names, lesson titles, lesson types, and exercise descriptions
- Optional: the user's existing writing samples, voice/tone preferences, or reference content

## Workflow

### Step 1: Confirm Scope and Voice

Before writing, clarify:
- **Which module(s)** to write (one at a time recommended)
- **Format:** Text-only, or text + video script outline?
- **Voice/tone:** Professional, conversational, motivational, no-BS? Ask for a writing sample if available.
- **Length per lesson:** Default is 800-2000 words per lesson

### Step 2: Write Module Introduction

Every module opens with a brief intro (150-300 words):
- What this module covers
- Why it matters (connect to the overall transformation)
- What the student will be able to DO after completing it
- Quick overview of the lessons ahead

### Step 3: Write Each Lesson

Follow this structure per lesson:

**For Concept Lessons:**
1. Hook - Why this matters right now (2-3 sentences)
2. Core concept/framework - The big idea with a clear name
3. Explanation - Break it down simply
4. Example - Show it in action (real or realistic)
5. Common mistakes - What to avoid
6. Key takeaway - One sentence summary

**For Tutorial Lessons:**
1. What you'll accomplish in this lesson
2. Prerequisites/setup (if any)
3. Step-by-step instructions (numbered, clear)
4. Screenshots/visuals notes (describe what visual aids would be helpful)
5. Expected result - What it looks like when done right
6. Troubleshooting - Common issues and fixes

**For Example Lessons:**
1. Context - Why this example was chosen
2. The example itself (full walkthrough)
3. Breakdown - What makes it work (annotated)
4. How to apply it to their situation
5. Variations - How to adapt it

**For Exercise Lessons:**
1. Exercise objective (what they'll produce)
2. Step-by-step instructions
3. Template or starting framework (if applicable)
4. Time estimate
5. Completion criteria - How they know they're done
6. Optional: sharing prompt for community feedback

### Step 4: Write Module Exercise

Each module ends with a hands-on exercise:
- Clear objective and deliverable
- Step-by-step instructions
- Template if applicable
- Completion criteria

### Step 5: Write Module Wrap-Up

Close each module with (100-200 words):
- Recap of what they learned
- What they should have completed (exercise deliverable)
- Bridge to the next module (what's coming and why)

## Writing Style Guidelines

- **Teach through frameworks first, then examples.** Name the framework, explain it, show it.
- **Use "you" language.** Speak directly to the student.
- **One idea per paragraph.** Short paragraphs, scannable structure.
- **Bold key terms** on first use.
- **Use headers liberally.** Students should be able to skim and find what they need.
- **Include action items.** Tell them exactly what to DO, not just what to know.
- **Avoid filler.** Every sentence should teach, motivate, or instruct.

## Output Format

Output each lesson as a standalone section with clear headers:

```
# Module [N]: [Module Name]

## Introduction
[Module intro text]

## Lesson [N.1]: [Title]
[Full lesson content]

## Lesson [N.2]: [Title]
[Full lesson content]

...

## Exercise: [Exercise Name]
[Exercise instructions and template]

## Wrap-Up
[Module closing]
```

## Integration

- **Input from:** `product-architect` (curriculum outline)
- **Do NOT run through humanizer** - this is internal product content, not outward-facing marketing
