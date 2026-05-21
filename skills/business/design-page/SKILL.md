---
name: design-page
description: |
  Design and build production-grade web pages, landing pages, and frontend interfaces with
  high visual quality. Covers campaign-specific landing pages (quiz funnels, lead magnets,
  sales pages, webinar registrations) from brand briefs AND general-purpose web UI design
  (dashboards, React components, HTML/CSS layouts, posters, applications). Use when user
  asks to build a landing page, design a web page, create a frontend interface, style a
  web UI, or says "page-designer," "frontend-design," "landing page," "sales page,"
  "quiz funnel page," "webinar page," "build me a page," "design a dashboard," "web
  component," "React component," "HTML page," "beautify this UI," or "make it look good."
license: Complete terms in LICENSE.txt (frontend-design component)
---

# Design Page

Build conversion-focused landing pages and distinctive frontend interfaces. This skill has two paths: campaign-specific landing pages (from brand briefs, with conversion optimization) and general-purpose web UI design (any interface, any framework, with bold aesthetics). Choose the path that fits, or blend both.

**Each landing-page project gets a DESIGN.md.** When building a set of pages for a single campaign or brand, produce a `DESIGN.md` at the project root capturing the design tokens (colors, typography, spacing, components). Pages within the project inherit the tokens. Cross-page consistency is enforced by the single source of truth. See `skills/design-md/SKILL.md` and `skills/design-md/templates/design-md-starter.md`.

---

## Path A: Campaign Landing Pages

Use this path when building a specific conversion-focused page for a campaign, product launch, or lead magnet. Requires a brand bible or design system.

### Prerequisites

1. **Brand bible**: Run `/website_brand_analysis` first if missing
2. **Design system CSS**: Should exist at `output/{brand}-design-system.css`
3. **Clear offer**: What's the CTA? What does the user get?

### Workflow

1. **Confirm inputs**: Brand bible path, page type, offer details
2. **Load design system**: Read the CSS tokens and component patterns
3. **Draft structure**: Outline sections based on page type template
4. **Build HTML**: Single self-contained file with inline CSS
5. **Review with user**: Send file, get feedback, iterate

### Page Types

**Quiz/Assessment Landing Page:**
This page type covers the landing page that drives quiz starts. For the quiz itself (questions, branching logic, recommendation screen copy), see `quiz-funnel`.
```
Nav (sticky)
Hero (gold bg): headline + value prop + CTA + meta (time, questions, results)
Discover (cream bg): 3 cards: what they'll learn
Sample (peach bg): preview question with interactive styling
Social Proof (navy bg): big number + logos
Final CTA (cream bg): repeat primary CTA
Footer (navy bg)
```

**Lead Magnet / Free Resource:**
```
Nav
Hero, headline + subhead + email capture form
Preview, what's inside (screenshots, outline)
Benefits, 3 key outcomes
Testimonials, social proof
Final CTA, repeat form
Footer
```

**Webinar / Event Registration:**
```
Nav
Hero, event title + date/time + host + register CTA
What You'll Learn, 3-4 bullet outcomes
Speaker Bio, photo + credibility
Agenda, timeline or topics
Final CTA, urgency element + register
Footer
```

**Course Sales Page:**
```
Nav
Hero, course name + tagline + price + enroll CTA
Pain Points, problems this solves
Transformation, before/after
Curriculum, modules/lessons
Instructor, bio + credibility
Testimonials
Pricing, card with features
FAQ
Final CTA
Footer
```

**Advertorial / DR Landing Page:**
A page that looks like editorial content but follows a direct response persuasion structure. Designed to warm cold traffic before sending them to a sales page or checkout.
```
Nav (minimal -- no distracting links, looks editorial)
Editorial Header (styled like an article, not an ad -- publication-style masthead)
Story Lead (personal narrative or case study opening that hooks the reader)
Problem Identification (name the pain in the reader's language)
Pain Escalation (make the problem feel urgent -- consequences of not solving it)
Failed Solutions (what doesn't work -- competitor approaches, common advice)
Root Cause Reframe (the "real reason" behind the problem that others miss)
Mechanism Introduction (the unique approach/ingredient/method that works)
Product Reveal (bridge from story to product -- natural, not salesy)
Benefit Stack (benefits in order of importance, with proof next to each)
Social Proof Stack (testimonials, before/after, numbers, press mentions)
Objection Handling (2-3 common doubts addressed directly)
Offer + CTA (clear value proposition, guarantee, scarcity if genuine)
FAQ (address remaining objections)
Final CTA (urgency element + repeat offer)
Footer (minimal, editorial style)
```

**Advertorial Design Rules:**
- Looks like content, not an ad. No flashy colors or aggressive CTAs above the fold.
- Typography: editorial/magazine style. Serif headlines, clean body text, generous line height.
- One column layout. No sidebars. Reading experience, not shopping experience.
- CTAs appear at least 3 times (after mechanism, after proof stack, at end).
- Product reveal happens in the middle, not the beginning.
- Every claim has a proof element nearby (stat, quote, screenshot).
- Mobile-first -- most cold traffic reads on phone.

### Advertorial Extraction + Rebuild Workflow

When the user provides a reference advertorial (URL, HTML file, or screenshot) and asks to "clone this," "rebuild this for my brand," or "use this structure":

**Step 1: Extract the DR Framework**
Analyze the reference page and label every section by its persuasion function:

```markdown
## Framework Analysis: [Reference Page]

| Section | Persuasion Function | Emotional Lever | Copy Technique |
|---------|-------------------|-----------------|----------------|
| Opening | Authority/credibility | Trust | Byline + publication style |
| Para 1-3 | Story lead | Curiosity | Personal narrative |
| Para 4-5 | Problem identification | Fear/frustration | Reader's language |
| ... | ... | ... | ... |
```

**Step 2: Get User Approval**
Present the framework analysis. Ask: "This is the persuasion structure I extracted. Ready to rebuild it for your brand?"

**Step 3: Rebuild**
Swap in the user's brand, product, claims, proof points, and testimonials while preserving the persuasion structure exactly. Write real copy -- no Lorem Ipsum placeholders.

**Step 4: Deliver**
Output three files:
- `[brand]-advertorial-framework.md` -- the extracted framework analysis
- `[brand]-advertorial.html` -- complete HTML page with inline CSS
- `[brand]-advertorial-editing-guide.md` -- section-by-section guide for customization

**Integration:**
- Uses `copy-writing` for body copy and storytelling
- Uses `review-miner` for social proof language and transformation stories
- Uses `sales-page-writer` for offer stack and guarantee copy
- Feeds into `cro` for conversion optimization after launch

### Design Tokens (Defaults)

Load from `output/{brand}-design-system.css` or use these defaults:

```css
/* Colors */
--navy: #0F1E35;        /* Headers, footer, dark sections */
--gold: #FFCA51;        /* Primary CTAs, hero backgrounds */
--orange: #FF6D33;      /* Hover states, interactive feedback */
--cream: #FFFDF9;       /* Main background */
--peach: #FCE6DF;       /* Accent sections */

/* Typography */
--font-heading: 'Circular Std', system-ui, sans-serif;
--font-body: 'Circular Std', system-ui, sans-serif;

/* Spacing */
--section-lg: 80px;
--section-md: 64px;
--section-sm: 48px;
```

### Component Patterns

**Primary Button (Gold):**
```css
.btn-primary {
  background: var(--gold);
  color: var(--navy);
  padding: 16px 32px;
  border-radius: 8px;
  font-weight: 700;
  box-shadow: 0 4px 20px rgba(255, 202, 81, 0.4);
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(255, 202, 81, 0.5);
}
```

**Card with Orange Hover Accent:**
```css
.card {
  background: white;
  border-radius: 12px;
  border: 1px solid rgba(15, 30, 53, 0.08);
  transition: all 0.25s ease;
}
.card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: var(--orange);
  opacity: 0;
  transition: opacity 0.25s;
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(15, 30, 53, 0.12);
}
.card:hover::before { opacity: 1; }
```

### Campaign Page Output

- **File**: `output/{brand}-landing-{page-type}.html`
- **Format**: Single self-contained HTML (inline CSS, no external deps except fonts)
- **Responsive**: Mobile-first, breakpoints at 768px and 1024px

---

## Path B: General Web UI Design

Use this path when building any web interface that is not a campaign-specific landing page: dashboards, applications, components, posters, creative pages. No brand bible required.

### Design Thinking

Before coding, understand the context and commit to a BOLD aesthetic direction:
- **Purpose**: What problem does this interface solve? Who uses it?
- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian. Use these for inspiration but design one true to the aesthetic direction.
- **Constraints**: Technical requirements (framework, performance, accessibility).
- **Differentiation**: What makes this UNFORGETTABLE? What's the one thing someone will remember?

**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work. The key is intentionality, not intensity.

Then implement working code (HTML/CSS/JS, React, Vue, etc.) that is:
- Production-grade and functional
- Visually striking and memorable
- Cohesive with a clear aesthetic point-of-view
- Meticulously refined in every detail

### Frontend Aesthetics Guidelines

- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter. Pair a distinctive display font with a refined body font.
- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.
- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. One well-orchestrated page load with staggered reveals creates more delight than scattered micro-interactions.
- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.
- **Backgrounds & Visual Details**: Create atmosphere and depth. Gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, grain overlays.

NEVER use generic AI-generated aesthetics: overused fonts (Inter, Roboto, Arial, system fonts), cliched color schemes (purple gradients on white), predictable layouts. No design should be the same across generations.

**Match complexity to vision.** Maximalist designs need elaborate code with extensive animations. Minimalist designs need restraint, precision, and careful attention to spacing and typography.

---

## Brunson Funnel & Page Architecture

Kennedy tells you what to say. Brunson tells you which page to build and where it sits in the sequence. See `references/brunson-frameworks.md` for funnel type taxonomy (Tripwire, Webinar, Application, Book, Challenge) and the Seven Funnel Phases (traffic temperature through environment change). Use both references together.

## Kennedy Landing Page Principles

Every landing page is a sales letter. Same psychology, same structure. See `references/kennedy-landing-page.md` for full frameworks.

- [ ] Headline uses a proven formula. Run the 50-headline process (write 50, narrow to 3, test).
- [ ] Problem section uses the prospect's language, not industry jargon.
- [ ] Damaging admission included somewhere on the page. Admitting flaws increases credibility on everything else.
- [ ] Guarantee is visually prominent and mentioned at least twice (near the price and in the P.S.).
- [ ] P.S. section exists and restates the offer plus the deadline. Second most-read element on any page.
- [ ] Every CTA gives clear, specific instructions ("Click the yellow button below").
- [ ] Tracking pixels and UTMs are in place before going live. If you can't measure it, you can't improve it.
- [ ] Risk reversal is a selling point, not fine print buried in the FAQ.

For headline formulas, the damaging admission technique, guarantee placement rules, and the complete sales letter structure: `references/kennedy-landing-page.md`.

---

## Quality Checklist

### Campaign Pages
- [ ] All sections use correct background colors from design system
- [ ] Primary CTAs match brand colors
- [ ] Interactive elements have hover states
- [ ] Typography matches brand fonts
- [ ] Hero has subtle depth (gradient or shadow)
- [ ] Cards lift on hover with accent
- [ ] Mobile responsive (stacked grids, adjusted padding)

### General Web UI
- [ ] Distinctive typography (not generic)
- [ ] Cohesive color palette with CSS variables
- [ ] Meaningful animations and transitions
- [ ] Responsive across breakpoints
- [ ] Accessible (contrast, keyboard navigation)
- [ ] Production-grade code quality

---

## Hormozi Proof & CTA Layout Guidance

### 13-Point Proof Checklist (Layout Application)
When designing sales pages or landing pages, use these 13 proof types as visual section planning. Each proof type should have a dedicated layout treatment. See `sales-page-writer/references/hormozi-proof-checklist.md` for full checklist.

**Layout recommendations for proof sections:**
- **Results/metrics** -- large number callouts, before/after side-by-side layouts
- **Testimonials** -- card grids with photos, star ratings, or video embeds. Use the Six-Point Testimonial Script structure for testimonial cards
- **Case studies** -- timeline/journey layouts showing transformation
- **Social proof counters** -- prominent placement above the fold ("10,000+ customers")
- **Screenshots/evidence** -- gallery or carousel with captions
- **Guarantees** -- visually prominent badge or seal, mentioned near price AND in P.S.
- **Authority signals** -- logo bars, media mentions, certifications

The key insight: "80% of our top 50 ads didn't have my face in them. They were our customers." Design pages around customer proof, not founder authority.

### CTA Formula Visual Elements
Hormozi's CTA has 5 elements. Each should be visually represented:
1. **What to do** -- clear button text ("Start Free Trial")
2. **How to do it** -- visual arrow or animation pointing to the CTA
3. **When to do it** -- urgency element near the button (countdown, "spots left")
4. **What they get** -- benefit text directly below/above the button
5. **What happens next** -- micro-copy below button ("You'll get instant access to...")

"Clear > Clever" applies to visual CTAs too. The button and surrounding elements should show+tell what happens when they click.

---

## Integration

Works with:
- `website-brand-analysis`: Provides brand bible and design system
- `creative-director`: Orchestrates full asset creation
- `marketing-ads`: Provides page briefs
- `copy-writing`: Page copy
- `cro`: Conversion rate optimization for landing pages
- `video-scriptwriter`: Scripts point to these landing pages
- `product-offer`: Offer strategy and value ladder that feeds page design
- `sales-page-writer/references/hormozi-proof-checklist.md`: 13-Point Proof Checklist for section planning
- `ads-creative/references/hormozi-goated-ads.md`: CTA Formula details
