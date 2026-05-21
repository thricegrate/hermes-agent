# X Algorithm: What the Source Code Actually Says

This isn't "algorithm tips" from social media gurus. These are from the actual open-source Earlybird ranking system that X/Twitter uses to score and distribute tweets. Each section gives you the raw mechanic, then tells you what to do about it.

## Contents
- The Earlybird Scoring Formula
- The Small Account Advantage (MTL Normalization)
- The One-Like Viral Gateway (UTEG Social Proof)
- Topic Matching (SimClusters)
- Deep Engagement Signals (Bookmarks & Shares)
- The Complete Viral Loop
- What Kills Your Reach (Penalty Signals)
- The Reply-First Content Checklist

---

## The Earlybird Scoring Formula

```
Score = (replies x 10,000) + (likes x 1,000) + (quotes x 1,000)
```

Replies are worth 10x more than likes. Not "a bit more." Not "somewhat more." Ten times. Likes and quotes are scored equally. Retweets have separate distribution mechanics.

**The math that changes everything:**

| Scenario | Replies | Likes | Score |
|----------|---------|-------|-------|
| Post A: reply-heavy | 50 | 100 | 600,000 |
| Post B: like-heavy | 2 | 500 | 520,000 |
| Post C: balanced | 20 | 200 | 400,000 |

Post A wins despite having fewer total engagements than Post B. The 50 replies carry it. Post B has 502 total engagements vs Post A's 150, but Post A scores higher.

**Writing Rule:** Engineer every post for replies first, everything else second. A post that gets 50 replies and 100 likes beats a post that gets 500 likes and 2 replies. Reply generation is the single highest-leverage skill on X.

**Practical tactics:**
- End with a real question (not rhetorical -- one people actually answer)
- Use "completion gaps" (intentionally leave something out so people reply "you missed X")
- Comment-gated CTAs ("write X in comments") are algorithmically optimal -- they directly generate the highest-value signal
- Provocative/contrarian takes that split the audience into camps generate debate replies
- "Unpopular opinion" and "hot take" formats work because they provoke disagreement replies
- Ask people to share their version: "What's yours?" "What would you add?"

---

## The Small Account Advantage (MTL Normalization)

The algorithm has a built-in follower-count normalizer called `RescoreMTLNormalization`. It adjusts scores upward for low-follower authors so they compete fairly against large accounts.

Your engagement-per-follower ratio matters more than raw numbers. A 500-follower account with 10 replies gets a HIGHER normalized score than a 50K account with the same 10 replies. The algorithm is literally designed to give small accounts a fair shot.

**Writing Rule:** Stop chasing follower count. A smaller, engaged audience is algorithmically superior to a large, passive one. This is why niche content outperforms broad content -- smaller audience, higher engagement rate, better normalization score.

**Practical tactics:**
- Focus on engagement rate, not follower count as your north star metric
- Don't buy followers or do follow-for-follow -- inflating followers without matching engagement HURTS your normalization score
- Niche down hard. 500 followers who all care about your topic > 5,000 who vaguely followed you once
- Your first 100 engaged followers matter more than your next 10,000 passive ones
- When evaluating performance, look at engagement/follower ratio, not raw numbers

---

## The One-Like Viral Gateway (UTEG Social Proof)

The User Tweet Entity Graph (UTEG) has a social proof threshold of just 1 (`MinNumFavoritedByUserIds = 1`).

ONE like from someone who follows you makes your tweet eligible to appear in the feeds of THEIR followers as an out-of-network recommendation. Not 10 likes. Not 100. One single like is the gateway to the viral loop.

**Writing Rule:** Your first few engaged followers are your most important asset. When someone consistently likes your content, your tweets get shown to their entire network. Every engaged follower is a distribution channel.

**Practical tactics:**
- Build a core group of 20-50 people who consistently engage with your content. They are your distribution network.
- When you engage with other creators' content (genuine comments, not "great post!"), you become their "connected user." Their followers start seeing YOUR content too.
- This is why the "engage with 5-10 posts from target accounts daily" strategy works -- you're building UTEG connections, not just being nice.
- Respond to every reply on your tweets. Each response builds a connection that makes your future tweets eligible for their followers' feeds.
- Quality of followers > quantity. One active follower who likes every tweet = your content shown to their entire network.

---

## Topic Matching (SimClusters)

The algorithm uses AI embeddings called SimClusters to match tweets to user interest clusters. The minimum matching threshold is very low: `MinScore = 0.072`.

If your tweet clearly maps to a topic cluster (like "machine learning," "newsletters," "solopreneurship"), it gets surfaced to people interested in that topic -- regardless of your follower count. Clear, topic-specific language is how you get discovered by people who don't follow you yet.

**Writing Rule:** Stay on-topic within each tweet. Use specific terminology your audience uses. The algorithm builds a topic profile for you over time -- niche consistency beats random variety. Vague, generic language confuses the topic matcher and makes you invisible to interested users.

**Practical tactics:**
- Use the actual words your niche uses. "Claude prompts for SEO" is matchable. "Cool AI stuff" is not.
- Don't mix topics in one tweet. A post about AI + fitness + philosophy confuses SimClusters. Pick one.
- Consistency across posts matters. The algorithm learns YOUR topic profile. If you post about AI automation for 20 tweets, then random cooking content, the cooking tweet won't match anyone.
- The 0.072 threshold is very low -- you don't need to be a perfect topic match. Just be clear and specific.
- Industry jargon actually helps here. It signals which cluster you belong to.
- This is why niche accounts grow faster than "lifestyle" accounts -- clear topic matching.

---

## Deep Engagement Signals (Bookmarks & Shares)

The algorithm tracks `PredictedBookmarkScoreFeature` and `PredictedShareScoreFeature` as distinct high-value engagement signals, separate from likes.

A bookmark signals "I need this later" (utility). A share signals "others need this" (status transfer). Both indicate deeper interest than a casual double-tap like, and the algorithm treats them as stronger quality indicators.

**Writing Rule:** Design for bookmarks AND replies. They serve different functions. Replies drive your Earlybird score (10,000 pts each). Bookmarks signal deep utility to the algorithm's quality assessment. The best content generates both: a useful reference resource (bookmarks) with a provocative angle or question (replies).

**Practical tactics:**
- For bookmarks: make content a reference resource, not a one-time read. Prompt packs, tool lists, cheat sheets, numbered frameworks.
- For shares: make sharing your content a status signal. "If I share this, I look smart/informed/generous."
- The ideal tweet is save-worthy AND debate-worthy. A list of prompts (save) with a controversial take about why most people use AI wrong (reply).
- Add explicit save CTAs: "(Save for later)" or "(Bookmark this)" -- but pair them with a reply prompt too.

---

## The Complete Viral Loop

Here's how a tweet goes from zero to viral, with the actual thresholds at each step:

```
1. You post a tweet with clear topic language
   └─ SimClusters can match it to interest clusters (threshold: 0.072)

2. A follower likes it
   └─ UTEG social proof threshold met (just 1 like needed)

3. Tweet becomes eligible for out-of-network recommendations
   └─ Shown to ~50-100 people who follow that person

4. Out-of-network penalty applies
   └─ 0.75x multiplier on score for non-followers (you start at a disadvantage)

5. MTL normalization kicks in
   └─ If you have few followers, your score gets BOOSTED (small account advantage)

6. Some of those new people reply
   └─ Each reply = 10,000 Earlybird points (10x a like)

7. Score jumps, shown to more people
   └─ More replies = more score = more distribution

8. Exponential growth if reply rate holds
   └─ The loop feeds itself until engagement rate drops
```

**The key insight:** The viral loop has a specific entry point. Get ONE like from an engaged follower on a topically clear tweet. That's it. Everything else is downstream. Your first-follower engagement strategy matters more than your 10,000th-follower acquisition strategy.

**Why most tweets don't go viral:** They fail at step 1 (vague topic language, poor SimClusters matching) or step 2 (no engaged followers to trigger UTEG). The algorithm isn't suppressing you. You're not giving it what it needs to distribute you.

---

## What Kills Your Reach (Penalty Signals)

These are negative signals from the algorithm source code. They subtract from your score or multiply it downward.

| Signal | Penalty | What It Means |
|--------|---------|---------------|
| "Not Interested" clicks | Up to -10,000 | One click wipes out 10 likes or 1 reply worth of score |
| Reports | Up to -20,000 | Nuclear. Two reports undo 20 likes worth of reach |
| Mutes/blocks | -1,000 each | Every mute costs you a like's worth of score |
| Out-of-network penalty | 0.75x multiplier | All tweets shown to non-followers start at 75% effectiveness |
| Same-author fatigue | Decays to 0.25x | After multiple tweets shown, each new one is worth only 25% |

**Writing Rules:**

**Don't spam-post.** The same-author fatigue decay is brutal. If someone sees 4 of your tweets, the 5th is shown at 25% effectiveness. Posting 10x/day doesn't mean 10x the reach. It means each post gets a fraction of what it could have gotten. 3-5 high-quality posts/day beats 10 mediocre ones. The algorithm literally punishes volume over quality.

**Don't irritate people.** A single "Not Interested" click costs you -10,000 points. That's the same as losing a reply or 10 likes worth of score. If your content makes people click "Not Interested," you're actively destroying your reach. Generic, repetitive, off-topic content triggers this.

**Don't be report-bait.** Reports cost up to -20,000 points each. Two reports nuke 20 likes worth of score. Be provocative enough to spark replies, but not offensive enough to trigger reports. There's a line between "hot take" and "reported."

**Don't grow followers without engagement.** Every new follower who doesn't engage with you worsens your MTL normalization ratio. Follower count without matching engagement is a liability, not an asset.

**Practical anti-pattern checklist:**
- [ ] Am I posting more than 5x/day? (fatigue decay will eat my reach)
- [ ] Is this tweet so generic people might hit "Not Interested"? (-10,000 per click)
- [ ] Could this get reported? (-20,000 per report)
- [ ] Am I posting off-topic from my usual content? (SimClusters confusion + "Not Interested" risk)
- [ ] Am I repeating the same format/hook I used yesterday? (pattern fatigue + "Not Interested")

---

## The Reply-First Content Checklist

Based on everything above, run this checklist before posting on X:

1. **Reply trigger?** Does this post have a built-in reason for people to reply? (question, gap, controversy, "what's yours?")
2. **Topic clarity?** Would SimClusters know what this is about? Can you name the topic in 2 words?
3. **Save-worthy?** Is this something people would bookmark to reference later?
4. **Not irritating?** Would anyone click "Not Interested" on this? Is it generic enough to bore people?
5. **Fatigue check?** Have I already posted 3+ times today? (if yes, this better be exceptional)
6. **Connected users?** Have I engaged with other creators today so my UTEG connections are warm?

If you can't check boxes 1 and 2, don't post. Those are the entry points to the viral loop.

---

## Source & Caveats

These mechanics come from the open-source Earlybird ranking system repository. The algorithm evolves continuously -- specific thresholds and weights may shift over time. But the structural priorities (replies >> likes, topic matching, small-account normalization, penalty signals) represent fundamental design decisions that are unlikely to change dramatically.

Use these as directional guidance, not absolute rules. The principles matter more than the exact numbers.
