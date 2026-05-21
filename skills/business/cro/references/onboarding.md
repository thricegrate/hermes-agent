# Onboarding CRO Reference

Deep methodology for optimizing post-signup onboarding, user activation, and first-run experience.

## Core Principles

### 1. Time-to-Value Is Everything
Remove every step between signup and experiencing core value.

### 2. One Goal Per Session
Focus first session on one successful outcome. Save advanced features for later.

### 3. Do, Don't Show
Interactive > Tutorial. Doing the thing > Learning about the thing.

### 4. Progress Creates Motivation
Show advancement. Celebrate completions. Make the path visible.

---

## Defining Activation

### Find Your Aha Moment

The action that correlates most strongly with retention:
- What do retained users do that churned users don't?
- What's the earliest indicator of future engagement?

**Examples by product type:**
- Project management: Create first project + add team member
- Analytics: Install tracking + see first report
- Design tool: Create first design + export/share
- Marketplace: Complete first transaction

### Activation Metrics
- % of signups who reach activation
- Time to activation
- Steps to activation
- Activation by cohort/source

---

## Onboarding Flow Design

### Immediate Post-Signup (First 30 Seconds)

**Product-first approach:** Best for simple products, B2C, mobile. Risk: blank slate overwhelm.

**Guided setup approach:** Best for products needing personalization. Risk: adds friction before value.

**Value-first approach:** Best for products with demo data. Risk: may not feel "real."

**Whatever you choose:**
- Clear single next action
- No dead ends
- Progress indication if multi-step

### Onboarding Checklist Pattern

**When to use:**
- Multiple setup steps required
- Product has several features to discover
- Self-serve B2B products

**Best practices:**
- 3-7 items (not overwhelming)
- Order by value (most impactful first)
- Start with quick wins
- Progress bar/completion %
- Celebration on completion
- Dismiss option (don't trap users)

### Empty States

Empty states are onboarding opportunities, not dead ends.

**Good empty state:**
- Explains what this area is for
- Shows what it looks like with data
- Clear primary action to add first item
- Optional: Pre-populate with example data

### Tooltips and Guided Tours

**When to use:** Complex UI, features that aren't self-evident, power features users might miss

**Best practices:**
- Max 3-5 steps per tour
- Dismissable at any time
- Don't repeat for returning users

---

## Multi-Channel Onboarding

### Email + In-App Coordination

**Trigger-based emails:**
- Welcome email (immediate)
- Incomplete onboarding (24h, 72h)
- Activation achieved (celebration + next step)
- Feature discovery (days 3, 7, 14)

**Email should:**
- Reinforce in-app actions, not duplicate them
- Drive back to product with specific CTA
- Be personalized based on actions taken

---

## Handling Stalled Users

### Detection
Define "stalled" criteria (X days inactive, incomplete setup)

### Re-engagement Tactics

1. **Email sequence** - Reminder of value, address blockers, offer help
2. **In-app recovery** - Welcome back, pick up where left off
3. **Human touch** - For high-value accounts, personal outreach

---

## Common Patterns by Product Type

**B2B SaaS:** Setup wizard -> First value action -> Team invite -> Deep setup

**Marketplace:** Complete profile -> Browse -> First transaction -> Repeat loop

**Mobile App:** Permissions -> Quick win -> Push setup -> Habit loop

**Content Platform:** Follow/customize -> Consume -> Create -> Engage

---

## Measurement

### Key Metrics
- **Activation rate**: % reaching activation event
- **Time to activation**: How long to first value
- **Onboarding completion**: % completing setup
- **Day 1/7/30 retention**: Return rate by timeframe

### Funnel Analysis

Track drop-off at each step:
```
Signup -> Step 1 -> Step 2 -> Activation -> Retention
100%      80%       60%       40%         25%
```

Identify biggest drops and focus there.

---

## Onboarding Experiment Ideas

### Flow Simplification

**Reduce Friction**

| Test | Hypothesis |
|------|------------|
| Email verification timing | During vs. after onboarding |
| Empty states vs. dummy data | Pre-populated examples |
| Pre-filled templates | Accelerate setup with templates |
| OAuth options | Faster account linking |
| Required step count | Fewer required steps |
| Optional vs. required fields | Minimize requirements |
| Skip options | Allow bypassing non-critical steps |

**Step Sequencing**

| Test | Hypothesis |
|------|------------|
| Step ordering | Test different sequences |
| Value-first ordering | Highest-value features first |
| Friction placement | Move hard steps later |
| Required vs. optional balance | Ratio of required steps |
| Single vs. branching paths | One path vs. personalized |
| Quick start vs. full setup | Minimal path to value |

**Progress & Motivation**

| Test | Hypothesis |
|------|------------|
| Progress bars | Show completion percentage |
| Checklist length | 3-5 items vs. 5-7 items |
| Gamification | Badges, rewards, achievements |
| Completion messaging | "X% complete" visibility |
| Starting point | Begin at 20% vs. 0% |
| Celebration moments | Acknowledge completions |

### Guided Experience

**Product Tours**

| Test | Hypothesis |
|------|------------|
| Interactive tours | Tools like Navattic, Storylane |
| Tooltip vs. modal guidance | Subtle vs. attention-grabbing |
| Video tutorials | For complex workflows |
| Self-paced vs. guided | User control vs. structured |
| Tour length | Shorter vs. comprehensive |
| Tour triggering | Automatic vs. user-initiated |

**CTA Optimization**

| Test | Hypothesis |
|------|------------|
| CTA text variations | Action-oriented copy testing |
| CTA placement | Position within screens |
| In-app tooltips | Feature discovery prompts |
| Sticky CTAs | Persist during onboarding |
| CTA contrast | Visual prominence |
| Secondary CTAs | "Learn more" vs. primary only |

**UI Guidance**

| Test | Hypothesis |
|------|------------|
| Hotspot highlights | Draw attention to key features |
| Coachmarks | Contextual tips |
| Feature announcements | New feature discovery |
| Contextual help | Help where users need it |
| Search vs. guided | Self-service vs. directed |

### Personalization

**User Segmentation**

| Test | Hypothesis |
|------|------------|
| Role-based onboarding | Different paths by role |
| Goal-based paths | Customize by stated goal |
| Role-specific dashboards | Relevant default views |
| Use-case question | Personalize based on answer |
| Industry-specific paths | Vertical customization |
| Experience-based | Beginner vs. expert paths |

**Dynamic Content**

| Test | Hypothesis |
|------|------------|
| Personalized welcome | Name, company, role |
| Industry examples | Relevant use cases |
| Dynamic recommendations | Based on user answers |
| Template suggestions | Pre-filled for segment |
| Feature highlighting | Relevant to stated goals |
| Benchmark data | Industry-specific metrics |

### Quick Wins & Engagement

**Time-to-Value**

| Test | Hypothesis |
|------|------------|
| First quick win | "Complete your first X" |
| Success messages | After key actions |
| Progress celebrations | Milestone moments |
| Next step suggestions | After each completion |
| Value demonstration | Show what they achieved |
| Outcome preview | What success looks like |

**Motivation Mechanics**

| Test | Hypothesis |
|------|------------|
| Achievement badges | Gamification elements |
| Streaks | Consecutive day engagement |
| Leaderboards | Social comparison (if appropriate) |
| Rewards | Incentives for completion |
| Unlock mechanics | Features revealed progressively |

**Support & Help**

| Test | Hypothesis |
|------|------------|
| Free onboarding calls | For complex products |
| Contextual help | Throughout onboarding |
| Chat support | Availability during onboarding |
| Proactive outreach | For stuck users |
| Self-service resources | Help docs, videos |
| Community access | Peer support early |

### Email & Multi-Channel

**Onboarding Emails**

| Test | Hypothesis |
|------|------------|
| Founder welcome email | Personal vs. generic |
| Behavior-based triggers | Action/inaction based |
| Email timing | Immediate vs. delayed |
| Email frequency | More vs. fewer touches |
| Quick tips format | Short actionable content |
| Video in email | More engaging format |

**Email Content**

| Test | Hypothesis |
|------|------------|
| Subject lines | Open rate optimization |
| Personalization depth | Name vs. behavior-based |
| CTA prominence | Single clear action |
| Social proof inclusion | Testimonials in email |
| Urgency messaging | Trial reminders |
| Plain text vs. designed | Format testing |

**Feedback Loops**

| Test | Hypothesis |
|------|------------|
| NPS during onboarding | When to ask |
| Blocking question | "What's stopping you?" |
| NPS follow-up | Actions based on score |
| In-app feedback | Thumbs up/down on features |
| Survey timing | When to request feedback |
| Feedback incentives | Reward for completing |

### Re-engagement

**Stalled User Recovery**

| Test | Hypothesis |
|------|------------|
| Re-engagement email timing | When to send |
| Personal outreach | Human vs. automated |
| Simplified path | Reduced steps for returners |
| Incentive offers | Discount or extended trial |
| Problem identification | Ask what's blocking |
| Demo offer | Live walkthrough |

**Return Experience**

| Test | Hypothesis |
|------|------------|
| Welcome back message | Acknowledge return |
| Progress resume | Pick up where left off |
| Changed state | What happened while away |
| Re-onboarding | Fresh start option |
| Urgency messaging | Trial time remaining |

### Technical & UX

**Performance**

| Test | Hypothesis |
|------|------------|
| Load time optimization | Faster = higher completion |
| Progressive loading | Perceived performance |
| Offline capability | Mobile experience |
| Error handling | Graceful failure recovery |

**Mobile Onboarding**

| Test | Hypothesis |
|------|------------|
| Touch targets | Size and spacing |
| Swipe navigation | Mobile-native patterns |
| Screen count | Fewer screens needed |
| Input optimization | Mobile-friendly forms |
| Permission timing | When to ask |

**Accessibility**

| Test | Hypothesis |
|------|------------|
| Screen reader support | Accessibility impact |
| Keyboard navigation | Non-mouse users |
| Color contrast | Visibility |
| Font sizing | Readability |

---

## Metrics to Track

For all experiments, measure:

| Metric | Description |
|--------|-------------|
| Activation rate | % reaching activation event |
| Time to activation | Hours/days to first value |
| Step completion rate | % completing each step |
| Drop-off points | Where users abandon |
| Return rate | Users who come back |
| Day 1/7/30 retention | Engagement over time |
| Feature adoption | Which features get used |
| Support requests | Volume during onboarding |
