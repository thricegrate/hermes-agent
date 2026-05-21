# Apple Compliance: What Gets Banned and How to Avoid It

Apple's review process is consistent. Founders who follow the rules get approved fast. Founders who do not lose weeks in the appeal process burning cashflow.

This file covers the rejection patterns that kill iOS app launches and the patterns that ship every time.

## The 5 rejection patterns that kill launches

### 1. Direct cloning of another app

Apple rejects apps that copy another app's UI, branding, or core feature set without meaningful differentiation. The original founder also reports clones, which gets the app pulled even after launch.

**What "direct clone" looks like to Apple:**
- Same color palette + same typography + same screen flow
- Same core feature with the same UX
- Same app name structure ("Face Score" → "Face Rate" reads as clone)

**How to avoid:**
- Take the blueprint, improve the execution
- Use a different aesthetic (different colors, fonts, illustrations)
- Add at least one feature dimension the original does not have
- Use a different app name and a different positioning angle

See [app-strategy.md](app-strategy.md) for the "study + improve + own angle" formula.

### 2. Retention offer shown outside the cancellation flow

The retention offer is one of the highest-leverage revenue features. It is also one of the most common rejection causes when implemented wrong.

**What gets rejected:**
- Retention offer as a popup on app open
- Retention offer as a banner on the main feed
- Retention offer pushed via email or notification
- Retention offer shown before the user has tried to cancel

**The flow Apple approves every time:**

1. User goes to Settings → Subscriptions → Cancel
2. Before the cancellation completes, the app shows a screen: "Wait, before you go..."
3. The retention offer appears at $44.99/year (or whatever discount price)
4. The user can accept the discount and stay, or proceed to cancel

The retention offer must be triggered BY the cancellation attempt, not pushed at the user any other way. This is the only flow that consistently passes review.

### 3. Hidden subscription terms

Apple requires explicit disclosure of subscription terms on the paywall itself. Hidden terms get rejected.

**What must be visible on the paywall:**

- Subscription length (e.g., "Renews weekly")
- Total cost per period (e.g., "$12.99/week")
- Auto-renewal disclosure (e.g., "Subscription auto-renews unless canceled")
- Link to Terms of Service
- Link to Privacy Policy
- "Restore Purchases" button (mandatory)

These elements can be small text, but they MUST be on the paywall screen. Hiding them in a separate Settings page or behind a "Learn More" link gets rejected.

### 4. Misleading paywall copy

Apple's reviewers read paywall copy carefully. Common rejections:

- "Free trial" when there is no actual free trial (the user is charged immediately)
- "Limited time" when the price is not actually limited
- "1 of N spots left" when there is no real scarcity
- "Cancel anytime" without clarifying that auto-renewal continues unless explicitly canceled

If the copy implies something the app does not deliver, it gets flagged.

**How to write paywall copy that ships:**
- Match the copy to the actual mechanics
- "Renews weekly at $12.99" beats "Just $1.85/day" if the actual charge is weekly
- "Cancel anytime in Settings" is fine. "Cancel anytime, no commitment" is misleading if auto-renewal continues.

### 5. Insufficient app substance

Apps that are just a paywall with minimal functionality get rejected as "thin content" or "spam." The app must deliver real value to justify the subscription.

**What gets flagged:**
- App that is essentially just a screen with the viral feature and a paywall
- Subscription that gates almost all functionality with no preview
- Apps where the only feature is the reveal moment and the user must pay for everything else

**How to avoid:**
- Give users meaningful interaction with the viral feature for free (the reveal moment is free)
- Gate the "full report," "history," "advanced features," "additional scans," etc. behind the paywall
- Have at least 3-4 distinct screens of functionality the user can explore
- Real content that provides standalone value (not just a paywall wrapper)

## The Apple Small Business Program (free money)

Apple's Small Business Program cuts the standard 30% fee to 15% for businesses making under $1M/year on the App Store. Free to apply.

**Eligibility:**
- Less than $1M in net proceeds across all your apps in the prior calendar year
- Apply via App Store Connect once eligible

**The math:**

At $12.99/week, Apple's standard 30% fee is $3.90/week. Under the Small Business Program at 15%, the fee drops to $1.95/week. That is $1.95/week back per subscriber, pure profit.

Across 1,000 active weekly subscribers, that is $1,950/week in saved fees. Across 10,000 subscribers, $19,500/week.

**How to apply:**
1. Log in to App Store Connect
2. Go to Agreements, Tax, and Banking
3. Find the Small Business Program section
4. Submit the enrollment form
5. Approval typically takes 1-2 weeks

If you forget to apply, Apple does not auto-enroll you. You will pay 30% indefinitely. Apply on day one.

## Apple's 45-day payout cycle

Apple holds revenue for ~45 days before paying out. Plan cashflow accordingly.

**Why this matters:**
- Day 1: subscriptions start coming in
- Day 30: first month's subscriptions accrue
- Day 45-60: first payout arrives in your bank account

**What this means for ad spend:**
- The TikTok ad credit (matches first $6K spend) helps bridge the cashflow gap
- If you have $1K total to launch with, split it across 2 months. Do not blow it all in week 1 and then wait 45 days for revenue.
- If you have nothing, prove profitability at $50/day for 2-3 weeks, then raise from friends and family or use a credit line

For full cashflow planning, see [metrics-and-cheat-codes.md](metrics-and-cheat-codes.md).

## App Store guidelines that consistently trip up launches

Quick reference for the rules most often violated:

### Guideline 3.1.2 (Subscriptions)
- Subscription terms must be clearly disclosed on the purchase screen
- Auto-renewal disclosure is mandatory
- "Restore Purchases" button is mandatory

### Guideline 4.0 (Design / Spam)
- Apps must offer real functionality beyond a paywall
- Apps that are clones or near-duplicates of other apps get rejected
- Generic "AI [niche]" apps without unique value get flagged

### Guideline 5.1.1 (Privacy)
- Privacy Policy link must be on the paywall
- Data collection must be disclosed in the App Store listing privacy section
- If the app uses face data (face rating apps), the privacy disclosure must be specific

### Guideline 5.6.1 (Misleading apps)
- App description must accurately describe what the app does
- Screenshots must show actual app content (not concept art or marketing mockups)
- Reviews and ratings cannot be incentivized or manipulated

## The pre-submission checklist

Before submitting to App Store review, confirm:

- [ ] Restore Purchases button on paywall
- [ ] Auto-renewal disclosure on paywall ("Subscription auto-renews unless canceled")
- [ ] Subscription length and price clearly visible on paywall
- [ ] Terms of Service link on paywall
- [ ] Privacy Policy link on paywall
- [ ] Retention offer ONLY triggers in the cancellation flow (not anywhere else)
- [ ] At least 3-4 distinct functional screens beyond the viral feature
- [ ] App description matches actual functionality
- [ ] Screenshots show real app content
- [ ] Privacy disclosures match data collection
- [ ] If app uses face data, the privacy section calls it out specifically
- [ ] App is not a direct clone of another shipped app

If any box is unchecked, fix before submission. The 24-48 hour review cycle is fast IF the app passes. The appeal cycle if rejected can take 1-2 weeks.

## What to do if you get rejected

Apple sends a rejection notice with the specific guideline violated and a description of the issue.

**The fastest path back:**

1. Read the rejection notice carefully. The guideline number is the most important thing.
2. Fix the specific issue cited. Do not over-fix; targeted fixes ship faster than overhauls.
3. Reply to the rejection inside Resolution Center with a clear explanation of what was changed.
4. Resubmit.

Most first-time rejections are easy to fix (missing Restore Purchases button, unclear auto-renewal disclosure, retention offer in the wrong place). Once you fix these, subsequent submissions go through smoothly.

## Cross-references

- Paywall structure (the screen that needs to pass compliance): [paywall-and-pricing.md](paywall-and-pricing.md)
- App strategy (avoiding direct cloning): [app-strategy.md](app-strategy.md)
- Cashflow planning around the 45-day payout cycle: [metrics-and-cheat-codes.md](metrics-and-cheat-codes.md)
- App Store listing optimization: `skills/app-store-optimization/SKILL.md` (if available in project)
