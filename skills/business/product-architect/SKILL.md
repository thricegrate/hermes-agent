---
name: product-architect
description: Designs the complete curriculum and module structure for a low-ticket digital product ($9-$350). Use when user wants to outline a course, structure a digital product, plan modules and lessons, or design a curriculum.
---

# Product Architect

## Prerequisites

- A validated product idea brief (from `niche-finder` or user-provided)
- Must include: niche, primary problem, target customer, and desirable outcome
- Optional: existing content, blog posts, or frameworks the user wants to incorporate

## References

- `references/cole-curriculum-framework.md`: Cole's "Action > Learning" principle, 5-Step Curriculum Outline, Perfect Course Module Framework (7 sections per module), V1-to-V2 naming progression, sizing guidelines (10-20 modules, 2K words/module minimum)
- `references/yc-seibel-mvp.md`: YC MVP framework -- core hypothesis identification ("What ONE thing must be true?"), feature prioritization via the "Remove It" test, launch velocity > feature completeness, "do things that don't scale" principle, Build-Measure-Learn cycle (3 days build, 2-3 days measure, 1 day decide). Essential for fast-iteration app development.

## Workflow

### Step 1: Define the Transformation Arc

Before outlining modules, define where the student starts and where they end.

**Ask the user:**
- "Where is your customer RIGHT NOW?" (their current painful state)
- "Where will they be AFTER completing your product?" (the promised transformation)

**Format:**
```
FROM: [Current painful state - specific and measurable]
TO: [Desired outcome - specific and measurable]
```

**Example:**
- FROM: "I want to write online but I'm paralyzed by perfectionism, I don't know what platform to use, and I can't stay consistent."
- TO: "I've published 30 pieces of online writing in 30 days, built a writing habit, and know exactly what platform works for me."

### Step 2: Break Into 3-7 Modules

Each module should represent one major milestone on the transformation journey.

**Module design rules:**
- 3-7 modules total (fewer = focused, more = overwhelming)
- Each module has ONE clear learning outcome
- Modules build on each other sequentially
- First module removes the biggest mental/knowledge barrier
- Last module delivers the "victory lap" or final deliverable

**Module structure template:**
```
Module [N]: [Name]
- Learning Outcome: [What the student can DO after this module]
- Key Concept: [The one big idea]
- Lessons: [3-5 lessons]
- Exercise: [What they produce/practice]
```

### Step 3: Design Lessons Within Each Module

Each module contains 3-5 lessons. Each lesson teaches ONE concept or skill.

**Lesson types:**
- **Concept lesson** - Teaches a framework, model, or way of thinking
- **Tutorial lesson** - Step-by-step walkthrough of a process
- **Example lesson** - Shows real-world examples with breakdowns
- **Exercise lesson** - Guided practice with a specific deliverable

**Lesson format:**
```
Lesson [N.M]: [Title]
- Type: [Concept / Tutorial / Example / Exercise]
- Duration: [Estimated read/watch time]
- Format: [Text / Video / Both]
- Key takeaway: [One sentence]
```

### Step 4: Add Exercises and Deliverables

Every module should have at least one exercise that produces a tangible output.

**Exercise design principles:**
- Should be completable in 15-30 minutes
- Produces something concrete (a document, a list, a draft, a plan)
- Builds toward the final transformation
- Can be shared for feedback (in Skool community or elsewhere)

### Step 5: Structure the Curriculum Document

Compile everything into a complete curriculum outline:

```
## [Product Name] - Curriculum Outline

### Transformation
FROM: [X]
TO: [X]

### Module 1: [Name]
**Learning Outcome:** [X]
- Lesson 1.1: [Title] ([Type], [Duration])
- Lesson 1.2: [Title] ([Type], [Duration])
- Lesson 1.3: [Title] ([Type], [Duration])
- Exercise: [Description] -> Deliverable: [What they produce]

### Module 2: [Name]
...

### Module [N]: [Name]
...

### Total Estimated Completion Time: [X hours]
```

### Step 6: Add a "Start Here" Module

Prepend a brief onboarding module:
- Welcome and what to expect
- How to navigate the product (Skool/Notion)
- How to get the most out of the material
- Community introduction (if applicable)

## Integration

- **Input from:** `niche-finder` (product idea brief), `presell-validator` (validated idea + demand proof + waitlist data)
- **Output feeds into:** `product-writer` (to write the actual content), `product-offer` (curriculum informs pricing justification)
