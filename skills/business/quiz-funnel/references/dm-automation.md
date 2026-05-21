# DM Automation for Quiz Delivery

An alternative entry point to the quiz funnel that drives engagement metrics AND captures leads simultaneously. Instead of routing through link-in-bio, viewers comment a keyword and receive the quiz link via DM.

---

## Why Comment-Gated Quiz Delivery Works

1. **Algorithm boost:** Comments are the highest-weight engagement signal on Instagram and TikTok. A reel that generates 200 comments distributes further than one with 200 likes.
2. **Intent signal:** Someone who comments a keyword has higher purchase intent than someone who clicks a link-in-bio. They took a deliberate action.
3. **DM channel opened:** Once they receive a DM, you have a direct communication channel that bypasses the feed algorithm entirely.
4. **Double capture:** You get both the DM channel AND the email (when they complete the quiz). Two touchpoints instead of one.

---

## The Comment-to-Quiz Pipeline

```
Viewer watches UGC reel
  -> CTA: "Comment [KEYWORD] and I'll send you the quiz"
  -> ManyChat detects keyword comment
  -> ManyChat sends DM with quiz link + brief context
  -> Viewer clicks link, takes quiz
  -> Quiz captures email before showing results
  -> Quiz recommends product based on answers
  -> Email sequence follows up by quiz path
  -> ManyChat DM sequence follows up in parallel
```

---

## ManyChat Setup

**Platform:** ManyChat (manychat.com) -- works with Instagram and Facebook. For TikTok, use TikTok's native auto-reply or a custom solution.

### Trigger Configuration
- **Trigger type:** Comment keyword
- **Keywords:** Set 2-3 variants (e.g., "QUIZ", "quiz", "Quiz", "READY", "YES")
- **Platform:** Instagram DM (primary), Facebook Messenger (secondary)

### DM Message Sequence

**Message 1 (immediate, upon keyword comment):**
> "Hey! Here's your personalized quiz -- it takes about 90 seconds and tells you exactly which [product/approach] fits your situation: [QUIZ URL]
>
> Fair warning: be honest with the answers. The recommendation is only as good as the info you give it."

**Message 2 (24 hours later, if quiz not completed):**
> "Did you get a chance to take the quiz? No pressure -- just wanted to make sure the link worked. Here it is again: [QUIZ URL]"

**Message 3 (48 hours later, if quiz completed but no purchase):**
> "I saw you finished the quiz! How did the recommendation feel? If you have questions about [recommended product], just reply here -- happy to help."

### Tracking
- Tag each DM lead with the keyword they used (for multi-campaign tracking)
- Pass UTM parameters in the quiz link: `?utm_source=instagram&utm_medium=dm&utm_campaign=[reel_id]`
- Track DM-to-quiz-completion rate separately from link-in-bio-to-quiz rate

---

## UGC Script CTA Integration

The CTA in Section 6 of the UGC Cold Traffic script architecture changes when using DM automation:

**Standard (link-in-bio):**
> "The link is below if you want to see what I used."

**DM automation:**
> "Comment QUIZ and I'll send you a quick assessment that tells you exactly which [product/approach] fits your situation."

**Why DM CTA works better for cold traffic:**
- Lower friction than "click the link in bio" (which requires navigating to the profile)
- The act of commenting creates public social proof (other viewers see the comments)
- The DM feels personal, like a 1:1 recommendation
- Comment volume boosts the reel's algorithmic distribution

---

## Platform-Specific Notes

### Instagram
- ManyChat's Instagram DM automation is the most mature option
- Keyword triggers work in both Reels comments and Story replies
- Stories + "DM me QUIZ" is an additional entry point beyond Reels
- Limitation: Instagram limits automated DMs to accounts that have interacted first (the comment satisfies this)

### TikTok
- TikTok's native auto-reply feature handles basic keyword triggering
- For more sophisticated flows, use a custom webhook to TikTok's messaging API
- Limitation: TikTok DM automation is less mature than Instagram. Consider routing TikTok viewers to link-in-bio instead.

### Facebook
- ManyChat's original platform. Full automation capability.
- Works well for Facebook Reels and regular video posts
- Messenger has higher open rates than email (~80% vs ~25%)

---

## Metrics to Track

| Metric | Benchmark | Why It Matters |
|--------|-----------|----------------|
| Comment-to-DM rate | 85-95% | ManyChat reliability. Below 85% = tech issue. |
| DM-to-quiz-start rate | 50-70% | Message quality. Below 50% = rewrite DM copy. |
| Quiz completion (DM traffic) | 65-80% | Should be higher than link-in-bio traffic (higher intent). |
| DM lead-to-purchase (30 day) | 8-15% | Combined quiz + DM sequence conversion. |
| Comments per reel (DM CTA vs standard CTA) | 2-5x standard | The algorithm boost from comment volume. |

---

## Integration

- **Receives from:** `video-scriptwriter` UGC Cold Traffic CTA (Section 6 adapted for comment keyword)
- **Feeds into:** `quiz-funnel` (quiz link as DM destination), `email-sequence` (email captured within quiz), `content-social` (comment volume data informs content strategy)
- **Parallel channel:** DM sequences run alongside email sequences for dual-channel follow-up. Don't send the same message on both channels on the same day.
