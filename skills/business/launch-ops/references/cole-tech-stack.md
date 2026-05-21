# Low-Ticket Product Tech Stack (Cole/Bush)

Source: Nicolas Cole & Dickie Bush (Ship 30 for 30), Low-Ticket Product M&M Course, Module 3

---

## The 5-Component Tech Stack

Every low-ticket digital product business needs exactly 5 things:

1. **Product Hosting** -- where customers access your content
2. **Payment Processing** -- how you collect money
3. **Sales/Checkout Pages** -- how you present and sell your offer
4. **Email Marketing** -- how you nurture and convert your audience
5. **Automations** -- how you connect everything without manual work

---

## 1. Product Hosting

**What it needs to do:**
- Organize course materials in a logical, easy-to-navigate structure
- Restrict access to paying customers only
- Provide a smooth, professional experience
- (Optional) Support community features and student interaction

### Primary: Skool ($99/mo flat)

Cole/Bush host all their products on Skool: Ship 30, Full Stack Writer, Low-Ticket Launchpad, Category Newsletter Creator, Premium Ghostwriting Academy.

**Why Skool:**
- Simple, fast, intuitive -- intentional constraints prevent overthinking
- Flat $99/mo regardless of how many customers or how much revenue
- Built-in community feed, calendar, and gamification features
- No extra tools needed if you want community around your product

**Why NOT a more customizable platform (Circle, MightyNetworks, Podia):**
Cole/Bush tested several and found Skool's constraints actually help. Less time choosing button colors, more time creating content people consume.

### Budget Alternative: Notion (Free)

Use Notion as your v1 product hosting when:
- You're on a tight budget
- You want to launch fast and collect feedback first
- You're already familiar with Notion

**Notion pros:** Free, clean interface, easy to update, flexible organization, zero learning curve.

**Notion con:** No built-in access control -- someone could share the link. At launch stage, this doesn't matter. Get the product out, iterate later.

Cole/Bush used Notion as v1 hosting MULTIPLE times before upgrading to Skool.

### Decision Tree

```
Starting out / tight budget? --> Notion (free)
Ready to invest / want community? --> Skool ($99/mo)
```

### Skool Setup Checklist

1. **Sign up** at skool.com -- $99/mo, all features, unlimited everything, no additional fees
2. **Set up branding** -- Settings > General: upload Icon, Cover, fill in Group description
3. **(Optional) Create discussion categories** -- Settings > Categories: add categories for community feed organization
4. **Shell out modules in Classroom**
   - Create a "course" for each major section
   - Arrange modules in logical progression (drag to reorder)
   - (Optional) Add a banner to each module for visual polish
   - **MODULE VISIBILITY RULE:** All modules should be "Open" UNLESS that section is an upsell product -- then make it "Private"
5. **Upload all content** -- add lessons with clear titles, upload videos/PDFs/resources, include descriptions
6. **Set up automatic access** -- handled via Zapier (see Automations section)
7. **Pro tips:**
   - Design a "Start Here" module to orient new customers
   - Create a pinned post with important information
   - **Set up Auto-DM:** Settings > Plugins > "Auto DM new members" > fill in welcome script > toggle ON

---

## 2. Payment Processing

**What it needs to do:**
- Accept online payments securely
- Handle subscription or payment plan billing
- Process credit cards and other payment methods
- Track financial data for tax/accounting
- Issue refunds when necessary

### Primary (and Only): Stripe (2.9% + $0.30 per transaction)

No budget alternative needed. Stripe is already the best option at any stage.

**Why Stripe:**
- Industry standard, integrates with virtually every other tool
- No monthly fees -- pay-as-you-go model
- Detailed reporting, tax calculations, scales with your business
- Pay-per-transaction means accessible even on a tight budget

### Stripe Setup Checklist

1. **Create account** at dashboard.stripe.com/register -- email, password, basic business info
2. **Complete verification** -- legal business info (or personal if sole proprietor), tax ID/SSN, connect bank account for payouts, upload verification documents
3. **Configure settings** -- business display name (what customers see on statements), business address/contact info, payout schedule
4. **Enable payment methods** -- credit/debit cards enabled by default; consider Apple Pay, Google Pay
5. **Connect to checkout solution** -- link to ThriveCart or SamCart (next section)

---

## 3. Sales/Checkout Pages

**What it needs to do:**
- Create professional sales pages that convert
- Present your offer compellingly
- Process payments and handle checkout smoothly
- Offer payment plans, coupons, discounting options
- Implement order bumps and upsells to maximize customer lifetime value

### Primary: SamCart ($99-200/mo)

Cole/Bush use SamCart for all their checkout and sales pages.

**Why SamCart:**
- Order bumps and upsell funnels (increase average order value)
- Built-in affiliate program functionality
- Flexible payment options (payment plans, coupons, free trials)
- Drag-and-drop sales page builder

**Best for:** Businesses already profitable that can justify the monthly cost.

### Budget Alternative: ThriveCart ($495 lifetime -- one-time payment)

Recommended for beginners. ~80% of SamCart's functionality, no recurring fees.

**ThriveCart features:**
- Customizable checkout pages
- Built-in affiliate program system
- Coupon codes and special offers
- Order bumps and one-click upsells
- Payment plans and subscription options
- Native integration with Kit

### Decision Tree

```
Just launching first product / keeping costs low? --> ThriveCart ($495 one-time)
Already profitable / need advanced features? --> SamCart ($99-200/mo)
```

### ThriveCart Setup Checklist

1. **Create account** -- sign up, complete business details, finish onboarding
2. **Create first product** -- Products > Create product > fill in product name and URL
3. **Set pricing** -- set product price > select payment type > save
4. **(Skip for now) Order bump** -- advanced feature, skip initially
5. **Connect Stripe** -- Settings > Integrations > Stripe > Connect Stripe account > select correct account
6. **Set fulfillment** -- add support email, (optional) set Thank You page redirect URL
7. **Select checkout page design** -- browse gallery > "sales carts" tab > pick a simple template with few pre-built elements (you'll add your own copy later)
8. **Set up Kit behavior rule** (after Kit account is created):
   - **Connect Kit to ThriveCart:** Settings > View Integrations > ConvertKit > "Integrate now" > add Kit credentials
   - **Create tag in Kit:** naming convention = "Purchased - {Your Product Name}"
   - **Create behavior rule:** Product settings > Behavior > Add rule > select purchased tag > Save
9. **Test checkout** -- create 100%-off coupon, complete a test transaction, verify thank you page and confirmation emails
10. **Connect to Skool** -- via Zapier (see Automations section)

### SamCart Setup Checklist

1. **Create account** -- select plan, start free trial, complete business details, finish onboarding
2. **Create first product** -- Products > New product > fill in product name, type, price
3. **Set up product details** -- (optional) customize URL, description, image, Thank You page redirect
4. **Design sales/checkout page** -- use drag-and-drop builder (add copy after writing it in Module 4)
5. **Set up Kit integration:**
   - **Connect Kit to SamCart:** Apps dashboard > find ConvertKit > add Kit credentials
   - **Create tag in Kit:** naming convention = "Purchased - {Your Product Name}"
   - **Create automation rule:** Product settings > Apps > Add new rule > select ConvertKit > "Add tag to subscriber" > select purchased tag > trigger = "Product purchased"
6. **Test checkout** -- create 100%-off coupon, complete test transaction, verify thank you page and confirmation emails
7. **Connect to Skool** -- via Zapier (see Automations section)

---

## 4. Email Marketing

**What it needs to do:**
- Build and grow your email list
- Send regular newsletters to nurture your audience
- Run experiments and track email performance
- Create automated sequences that drive sales while you sleep
- Segment your audience so everyone gets the right emails automatically

### Primary (and Only): Kit / ConvertKit (Free to start)

No budget alternative needed. Kit's free plan covers essentials for beginners.

**Why Kit over Substack/Beehiiv:**
Substack and Beehiiv are designed for newsletter businesses. Kit is designed to help you use email as a tool to grow a digital product business. Key difference.

**Why Kit specifically:**
- Direct integrations with ThriveCart and SamCart
- Complete newsletter toolkit
- Advanced but simple segmentation
- Robust automation capabilities (abandoned cart, welcome sequences, etc.)

**Free plan limitations:** Only 1 single-step visual automation. Enough to start building your list and newsletter. Upgrade when you're ready to launch and need advanced sequences -- by then you'll have revenue to cover it.

**Sequences Kit powers (covered in later modules):**
1. Onboarding/Post-Purchase Sequence
2. Abandoned Cart Sequence
3. Objection Handling Sequence for Clickers
4. 10-Day Launch Sequence
5. 10-Day Pre-Launch Sequence

### Kit Setup Checklist

1. Go to Kit pricing page, find the "Free" plan
2. Click "sign up free"
3. Enter email, create password
4. Complete profile setup
5. If you see a yellow verification banner at the top of your dashboard, click it and provide the requested info so Kit can validate your account

---

## 5. Automations

**What it needs to do:**
- Connect tools that don't have native integrations
- Reduce manual work and human error
- Create workflows that trigger automatically based on events
- Scale operations while keeping the business lean
- All without code

### Primary: Zapier (Free: 5 Zaps, 100 tasks/mo)

**Why Zapier:**
- Most integrations of any automation platform (7,000+)
- Extremely user-friendly, no coding needed
- Free plan covers most starter automations

### Budget Alternative: Make.com

**When to consider Make.com:** You have a coding/automation background AND need high-volume or complex workflows. More cost-effective at scale but much steeper learning curve.

**Recommendation:** Start with Zapier's free plan. Switch to Make only if/when you outgrow it and have the technical chops.

### Zapier Setup Checklist

1. **Create account** at zapier.com -- start with free plan
2. **Connect essential tools** -- go to "My Apps" in dashboard, connect: ThriveCart/SamCart, Skool, Kit, Google Sheets
   - **Skool API key location:** Skool group > Settings > Plugins > Zapier integration

### 4 Pre-Built Zap Templates

**Zap #1: Course access after purchase (ThriveCart)**
- Trigger: New successful order in ThriveCart
- Action: Add member to Skool group

**Zap #2: Course access after purchase (SamCart)**
- Trigger: New successful order in SamCart
- Action: Add member to Skool group

**Zap #3: Track sales in spreadsheet (ThriveCart)**
- Trigger: New successful order in ThriveCart
- Action: Add row to Google Sheets

**Zap #4: Track sales in spreadsheet (SamCart)**
- Trigger: New successful order in SamCart
- Action: Add row to Google Sheets

---

## Minimum Viable Stack for Launch

You don't need to implement everything perfectly from day one. Start with the basics:

| Component | MVP Tool | Cost |
|---|---|---|
| Product Hosting | Notion | Free |
| Payment Processing | Stripe | 2.9% + $0.30/transaction |
| Sales/Checkout | ThriveCart | $495 one-time |
| Email Marketing | Kit (free plan) | Free |
| Automations | Zapier (free plan) | Free |

**Total upfront cost: $495 (ThriveCart) + per-transaction Stripe fees.**

No monthly recurring costs until you're ready to upgrade.

The most important thing is to get started and put your product in the hands of customers. That's the only way to gather feedback, iterate, and make the product better.

---

## Module Visibility Rule

When setting up modules in Skool's Classroom:

- **"Open"** -- default for all modules
- **"Private"** -- ONLY if that module is an upsell product (content only certain customers/tiers can access)

This is how you gate upsell content within the same Skool group without needing a separate group.
