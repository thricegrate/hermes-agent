---
name: app-design
description: |
  Use when user asks to design, build, review, or improve a mobile app UI. Triggers:
  "design an app," "build a mobile UI," "app layout," "wireframe," "mockup,"
  "review my app design," "improve this UI," "mobile interface," "app UX,"
  "touch-friendly design," "make this app better," "mobile-first," "app screen,"
  "design system for app," "dark mode," "responsive mobile," "form design,"
  "user flow," "information architecture," "screen map," "app structure,"
  "navigation structure," or any task involving mobile or app interface design decisions.
---

# App Design

Design and review mobile app interfaces with production-quality specs. Works for any app: the product tools, Claude Artifacts, Cloud Run apps, native mobile, PWAs.

**Canonical output format: DESIGN.md.** Every app this skill designs should produce a `DESIGN.md` file at the project root that captures the design tokens (colors, typography, spacing, rounded, components) plus rationale. The `design-tokens.md` reference below is the schema source for the YAML frontmatter. See `skills/design-md/SKILL.md` for the format and `skills/design-md/templates/design-md-starter.md` to slot-fill.

For the iOS app monetization playbook (paywall design, pricing, Apple compliance, TikTok ads to drive installs), see `skills/ios-app-monetization/SKILL.md`. This skill covers UI/UX; that skill covers monetization mechanics + paid acquisition.

## References (Load On Demand)

| Doc | What's In It | When to Load |
|-----|-------------|--------------|
| `references/ui-principles.md` | 7 UI principles (hierarchy, progressive disclosure, consistency, contrast, proximity, accessibility, alignment) + 4 pro tips | Every design/review session. Core framework. |
| `references/design-patterns.md` | M3 + Apple HIG component specs, navigation patterns, bottom sheets, loading states, gestures, breakpoints, iOS vs Android differences, anti-patterns | When building components, choosing patterns, or targeting a specific platform. |
| `references/design-tokens.md` | Code-ready color tokens (M3 + shadcn), typography scale, spacing system, component sizes, border radius, easing curves, animation durations, form specs | When writing actual CSS/code. Copy-paste values. |
| `references/user-flows-ia.md` | Screen inventory template, navigation architecture patterns (flat/hierarchical/hybrid), user flow notation, screen spec template, common flow patterns | When planning app structure, mapping screens, or defining navigation before visual design. |
| `references/performance-and-media.md` | Load speed optimization, image handling (formats, responsive srcset, aspect ratios, optimization), screen density specs (1x/2x/3x, LDPI-XXXHDPI), app icon design | When optimizing performance, working with images, or designing app icons. |
| `references/universal-design-principles.md` | 13 universal principles: priming, attractive bias, depth of processing, uniform connectedness, symmetry, golden ratio, layering, affordance, mimicry, iconic representation, constraint, redundancy, 80/20 rule | When reviewing design decisions, auditing overall quality, or checking principles beyond the core 7. |
| `references/mobile-ux-psychology.md` | Thumb zones, back navigation, scan patterns, CTA conversion stats, cognitive load, input minimization, onboarding, push notifications, personalisation, auth UX, empty/error/loading states, Gestalt principles, Laws of UX | When making layout decisions, designing flows, or optimizing conversions. |

---

## Mode A: Design (New App UI)

Use when building a new screen or flow from scratch.

### Workflow

1. **Define the product**
   - What problem does this app solve? For whom?
   - Generate 1-3 user personas (name, role, goal, frustration, tech comfort -- 2-3 sentences each)
   - What's the core value proposition in one sentence?
   - Target platform: iOS / Android / cross-platform / PWA?
   - What does success look like? (key metric: signups, completions, purchases, etc.)

2. **Map user flows** (load `references/user-flows-ia.md`)
   - List all screens the app needs (primary, secondary, modals)
   - Map the primary flow (happy path) as a numbered sequence
   - Identify branching points (authenticated vs guest, success vs error)
   - Note entry points (organic, deep link, push notification)
   - Choose navigation architecture: flat (tabs), hierarchical, or hybrid

3. **Wireframe structure**
   - For each key screen, define content zones: header, body, actions, navigation
   - Specify what goes in each zone (content type, not visual style)
   - Define content hierarchy per screen: what is primary, secondary, tertiary
   - Use screen spec template from `user-flows-ia.md`

4. **Set up design tokens** (load `references/design-tokens.md`)
   - Color system: pick semantic tokens (primary, surface, error, etc.)
   - Typography scale: set heading, body, caption, label sizes
   - Spacing: define grid (4px base, multiples of 4/8/16/24)
   - Border radius: pick a consistent scale
   - Dark mode: set surface elevation tokens

5. **Define hierarchy** (load `references/ui-principles.md`)
   - What does the user see first? What's secondary? What's hidden?
   - Apply font size, weight, and contrast to establish visual order
   - One primary CTA per screen, visually dominant

6. **Apply universal design principles** (load `references/universal-design-principles.md`)
   - Affordance: do interactive elements look interactive?
   - 80/20: are the most-used features the most accessible?
   - Constraint: can the user make mistakes? Prevent via UI, not error messages
   - Redundancy: can top features be reached from multiple paths?
   - Priming: does the first screen set the right expectations?

7. **Plan progressive disclosure**
   - Can this be broken into steps? One decision per screen.
   - What reveals on demand? (bottom sheets, expandable sections)
   - Step indicators for multi-step flows

8. **Choose components** (load `references/design-patterns.md`)
   - Navigation: bottom tabs (3-5 items), drawer, or stack?
   - Content: cards, lists, or custom layout?
   - Actions: buttons (filled/tonal/outlined), FAB, swipe actions?
   - Inputs: outlined or filled? Floating or top-aligned labels?
   - Search: if app has searchable content, design in-app search (see Section 19)
   - Location: if location-dependent, plan auto-detect + manual override (see Section 20)
   - Design system: define minimum viable components (see Section 18)

9. **Apply UX psychology** (load `references/mobile-ux-psychology.md`)
   - Thumb zone: primary actions in bottom third
   - Scan pattern: Z-pattern for sparse, layer-cake for structured
   - Cognitive load: chunk info, smart defaults, reduce choices
   - Fitts's Law: large targets, short reach distance

10. **Design all states**
   - Empty state: context + CTA + illustration
   - Loading state: skeleton screens (not spinners) for >300ms loads
   - Error state: human explanation + specific recovery path
   - Success state: confirmation + clear next step
   - Disabled state: 0.38 opacity

11. **Add motion** (see animation specs in `design-tokens.md`)
    - Enter: emphasized-decelerate, 300ms
    - Exit: emphasized-accelerate, 250ms
    - Micro-feedback: 100ms for taps
    - Only animate `transform` and `opacity` (60fps rule)

12. **Optimize for performance** (load `references/performance-and-media.md`)
    - Images: responsive srcset, lazy loading, correct aspect ratios, WebP/AVIF
    - Speed: minimize requests, skeleton screens, code splitting
    - App icon: if designing full app, design the icon (focal point in center, test at all sizes)

13. **Accessibility check**
    - Touch targets: 44px+ (iOS) / 48dp+ (Android)
    - Contrast: 4.5:1 text, 3:1 UI components
    - Screen reader labels on all interactive elements
    - Keyboard/switch navigation support
    - Dynamic type / system font scaling
    - Don't use color as only indicator

14. **Final review against 7 principles + universal design principles**
    - 7 core: hierarchy, progressive disclosure, consistency, contrast, proximity, accessibility, alignment
    - Universal: affordance, 80/20, constraint, redundancy, symmetry, layering, priming

15. **Document the design system**
    - Spec each reusable component (see component spec template in `design-patterns.md`)
    - Record all token values, variants, and states
    - This becomes the single source of truth for development

### Mobile-First Defaults

```
Touch targets:     44x44px minimum
Body text:         16px / 24px
Input font:        16px minimum (prevents iOS auto-zoom)
Screen margins:    16px phone / 24px tablet
Spacing grid:      4px base (8, 12, 16, 24, 32, 48)
Max content width: 1200px centered
Primary CTA:       bottom of screen, full-width on mobile
Viewport height:   100dvh (never 100vh on mobile)
```

---

## Mode B: Review (Audit Existing Design)

Use when evaluating a screenshot, mockup, or existing code.

### Workflow

1. **Examine**: Screenshot, HTML/CSS, or description

2. **Score each principle** (pass / needs work / fail):
   - Hierarchy: most important element obvious at a glance?
   - Progressive disclosure: complexity managed or overwhelming?
   - Consistency: similar elements same look + behavior?
   - Contrast: primary actions visually distinct?
   - Proximity: related items grouped logically?
   - Accessibility: touch targets, contrast ratios, labels?
   - Alignment: visible grid? Elements line up?

3. **Check UX psychology** (load `references/mobile-ux-psychology.md`):
   - Thumb zone: primary CTA reachable one-handed?
   - Cognitive load: too many choices? Too dense?
   - States: empty, error, loading states designed?
   - Fitts's Law: targets large enough, close enough?

4. **Check platform compliance** (load `references/design-patterns.md`):
   - Touch targets meet platform minimums?
   - Safe areas respected?
   - Navigation follows platform conventions?
   - Anti-patterns present? (hamburger as primary nav, 100vh, no loading states)

5. **Check flow coherence** (load `references/user-flows-ia.md`):
   - Does the user know where they are? (titles, breadcrumbs, back affordance)
   - Can they reach any top-level destination in 2 taps or fewer?
   - Are dead ends avoided? (every screen has a clear next action)
   - Is the navigation model consistent throughout?

6. **Check universal design principles** (load `references/universal-design-principles.md`):
   - Affordance: do all interactive elements look tappable/clickable?
   - 80/20: are the most-used features the most prominent?
   - Constraint: can users make preventable mistakes?
   - Redundancy: can key features be reached from multiple paths?
   - Symmetry: is the layout visually balanced?

7. **Prioritize fixes**: Specific, actionable changes ranked by impact

8. **Apply fixes**: Update code/design with recommendations

---

## Quick Checklist (Every Screen)

- [ ] One clear primary action, visually dominant
- [ ] Visual hierarchy guides eye top-to-bottom
- [ ] Touch targets 44px+ with 8px+ spacing between
- [ ] Contrast 4.5:1+ text, 3:1+ UI elements
- [ ] Related items grouped, unrelated separated
- [ ] Consistent with other screens in the app
- [ ] Aligned to 4px grid
- [ ] Primary CTA in thumb-reachable zone
- [ ] Works in dark mode
- [ ] All states designed (empty, loading, error, success)
- [ ] Accessible (labels, focus order, dynamic type)
- [ ] Input font-size 16px+ (iOS zoom prevention)
- [ ] Uses 100dvh not 100vh
- [ ] Animations use transform/opacity only (60fps)
- [ ] Images use correct aspect ratios, never stretched or distorted
- [ ] Images optimized (compressed, responsive srcset, lazy-loaded)
- [ ] In-app search prominent and functional (if applicable)
- [ ] App icon tested at all sizes (if designing full app)
- [ ] Push notification strategy defined (value-based, not spam)
- [ ] Personalisation considered (recommendations, preferences, smart defaults)
- [ ] Interactive elements look interactive -- affordance clear (buttons, links, toggles)
- [ ] Most-used features reachable in 1-2 taps (80/20 rule)
- [ ] Key features reachable from multiple paths (redundancy)
- [ ] Layout visually balanced (symmetry check)
