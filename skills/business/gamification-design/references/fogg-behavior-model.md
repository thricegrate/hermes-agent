# B.J. Fogg Behavior Model (B = MAP)

Complete framework for designing habit-forming learning apps based on Stanford behavioral science research.

---

## The Core Equation

**Behavior = Motivation + Ability + Prompt**

All three must converge at the same moment for the behavior to occur. If any one element is insufficient, the behavior does not happen — regardless of how strong the other two are.

```
                    High
                     |
                     |   Prompts succeed here
    M                |   ████████████████████
    O                |   ████████████████████
    T                |   ████████████████████
    I    ────────────┼──── ACTION LINE ──────
    V                |
    A                |   Prompts fail here
    T                |
    I                |
    O                |
    N               Low
                    Hard ──── ABILITY ──── Easy
```

Anything above the **Action Line** = behavior happens when prompted. Below = it doesn't, no matter how good your notification is.

The Action Line is not straight — it curves. When motivation is very high, people can do hard things. When ability is very high (the action is trivially easy), people do it even with low motivation.

---

## Motivation: The Unreliable Engine

Fogg identifies three core motivators, each with two sides:

| Motivator | Positive Side | Negative Side |
|-----------|--------------|---------------|
| **Sensation** | Pleasure | Pain |
| **Anticipation** | Hope | Fear |
| **Belonging** | Social acceptance | Social rejection |

### Motivation Waves

Motivation is NOT constant. It follows predictable patterns:

```
High ──╮    ╭──╮         ╭──╮
       │    │  │         │  │
       ╰──╮│  ╰──╮   ╭──╯  ╰──╮
          ╰╯     ╰───╯        ╰── Low
Day: 1  3  5  7  10  14  17  21  28
```

- **Days 1-3**: High motivation (novelty, excitement, "new year's resolution" energy)
- **Days 4-7**: First dip (novelty wears off, reality sets in)
- **Days 8-14**: Recovery IF habit has started to form, continued decline if not
- **Days 15-21**: Second dip (the "trough of disillusionment" for habits)
- **Days 22-28**: Stabilization if habit survives. Autopilot begins.

**Design implication:** Your gamification must carry users through the Day 4-7 and Day 15-21 dips. This is where streaks, loss aversion, and social accountability earn their value.

### Designing for Low-Motivation Days

This is the most important section. Most apps design for enthusiastic users. Winners design for tired, distracted, "I don't feel like it" users.

**Rules for low-motivation design:**
1. The minimum completable action must take under 60 seconds
2. The action must require zero decisions ("Tap to start today's lesson" — not "Choose a topic")
3. The action must be available from a single notification tap (deep link straight to the lesson)
4. Progress must be visible immediately (streak count visible, XP animation plays)
5. The "done" celebration must be disproportionately rewarding for the tiny effort

**Copy examples for low-motivation prompts:**
- "Just 2 minutes today. That's it." (reduce perceived effort)
- "Your 12-day streak is waiting." (loss aversion)
- "85% of learners at your level completed today's lesson." (social proof)
- "Today's lesson is one of the shortest." (even if they're all short)

---

## Ability: The Reliable Engine

Ability is what you CAN control. Fogg ranks ability factors from most to least impactful:

### Ability Chain (Design for These in Order)

| Factor | Question | Learning App Application |
|--------|----------|------------------------|
| **Time** | How long does it take? | Under 3 minutes. Ideally under 2. Show a timer. |
| **Money** | Does it cost anything? | Free tier must be fully functional. Paywall gates premium, not core habit. |
| **Physical effort** | How many taps/actions? | One tap from notification to lesson. No login walls. No intermediate screens. |
| **Mental effort** | How much thinking? | No decisions required to start. Auto-serve today's lesson. Reduce cognitive load. |
| **Social deviance** | Does it violate norms? | Learning AI should feel aspirational, not embarrassing. Frame as "smart people do this." |
| **Routine** | Does it fit existing habits? | Anchor to morning coffee, commute, lunch break. Let users set their "learning time." |

### Simplicity Stack for a Learning App

```
BEST:  Notification → Tap → Lesson starts → 2 min → Done → Confetti
GOOD:  Open app → Today's lesson visible → Tap → Lesson → Done
OK:    Open app → Choose category → Choose lesson → Lesson → Done
BAD:   Open app → Login → Dashboard → Browse → Choose → Lesson → Done
WORST: Open app → Login → Loading → Dashboard → Browse → Filter → Choose → Lesson → Paywall → Done
```

Each additional step between "prompt" and "action" loses 20-40% of users. For a 5-step funnel starting at 100 users with 70% pass-through per step: 100 → 70 → 49 → 34 → 24. You've lost 76% before they even started.

---

## Prompt: The Trigger That Starts Everything

Three types of prompts, used at different motivation levels:

### 1. Spark (High Ability, Low Motivation)
The user CAN do it but doesn't WANT to. The prompt must increase motivation.

- "You're 2 lessons away from your Expert badge"
- "Your streak is at 11 days — don't break it now"
- "People who complete today's lesson earn 2x more on average" (aspirational claim)

### 2. Facilitator (High Motivation, Low Ability)
The user WANTS to do it but it feels too HARD. The prompt must simplify the action.

- "Today's lesson is just 90 seconds"
- "Tap here to start — no setup needed"
- "We picked today's lesson for you based on your goals"

### 3. Signal (High Ability, High Motivation)
The user is ready and able. The prompt just needs to REMIND them.

- "Time for your daily lesson" (simple, no persuasion needed)
- Calendar notification at their set time
- App badge icon

**Matching prompt to user state:**

| User State | Signal | Motivation Level | Prompt Type |
|-----------|--------|-----------------|-------------|
| Day 1-3 user | High engagement | High | Signal (just remind) |
| Day 4-7 user | Engagement dropping | Medium | Spark (re-motivate) |
| Missed yesterday | At-risk | Low | Spark (loss aversion) |
| 14+ day streak | Habitual | Medium-High | Signal (don't over-notify) |
| Returning after absence | Uncertain | Variable | Facilitator (make it easy to restart) |

---

## Tiny Habits: The Fogg Implementation Method

### The Recipe

**"After I [ANCHOR], I will [TINY BEHAVIOR], and then I [CELEBRATE]."**

For a learning app:
- **Anchor**: "After I pour my morning coffee..."
- **Tiny behavior**: "...I will open the app and read one card..."
- **Celebrate**: "...and I will say 'Nice!' when I see my streak update."

### Shrinking the Behavior

The behavior must be so small it's almost impossible to fail:

| Too Big | Just Right | Why |
|---------|-----------|-----|
| "Complete a full lesson" | "Read the first card" | Reading one card takes 10 seconds. Once started, 85% of users finish. |
| "Master a new AI tool" | "Learn one thing about ChatGPT" | Framing matters. "One thing" feels achievable. |
| "Study for 30 minutes" | "Open the app" | If the minimum action is just opening, the streak is protected even on terrible days. |

**The 2-minute rule (from James Clear's Atomic Habits, building on Fogg):** The habit-starting behavior should take less than 2 minutes. The rest is momentum.

### Celebration Design

Celebration is the most underrated element. It creates the positive emotion that wires the habit into the brain. Without celebration, the behavior stays a chore.

**Effective celebrations in apps:**
- Confetti animation (0.5 sec, triggered instantly on completion)
- Sound effect (satisfying "ding" or "level up" sound)
- Haptic feedback (short vibration on mobile)
- Streak counter increment with animation
- XP counter incrementing with a rising-number animation
- "Great job!" with the user's name: "Nice work, Sarah!"
- Social proof: "You're in the top 15% of learners today"

**Timing is everything:** The celebration must fire within 500ms of the completing action. Any delay weakens the association. The brain connects the emotion to whatever it was doing in the last half-second.

**Celebration should scale with achievement:**
- Complete a normal lesson: confetti + XP animation
- Hit a streak milestone: bigger confetti + badge animation + sound
- Complete the 28-day challenge: full-screen celebration + certificate + share prompt

---

## Applying B=MAP to the 28-Day Challenge

| Day Range | Motivation | Ability Design | Prompt Strategy |
|-----------|-----------|---------------|----------------|
| 1-3 | High (novelty) | Can afford more complexity, but don't. Set the habit of "easy." | Signal prompts. User is eager. |
| 4-7 | Dropping | Shortest lessons of the whole challenge. 60-90 seconds. | Spark prompts. Streak at risk. "Day 5 of 28 — almost 20% done!" |
| 8-14 | Recovering or gone | Introduce first "interesting" content. Variable rewards start. | Mix of Spark and Facilitator. Reference their progress. |
| 15-21 | Second dip | Bring back short lessons. Hidden badges appear. | Spark prompts with loss aversion. "Your 15-day streak is rare — only 8% of users reach this." |
| 22-28 | Stabilizing | Challenge content OK now. User has built skill. | Signal prompts. Countdown to completion. "6 days until your certificate!" |

---

## Common Mistakes

1. **Designing for high motivation**: Your Day 1 user is not your Day 7 user. The system must work when motivation is at its lowest.
2. **Too many prompts**: More than 1 notification per day creates prompt fatigue. The user starts ignoring ALL prompts.
3. **Punishment for failure**: Never frame a missed day as failure. Frame it as a pause. "Welcome back" not "You missed yesterday."
4. **Ignoring the Ability axis**: If your lesson takes 10 minutes, no amount of motivation or prompting will save Day 7 retention.
5. **Generic celebrations**: "Good job!" means nothing after the 5th time. Vary the celebration. Reference specific achievements. Use the user's name.
