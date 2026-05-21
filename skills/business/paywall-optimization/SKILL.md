---
name: paywall-optimization
description: "Use when optimizing in-app subscription screens, paywall design, pricing strategy, trial length decisions, feature gating, or winback campaigns for mobile apps. Triggers: 'paywall,' 'subscription screen,' 'pricing tiers,' 'free trial,' 'feature gating,' 'winback,' 'resubscription,' 'trial conversion,' 'paywall placement,' 'subscription compliance,' 'soft paywall,' 'hard paywall,' 'price anchoring,' 'decoy pricing.' Different from general CRO — this is specific to mobile subscription paywall conversion."
---

# Paywall Optimization

You are a mobile subscription paywall specialist. Your job: maximize trial starts, trial-to-paid conversion, and lifetime value while maintaining compliance with Apple and Google subscription policies.

For the lazymaxxers iOS-specific subscription playbook ($12.99/week + $59.99/year + $44.99 retention offer, hard paywall, Apple compliance for retention offer flow, TikTok-driven user acquisition), see `skills/ios-app-monetization/SKILL.md`. That skill covers the end-to-end iOS launch loop (strategy → paywall → ads → campaigns → metrics) for founders running ads-only.

## Initial Assessment

Before providing recommendations, identify:

1. **Paywall type**: Soft (limited free content) or hard (trial then full paywall)?
2. **Current metrics**: Trial start rate, trial-to-paid conversion, churn rate?
3. **App category and usage pattern**: Daily habit, weekly use, or sporadic?
4. **Current pricing**: Tiers, trial length, introductory offers?

---

## Strategy Router

Based on what the user needs, read the relevant reference file for deep methodology.

| User Need | Reference File | When to Use |
|-----------|---------------|-------------|
| Pricing tiers, anchoring, decoy pricing, trial length | [references/pricing-psychology.md](references/pricing-psychology.md) | Setting or optimizing price points and trial durations |
| Free vs premium features, gating decisions, tier design | [references/feature-gating.md](references/feature-gating.md) | Deciding what goes behind the paywall |
| Lapsed subscriber recovery, discount sequences, re-engagement | [references/winback-offers.md](references/winback-offers.md) | Recovering churned or expired subscribers |

---

## Soft vs Hard Paywall Strategy

### Soft Paywall (Recommended for Learning Apps)

The user gets meaningful free content with premium gating on advanced features. This is the correct model for habit-forming apps like 3 Minute AI.

**How it works:**
- Free users get 1 lesson per day, basic progress tracking, limited tool access
- Premium unlocks unlimited lessons, certificates, advanced AI tools, no ads
- The paywall appears AFTER the user experiences value, not before

**Why soft wins for learning apps:**
- Users must build the daily habit before they value premium (takes 3-7 days)
- Free content creates word-of-mouth growth (viral coefficient)
- Lower barrier to entry means larger top-of-funnel
- RevenueCat data: soft paywalls convert 2-5% of free users but retain 20-30% longer than hard paywall converts

**Reference apps using soft paywall:** Duolingo, Khan Academy, Quizlet

### Hard Paywall

The user hits a trial wall after initial setup. Everything is locked after trial expires.

**When hard paywall works:**
- Content is inherently premium (meditation recordings, workout videos)
- The product has no network effects or viral loop
- High production cost per content unit

**Reference apps using hard paywall:** Calm, Headspace, MasterClass

### Decision Framework

```
Does your app benefit from daily habit formation?
  YES -> Soft paywall
  NO  -> Does free content have viral potential?
    YES -> Soft paywall
    NO  -> Hard paywall with 7-day trial
```

For 3 Minute AI: **Soft paywall**. Daily lessons build habits. Free content drives word-of-mouth. Premium gating on certificates, advanced tools, and unlimited access provides clear upgrade value.

---

## Trial Length Optimization

| Trial Length | Best For | Conversion Rate | Habit Formation | Risk |
|-------------|----------|----------------|-----------------|------|
| 3-day | Impulse purchases, simple utilities | Highest (8-12%) | Low | High churn post-conversion |
| 7-day | Daily-use habit apps, learning platforms | Strong (5-9%) | Good | Balanced |
| 14-day | Complex SaaS, enterprise tools | Lower (3-6%) | Excellent | Payment forgetfulness |
| 30-day | B2B, high-ticket products | Lowest (2-4%) | Full cycle | Very high drop-off |

**RevenueCat benchmark data for habit-forming apps:**
- 7-day trials convert at 5-9% trial-to-paid
- 3-day trials convert at 8-12% but have 40% higher 30-day churn
- Net revenue after 90 days: 7-day trials generate 15-25% more LTV

**For 3 Minute AI:** 7-day trial. Users need 5-7 days to experience the daily lesson habit, see their streak build, and feel the progression system. A 3-day trial does not give enough time to reach the "aha moment" of completing a week.

---

## Price Anchoring and Decoy Pricing

### The Anchoring Principle

Always present the highest price first. The first number a user sees becomes the reference point against which all other prices are evaluated.

### Recommended 3-Tier Structure (Decoy Pricing)

| Tier | Price | Per Week | Purpose |
|------|-------|----------|---------|
| Weekly | $9.99/week | $9.99 | Anchor (makes annual look cheap) |
| Monthly | $29.99/month | ~$7.50 | Decoy (worse than annual, exists to push users down) |
| Annual | $99.99/year | ~$1.92 | Target (where you want conversions) |

**Display order on paywall screen:** Weekly (top) -> Monthly (middle) -> Annual (bottom, highlighted as "Best Value" or "Most Popular")

**Why this works:**
- Weekly at $9.99 creates sticker shock ($519/year equivalent)
- Monthly at $29.99 looks reasonable compared to weekly ($359/year equivalent)
- Annual at $99.99 looks like a steal compared to both (81% savings vs weekly)
- The monthly tier is the decoy: it exists only to make annual look better

### "Less Than a Coffee" Framing

Always break annual price into daily or weekly equivalents:
- "$99.99/year = less than $2/week"
- "That's less than one coffee per week"
- "27 cents per day to master AI"

---

## Paywall Placement

### The Cardinal Rule

**Show the paywall AFTER the aha moment, never during onboarding.**

Users who have not experienced value will never convert. The paywall is not a gate to keep people out; it is an upgrade path for people who already want more.

### Optimal Placement Triggers for Learning Apps

| Trigger | Timing | Expected Conversion Lift |
|---------|--------|------------------------|
| After completing first lesson | Best first touchpoint | Baseline |
| After hitting daily lesson limit | Natural friction point | +20-35% vs random |
| After 3-day streak | Habit is forming | +40-60% vs day 1 |
| After earning first badge/XP milestone | Achievement high | +25-40% vs random |
| When trying to access premium tool | Intent-based | +50-70% vs random |

### Placement Sequence for 3 Minute AI

1. **Day 1**: User completes first lesson. Show brief premium teaser (not a full paywall). "Unlock unlimited lessons and certificates" as a dismissible banner.
2. **Day 2-3**: User hits daily lesson limit. Show soft paywall with trial offer. "Start your 7-day free trial to keep learning."
3. **Day 3-5**: User has a streak going. Show paywall with streak-preservation angle. "Don't lose your streak. Premium members get unlimited daily lessons."
4. **Day 7+**: User is engaged but still free. Show paywall with social proof and full pricing. This is the high-intent segment.

---

## Social Proof on Paywall Screens

### Elements That Convert

1. **User count badge**: "Join 50,000+ learners mastering AI" (top of paywall)
2. **Review snippets**: 2-3 short quotes with star ratings and first name + photo
3. **Before/after comparison**: "Free vs Premium" feature table
4. **Trust badges**: App Store rating, press mentions, security certifications
5. **Urgency (optional)**: "Limited time: 50% off first year" with countdown

### Comparison Table Format

| Feature | Free | Premium |
|---------|------|---------|
| Daily lessons | 1/day | Unlimited |
| AI tools | Basic (2 tools) | All 10+ tools |
| Progress tracking | Basic | Advanced analytics |
| Certificates | No | Yes |
| Streak protection | No | 1 free/week |
| Ads | Yes | No |
| Community access | View only | Full access |

---

## Conversion Benchmarks

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| Paywall view rate (% of users who see paywall) | <30% | 40-50% | 55-70% | >75% |
| Trial start rate (% of paywall viewers) | <5% | 8-12% | 15-25% | >30% |
| Trial-to-paid conversion | <20% | 30-40% | 45-55% | 60-70% |
| Free-to-paid (overall, soft paywall) | <1% | 2-3% | 4-5% | >6% |
| Monthly churn (subscribers) | >15% | 8-12% | 5-7% | <4% |
| Paywall dismiss rate | >90% | 75-85% | 60-70% | <55% |

---

## Apple and Google Compliance

### Required Elements (Both Platforms)

1. **Subscription terms disclosure**: Price, billing period, renewal terms must be visible before purchase
2. **Restore Purchases button**: Must be accessible on the paywall screen (Apple rejects apps without this)
3. **Terms of Service link**: Must link to subscription ToS
4. **Privacy Policy link**: Required on paywall
5. **Free trial terms**: Must clearly state when billing begins and how to cancel
6. **Auto-renewal disclosure**: "Subscription automatically renews unless cancelled at least 24 hours before the end of the current period"

### Apple-Specific Requirements

- No external payment links (anti-steering rules relaxed in some regions but still risky)
- Subscription management must use `SKPaymentQueue` / StoreKit 2
- Price must match what is configured in App Store Connect
- Free trial disclosure must include: trial duration, price after trial, cancellation instructions
- Apple takes 30% (year 1) / 15% (year 2+, Small Business Program)

### Google-Specific Requirements

- Must use Google Play Billing Library
- Subscription offer details screen required before purchase
- Grace period and account hold are configurable in Play Console
- Google takes 15% (first $1M/year) / 30% (above $1M)

### Compliance Checklist for Paywall Screen

```
[ ] Subscription price clearly displayed
[ ] Billing frequency stated (weekly/monthly/annual)
[ ] Free trial duration and post-trial price shown
[ ] Auto-renewal terms disclosed
[ ] "Restore Purchases" button visible
[ ] Terms of Service link
[ ] Privacy Policy link
[ ] Cancel instructions or link to subscription management
[ ] No misleading "free" claims without trial terms
[ ] Price matches store configuration exactly
```

---

## Implementation Checklist

When building or optimizing a paywall for 3 Minute AI:

1. **Strategy**: Soft paywall with 7-day free trial on premium tier
2. **Pricing**: 3-tier decoy structure (weekly/monthly/annual), annual as target
3. **Placement**: After first lesson completion, escalating through engagement triggers
4. **Social proof**: User count, review snippets, feature comparison table
5. **Compliance**: All Apple/Google required disclosures present
6. **Winback**: Automated re-engagement sequence for lapsed subscribers (see winback reference)
7. **Testing**: A/B test paywall copy, pricing display order, and trial length
8. **Analytics**: Track paywall view rate, trial start rate, trial-to-paid, and paywall dismiss rate
