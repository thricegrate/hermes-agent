---
name: user-research
description: |
  Structured user research and customer interviews to validate ideas, understand audience needs,
  and prevent building things nobody wants. Covers interview design, question frameworks, analysis,
  and language mining. Use when user wants to talk to users, run customer interviews, validate
  an idea with real people, understand why something failed, survey their audience, do customer
  discovery, figure out what their audience actually wants, or says "talk to users," "user
  interviews," "customer research," "validate idea," "why did this fail," "understand audience,"
  "customer discovery," "audience research," "what do they want."
---

# User Research

Stop guessing what your audience wants. Talk to them. The coach app bombed because the audience wanted to learn AI, not get coached. That's a $0 lesson you can learn for free by asking 20 people the right questions before building anything.

This skill is based on Eric Migicovsky's YC framework (see `references/yc-migicovsky-talk-to-users.md`) plus practical adaptations for newsletter/product businesses.

## When to Use

- **Before building anything** -- validate the idea with real users first
- **After something fails** -- understand WHY it failed from users' perspective
- **When pivoting** -- figure out what direction to go next
- **When survey data is confusing** -- surveys tell you WHAT, interviews tell you WHY
- **When assumptions feel shaky** -- "I think they want X" needs proof

## When NOT to Use

- You already have strong quantitative signal (high conversion, repeat purchases)
- The product is live and performing well (use `newsletter-analyst` or `cro-funnel` instead)
- You need market sizing (use `niche-finder`)

## Prerequisites

- Access to your audience (email list, social followers, DM contacts, community members)
- A hypothesis about what they want or need (even a rough one)
- 30-60 minutes per interview, 10-20 interviews minimum

## Core Principle: Actions > Words > Intentions

What people DO is more reliable than what they SAY, which is more reliable than what they SAY THEY'LL DO.

- "I would totally buy that" = weak signal (intention)
- "I tried 3 other tools this month" = strong signal (action)
- "I already paid $50 for something similar" = strongest signal (past behavior)

Always ask about PAST behavior, not future intentions.

---

## Workflow

### Step 1: Define Your Research Goal

Before any interviews, answer these:

1. **What decision will this research inform?** (build/kill/pivot, pricing, positioning, feature priority)
2. **What's your current hypothesis?** (what do you THINK they want?)
3. **What would change your mind?** (what would make you kill the idea?)

Write these down. If you can't articulate them, you're not ready to interview.

### Step 2: Recruit Interviewees (10-20 people)

**Who to talk to:**
- Existing subscribers/customers who are ACTIVE (open emails, click links)
- People who signed up but DIDN'T buy (they're interested but something stopped them)
- People who unsubscribed or churned (painful but gold)
- People in your target audience who DON'T know you yet (unbiased perspective)

**How to recruit:**
- Email your list: "I'm building something new and need 15 minutes of your time. In exchange, [incentive]."
- DM active commenters on social
- Post in relevant communities
- Ask existing customers for referrals

**Sample sizes:**
- 5 interviews: enough to spot obvious patterns
- 10 interviews: enough for confident directional decisions
- 20 interviews: enough for nuanced segmentation
- 30+: diminishing returns for most decisions

### Step 3: Run the Interview

Use `templates/interview-guide.md` for the full script. Key principles:

**The Five Rules of User Interviews:**

1. **Ask about their life, not your idea.** Don't pitch. Don't explain what you're building. Ask about THEIR problems, THEIR workflow, THEIR frustrations.

2. **Ask about specifics, not generalities.** Not "Do you struggle with AI?" but "Tell me about the last time you tried to use AI for something and it didn't work out."

3. **Talk less, listen more.** Aim for 80/20 -- they talk 80% of the time. If you're talking more than 20%, you're interviewing wrong.

4. **Follow the energy.** When they light up or get frustrated, go deeper. "Tell me more about that." "Why was that frustrating?" "What did you do next?"

5. **Use the Five Whys.** When they give a surface answer, ask why. Then ask why again. Root causes live 3-5 layers deep.

**Question sequence (from `references/yc-migicovsky-talk-to-users.md`):**

Phase 1 -- Context (2-3 min):
- "What do you do day-to-day?"
- "How did you first hear about [topic/tool/category]?"

Phase 2 -- Problem Exploration (10-15 min):
- "Tell me about the last time you tried to [relevant activity]. Walk me through what happened."
- "What's the hardest part about [doing X]?"
- "Why is that hard?" (Five Whys from here)
- "How do you currently solve this?"
- "What don't you love about your current solution?"

Phase 3 -- Solution Discovery (5-10 min):
- "If you could wave a magic wand, what would change?"
- "Have you looked for better solutions? What happened?"
- "Would you pay for something that solved this? How much?"
- "What would make you switch from your current approach?"

Phase 4 -- Language Mining (2-3 min):
- Listen for the EXACT words they use to describe their problem
- Note emotional language, metaphors, specific phrases
- These become your copy, headlines, and positioning

### Step 4: Analyze Patterns

After 5+ interviews, patterns emerge. Track:

**Pattern Analysis Framework:**

| Category | What to Track | Signal Strength |
|----------|---------------|-----------------|
| Problems mentioned | Frequency across interviews | 5+ mentions = validated problem |
| Current solutions | What they already use/pay for | Willingness to spend = real need |
| Language patterns | Exact words/phrases repeated | 3+ people use same phrase = copy gold |
| Emotional moments | Where they got frustrated/excited | Emotional intensity = importance |
| Objections | Why they haven't solved it yet | These become your sales page objections to address |
| Segments | Different types of people with different needs | May need different products for different segments |

**Decision Framework:**

| Signal | What It Means | Action |
|--------|---------------|--------|
| 8/10+ describe same problem | Strong problem-market fit | BUILD -- address this specific problem |
| People already paying for alternatives | Validated willingness to pay | BUILD -- position against alternatives |
| Mixed problems, no clear pattern | Audience is too broad or problem is too vague | NARROW -- pick a segment, re-interview |
| "That sounds nice" but no past behavior | Vitamin, not painkiller | PIVOT -- find the painkiller |
| Strong problem but wrong audience | Right idea, wrong list | PIVOT audience OR reposition |
| Nobody cares | Dead idea | KILL -- move on |

### Step 5: Synthesize Into Action

Output a research summary using this format:

```
## User Research Summary

**Research Goal:** [What decision this informs]
**Interviews Completed:** [N]
**Date Range:** [When conducted]

### Top Findings
1. [Finding 1 -- with supporting quotes]
2. [Finding 2 -- with supporting quotes]
3. [Finding 3 -- with supporting quotes]

### Validated Problems (ranked by frequency + intensity)
1. [Problem] -- mentioned by [N/total] interviewees
2. [Problem] -- mentioned by [N/total] interviewees

### Language Bank
- "[Exact quote]" -- used by [N] people
- "[Exact quote]" -- used by [N] people

### Current Solutions They Use
- [Solution] -- [what they like/dislike about it]

### Decision
[BUILD / PIVOT / KILL] because [evidence-based reasoning]

### Next Steps
- [Specific actions based on findings]
```

Save to `private project research/[topic]-research-[date].md`.

---

## Integration with Other Skills

- **Before building:** user-research -> `presell-validator` -> `product-architect`
- **After failure:** user-research -> understand why -> `presell-validator` (re-validate)
- **For positioning:** user-research (language mining) -> `newsletter-positioner` or `product-offer`
- **For content:** user-research (problems + language) -> `content-strategy` or `newsletter-writer`

## Jobs to Be Done (JTBD) Output

When extracting from research, capture three job dimensions per persona or segment:

- **Functional job:** the task itself. What are they trying to accomplish in concrete terms?
- **Emotional job:** how they want to feel during or after the task (confident, relieved, smart, in control).
- **Social job:** how they want to be perceived by others (competent boss, trusted partner, savvy buyer).

A JTBD map prevents "vitamin not painkiller" mistakes. If a finding only has a functional job and no emotional or social pull, the willingness to pay is usually weak.

## Digital Watering Hole Mode (Mode 2)

Interviews are Mode 1. Mode 2 is mining online sources where customers speak without a filter: Reddit, G2/Capterra, Hacker News, app store reviews (1-3 star), LinkedIn posts, YouTube comments. Most engagements combine both. Pick Mode 2 when:
- The user has no list to interview yet
- You want unbiased perspectives (people who do not know you)
- You need raw language for copy (people speak more honestly in public than to a stranger on a call)

For source-by-source playbooks (where to search, what operators to use, what signals to capture per platform) and the watering hole synthesis template, see [corey-customer-research.md](references/corey-customer-research.md).

## References

- `references/yc-migicovsky-talk-to-users.md` -- Eric Migicovsky's YC framework (interview structure, question types, analysis methods)
- `references/corey-customer-research.md` -- Corey Haines (MIT): two-mode framework (asset analysis + watering hole mining), JTBD extraction, persona structure, source guides by ICP type, research quality guardrails

## Templates

- `templates/interview-guide.md` -- Ready-to-use interview script with all question phases
