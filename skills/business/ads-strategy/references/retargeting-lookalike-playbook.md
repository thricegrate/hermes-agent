# Retargeting & Lookalike Audience Playbook

Source: LearnWorlds "Essential Guide Selling Online Courses Using Facebook Ads"

## Core Principle

98% of web visitors don't convert on first visit. Retargeting that 98% is the highest-leverage paid ads move available. The Facebook Pixel compounds in value over time — install it immediately, even before running any ads.

---

## 1. Facebook Pixel Setup

Install the Pixel on every page. Standard events to track:
- **PageView** (all pages)
- **CompleteRegistration** (with login method data)
- **Purchase** (with product name, ID, type, price, currency)

Custom Conversions (trackable independently of specific ads):
- Add Payment Info, Complete Registration, Initiate Checkout, Lead, Purchase, Search, View Content

**Rule:** Install Pixel day one. The longer it runs, the smarter targeting becomes.

---

## 2. Retargeting Campaign Structure

### Three Use Cases
1. **Brand reminder** — stay top-of-mind with past visitors
2. **Discount/coupon delivery** — incentivize non-buyers to return
3. **Upsell/cross-sell** — offer complementary products to existing customers

### Custom Audience Setup
- Create Custom Audience from Website Traffic in Ads Manager
- **Window sweet spot:** 40-60 days (default 30, max 180)
- For product-specific retargeting: use "People who visit specific web pages" with URL keyword matching (e.g., "online-advertising" in the URL)

### Abandoned Cart Audience (Custom Combination)
This is the highest-converting retargeting segment:
1. **Include:** People who visited the checkout/pricing URL
2. **Exclude:** People who visited the course player/thank-you URL (already purchased)
3. This creates a precise "almost-bought" audience

**Rules:**
- Always exclude purchasers from retargeting campaigns
- Stop abandoned cart retargeting after **7-10 days** — beyond this, ads become annoying rather than persuasive
- Never retarget sensitive categories (kids' content, health, religion)

---

## 3. Retargeting Ad Creative

### Two Recommended Formats
- **Video ads** (autoplay in feed) — highest engagement
- **Slideshows** — lower production cost than video, still effective

### Three Required Elements
1. Engaging headline that piques attention
2. Click-worthy CTA button
3. Gets to the point quickly with an incentive

### Transparency Tactic
Acknowledge the retargeting explicitly in ad copy rather than being creepy about it:
> "We are not sure why you didn't complete your recent transaction at our school but if you do it now we will give you 20% off!"

This approach disarms suspicion and adds value simultaneously.

---

## 4. Lookalike Audiences

### Source Options (ranked by quality)
1. **Existing Custom Audience** from website visitors (Pixel data)
2. **Email list upload** from newsletter/CRM — Facebook matches emails to user profiles
3. **Facebook Page engagement** data

### Email List Pipeline (most relevant for newsletter businesses)
1. Export subscriber list (CSV)
2. Upload to Facebook Custom Audiences
3. Facebook matches emails to user profiles (not all match — personal vs. professional email mismatch)
4. Build Lookalike from matched profiles

### Audience Size
- **Slider:** 1%-10% of target country population
- **Start at 1%** for tightest match to source audience
- At 1% for US = ~2.1 million people
- **Minimum source audience:** 100 people from same country (more is better)

### Layering
After creating Lookalike, layer demographic and interest filters on top for tighter targeting. Don't rely on Lookalike alone.

---

## 5. Metrics Framework

| Metric | What It Tells You | Action |
|--------|-------------------|--------|
| **ROAS** | Total return based on Pixel-recorded conversions | Primary success metric. Scale campaigns producing positive ROAS |
| **Relevance Score** | How well your ad matches the audience | Higher score = lower CPC. Facebook rewards relevant ads |
| **CTR** | Click-through rate | Directly affects Relevance Score. Improve with appropriate CTAs, simple copy, low frequency |
| **CPM** | Cost per 1,000 impressions | Monitor for audience saturation |
| **CPA** | Cost per action | Right metric when goal is action beyond a click |
| **CPL** | Cost per lead (ad spend / leads) | Track for lead gen campaigns |

---

## 6. Budget Rules

- **Start:** $8-10/day per campaign
- **Success threshold:** Campaign producing $1 more in sales than it costs
- **Scale rule:** Once you find a winning campaign, increase budget gradually (20% per day max to avoid learning phase reset)
- **Review cycle:** Review results, identify what's working, iterate

---

## 7. Application to Newsletter/Product Funnels

For a newsletter business with 200K+ subscribers:
1. Upload subscriber list → build Lookalike → run cold acquisition ads to Lookalike audience
2. Install Pixel on all sales pages, checkout pages, and product pages
3. Build abandoned cart Custom Combination for product launches
4. Retarget non-buyers with incentive ads during launch window (7-10 day cap)
5. Exclude existing buyers from all retargeting campaigns
6. Use Lookalike + interest layering for cold traffic to free tool/lead magnet pages
