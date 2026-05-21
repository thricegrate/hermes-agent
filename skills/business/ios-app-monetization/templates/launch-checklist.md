# iOS App Launch Checklist

End-to-end checklist that ties the 5 modes of the skill together. Use this from concept to first $10K MRR.

For each section, the linked references explain WHY the rule exists. This template is the WHAT to do, in order.

## Phase 0: Pre-launch foundations (week -2 to week 0)

Apply for these on day 1 of the project. They take 1-2 weeks to approve and you do not want to wait once revenue is coming in.

- [ ] **Apple Developer account** ($99/year, 1-2 day approval)
- [ ] **Apple Small Business Program enrollment** (cuts fees from 30% to 15%, 1-2 week approval)
  - Why: 50% margin improvement on every subscription. Free to apply. See [../references/apple-compliance.md](../references/apple-compliance.md).
- [ ] **TikTok Ads account** (instant)
- [ ] **TikTok ad credit verification** (the $6K matched credit auto-applies on new accounts; verify it shows in your account)
  - Why: Doubles your effective ad budget for the first $6K of spend. See [../references/metrics-and-cheat-codes.md](../references/metrics-and-cheat-codes.md).
- [ ] **App Store Connect access** confirmed
- [ ] **Domain + email** for the app (Privacy Policy and Terms hosted)
- [ ] **Stripe / RevenueCat account** for subscription management (RevenueCat handles iOS subscription complexity well)

## Phase 1: Concept locked (week 0)

Before writing any code, lock the concept. See [../references/app-strategy.md](../references/app-strategy.md).

- [ ] **Studied 3-5 competitor apps** using [competitor-study.md](competitor-study.md)
- [ ] **Identified the core human desire** (one sentence, "I want..." or "I am scared of...")
- [ ] **Defined the viral feature** (one screen-recordable reveal moment)
- [ ] **Picked your "study + improve + own angle" position** (which app you are improving on, what you are improving, what your angle is)
- [ ] **Confirmed the concept is NOT a direct clone** of any studied competitor

If any item above is fuzzy, the concept is not ready. Refine first. Code second.

## Phase 2: App build (week 1-3)

The app does not need to be perfect. It needs to deliver the viral feature reveal and have enough substance to pass Apple review.

- [ ] **Onboarding flow built** (3-5 personalization questions max)
- [ ] **Viral feature working** (the reveal moment is screen-recordable)
- [ ] **Result screen** (shows the user their score / scan / prediction)
- [ ] **At least 3-4 functional screens beyond the paywall** (Apple rejects "thin content" apps)
- [ ] **Paywall built** ($12.99/week + $59.99/year, hard paywall, no skip button)
  - Required elements per [../references/apple-compliance.md](../references/apple-compliance.md):
    - [ ] Subscription length and price visible
    - [ ] Auto-renewal disclosure
    - [ ] Restore Purchases button
    - [ ] Terms of Service link
    - [ ] Privacy Policy link
- [ ] **Retention offer flow built** ($44.99/year inside Cancel flow ONLY)
  - [ ] Triggers when user goes to Settings → Subscriptions → Cancel
  - [ ] Does NOT trigger as a popup, banner, or push notification
- [ ] **iOS App Events SDK installed** (for TikTok event tracking)
- [ ] **Subscription event firing correctly** (test with TikTok Ads Manager event verification)

## Phase 3: App Store submission (week 3-4)

Pre-submission checklist before pressing Submit. See [../references/apple-compliance.md](../references/apple-compliance.md) for full guideline reference.

### Build readiness

- [ ] App passes a full personal walk-through (open → onboarding → reveal → paywall → cancel flow)
- [ ] All copy proofread (no typos, no broken strings)
- [ ] No crashes in 5 minutes of normal use
- [ ] Restore Purchases button works (test by canceling on one device, restoring on another)
- [ ] Privacy Policy and Terms of Service URLs live and accessible

### App Store listing

- [ ] App name (matches the app, not a clone of a competitor's name)
- [ ] Subtitle (one line summarizing the core promise)
- [ ] Description (matches actual functionality, no misleading claims)
- [ ] Screenshots (real app content, 9:16 portrait)
- [ ] Optional: app preview video (10-30 seconds)
- [ ] App icon (distinct, not a clone of a competitor's icon)
- [ ] Privacy section (matches actual data collection)
- [ ] Keywords (researched for ASO; see `skills/app-store-optimization/SKILL.md` if available)
- [ ] Age rating
- [ ] Pricing tier set in App Store Connect

### Submission

- [ ] Build uploaded to App Store Connect
- [ ] Build assigned to the right version
- [ ] All required compliance answers filled in (Export Compliance, Content Rights, etc.)
- [ ] Submit for review

Approval takes 24-48 hours typically. Expect 1-2 rounds of rejection on first launch (usually for missing Restore Purchases button or unclear paywall disclosure). Fix and resubmit fast.

## Phase 4: Ad creative production (week 3-4, parallel to App Store submission)

Once the app is in review, produce the ads. See [../references/before-after-ad-workflow.md](../references/before-after-ad-workflow.md).

- [ ] **Recorded action footage** (you doing the app's action, 5-10 seconds, phone camera)
- [ ] **Generated 10-12 AI face/body images** with Z-Image Turbo (LoRA), matching the target demographic
  - [ ] Used the variant prompt template ([ad-batch-prompt.md](ad-batch-prompt.md))
- [ ] **Ran face-swap through SwapTok** (or equivalent tool)
- [ ] **Edited 10-12 ad variants** in CapCut or TikTok Studio
  - Each ad has:
    - [ ] Hook in first 2 seconds
    - [ ] Before/after structure
    - [ ] App reveal screenshot in the middle
    - [ ] Trending audio
    - [ ] Comment-bait element
    - [ ] Soft CTA at the end
- [ ] **All variants exported** at 9:16 portrait, 1080x1920

## Phase 5: TikTok campaign launch (day of App Store approval)

See [../references/tiktok-smartplus-campaigns.md](../references/tiktok-smartplus-campaigns.md).

- [ ] **TikTok pixel verified** (subscription event fires correctly)
- [ ] **Campaign created**: Smart+, optimize for Subscription event, USA only, $50/day
- [ ] **4-6 ads uploaded** (best variants from the 10-12 produced)
- [ ] **Campaign launched**

Initial test window: 2-3 days. Do NOT change anything during this period.

## Phase 6: Daily metric check (continuous from launch)

See [../references/metrics-and-cheat-codes.md](../references/metrics-and-cheat-codes.md).

Daily, under 60 seconds:

- [ ] CPI per ad (target < $2.00)
- [ ] CTR per ad (target > 1.00%)
- [ ] CPA per ad (target < LTV; LTV ≈ $30)
- [ ] Decisions:
  - [ ] Scale: ad hits all 3 metrics for 3+ days → +30% budget
  - [ ] Hold: 2 of 3 metrics hit → leave alone for another 2-3 days
  - [ ] Kill: all 3 missing for 3+ days → kill the ad, make new creative

## Phase 7: Comment management (daily, 10 minutes)

- [ ] **Review TikTok ad comments**
- [ ] **Delete revenue-killing comments**:
  - "It costs money"
  - "It is just AI"
  - "It is a scam"
- [ ] **Keep engagement-driving comments**:
  - Arguments about results
  - Reactions to comment-bait
  - Debates between commenters

## Phase 8: Variant production (week 2 onward)

Once you have a winning ad:

- [ ] **Spin 8-10 variants of the winner** using the same hook, different person/story
- [ ] **Run alongside the original winner**
- [ ] **Track which variants outperform**
- [ ] **Retire weak variants, expand strong ones**

For component-level variation at scale (when you want to multiply 1 winner into 1000+), see `skills/ugc-production/templates/variation-from-winner-reel.md`.

## Phase 9: Scaling (week 3-8)

- [ ] **Scale budget +30% every 3 days** when metrics stay green
- [ ] **Watch for saturation signals** (CPA creeping up, CTR dropping, conversions plateauing)
- [ ] **Add UK / Canada / Australia** when US plateaus
- [ ] **Begin testing new creative angles** for the next winner

## Phase 10: Cashflow management (continuous)

See [../references/metrics-and-cheat-codes.md](../references/metrics-and-cheat-codes.md).

- [ ] **First Apple payout** arrives 45-60 days after first revenue
- [ ] **Reinvest first payout** into ad spend
- [ ] **Track gross subscription revenue vs ad spend** weekly
- [ ] **Apply Apple Small Business Program savings** to the math (15% fee, not 30%)

## Phase 11: Iterate or build the next one

After 8-12 weeks:

### If the app is profitable
- [ ] Continue scaling
- [ ] Add markets
- [ ] Test new creative angles
- [ ] Optimize paywall A/B tests (per [../references/paywall-and-pricing.md](../references/paywall-and-pricing.md))
- [ ] Add push notification retention (per `skills/push-notification-strategy/SKILL.md` if available)

### If the app is breakeven
- [ ] Investigate the bottleneck (which step in the funnel is dropping)
- [ ] Test paywall variants
- [ ] Test new creative angles
- [ ] Give it another 4-6 weeks to find a winner

### If the app is unprofitable after 8-12 weeks
- [ ] Archive the app
- [ ] Document the lessons (what worked, what failed, what surprised you)
- [ ] Build the next one (the lazymaxxers approach favors velocity over polish)

## The "I'm done" exit criteria

The app is at $10K MRR when:

- ~333 active weekly subscribers at $12.99/week (100% weekly), OR
- ~166 active annual subscribers at $59.99/year (100% annual), OR
- Some mix of weekly + annual + retention totaling $10K MRR

Realistic mix at $10K MRR:
- 200 weekly subscribers at $12.99 = $10,400/month gross
- Plus 50 annual subscribers at $59.99/12 = $250/month gross
- Plus 30 retention offer subscribers at $44.99/12 = $112/month gross
- Total: ~$10,762/month gross
- Apple fee at Small Business Program (15%): ~$1,615/month
- Net: ~$9,147/month after Apple

To net $10K MRR, gross is closer to $11.7K/month. Add ad spend on top of that to determine actual profit.

## Cross-references

- Full skill: [../SKILL.md](../SKILL.md)
- App strategy reference: [../references/app-strategy.md](../references/app-strategy.md)
- Paywall reference: [../references/paywall-and-pricing.md](../references/paywall-and-pricing.md)
- Apple compliance reference: [../references/apple-compliance.md](../references/apple-compliance.md)
- TikTok campaigns reference: [../references/tiktok-smartplus-campaigns.md](../references/tiktok-smartplus-campaigns.md)
- Ad workflow reference: [../references/before-after-ad-workflow.md](../references/before-after-ad-workflow.md)
- Metrics + cheat codes reference: [../references/metrics-and-cheat-codes.md](../references/metrics-and-cheat-codes.md)
- 3 Minute AI-specific application: [../references/3-minute-ai-application.md](../references/3-minute-ai-application.md)
