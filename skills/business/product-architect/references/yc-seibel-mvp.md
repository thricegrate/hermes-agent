# YC Framework: How to Plan an MVP (Michael Seibel)

Source: Y Combinator Startup School 2020 -- Michael Seibel

## Core Principle: An MVP Is Not a "Lite" Version of Your Vision

An MVP is the smallest thing you can build to test your CORE HYPOTHESIS. It's a learning tool, not a product preview.

**The question:** "What ONE thing must be true for this business to work?"

That one thing is your core hypothesis. Your MVP tests ONLY that. Everything else is scope creep.

## Core Hypothesis Identification

Before building anything, write this down:

```
My business works IF: [one specific thing]
```

Examples:
- "My business works IF people will pay $47 for a packaged AI skill"
- "My business works IF newsletter subscribers will click through to an interactive AI tool"
- "My business works IF non-technical people can get value from a pre-built AI workflow"

**The test:** If your core hypothesis is FALSE, does anything else matter? If not, you've found the right hypothesis.

**Common mistake:** Testing multiple hypotheses at once. "Will they sign up AND complete the course AND refer friends?" Pick ONE. Test that first.

## Feature Prioritization: The "Remove It" Test

For every feature you're planning, ask:

**"If I remove this feature, can I still test my core hypothesis?"**

- If YES: Remove it. Don't build it. Add it later if the hypothesis validates.
- If NO: Keep it. This is essential to the test.

**For a 3-day build cycle, this means:**

| Include | Exclude |
|---------|---------|
| The core interaction (the ONE thing you're testing) | User accounts / login |
| Minimal UI to make it usable | Analytics dashboard |
| One clear CTA | Settings / preferences |
| Basic error handling | Onboarding flow |
| | Social sharing |
| | Multiple output formats |
| | Polish / animations |

## Launch Velocity > Feature Completeness

Speed to market beats completeness. Every day you're building instead of testing is a day of learning you've lost.

**The math:**
- Building for 2 weeks + 2 weeks of user feedback = 4 weeks for one learning cycle
- Building for 3 days + 4 days of feedback = 1 week for one learning cycle
- In 4 weeks, the slow builder gets 1 cycle. The fast builder gets 4 cycles.

Four cycles of learning beats one cycle of polish. Every time.

## "Do Things That Don't Scale"

Manual work is not only acceptable in MVP phase -- it's PREFERABLE.

**Examples of unscalable MVP tactics:**
- Manually onboard every user (learn what confuses them)
- Do parts of the service by hand (validate demand before automating)
- Email users individually for feedback (personal touch = better data)
- Curate content manually (before building recommendation algorithms)
- Use Google Sheets as your database (before building a real backend)

**Why this works:**
1. You learn faster (you see every friction point firsthand)
2. You build relationships (early users become evangelists)
3. You avoid premature optimization (don't automate what you don't understand)

**Application to app iteration strategy:**
- App 1: Manual curation + simple UI. Test if people engage.
- App 2: Semi-automated. Test if automation maintains quality.
- App 3: Fully automated. Scale what works.

## The MVP Decision Matrix

For each app/product in the fast iteration cycle:

| Question | Answer | Action |
|----------|--------|--------|
| Can I test my hypothesis with a landing page + email? | Yes | Don't build anything. Use `presell-validator`. |
| Can I test with a Claude Artifact or simple tool? | Yes | Build the Artifact. 1-day effort max. |
| Does testing require a full app? | Yes | 3-day build max. Strip to core hypothesis only. |
| Will I need ongoing data to validate? | Yes | Add one metric tracker. Nothing else. |

## Post-MVP: The Feedback Loop

After launch, the only three things that matter:

1. **Talk to users immediately.** Not in a week. TODAY. (see `user-research`)
2. **Measure one metric.** The one that proves or disproves your hypothesis.
3. **Iterate or kill within 7 days.** If signal is weak after 7 days of effort, move on.

**Build-Measure-Learn cycle:**
```
BUILD (3 days) -> MEASURE (2-3 days) -> LEARN (1 day) -> DECIDE: iterate or kill
```

## Common MVP Mistakes

1. **Building too much.** The #1 mistake. If it took more than a week, you built too much.
2. **Testing the wrong hypothesis.** "Can I build this?" is not a business hypothesis. "Will people pay for this?" is.
3. **Ignoring negative signal.** If 50 people use it and nobody comes back, that's a KILL signal. Don't rationalize.
4. **Polishing before validating.** Pretty UI on a product nobody wants is still a product nobody wants.
5. **Avoiding user contact.** If you're afraid to show it to people, you already know it's not ready. Show it anyway.

## Integration with Other Skills

- **Before MVP:** `user-research` (understand the problem) -> `presell-validator` (test demand) -> `product-architect` (plan the build)
- **During MVP:** Build to core hypothesis only. Use this reference to cut scope ruthlessly.
- **After MVP:** If validated -> full `product-architect` build. If not -> back to `user-research`.
