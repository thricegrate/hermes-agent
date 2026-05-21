# Curriculum Architecture: 28-Day AI Challenge

## Design Principles

1. **One tool per day, one concept per lesson.** No multi-tool days.
2. **Category rotation** prevents fatigue. Never two consecutive days in the same category.
3. **Spaced repetition** is built into the schedule, not bolted on.
4. **Progressive difficulty** follows Use-Modify-Create across 4 weeks.
5. **Each week has a theme** that maps to Bloom's Taxonomy.

---

## 28-Day Master Schedule

### Week 1: DISCOVER (Bloom's: Remember + Understand)
*Theme: "What can AI do?" — Survey the landscape, build confidence*
*Exercise type: Multiple choice only*
*UMC phase: USE*

| Day | Tool | Category | Concept Name | Learning Objective |
|-----|------|----------|-------------|-------------------|
| 1 | ChatGPT | Writing | The First Prompt | Write your first ChatGPT prompt and get a useful response |
| 2 | DALL-E | Images | Describe What You See | Understand that image AI needs visual descriptions, not abstract ideas |
| 3 | ChatGPT | Writing | The Role Prompt | Assign ChatGPT a professional role to get domain-specific output |
| 4 | Otter.ai | Save Time | Speaker Intelligence | Enable speaker identification to make transcripts searchable |
| 5 | DALL-E | Images | Style Anchoring Intro | Recognize that specific style references beat subjective adjectives |
| 6 | ChatGPT | Money | The Freelancer Prompt | Frame prompts to produce client-deliverable output |
| 7 | Gemini | Learning | The Research Prompt | Use Gemini to research a topic with source citations |

**Week 1 review days:** Day 3 reviews Day 1 concepts. Day 7 reviews Day 1 + Day 5 concepts.

### Week 2: APPLY (Bloom's: Apply)
*Theme: "Use AI for real tasks" — Complete real-world mini-projects*
*Exercise type: Fill-in-the-blank*
*UMC phase: USE (transitioning to MODIFY)*

| Day | Tool | Category | Concept Name | Learning Objective |
|-----|------|----------|-------------|-------------------|
| 8 | ChatGPT | Writing | The Tone Dial | Control output tone by specifying audience and formality level |
| 9 | Midjourney | Images | Composition Control | Use framing keywords (close-up, wide shot, bird's eye) to control image layout |
| 10 | ElevenLabs | Fun | Voice Cloning Basics | Clone a voice sample and generate speech in that voice |
| 11 | ChatGPT | Save Time | The Summary Prompt | Summarize long documents with structured output format |
| 12 | DALL-E | Images | Style Anchoring Advanced | Combine medium + era + reference for precise style control |
| 13 | Gemini | Learning | The Analysis Prompt | Have Gemini analyze data or compare options with structured reasoning |
| 14 | ChatGPT | Money | The Proposal Prompt | Generate client proposals that sound custom, not templated |

**Week 2 review days:** Day 8 reviews Day 6. Day 9 reviews Day 3 (N+6). Day 10 reviews Day 8 (N+2). Day 13 reviews Day 7 (N+6) + Day 1 (N+12 ≈ N+13).

### Week 3: ANALYZE (Bloom's: Analyze + Evaluate)
*Theme: "Why does this work?" — Compare approaches, debug prompts*
*Exercise type: Prompt rewrite*
*UMC phase: MODIFY*

| Day | Tool | Category | Concept Name | Learning Objective |
|-----|------|----------|-------------|-------------------|
| 15 | ChatGPT | Writing | The Specificity Ladder | Evaluate why specific prompts outperform vague ones by analyzing output differences |
| 16 | ChatGPT | Writing | The Constraint Prompt | Diagnose and fix generic output by adding measurable constraints |
| 17 | DALL-E | Images | The Negative Prompt | Improve images by specifying what to exclude, not just what to include |
| 18 | Midjourney | Images | Parameter Tuning | Evaluate how --stylize, --chaos, and --quality parameters change output |
| 19 | Otter.ai | Save Time | The Action Item Extract | Configure Otter to automatically extract action items and decisions |
| 20 | ElevenLabs | Fun | Voice Emotion Control | Analyze how voice settings (stability, similarity, style) affect perceived emotion |
| 21 | ChatGPT | Money | The Revision Prompt | Evaluate AI output critically and iterate systematically |

**Week 3 review days:** Day 15 reviews Day 9 (N+6). Day 16 reviews Day 3 (N+13). Day 17 reviews Day 11 (N+6) + Day 15 (N+2). Day 19 reviews Day 13 (N+6). Day 21 reviews Day 8 (N+13) + Day 15 (N+6).

### Week 4: CREATE (Bloom's: Create + Synthesize)
*Theme: "Build something real" — Multi-step workflows, tool combinations*
*Exercise type: Write from scratch*
*UMC phase: CREATE*

| Day | Tool | Category | Concept Name | Learning Objective |
|-----|------|----------|-------------|-------------------|
| 22 | ChatGPT + DALL-E | Writing + Images | The Content Pipeline | Build a blog post + header image using chained prompts |
| 23 | ChatGPT | Money | The Portfolio Piece | Create a complete, portfolio-ready deliverable from a client brief |
| 24 | Gemini + Otter.ai | Save Time + Learning | The Meeting Brain | Design a workflow: transcribe, summarize, extract actions, draft follow-up |
| 25 | DALL-E + Midjourney | Images | Style Consistency | Create a series of 3 images with consistent visual style across prompts |
| 26 | ElevenLabs + ChatGPT | Fun + Writing | The Audio Content | Write a script and convert it to professional narration |
| 27 | ChatGPT | Learning | The Learning System | Build a personal AI learning workflow combining 3+ concepts |
| 28 | All tools | All | The AI Toolkit | Design your personal AI toolkit — which tools for which tasks |

**Week 4 review days:** Day 22 reviews Day 16 (N+6) + Day 9 (N+13). Day 24 reviews Day 11 (N+13) + Day 18 (N+6). Day 27 reviews Day 14 (N+13) + Day 21 (N+6). Day 28 reviews Day 1 (N+27) — full circle.

---

## Category Rotation Pattern

The schedule follows a rotation to prevent fatigue and maintain variety:

```
Week 1: Writing → Images → Writing → Save Time → Images → Money → Learning
Week 2: Writing → Images → Fun → Save Time → Images → Learning → Money
Week 3: Writing → Writing → Images → Images → Save Time → Fun → Money
Week 4: Writing+Images → Money → Save Time+Learning → Images → Fun+Writing → Learning → All
```

**Rules:**
- No more than 2 consecutive days in the same category
- Every category appears at least 3 times across 28 days
- Writing and Images get the most coverage (highest learner demand)
- Fun and Learning are intermixed to prevent all-work fatigue

**Category distribution across 28 days:**

| Category | Days | Count |
|----------|------|-------|
| Writing | 1, 3, 6, 8, 11, 15, 16, 21, 22, 23, 26, 27 | 12 |
| Images | 2, 5, 9, 12, 17, 18, 22, 25 | 8 |
| Save Time | 4, 11, 19, 24 | 4 |
| Money | 6, 14, 21, 23 | 4 |
| Fun | 10, 20, 26 | 3 |
| Learning | 7, 13, 24, 27, 28 | 5 |

*Note: Some Day 22+ lessons span two categories due to multi-tool exercises.*

---

## Spaced Repetition Schedule

### Retrieval Intervals

| Review | Interval | Retention Target | Exercise Format |
|--------|----------|-----------------|-----------------|
| R1 | N+2 days | ~90% (short-term) | Multiple choice referencing original concept |
| R2 | N+6 days | ~75% (medium-term) | Apply concept in a NEW context or different tool |
| R3 | N+13 days | ~60% (long-term) | Combine with another concept learned since |
| R4 | N+27 days | ~50% (mastery) | Use in a multi-step workflow (Day 28 only) |

### How Reviews Are Embedded

Reviews are NOT separate lessons. They are woven into new lessons as exercise context:

**Embedding patterns:**
1. **The hook references a prior concept:** "Remember The Role Prompt from Day 3? Today we're adding a second layer..."
2. **The exercise requires a prior concept:** "Write this prompt using both The Role Prompt AND today's Constraint Prompt"
3. **The before/after uses a prior concept as the 'before':** "Day 3's technique gets you here. Today's technique gets you here."

**Example — Day 9 reviewing Day 3 (N+6):**
```
Day 9 Concept: Composition Control (Midjourney)
Day 9 Exercise: "Write a Midjourney prompt for a product photo"

Review of Day 3 (Role Prompt) embedded:
"Before you write the image prompt, use ChatGPT with
The Role Prompt to generate the product description.
Then feed that description into Midjourney."

This forces retrieval of Day 3's concept in a new context.
```

### Full Review Map

```
Day  1 concepts reviewed on: Day 3, Day 7, Day 14, Day 28
Day  2 concepts reviewed on: Day 4, Day 8, Day 15
Day  3 concepts reviewed on: Day 5, Day 9, Day 16
Day  4 concepts reviewed on: Day 6, Day 10, Day 17
Day  5 concepts reviewed on: Day 7, Day 11, Day 18
Day  6 concepts reviewed on: Day 8, Day 12, Day 19
Day  7 concepts reviewed on: Day 9, Day 13, Day 20
Day  8 concepts reviewed on: Day 10, Day 14, Day 21
Day  9 concepts reviewed on: Day 11, Day 15, Day 22
Day 10 concepts reviewed on: Day 12, Day 16, Day 23
Day 11 concepts reviewed on: Day 13, Day 17, Day 24
Day 12 concepts reviewed on: Day 14, Day 18, Day 25
Day 13 concepts reviewed on: Day 15, Day 19, Day 26
Day 14 concepts reviewed on: Day 16, Day 20, Day 27
Day 15 concepts reviewed on: Day 17, Day 21, Day 28
Day 16-28: Reviews tail off naturally as the challenge ends
```

---

## Bloom's Taxonomy Mapping

### Detailed Verb Guide per Week

**Week 1 — Remember + Understand:**
- Identify which tool is best for a task
- Describe what a tool does in one sentence
- Explain the difference between two approaches
- Compare two outputs and identify the better one
- List the key settings for a tool

**Week 2 — Apply:**
- Use a prompt template to complete a real task
- Implement a technique to improve output quality
- Execute a multi-step tool configuration
- Demonstrate a concept by producing a specific output
- Complete a prompt by filling in the right element

**Week 3 — Analyze + Evaluate:**
- Compare two prompt approaches and explain why one works better
- Contrast the output of different parameter settings
- Critique a prompt and identify its specific weakness
- Improve a prompt by diagnosing and fixing one flaw
- Judge whether an AI output meets professional standards

**Week 4 — Create + Synthesize:**
- Design a complete prompt from a client brief
- Construct a multi-step workflow across tools
- Combine 2-3 learned concepts into one prompt
- Produce a portfolio-ready deliverable
- Build a personal AI toolkit matched to your goals

---

## Lesson Interconnection Map

Lessons build on each other. Here are the dependency chains:

```
The First Prompt (Day 1)
  └→ The Role Prompt (Day 3)
       └→ The Tone Dial (Day 8)
            └→ The Constraint Prompt (Day 16)
                 └→ The Portfolio Piece (Day 23)

Describe What You See (Day 2)
  └→ Style Anchoring Intro (Day 5)
       └→ Style Anchoring Advanced (Day 12)
            └→ The Negative Prompt (Day 17)
                 └→ Style Consistency (Day 25)

Speaker Intelligence (Day 4)
  └→ The Summary Prompt (Day 11)
       └→ The Action Item Extract (Day 19)
            └→ The Meeting Brain (Day 24)

The Freelancer Prompt (Day 6)
  └→ The Proposal Prompt (Day 14)
       └→ The Revision Prompt (Day 21)
            └→ The Portfolio Piece (Day 23)
```

Each arrow means "the later lesson assumes the earlier concept is known." This is why spaced repetition reviews are critical — they keep earlier concepts fresh when the dependent lesson arrives.

---

## Daily Lesson Word Budget

Total budget: ~600 words per lesson (3 minutes at 200 WPM)

| Block | Words | % of Total |
|-------|-------|-----------|
| Hook | 40 | 7% |
| Concept (name + principle) | 60 | 10% |
| Concept (before/after) | 200 | 33% |
| Exercise (prompt + context) | 150 | 25% |
| Result reveal | 100 | 17% |
| CTA | 40 | 7% |
| **Total** | **590** | **~100%** |

**Hard limits:**
- Hook: 40 words max
- CTA: 40 words max
- Total lesson: 650 words absolute max
- If the before/after example is long, shorten the exercise context
- Interactive elements (tapping, selecting) don't count toward word budget
