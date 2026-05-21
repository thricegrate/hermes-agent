# Feature Gating Framework for Learning Apps

## The Core Principle

Free tier must give enough value to build the habit. Premium tier must offer enough to make the upgrade feel necessary. If free is too generous, nobody upgrades. If free is too restrictive, nobody stays long enough to want to upgrade.

---

## The Habit-Value Matrix

Every feature falls into one of four quadrants:

```
                    HIGH habit-forming
                         |
            FREE         |        PREMIUM
        (Hook features)  |    (Retention features)
                         |
LOW value ───────────────┼──────────────── HIGH value
                         |
            REMOVE       |        FREE
        (Noise)          |    (Core value)
                         |
                    LOW habit-forming
```

### Quadrant Definitions

**Free - Hook Features** (high habit-forming, lower standalone value):
- Daily streaks and basic progress tracking
- 1 lesson per day
- Basic AI tool access (1-2 tools)
- Achievement notifications
- These create the loop that brings users back daily

**Premium - Retention Features** (high habit-forming, high value):
- Unlimited lessons per day
- All AI tools (10+)
- Certificates of completion
- Advanced progress analytics
- Streak protection (miss a day without losing streak)
- These are what make premium worth keeping

**Free - Core Value** (low habit-forming, high value):
- Account creation and profile
- Lesson content quality (same quality for free and premium lessons)
- Community viewing (read-only)
- Basic learning path visibility
- These must be free because they ARE the product

**Remove** (low habit-forming, low value):
- Features that add complexity without driving engagement or upgrades
- Anything users don't notice when it's gone

---

## Feature Gating Matrix for 3 Minute AI

| Feature | Free Tier | Premium Tier | Gating Rationale |
|---------|-----------|-------------|------------------|
| **Daily lessons** | 1 per day | Unlimited | Core hook: free gives enough to build habit, limit creates upgrade desire |
| **Lesson quality** | Full quality | Full quality | Never degrade free content quality; it kills trust and word-of-mouth |
| **AI tools** | 2 basic (ChatGPT, Gemini) | All 10+ tools | Free tools demonstrate value; premium unlocks the full toolkit |
| **Progress tracking** | Basic (streak count, lessons completed) | Advanced (analytics, insights, time spent, skill radar) | Basic tracking drives engagement; advanced tracking drives premium |
| **Streak system** | Streak counter, streak display | Streak protection (1 free miss/week), streak freeze items | Free streak creates attachment; premium streak protection prevents loss aversion |
| **Certificates** | None | 7-day, 14-day, 28-day completion certificates | Certificates are a strong premium motivator for learning apps |
| **XP and levels** | Earn XP, see level | XP boosters, bonus XP challenges | Progression is free (drives engagement); acceleration is premium |
| **Badges** | Basic badges (first lesson, first streak) | All badges including rare/special event badges | Basic badges give taste; premium badges give completionism |
| **Community** | View discussions | Post, comment, share progress | Read access shows the community exists; write access is premium |
| **Ads** | Display ads (non-intrusive) | No ads | Standard freemium monetization layer |
| **Content library** | Current day's content only | Full library access (past lessons, upcoming preview) | Scarcity of current-day-only drives daily return AND premium desire |
| **Learning path** | Linear (one path) | Choose from multiple paths, customize order | Single path is fine for free; choice is a premium perk |
| **Support** | Community FAQ | Priority support | Low-cost premium perk that increases perceived value |

---

## Gating Decision Framework

When deciding whether a new feature should be free or premium, run through this checklist:

### Gate It (Premium) If:

1. **It accelerates existing behavior** but is not required for it
   - Example: Streak protection accelerates streak maintenance but isn't required
2. **It provides status or recognition** beyond basic progress
   - Example: Certificates, rare badges, leaderboard position
3. **It costs you money to provide** at scale
   - Example: Advanced AI API calls, personalized content generation
4. **It removes friction** that free users tolerate
   - Example: Ad removal, offline access, faster loading
5. **Users only want it after they are already engaged**
   - Example: Advanced analytics, content library, custom learning paths

### Keep It Free If:

1. **Removing it would break the core loop**
   - Example: Daily lesson access, basic streak tracking
2. **It drives word-of-mouth or virality**
   - Example: Shareable progress cards, referral program
3. **It is part of the initial value demonstration**
   - Example: First lesson experience, basic AI tool access
4. **Without it, users would never reach the premium trigger**
   - Example: Onboarding flow, basic progress visualization
5. **It differentiates you from competitors who charge for it**
   - Example: High-quality free lesson content

---

## Common Gating Mistakes

### Mistake 1: Gating the Core Value

**Wrong:** Free users get lower-quality lessons.
**Right:** Free users get fewer lessons, but each one is full quality.

If your free content feels cheap, users assume premium is also cheap. Quality builds trust; quantity creates upgrade desire.

### Mistake 2: Too Much Free

**Wrong:** Free users get 5 lessons/day, all tools, and most badges.
**Right:** Free users get 1 lesson/day, 2 tools, and basic badges.

If free gives 80% of the value, premium only adds 20%. That is not enough to justify a subscription. The ideal ratio: free gives 40-50% of the experience, premium gives 100%.

### Mistake 3: Hard Gating Without Tease

**Wrong:** Premium features are completely invisible to free users.
**Right:** Premium features are visible but locked with a subtle lock icon and "Premium" label.

Users cannot desire what they do not know exists. Show locked features everywhere. When they tap, show a contextual mini-paywall specific to that feature.

### Mistake 4: Gating Social/Viral Features

**Wrong:** Only premium users can share their progress or refer friends.
**Right:** Every user can share progress, invite friends, and post to social.

Social features are your free marketing channel. Never gate them.

### Mistake 5: Binary Gate When Throttle Works Better

**Wrong:** Free users cannot use the AI image generator at all.
**Right:** Free users get 3 AI image generations per week. Premium gets unlimited.

Throttling (limited uses) is better than binary gating (on/off) because:
- Users experience the feature and understand its value
- The limit creates natural friction at the right moment
- It feels fair rather than restrictive

---

## Metrics to Track

| Metric | What It Tells You | Target |
|--------|------------------|--------|
| Feature engagement rate (free users) | Are free features driving daily use? | >60% DAU using core free features |
| Premium feature tap rate | Are free users discovering premium features? | >20% of free users tap a locked feature per week |
| Feature-specific conversion rate | Which locked features drive the most upgrades? | Identify top 3 conversion-driving features |
| Time-to-first-gate | How long before users hit a paywall trigger? | 1-3 days (not too fast, not too slow) |
| Post-upgrade feature usage | Do premium users actually use what they paid for? | >50% of premium users use 3+ premium features per week |

---

## Seasonal and Event Gating

Temporarily unlock premium features to drive conversion:

| Event | What to Unlock | Duration | Expected Lift |
|-------|---------------|----------|---------------|
| First week of new year | All AI tools for 48 hours | 2 days | +15-25% trial starts |
| User's 7-day streak | Unlock 1 premium lesson | 24 hours | +10-20% conversion |
| App anniversary | Full premium access | 3 days | +20-30% trial starts |
| Feature launch | New premium feature for all | 1 week | Drives awareness, +5-10% long-term conversion |

The psychology: once users experience premium, loss aversion kicks in. They have tasted unlimited lessons and certificates. Going back to 1 lesson/day feels like losing something.
