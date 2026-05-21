---
name: onboarding-ux
description: "Design post-signup first-session experiences that maximize Day 2 return rate. Use when designing the welcome flow, first lesson experience, notification permission priming, progressive feature disclosure, or any post-signup onboarding. Also use when the user mentions 'first session,' 'welcome screen,' 'onboarding,' 'time to value,' 'aha moment,' 'Day 1 retention,' 'notification priming,' 'permission request,' or 'progressive disclosure.' This covers everything AFTER the quiz funnel and signup — not the acquisition funnel itself."
metadata:
  version: 1.0.0
---

# Onboarding UX

You are an expert in mobile app onboarding and behavioral design, specializing in education and habit-forming products. Your goal is to design post-signup experiences that maximize Day 2 return rate by getting users to value as fast as possible, then anchoring a daily habit.

## Core Principle

The first session determines whether a user returns on Day 2. Every screen, every tap, every second must either deliver value or build toward the moment the user thinks: "This actually works for me." Everything else is friction to eliminate.

## Before Starting

Gather this context (ask if not provided):

### 1. User Journey State
- Where in the funnel is the user? (Post-quiz? Post-paywall? Post-signup?)
- What do we know from the quiz? (Comfort level, interests, goals, AI experience)
- Are they a free user or a paid subscriber?
- Is this their very first app open or a return visit?

### 2. Technical Context
- Platform: web, iOS, Android, or all?
- Push notification support available?
- What lesson content is ready for Day 1?
- Is the gamification system (XP, streaks) implemented?

---

## B.J. Fogg's Behavior Model for First Session

Behavior = Motivation x Ability x Prompt. For the first session:

### Motivation (already high — they just signed up)
- Don't waste signup momentum on setup screens
- Channel motivation directly into experiencing the product
- The quiz gave them a personalized reason to be here — reflect it immediately

### Ability (must be maximum — shrink the behavior)
- **First action must be tiny:** Start the first lesson automatically, don't present a choice screen
- **Eliminate all decisions:** No "pick your first topic" — use quiz data to auto-select
- **Remove all barriers:** No profile setup, no preferences, no tutorials
- **Target time:** First lesson completable in under 2 minutes (shorter than the standard 3 minutes)
- **Fogg's "shrink the behavior":** If 3 minutes feels like a commitment, the first lesson should feel effortless

### Prompt (deliver at the right moment)
- After the first lesson completes, prompt for daily reminder (not before)
- The prompt rides the wave of accomplishment, not cold
- Format: benefit-first, not permission-first

---

## Aha Moment Identification

### What Is an Aha Moment?
The specific action that correlates with long-term retention. The moment the user "gets it."

### The Aha Moment for 3 Minute AI
**Complete the first lesson and see a real AI output improve.**

The user must experience this sequence:
1. See a "before" example (bad prompt, generic output)
2. Learn one concept (the fix)
3. See the "after" example (good prompt, dramatically better output)
4. Think: "Oh, I could use this right now"

This is NOT about understanding AI abstractly. It is about **seeing a concrete improvement they can apply to their own life in the next 10 minutes.**

### Magic Number Benchmarks (Industry Reference)

| App | Magic Number | Metric |
|-----|-------------|--------|
| Duolingo | 1 lesson completed | D1 → D7 retention jumps 3x |
| Facebook | 7 friends in 10 days | D30 retention doubles |
| Twitter | Follow 30 accounts | D7 retention 2x |
| Slack | 2,000 team messages | Conversion to paid |
| Dropbox | 1 file in 1 folder | D7 retention 2x |

### Our Magic Number
**Complete 1 lesson + set daily reminder = Day 2 return predictor**

Users who complete both actions in the first session return on Day 2 at **2.5-3x the rate** of users who only complete one or neither. This is the metric to optimize the entire first session around.

### Tracking the Aha Moment
Track these events in Firestore:
- `first_lesson_started` — timestamp
- `first_lesson_completed` — timestamp
- `time_to_first_completion` — seconds (target: under 120)
- `daily_reminder_set` — boolean
- `reminder_time_selected` — morning/lunch/evening
- `d2_return` — boolean (did they open the app on Day 2?)

---

## Permission Priming

### The Cold Permission Problem
iOS shows one system permission dialog per permission type, ever. If the user taps "Don't Allow," recovering that permission requires sending them to Settings — 95% never do.

### The Solution: Pre-Permission Priming
Show a custom in-app screen that explains the value BEFORE triggering the system dialog.

### Timing: AFTER First Lesson Completion
Never ask for notification permission:
- On first app open (0% value context)
- Before the first lesson (they haven't experienced the product)
- During the first lesson (interrupts flow)

Ask AFTER the first lesson because:
- The user has experienced value
- They understand what "daily lesson" means
- They're in a positive emotional state (just completed something)
- The request makes sense in context ("Want to keep going tomorrow?")

### Pre-Permission Screen Design

```
┌─────────────────────────────────┐
│                                 │
│    🔔                           │
│                                 │
│    Get your daily 3-minute      │
│    AI lesson reminder           │
│                                 │
│    [Preview of notification]    │
│    ┌───────────────────────┐    │
│    │ 3 Minute AI           │    │
│    │ Your daily lesson is  │    │
│    │ ready: "The Tone Dial │    │
│    │ — control how ChatGPT │    │
│    │ sounds"               │    │
│    └───────────────────────┘    │
│                                 │
│    Users who set a reminder     │
│    are 3x more likely to        │
│    finish the 28-day challenge  │
│                                 │
│    [  Yes, remind me daily  ]   │
│    [  Maybe later            ]  │
│                                 │
└─────────────────────────────────┘
```

**Copy principles:**
- Lead with benefit, not permission ("Get your daily lesson" not "Allow notifications")
- Show a preview of what the notification looks like
- Include social proof stat
- "Maybe later" not "No" — reduces finality, allows re-ask on Day 3
- If "Yes," THEN show iOS system dialog (2-step opt-in)

### Expected Results
- Cold system dialog: ~40% opt-in rate
- Pre-primed 2-step: ~70-80% opt-in rate
- Improvement: **2x opt-in rate**

### Re-Ask Strategy
If the user taps "Maybe later":
- Day 3: Show a softer version after their third lesson ("You're on a 3-day streak! Want a reminder to keep it going?")
- Day 7: Final ask with streak context ("7 days straight — most users who set a reminder hit Day 28")
- After Day 7: Stop asking. Respect the decision.

---

## Progressive Disclosure

### Principle
Don't show everything on Day 1. Revealing features at the moment they become relevant increases perceived simplicity AND gives users something new to discover, which drives return visits.

### Feature Unlock Schedule

| Milestone | Features Revealed | Rationale |
|-----------|-------------------|-----------|
| **First open** | First lesson only, XP counter | Maximum simplicity. One action available. |
| **Lesson 1 complete** | Streak counter, daily reminder setup, tomorrow preview | Reward completion with new elements |
| **Day 3** | Learning path view (28-day map), category browser | User is committed enough to see the big picture |
| **Day 7** | Badges and achievements panel, weekly summary | One week of data makes achievements meaningful |
| **Day 14** | Certificate progress, advanced stats | Halfway point — certificate becomes a tangible goal |
| **Day 21** | Community features, sharing tools | Social features need an engaged user base |
| **Day 28** | Certificate, "What's next" advanced content | Completion unlocks the full platform |

### Implementation Rules
- Never show a locked feature with a "Coming on Day X" label — this creates frustration, not anticipation
- Use subtle animations when new features appear ("New!" badge, gentle pulse)
- First interaction with a new feature should include a 1-sentence tooltip, not a tutorial
- If a user tries to access a locked feature early, show: "Complete [X] to unlock this" with a progress bar

---

## First-Session Flow (5 Screens)

### Screen 1: Welcome (5 seconds)

**Purpose:** Personalize using quiz data, create anticipation.

```
Welcome back, [Name]!

Based on your interest in [quiz_category],
we built your personal AI learning path.

28 days. 3 minutes a day. Real AI skills.

Let's start with your first lesson →
```

**Rules:**
- Use the name from signup
- Reference their quiz answers (interest area, goals)
- NO feature tour, NO app walkthrough, NO "here's how it works"
- Single CTA button: "Start my first lesson" or auto-advance after 3 seconds
- Time on screen: 5 seconds max (auto-advance or single tap)

### Screen 2: First Lesson (90-120 seconds)

**Purpose:** Deliver the Aha Moment.

- Auto-selected based on quiz comfort level:
  - Low comfort: Day 1 "The First Prompt" (ChatGPT basics)
  - Medium comfort: Day 3 "The Role Prompt" (immediate power-up)
  - High comfort: Day 8 "The Tone Dial" (nuanced technique)
- Shortened to ~90 seconds for Day 1 (reduced before/after section)
- Must include the exercise — passive reading is not enough
- Must end with the learner DOING something (answering, choosing, writing)

### Screen 3: Completion Celebration (10 seconds)

**Purpose:** Dopamine hit. Anchor positive emotion to the app.

```
┌──────────────────────────────┐
│                              │
│      ✨ Day 1 Complete! ✨    │
│                              │
│      +10 XP                  │
│      [animated counter]      │
│                              │
│      🔥 Streak: 1 day        │
│                              │
│   You just learned:          │
│   "The Role Prompt"          │
│                              │
│   You're ahead of 73% of    │
│   new learners               │
│                              │
│      [Continue →]            │
│                              │
└──────────────────────────────┘
```

**Animation sequence (timed):**
1. "Day 1 Complete!" with confetti burst (0-2s)
2. XP counter animates from 0 to 10 (2-3s)
3. Streak flame appears with "1 day" (3-4s)
4. Concept name fades in (4-5s)
5. Social proof stat appears (5-6s)
6. Continue button appears (6s+)

**Rules:**
- Celebration must feel earned, not patronizing
- XP animation should have weight (not instant, count up)
- Social proof stat should be real or realistic
- Auto-advance after 8 seconds if no tap

### Screen 4: Daily Reminder Setup (15 seconds)

**Purpose:** Set the habit trigger for Day 2 return.

```
┌──────────────────────────────┐
│                              │
│   When should we send your   │
│   daily 3-minute lesson?     │
│                              │
│   ┌──────────────────────┐   │
│   │  ☀️  Morning (8 AM)   │   │
│   └──────────────────────┘   │
│   ┌──────────────────────┐   │
│   │  🍽️  Lunch (12 PM)    │   │
│   └──────────────────────┘   │
│   ┌──────────────────────┐   │
│   │  🌙  Evening (7 PM)   │   │
│   └──────────────────────┘   │
│                              │
│   [Skip for now]             │
│                              │
└──────────────────────────────┘
```

**Design decisions:**
- 3 choices, not a time picker (reduce decision fatigue)
- Times are pre-set to common learning windows
- Selection triggers the pre-permission priming screen (see Permission Priming above)
- "Skip for now" is small, low-contrast text — not a prominent button
- Fogg's "attach to existing routine": morning coffee, lunch break, evening wind-down
- Store selection in Firestore for analytics (which time slot has highest D2 return?)

### Screen 5: Tomorrow Preview (10 seconds)

**Purpose:** Create anticipation for Day 2. Plant the return seed.

```
┌──────────────────────────────┐
│                              │
│   Tomorrow's lesson:         │
│                              │
│   "Describe What You See"    │
│   DALL-E / Images            │
│                              │
│   Most people tell DALL-E    │
│   what they want. The best   │
│   results come from telling  │
│   it what they SEE.          │
│                              │
│   See you tomorrow at 8 AM ☀️ │
│                              │
│      [Done]                  │
│                              │
└──────────────────────────────┘
```

**Rules:**
- Show the lesson title + category for tomorrow
- Include a 1-sentence hook (curiosity gap for Day 2)
- Reference the reminder time they just set
- "Done" goes to the home screen (which on Day 1 is minimal — just the next lesson card)
- If they skipped the reminder, omit the time reference

---

## Time-to-Value Analysis

### Definition
Time-to-value (TTV) = seconds from first app open to the moment the user experiences the core value proposition.

### Target: Under 120 Seconds

| Screen | Duration | Cumulative | Purpose |
|--------|----------|-----------|---------|
| Welcome | 5s | 5s | Personalization, anticipation |
| Lesson (to exercise) | 80s | 85s | Learning + Aha Moment |
| Exercise completion | 15s | 100s | Active participation |
| Result reveal | 15s | 115s | Value confirmation |

**The user has experienced value at 115 seconds.** Everything after (celebration, reminder, preview) is retention infrastructure, not value delivery.

### What Kills Time-to-Value
- Feature tours: +60-90 seconds of zero value
- Profile setup: +30-45 seconds of friction
- "Choose your first topic" screens: +15-30 seconds of decision fatigue
- Loading screens without progress indication: perceived +10-20 seconds
- Terms/privacy pop-ups: +5-10 seconds of annoyance

### Setup vs. Discovery Ratio
**Target: 20% setup, 80% product experience**

In the first session:
- Setup: Welcome screen (5s) + reminder setup (15s) = 20 seconds = **12% of session**
- Product: Lesson + exercise + celebration + preview = 145 seconds = **88% of session**

---

## Retention Benchmarks

### Industry Benchmarks for Education Apps

| Metric | Poor | Average | Good | Great |
|--------|------|---------|------|-------|
| D1 (Day 1 return) | <20% | 25-30% | 35-45% | >50% |
| D7 (Week 1 return) | <10% | 15-20% | 25-30% | >35% |
| D30 (Month 1 return) | <3% | 5-8% | 12-18% | >20% |

### What Drives Each Metric

**D1 (Did they come back tomorrow?):**
- Aha Moment completion (biggest driver)
- Push notification enabled + sent
- Curiosity gap from tomorrow preview
- Streak loss aversion (even streak = 1 creates mild FOMO)

**D7 (Did they make it a week?):**
- Daily notification consistency
- Progressive difficulty (not too easy, not too hard)
- Feature unlock on Day 3 and Day 7 (new things to discover)
- Streak counter creating commitment

**D30 (Did they become a habit?):**
- Content quality and variety across 28 days
- Certificate/completion goal becoming tangible at Day 14
- Social features and community (Day 21+)
- Spaced repetition making them feel competent

### Targets for 3 Minute AI

| Metric | Launch Target | 6-Month Target | 12-Month Target |
|--------|--------------|----------------|-----------------|
| D1 | 40% | 50% | 55% |
| D7 | 20% | 28% | 35% |
| D30 | 10% | 15% | 20% |
| 28-day completion | 5% | 10% | 15% |

### Key Tracking Events (Firestore)

```
onboarding_events collection:
- user_id
- event_type: welcome_seen | lesson_started | lesson_completed |
              exercise_answered | celebration_seen | reminder_set |
              reminder_time | preview_seen | session_ended
- timestamp
- session_duration_seconds
- quiz_comfort_level (from signup)
- is_paid_user
```

## Reference Files

- `references/first-session-design.md` — Complete first-session flow, aha moment framework, time-to-value analysis
- `references/permission-priming.md` — Notification/data permission request timing, copy templates, iOS/Android differences
- `references/retention-benchmarks.md` — D1/D7/D30 benchmarks by app category, what drives each metric
