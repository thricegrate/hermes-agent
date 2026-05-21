# SaaS Pricing Methodology

This reference consolidates SaaS/subscription pricing strategy: tier structures, packaging, research methods, value metrics, freemium vs free trial, and enterprise pricing.

---

## Pricing Fundamentals

### The Three Pricing Axes

**1. Packaging**: What's included at each tier?
- Features, limits, support level
- How tiers differ from each other

**2. Pricing Metric**: What do you charge for?
- Per user, per usage, flat fee
- How price scales with value

**3. Price Point**: How much do you charge?
- The actual dollar amounts
- Perceived value vs. cost

### Common Value Metrics

| Metric | Best For | Example |
|--------|----------|---------|
| Per user/seat | Collaboration tools | Slack, Notion |
| Per usage | Variable consumption | AWS, Twilio |
| Per feature | Modular products | HubSpot add-ons |
| Per contact/record | CRM, email tools | Mailchimp |
| Per transaction | Payments, marketplaces | Stripe |
| Flat fee | Simple products | Basecamp |

### Choosing Your Value Metric

Ask: "As a customer uses more of [metric], do they get more value?"
- If yes: good value metric
- If no: price doesn't align with value

---

## Tier Structure and Packaging

### How Many Tiers?

**2 tiers:** Simple, clear choice. Works for clear SMB vs Enterprise split. Risk: may leave money on table.

**3 tiers:** Industry standard. Good = Entry, Better = Recommended (anchor), Best = High-value.

**4+ tiers:** More granularity. Works for wide range of customer sizes. Risk: decision paralysis.

### Good-Better-Best Framework

**Good tier (Entry):**
- Purpose: Remove barriers to entry
- Includes: Core features, limited usage
- Price: Low, accessible
- Target: Small teams, try before you buy

**Better tier (Recommended):**
- Purpose: Where most customers land
- Includes: Full features, reasonable limits
- Price: Your "anchor" price
- Target: Growing teams, serious users

**Best tier (Premium):**
- Purpose: Capture high-value customers
- Includes: Everything, advanced features, higher limits
- Price: Premium (often 2-3x "Better")
- Target: Larger teams, power users, enterprises

### Tier Differentiation Strategies

- **Feature gating**: Basic vs advanced features
- **Usage limits**: Same features, different limits
- **Support level**: Email > Priority > Dedicated
- **Access**: API, SSO, custom branding

### Example Tier Structure

```
                Starter         Pro             Business
                $29/mo          $79/mo          $199/mo
Users           Up to 5         Up to 20        Unlimited
Projects        10              Unlimited       Unlimited
Storage         5 GB            50 GB           500 GB
Integrations    3               10              Unlimited
Analytics       Basic           Advanced        Custom
Support         Email           Priority        Dedicated
API Access      No              Yes             Yes
SSO             No              No              Yes
```

---

## Packaging for Personas

### Identifying Pricing Personas

Segment by: company size, use case, sophistication, industry.

| Persona | Size | Needs | WTP | Example |
|---------|------|-------|-----|---------|
| Freelancer | 1 person | Basic features | Low | $19/mo |
| Small Team | 2-10 | Collaboration | Medium | $49/mo |
| Growing Co | 10-50 | Scale, integrations | Higher | $149/mo |
| Enterprise | 50+ | Security, support | High | Custom |

Steps:
1. Define personas
2. Map features to personas
3. Price to value for each persona
4. Research willingness to pay per segment

---

## Pricing Research Methods

### Van Westendorp Price Sensitivity Meter

Four questions to identify acceptable price range:

1. "At what price would you consider [product] so expensive you wouldn't buy?" (Too expensive)
2. "At what price would you question its quality?" (Too cheap)
3. "At what price is it starting to get expensive but you'd still consider?" (Expensive/high side)
4. "At what price is it a bargain?" (Cheap/good value)

**Analysis:** Plot cumulative distributions, find intersections:
- **Point of Marginal Cheapness (PMC):** "Too cheap" crosses "Expensive"
- **Point of Marginal Expensiveness (PME):** "Too expensive" crosses "Cheap"
- **Optimal Price Point (OPP):** "Too cheap" crosses "Too expensive"
- **Indifference Price Point (IDP):** "Expensive" crosses "Cheap"

Acceptable range: PMC to PME. Optimal zone: OPP to IDP.

**Tips:** 100-300 respondents, segment by persona, use realistic descriptions.

### MaxDiff Analysis (Best-Worst Scaling)

Identifies which features customers value most:

1. List 8-15 features
2. Show sets of 4-5 features
3. Ask: Most important? Least important?
4. Statistical analysis produces importance scores

**Packaging decisions:**
- Top 20% utility: include in all tiers (table stakes)
- 20-50%: use to differentiate tiers
- 50-80%: higher tiers only
- Bottom 20%: consider cutting or premium add-on

### Other Methods

- **Gabor-Granger:** "Would you buy at $X?" Vary price to build demand curve.
- **Conjoint analysis:** Show product bundles at different prices. Reveals price sensitivity per feature.
- **Usage-Value Correlation:** Track usage data, correlate with retention/expansion, identify value thresholds.

---

## Freemium vs Free Trial

### When to Use Freemium

Works when: product has viral/network effects, free users provide value, large market, low marginal cost, clear upgrade triggers.

Risks: free users may never convert, devalues perception, support costs, harder to raise prices.

### When to Use Free Trial

Works when: product needs time to show value, setup investment required, B2B buying committees, higher prices, product is "sticky" once configured.

Best practices: 7-14 days for simple, 14-30 for complex, full access, clear countdown, consider credit card requirement (40-50% conversion with card vs 15-25% without).

### Hybrid Approaches

- **Freemium + Trial:** Free tier with limited features + trial of premium
- **Reverse trial:** Start with full access, downgrade to free after trial

---

## Enterprise Pricing

### When to Add Custom Pricing

When: deal sizes exceed $10k+ ARR, custom contracts needed, implementation required, security/compliance requirements.

### Enterprise Tier Elements

Table stakes: SSO/SAML, audit logs, admin controls, uptime SLA, security certifications.

Value-adds: dedicated support/success, custom onboarding, training, custom integrations, priority roadmap input.

### Enterprise Pricing Strategies

- **Per-seat at scale:** Volume discounts (e.g., $15/user standard, $10/user for 100+)
- **Platform fee + usage:** Base fee + usage-based above thresholds
- **Value-based contracts:** Price tied to customer's revenue/outcomes

---

## Pricing Page Best Practices

### Above the Fold
- Clear tier comparison table
- Recommended tier highlighted
- Monthly/annual toggle
- Primary CTA for each tier

### Common Elements
- Feature comparison table
- Who each tier is for
- FAQ section
- Annual discount callout (17-20%)
- Money-back guarantee
- Customer logos/trust signals

### Pricing Psychology
- **Anchoring:** Show higher-priced option first
- **Decoy effect:** Middle tier should be best value
- **Charm pricing:** $49 vs $50 (for value-focused)
- **Round pricing:** $50 vs $49 (for premium)
