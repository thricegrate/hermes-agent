# Mental Models & Problem-Solving

## Table of Contents
1. [5 Whys](#5-whys)
2. [Elon Musk's 5-Step Algorithm](#elon-musks-5-step-algorithm)
3. [First Principles Thinking](#first-principles-thinking)
4. [Second-Order Thinking](#second-order-thinking)
5. [Inversion Thinking](#inversion-thinking)
6. [Confirmation Bias](#confirmation-bias)
7. [Margin of Safety](#margin-of-safety)
8. [Leverage](#leverage)
9. [Map Is Not the Territory](#map-is-not-the-territory)
10. [Pareto Principle](#pareto-principle-8020)
11. [Additional Models](#additional-models)
12. [Application Methods](#application-methods)

---

## 5 Whys

Iterative root cause analysis. Ask "Why?" at least 5 times to get past symptoms to the real problem.

**Process:**
1. State the problem
2. Ask "Why?": get the first-level cause
3. Ask "Why?" again: dig deeper
4. Repeat until you reach a cause you can actually fix
5. Verify the chain: "If we fix [root cause], does the chain break?"

**Example:**
```
Problem: Agency clients keep leaving after 2-3 months

Why? → They don't see results
Why? → We don't have clear KPIs or reporting
Why? → We never set expectations during onboarding
Why? → We don't have an onboarding process
Why? → We've been too busy servicing clients to build systems

Root cause: No investment in systems/SOPs
Fix: Dedicate 2 hours/week to building onboarding SOP
```

**Rules:**
- Stay on one causal chain: don't branch into multiple "whys"
- Each answer must be factual, not speculative
- The root cause should be something within your control to fix
- Pair with "Five Hows" for solutions once root cause is found

**Coaching usage:** When the user describes a problem, don't accept the surface-level version. Drill with 5 Whys before prescribing.

---

## Elon Musk's 5-Step Algorithm

A systematic approach to eliminating waste and improving processes:

| Step | Action | Key Question |
|------|--------|-------------|
| 1 | **Question every requirement** | "Who specifically asked for this? Why?" |
| 2 | **Delete any unnecessary part/process** | "If we removed this, what would actually break?" |
| 3 | **Simplify and optimize** | "How can we make this simpler?" |
| 4 | **Accelerate cycle time** | "How can we do this faster?" |
| 5 | **Automate** | "Now that it's simple and fast, can a machine do it?" |

**Critical rule:** Steps MUST be done in order. "The most common mistake is to optimize something that shouldn't exist."

**Applied to business processes:**
- Step 1: "Why do we do a weekly 2-hour team meeting?" → "Who required this?" → "Nobody, we just always have."
- Step 2: DELETE the meeting. Replace with async updates.
- Step 3: Simplify async updates to a 3-question Slack template.
- Step 4: Set a daily 5-minute standup for truly urgent items only.
- Step 5: Automate the Slack template with a bot that prompts at 9 AM.

**Coaching questions:**
- "Walk me through your process for [X]. Why does each step exist?"
- "If you deleted [step], what would actually happen?"
- "What are you doing because 'that's how we've always done it'?"

---

## First Principles Thinking

Decompose complex problems into fundamental truths, then reason up from there.

**Process:**
1. Identify the assumption or conventional wisdom
2. Break it down: "What do we know for CERTAIN is true?"
3. Rebuild from those truths, ignoring what everyone else does
4. Test the rebuilt logic against reality

**Elon Musk example:** "Rocket costs $65M" → First principles: materials cost 2% of that ($1.3M) → SpaceX builds rockets for a fraction of traditional cost.

**Business application:**
```
Conventional wisdom: "You need 100K subscribers to make $5K/mo from a newsletter"

First principles:
- $5K/mo ÷ $0.05/sub (ad network CPM) = 100K subs needed → TRUE at that CPM
- But what if we don't rely on ad networks?
- 500 subscribers × $10/mo paid tier = $5K/mo
- 1,000 subscribers × $50 course = $50K (one-time)
- $5K/mo can come from 500 highly engaged subscribers, not 100K passive ones

New strategy: Focus on subscriber QUALITY and direct monetization, not quantity
```

**Coaching trigger:** Use when the user says "everyone says..." or "the standard approach is..." or "you need to..." Challenge the premise.

---

## Second-Order Thinking

Ask "And then what?" to look past immediate consequences to long-term effects.

**First-order vs. second-order:**
| Decision | First-Order Effect | Second-Order Effect |
|----------|-------------------|-------------------|
| Lower newsletter price | More subscribers | Lower quality subscribers, lower LTV, worse ad rates |
| Launch 10 newsletters at once | More total revenue | Quality drops, brand dilutes, team burns out |
| Fire low-performing agency client | Less revenue short-term | Team morale improves, capacity freed for better client |
| Raise prices 3x | Lose some customers | Better customers stay, margins explode, results improve |

**Coaching usage:** Every time the user proposes an action, ask "And then what happens? What's the second-order effect?"

---

## Inversion Thinking

Instead of asking "How do I succeed?", ask "What would guarantee failure?" Then avoid those things.

**Process:**
1. State the goal
2. Invert: "What would GUARANTEE I fail at this?"
3. List every way to fail
4. Invert again: "Am I doing any of these?"
5. Stop doing the failure-guaranteeing things

**Example:**
```
Goal: Scale newsletter business to $100K/mo

What would GUARANTEE failure?
- Never systematize anything (stay founder-dependent)
- Ignore subscriber quality, optimize only for quantity
- Never measure revenue per subscriber
- Launch new newsletters before existing ones are profitable
- Don't invest in retention (leaky bucket)
- Keep doing everything yourself (never hire)

Am I doing any of these? → [honest self-assessment]
```

**Coaching prompt:** "Tell me your goal. Now tell me: what would GUARANTEE you fail? ... Are you doing any of those things right now?"

---

## Confirmation Bias

Our tendency to search for evidence that supports what we already believe.

**Counter-measures:**
1. **"Why might I be wrong?"**: Force yourself to argue the opposite
2. **"Why do I want this to be true?"**: Identify emotional attachment to the idea
3. **"If I were on the other side, what would I say?"**: Steel-man the opposition
4. **"What would convince me I'm wrong?"**: Define the falsification criteria in advance

**Business application:** Before any major decision (launch a new newsletter, hire someone, change pricing), run the confirmation bias check:
- "Am I looking for reasons to do this, or genuinely evaluating both sides?"
- "What data would make me NOT do this? Do I have that data?"
- "Get a second opinion from someone with no skin in the game."

---

## Margin of Safety

**Definition:** The ability of a system to withstand loads greater than expected. "Keep some powder dry."

**Business application:**
- Don't spend 100% of cash flow on growth: keep 3-6 months runway
- Don't depend on a single revenue stream: diversify
- Don't plan for best case: plan for realistic case minus 30%
- Don't hire at full capacity: build team to handle 70% of projected load

**Decision framework:** Before any major business decision:
1. What could go wrong?
2. How likely is it?
3. How would we survive if it happened?
4. Do we have a hedge?

**Coaching question:** "What's your margin of safety right now? If your biggest revenue source disappeared tomorrow, how long do you survive?"

---

## Leverage

Small inputs that produce disproportionate outputs. The force multiplier.

**Types of business leverage:**
| Leverage Type | Description | Example |
|--------------|-------------|---------|
| **Code/Software** | Build once, serve infinite people | Newsletter automation, templates |
| **Media/Content** | Create once, reaches unlimited audience | Evergreen blog posts, YouTube videos |
| **Capital** | Money working for you | Paid ads with positive ROAS |
| **People** | Others doing work you've designed | Team executing your SOPs |
| **Network** | Relationships that compound | Co-promotion partnerships, referral networks |

**Key insight (Naval Ravikant):** "Give me a lever long enough and a fulcrum on which to place it, and I shall move the world."

**Newsletter leverage:** Content is infinite leverage: write once, deliver to 100K+ subscribers. Your writing is the lever. Systems are the fulcrum.

**Coaching question:** "Where in your business does a small input create a massive output? Are you maximizing that?"

---

## Pareto Principle (80/20)

20% of efforts produce 80% of results.

**Applied to business decisions:**
- **Revenue**: Which 20% of offerings produce 80% of revenue? Double down.
- **Customers**: Which 20% of customers produce 80% of profit? Serve them better.
- **Content**: Which 20% of content generates 80% of subscribers? Create more of that.
- **Time**: Which 20% of activities produce 80% of outcomes? Protect and expand that time.
- **Problems**: Which 20% of issues cause 80% of headaches? Fix those first.

**Newsletter 80/20 audit:**
- Which newsletter generates the most revenue per hour invested?
- Which acquisition channel has the best CAC?
- Which content type gets the highest engagement?
- Which team member produces the most output per dollar?

**Coaching action:** "Run an 80/20 audit on your business. Show me the top 20% of everything."

---

## Additional Models

### Parkinson's Law
Work expands to fill the time allotted. Set aggressive deadlines.
- Newsletter draft in 2 hours, not 2 days
- Client deliverables in 1 week, not "whenever it's ready"
- Project timelines at 50% of what feels comfortable

### Opportunity Cost
Every choice has a cost, what are you NOT doing?
- Every hour on agency work is an hour NOT growing your newsletter portfolio
- Every dollar spent on newsletter #8 is a dollar NOT optimizing newsletter #1
- "What am I saying NO to by saying YES to this?"

### Circle of Competence
Operate where you have an edge. Know your boundaries.
- You know newsletters. You know AI content. That's your circle.
- Agency services for newsletters = inside your circle
- Agency services for e-commerce = outside your circle (avoid)

### Red Queen Hypothesis
Staying in the same place = falling behind. You must continuously evolve.
- Newsletter industry evolves fast (AI, algorithms, reader preferences)
- What worked 6 months ago may not work today
- Continuous experimentation is survival, not optional

---

## Application Methods

### 1. Socratic Questioning
Use a series of open-ended questions to stimulate critical thinking:
- "What do you mean by that?"
- "What evidence supports that?"
- "What would happen if the opposite were true?"
- "What are you assuming?"
- "What are the implications of that?"

### 2. Memorable Soundtracks
Create phrases that trigger the right mental model:
- "Keep some powder dry" → Margin of Safety
- "And then what?" → Second-Order Thinking
- "What's the number?" → Anti-vagueness, push for specifics
- "Delete before you optimize" → Musk's 5-Step
- "What would guarantee failure?" → Inversion

### 3. Frequent Retrospectives
After every major decision or project:
- What went well? (Keep doing)
- What didn't work? (Stop or change)
- What did we learn? (Improve the model)
- Which mental model would have helped? (Build the habit)

### Usage in coaching sessions
- **Start of session**: Pareto audit: what's the 20% that matters?
- **Problem identification**: 5 Whys: drill to root cause
- **Solution design**: First Principles: question assumptions
- **Solution validation**: Inversion + Second-Order Thinking: stress test
- **Decision making**: Confirmation Bias check: are we being honest?
- **Planning**: Margin of Safety: what if it goes wrong?
- **Process improvement**: Musk's 5-Step: question, delete, simplify, accelerate, automate
