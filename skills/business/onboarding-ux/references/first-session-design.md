# First-Session Design

## The 165-Second First Session

The entire first session is designed to complete in under 3 minutes. Every second has a purpose.

### Second-by-Second Timeline

```
0s    ──── APP OPENS ────
       Welcome screen loads
5s    ──── LESSON STARTS ────
       Hook appears
25s   ──── CONCEPT BEGINS ────
       Named concept + principle
55s   ──── BEFORE/AFTER ────
       Contrast example
85s   ──── EXERCISE ────
       User makes a choice/writes
100s  ──── RESULT REVEAL ────
       Correct answer + XP
115s  ──── AHA MOMENT ────
       User has experienced value
       ─── RETENTION PHASE ───
120s  ──── CELEBRATION ────
       Confetti, XP animation
130s  ──── REMINDER SETUP ────
       Time selection
145s  ──── PERMISSION DIALOG ────
       (if opted in)
150s  ──── TOMORROW PREVIEW ────
       Curiosity gap planted
160s  ──── HOME SCREEN ────
       Session complete
165s  ──── SESSION END ────
```

---

## Aha Moment Framework

### Definition
The Aha Moment is when the user shifts from "trying this app" to "this is useful to me." It is a cognitive shift, not a feature interaction.

### For 3 Minute AI, the Aha Moment is:
**Seeing a before/after prompt comparison and thinking "I do the 'before' version — the 'after' is so much better."**

This requires three conditions:
1. The "before" example must feel familiar (the user recognizes their own behavior)
2. The improvement must be dramatic and obvious (not subtle)
3. The fix must feel achievable ("I could do that right now")

### Designing for the Aha Moment

**Condition 1: Familiar "before"**
Use the quiz data. If the user said they're interested in "Writing," the first lesson's before example should be a common writing prompt everyone has tried:
- "Write me an email" (generic, relatable)
- "Help me with my resume" (universal pain point)
- "Give me ideas for..." (common low-quality pattern)

**Condition 2: Dramatic improvement**
The after example must be visually different from the before, not just slightly better:
- Different length (2 sentences vs. a full paragraph with structure)
- Different specificity (generic advice vs. named project, specific dates, concrete actions)
- Different tone (robotic vs. human-sounding)

**Condition 3: Achievable fix**
The concept that bridges before and after must be one simple addition:
- "Add 5 words to the beginning of your prompt" (The Role Prompt)
- "Name one specific detail" (The Specificity Ladder)
- "Add one constraint" (The Constraint Prompt)

### Measuring the Aha Moment

Track these correlations in Firestore:

```
Hypothesis: Users who complete their first exercise
return at higher rates than those who only read.

Events to track:
- lesson_started → lesson_exercise_reached (completion rate)
- lesson_exercise_reached → exercise_answered (participation rate)
- exercise_answered → d2_return (aha → retention correlation)

Expected findings:
- lesson_started but not completed: ~15% D1
- lesson_completed without exercise: ~25% D1
- lesson_completed with exercise: ~45% D1
- lesson_completed + exercise + reminder: ~55% D1
```

---

## Personalization from Quiz Data

### Quiz Data Available at First Session

From the 17-step quiz funnel, we have:
1. **Comfort level with AI** (1-5 scale)
2. **AI tools already used** (list)
3. **Primary interest category** (Writing, Images, Save Time, Money, Fun, Learning)
4. **Goals** (career, side income, productivity, creativity, curiosity)
5. **Income level** (influences tool recommendations)
6. **Email** (for personalized notification copy)

### How to Use Each Data Point

| Quiz Data | First Session Impact |
|-----------|---------------------|
| Comfort = 1-2 | Start with Day 1 lesson, simpler language, more encouragement |
| Comfort = 3 | Start with Day 3 lesson, standard difficulty |
| Comfort = 4-5 | Start with Day 8 lesson, skip basics, more advanced concept |
| Category = Writing | First lesson is ChatGPT-focused |
| Category = Images | First lesson is DALL-E-focused |
| Category = Save Time | First lesson is Otter.ai or ChatGPT summarization |
| Goal = career | Frame CTA around professional development |
| Goal = side income | Frame CTA around freelancing opportunity |
| Goal = productivity | Frame CTA around time saved |

### Welcome Screen Copy Variants

**Comfort 1-2, Goal = career:**
> "Welcome! You told us AI feels overwhelming — we get it. Your first lesson takes 90 seconds and shows you the one trick that makes ChatGPT actually useful for work."

**Comfort 3, Goal = productivity:**
> "Welcome back! Based on your experience, we're skipping the basics. Your first lesson: a 5-word addition that makes ChatGPT write like your job title, not a robot."

**Comfort 4-5, Goal = side income:**
> "You already know the basics — nice. Let's go deeper. Your first lesson: how to control ChatGPT's output tone for client-ready deliverables."

---

## Edge Cases and Error States

### First Lesson Content Not Loaded
- Show a skeleton screen with animated placeholders (not a spinner)
- Pre-fetch Day 1 content during the quiz funnel completion
- If content fails to load after 3 seconds, show a retry button with: "Your lesson is loading. This usually takes a moment on first open."

### User Closes App During First Lesson
- Save progress locally (which block they reached)
- On next open: resume from where they left off, don't restart
- If they completed the exercise but closed before celebration: show celebration first on return

### User Skips Notification Permission
- Track `permission_declined` event
- Do NOT show the permission dialog again for 48 hours minimum
- Re-ask on Day 3 after third lesson completion (see Permission Priming)
- If declined 3 times (Day 1, Day 3, Day 7): never ask again

### User is Already Day 2+ (Not First Session)
- Skip welcome screen entirely
- Go straight to today's lesson
- Show streak counter prominently
- If streak = 0 (they missed yesterday), show: "Welcome back! Pick up where you left off."

### Paid vs. Free User First Session
- Identical first session for both
- Paywall differentiation begins on Day 2+
- Free users see the same first lesson quality as paid users
- This is critical: the free experience must be excellent to drive upgrades

---

## Anti-Patterns to Avoid

### 1. The Feature Tour
"Here's your home screen. Here's where lessons live. Here's your profile."
**Why it fails:** Users don't care about features, they care about outcomes. Feature tours add 60-90 seconds before any value.

### 2. The Choice Paradox
"Pick your first topic! Writing? Images? Productivity?"
**Why it fails:** Users just completed a 17-step quiz. They are decision-fatigued. Use quiz data to choose FOR them.

### 3. The Profile Setup Wall
"Add a profile photo. Set your username. Choose your interests."
**Why it fails:** Profile completion has zero correlation with retention. It's friction masquerading as engagement.

### 4. The Social Proof Dump
"Join 1M+ learners! Here are reviews! Look at this testimonial!"
**Why it fails:** They already signed up. Social proof is for pre-signup. Post-signup, it feels like you're still selling.

### 5. The Gamification Overload
"Here's your XP! Here's your level! Here are badges! Here's your streak!"
**Why it fails:** Gamification elements are meaningful only after the user has context. On Day 1, showing 15 locked badges feels overwhelming, not motivating.

### 6. The Premium Upsell on Day 1
"Upgrade to premium for full access!"
**Why it fails:** The user just went through a paywall. Showing another upgrade prompt destroys trust and signals the free experience is insufficient.
