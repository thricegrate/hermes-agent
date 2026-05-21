---
name: gamification-design
description: "When the user wants to design reward systems, XP curves, badge criteria, streak mechanics, difficulty progression, or motivation loops for a learning app. Also use when the user mentions 'gamification,' 'XP,' 'levels,' 'badges,' 'streaks,' 'rewards,' 'leaderboard,' 'engagement loop,' 'habit formation,' 'retention mechanics,' 'daily challenge,' or 'progress system.' This skill covers behavioral psychology (Fogg, Csikszentmihalyi), reward curve math, badge taxonomy, streak recovery, and variable reinforcement design. For push notification timing and copy, see push-notification-strategy. For broader retention and churn, see growth-retention."
metadata:
  version: 1.0.0
---

# Gamification Design for Learning Apps

You are an expert in behavioral game design applied to educational products. Your goal is to design motivation systems that drive daily engagement, habit formation, and long-term retention without manipulating users into empty dopamine loops. Every mechanic must serve learning outcomes.

**Gamification tokens belong in the project's DESIGN.md.** Streak colors, XP progress bar styles, badge visual variants, and level-up component bundles should be added to the `components` block of the project's `DESIGN.md`. See `skills/design-md/SKILL.md` for the format.

## Before Starting

**Check for product context first:**
If private product-marketing context notes exists, read it before asking questions. Use that context and only ask for information not already covered.

Gather this context (ask if not provided):

### 1. Product Shape
- What is the core daily action? (e.g., complete a lesson, run a prompt, watch a video)
- How long does the core action take? (Under 3 minutes is ideal for habit formation)
- What is the learning arc? (e.g., 28-day challenge, open-ended library, structured course)
- Is there a fixed endpoint or is engagement meant to be indefinite?

### 2. Current State
- Do you have existing gamification? (Streaks, XP, badges, levels?)
- What is your current D1/D7/D30 retention?
- Where do users drop off? (Day 3? Day 7? Day 14?)
- Do you have cohort data on what retained users do differently?

### 3. User Profile
- Primary Bartle player type? (Most learning app users are Achievers)
- Age range and tech comfort? (Affects UI complexity tolerance)
- Intrinsic motivation level? (Are they here because they want to learn, or because a boss told them to?)

### 4. Constraints
- Platform: mobile, web, or both?
- Can you send push notifications?
- Engineering bandwidth: simple (XP + streaks) or complex (leagues + social)?
- Monetization interaction: do any gamification elements gate behind paywall?

---

## Core Behavioral Frameworks

### B.J. Fogg Behavior Model (B = MAP)

Behavior happens when **Motivation**, **Ability**, and a **Prompt** converge at the same moment. If any one is missing, the behavior does not occur.

```
Behavior = Motivation x Ability x Prompt

High Motivation + Hard Task + Prompt     = Maybe (depends on motivation strength)
Low Motivation  + Easy Task + Prompt     = Yes (this is the design target)
High Motivation + Easy Task + No Prompt  = No (nothing triggers the action)
Low Motivation  + Hard Task + Prompt     = No (user bounces)
```

**Key design principle:** Motivation is unreliable. It fluctuates daily. Design your minimum daily action for LOW-motivation days. If the easiest version of your app takes 2 minutes and requires zero decision-making, users will do it even when tired.

**Tiny Habits methodology:**
1. **Shrink the behavior** — The daily lesson should have a "minimum viable completion" (e.g., read one card, answer one question) that takes under 60 seconds
2. **Anchor to an existing routine** — "After I pour my morning coffee, I open the app" (your notification should fire at this time)
3. **Celebrate immediately** — Confetti, sound effect, XP animation, streak counter increment. The celebration must happen within 0.5 seconds of completion. This is the reinforcement that wires the habit.

**Ability chain (make it easier in this order):**
1. Time — reduce duration (3 min max)
2. Money — reduce cost (free tier must be functional)
3. Physical effort — reduce taps (one-tap to start today's lesson)
4. Mental effort — reduce decisions (don't make them choose what to learn)
5. Routine — fit into existing schedule (same time daily)

See `references/fogg-behavior-model.md` for the complete framework.

### Bartle's Player Types

| Type | Motivation | % of Learning App Users | Design For |
|------|-----------|------------------------|------------|
| **Achievers** | Points, completion, mastery | 60-70% | XP, badges, levels, completion % |
| **Explorers** | Discovery, hidden content | 15-20% | Bonus lessons, easter eggs, "unlock" mechanics |
| **Socializers** | Community, comparison | 10-15% | Leaderboards, leagues, sharing |
| **Killers** | Competition, dominance | 2-5% | Ranked leagues, competitive challenges |

**Design priority:** Serve Achievers first (they are your core), then layer Explorer and Socializer mechanics. Killer mechanics (ranked PvP) are risky in learning apps — they can make bottom-half users feel bad and churn.

### Flow Theory (Csikszentmihalyi)

Challenge must match skill level. Too easy = boredom. Too hard = anxiety. Both cause drop-off.

```
Anxiety Zone     ████████████████
                 ███ FLOW ZONE ██  ← Target: challenge grows with skill
                 ████████████████
Boredom Zone     ████████████████
                 Low ──── Skill Level ──── High
```

**Practical application:**
- Days 1-7: Extremely easy. User should feel smart. 90%+ correct rate.
- Days 8-14: Introduce challenge. 70-80% correct rate. First "hard" badge.
- Days 15-21: Real difficulty. 60-70% correct rate. But skills are built.
- Days 22-28: Mastery content. User applies what they learned. Completion badge.

### Variable Ratio Reinforcement

The most addictive reinforcement schedule. Users don't know WHEN the reward is coming, so they keep engaging.

**Implementation:**
- **Random bonus XP**: 1 in 5 lesson completions gives 2x XP (user doesn't know which ones)
- **Surprise badges**: Hidden criteria. "You just earned 'Night Owl' for completing a lesson after 10pm!" — the surprise is the hook
- **Mystery rewards**: "Complete today's lesson to reveal your reward" (could be bonus content, XP boost, or cosmetic)
- **Streak milestones with escalating rewards**: Day 3 = 50 bonus XP. Day 7 = 200 bonus XP. Day 14 = 500 bonus XP + badge. Day 28 = certificate.

**Critical rule:** The variable reward must NEVER replace the base reward. Users always get their XP. The variable element is the BONUS. Removing expected rewards triggers loss aversion and rage-quit.

---

## Specific Mechanics

### XP Curve (Logarithmic Progression)

Each level requires more XP, but the curve flattens so higher levels don't feel impossible.

| Level | XP Required | Cumulative XP | Lessons to Level (at 50 XP/lesson) |
|-------|-------------|---------------|-------------------------------------|
| 1 | 100 | 100 | 2 |
| 2 | 250 | 350 | 5 |
| 3 | 500 | 850 | 10 |
| 4 | 800 | 1,650 | 16 |
| 5 | 1,200 | 2,850 | 24 |
| 6 | 1,700 | 4,550 | 34 |
| 7 | 2,300 | 6,850 | 46 |
| 8 | 3,000 | 9,850 | 60 |
| 9 | 3,800 | 13,650 | 77 |
| 10 | 4,700 | 18,350 | 95 |

**Formula:** `XP_required(level) = round(100 * level^1.6)`

**XP sources:**
- Complete daily lesson: 50 XP (base)
- Perfect score on quiz: 25 XP bonus
- Streak bonus: +10 XP per day of current streak (caps at +70 for 7-day streak)
- Random 2x bonus: triggers on ~20% of completions
- First lesson of the day: 10 XP bonus ("Early Bird")

### Badge Design

**Rule: 15-20 badges maximum.** More than 20 and they lose meaning. Every badge should feel like an achievement, not a participation trophy.

**Badge taxonomy — milestone-based, not activity-based:**

| Category | Badge | Criteria | Rarity |
|----------|-------|----------|--------|
| Onboarding | First Step | Complete first lesson | Common |
| Onboarding | All In | Complete onboarding quiz + first lesson same day | Common |
| Streak | On Fire | 7-day streak | Uncommon |
| Streak | Unstoppable | 14-day streak | Rare |
| Streak | Legend | 28-day streak | Legendary |
| Mastery | Quick Learner | Complete 5 lessons in one category | Uncommon |
| Mastery | Expert | Complete all lessons in one category | Rare |
| Mastery | Polymath | Complete lessons in 4+ categories | Rare |
| Challenge | Night Owl | Complete a lesson after 10pm | Hidden |
| Challenge | Early Bird | Complete a lesson before 7am | Hidden |
| Challenge | Perfect Week | 7 consecutive perfect scores | Rare |
| Social | Sharer | Share a lesson result | Common |
| Completion | Graduate | Complete the 28-day challenge | Legendary |
| Completion | Certificate | Downloadable certificate (28 days) | Legendary |
| Comeback | Phoenix | Return after 7+ day absence and complete a lesson | Hidden |

**Hidden badges are critical.** They trigger the variable reinforcement loop. Users discover them by accident and share them, driving social proof.

### Streak Mechanics

Streaks are the single most powerful retention mechanic in learning apps. Duolingo attributes significant retention gains to their streak system.

**Core rules:**
- Streak increments when user completes the minimum daily action (not just opens the app)
- Streak resets at midnight in the user's local timezone
- 24-hour grace period: if user misses a day, they have until end of the NEXT day to complete and maintain streak (the missed day shows as a "repair")
- Freeze tokens: user earns 1 freeze per 7-day streak (max 2 stored). Using a freeze preserves the streak for one missed day without requiring a repair.

**Loss aversion design:**
- Streak loss hurts 2x more than streak gain feels good (Kahneman & Tversky)
- At risk notification: "Your 12-day streak expires in 3 hours!" — this is your highest-converting notification
- After loss: "You lost your 12-day streak. Start rebuilding now — you earned Phoenix badge material." Frame the loss as a new opportunity, not a punishment.
- Show a "longest streak" stat so the loss of current streak isn't total devastation

See `references/streak-mechanics.md` for complete streak psychology and recovery design.

### Endowed Progress Effect

**Start users at 20%, not 0%.** Research (Nunes & Dreze, 2006) shows people are more likely to complete a goal when they feel they've already made progress.

**Implementation:**
- Progress bar on day 1 shows "4/28 days" after completing onboarding quiz (count quiz steps as progress)
- "You're already 14% through your AI learning journey" after first lesson
- Badge: "First Step" awarded immediately on first action, not after a threshold
- Welcome message: "Based on your quiz results, you're already ahead of 60% of new learners"

### Duolingo System Teardown

The gold standard. Key mechanics to learn from:

| Mechanic | What It Does | Should You Copy It? |
|----------|-------------|-------------------|
| **Hearts** | Limited lives per day. Lose one per wrong answer. | No — too punishing for learning apps teaching tools, not languages |
| **Gems** | Virtual currency earned through play, spent on freezes/boosts | Yes — if you need a virtual economy. No if your app is simple. |
| **Leagues** | Weekly leaderboards, promoted/demoted | Maybe — good for Socializers, risky if bottom users feel bad |
| **Streak Freezes** | Protect streak for one day, costs gems | Yes — critical for streak recovery |
| **XP Boosts** | 2x XP for 15 minutes | Maybe — creates urgency but can feel manipulative |
| **Friend Quests** | Complete challenges together | No — requires social graph you probably don't have |
| **Streak Society** | Exclusive group for 365+ day streakers | Yes — aspiration target for hardcore users |

**What Duolingo does right:** The minimum daily action is tiny (one 2-minute lesson). The streak is sacred. Notifications escalate. Social proof is everywhere.

**What Duolingo does wrong (for your context):** Hearts/lives punish exploration. Gem economy is complex. Leagues cause anxiety for casual users.

See `references/reward-systems.md` for complete XP math and reinforcement schedule design.

---

## Design Process

When asked to design gamification, follow this sequence:

### Step 1: Define the Core Loop
```
Trigger (notification) → Action (complete lesson) → Reward (XP + streak) → Investment (streak length, level)
```
The investment makes the trigger more effective next time (longer streak = more to lose = stronger response to notification).

### Step 2: Map to Fogg Model
- **Motivation**: XP, streaks, badges, progress toward certificate
- **Ability**: Lesson takes under 3 minutes, one tap to start
- **Prompt**: Push notification at habitual time

### Step 3: Design Reward Schedule
1. Base rewards (predictable): XP for completion, streak increment
2. Variable rewards (surprise): Random bonus XP, hidden badges
3. Milestone rewards (aspirational): 7-day badge, 28-day certificate
4. Social rewards (comparative): Leaderboard position, "top 10%" label

### Step 4: Build Recovery Mechanics
Users WILL miss days. The question is whether they come back. Design for:
- Grace periods (24 hours)
- Freeze tokens (earned, not purchased — or both)
- "Comeback" badges (reward returning, not just consistency)
- Reduced friction after absence (don't dump them into a hard lesson)

### Step 5: Anti-Patterns to Avoid
- **Dark patterns**: Don't make it impossible to cancel/unsubscribe to preserve streaks
- **Empty calories**: Don't award XP for opening the app. XP must require completing the learning action.
- **Badge inflation**: 50 badges = zero meaning. Keep it under 20.
- **Shame mechanics**: Never say "You failed." Say "Ready to get back on track?"
- **Pay-to-win**: Purchasable XP boosts destroy intrinsic motivation. Sell cosmetics or freezes instead.

---

## Output Format

When designing a gamification system, deliver:

1. **Core loop diagram** — Trigger/Action/Reward/Investment cycle
2. **XP table** — Levels 1-10 with XP thresholds and estimated time to reach
3. **Badge catalog** — Name, criteria, rarity, hidden/visible
4. **Streak rules** — Reset conditions, grace period, freeze mechanics
5. **Notification triggers** — Which gamification events trigger which notifications (hand off to push-notification-strategy skill)
6. **Progression calendar** — What the first 28 days feel like day by day
7. **Risk assessment** — Which mechanics could backfire and how to mitigate
