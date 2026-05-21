# UI Design Principles for Mobile Apps

Quick-reference guide for the 7 core UI principles + 4 pro tips. Each principle includes mobile-specific adaptations.

Source: Figma Advocacy Director Thomas Lowry + industry best practices.

---

## Principle 1: Hierarchy

Guide users to key information first. Control what they see, in what order.

**Visual levers:**
- Font size and weight (large/bold = important)
- Contrast (high-contrast colors for primary actions)
- Spacing (generous spacing signals grouping and importance)

**Mobile adaptations:**
- Primary CTA above the fold (visible without scrolling)
- One primary action per screen. Secondary actions visually demoted (smaller, muted color)
- Navigation hierarchy: tab bar for top-level, stack navigation for drill-down
- Card-based layouts work well on small screens for chunking related content
- Use size ratios aggressively: headlines 24-32px, body 16px, captions 12-14px

**Rule of thumb:** "What does the user care about most on this screen?" Put that first and biggest.

---

## Principle 2: Progressive Disclosure

Show only what's needed now. Reveal complexity as users advance.

**Techniques:**
- Multi-step flows instead of long forms (one question per screen on mobile)
- Expandable sections for advanced options
- "Show more" patterns for secondary content
- Onboarding wizards that collect info across steps, not one wall of inputs

**Mobile adaptations:**
- Step indicators (dots, progress bar) so users know where they are and how many steps remain
- Bottom sheets for contextual options (don't navigate away)
- Swipe-to-reveal for secondary actions (delete, archive)
- Collapse long lists behind "See all" links
- Keep each screen focused on ONE decision or action

**Watch out:** Don't hide critical info too deep. If users need it to make a decision on this screen, show it on this screen.

---

## Principle 3: Consistency

Same element = same look + same behavior everywhere.

**What to keep consistent:**
- Button styles (primary, secondary, destructive -- same colors/sizes throughout)
- Navigation patterns (don't mix tab bars and hamburger menus randomly)
- Spacing and padding (use a 4px or 8px grid system)
- Typography scale (fixed set of sizes, don't invent new ones per screen)
- Icon style (all outlined OR all filled, not mixed)
- Interaction patterns (swipe always means the same thing)

**Mobile adaptations:**
- Follow platform conventions (iOS: bottom tabs, back swipe. Android: top app bar, back button)
- Touch target size: minimum 44x44px (iOS) or 48x48dp (Android)
- Consistent gesture meanings across the app
- Design system / component library prevents drift

**Cross-channel consistency:**
- If you have a website, keep the app UI aligned with it
- Same color palette, typography feel, and brand identity across channels
- Same terminology (don't call it "Cart" on web and "Bag" in the app)
- Same interaction patterns where possible (familiar transitions reduce learning)
- Users who switch between devices expect a seamless experience

**Tom Lowry:** "If one UI button is suddenly bigger, users wonder why. That irregularity adds cognitive load."

---

## Principle 4: Contrast

Use contrast strategically to draw attention to what matters.

**Applications:**
- Primary actions: high contrast (filled button, bold color)
- Secondary actions: low contrast (outlined or gray)
- Destructive actions: red against neutral background (immediate visual warning)
- Status indicators: green/yellow/red with sufficient contrast ratios
- Active vs inactive states: clear visual difference

**Mobile adaptations:**
- Outdoor readability: higher contrast ratios than desktop (sunlight washes out subtle differences)
- Dark mode support: design for both light and dark, test contrast in both
- Use contrast to create clear tap targets (button must look tappable)
- Avoid relying on color alone (add icons/labels for colorblind users)

**Minimum contrast ratios (WCAG):**
- Normal text: 4.5:1
- Large text (18px+ bold or 24px+): 3:1
- UI components and graphics: 3:1

---

## Principle 5: Accessibility

Design for everyone. 1 in 4 users worldwide has a vision impairment.

**WCAG essentials for mobile:**
- Alternative text on all images and icons
- Sufficient padding and touch targets (44px minimum)
- Screen reader compatibility (proper labels, roles, headings)
- Keyboard/switch navigation support
- Sufficient color contrast (see Principle 4)
- Don't use color as the only indicator (add text labels or icons)
- Respect system font size settings (support Dynamic Type / sp units)
- Support reduced motion preferences
- Provide captions for video/audio content

**Mobile-specific:**
- Test with VoiceOver (iOS) and TalkBack (Android)
- Ensure all interactive elements have accessible labels
- Logical focus/reading order matches visual layout
- Haptic feedback as additional confirmation (not sole indicator)
- Support one-handed use where possible

---

## Principle 6: Proximity

Related elements stay together. Unrelated elements are visually separated.

**Applications:**
- Form labels directly above or beside their input fields
- Action buttons grouped by function (playback controls together, destructive actions isolated)
- Error messages adjacent to the field that caused them
- Related settings grouped in sections with clear headers

**Mobile adaptations:**
- Group bottom-bar actions by function (core nav together)
- Keep "confirm" and "cancel" buttons close but visually distinct
- Use section headers and dividers in scrollable lists
- Floating action buttons (FABs) isolated from other controls to prevent accidental taps
- Modal actions at the bottom of the sheet, close to thumb zone

**Streaming service example:** Play, fast-forward, rewind are in the same row (all playback). Quit button lives separately to prevent accidental taps.

---

## Principle 7: Alignment

Clean lines create order. Use a grid system.

**Grid systems for mobile:**
- 4-column grid for phones (with 16px margins, 8px gutters)
- 8-column grid for tablets
- Consistent left alignment for text-heavy screens (LTR languages)
- Center alignment sparingly (headlines, CTAs, empty states)

**Mobile adaptations:**
- Edge-to-edge images/cards bleed to screen edges for immersion
- Text content respects safe margins (16-20px from screen edge)
- Vertically: consistent spacing between sections (use multiples of 8px)
- Align interactive elements to a predictable vertical rhythm
- Bottom-aligned CTAs for thumb reachability

**Rule:** If elements don't align to the grid, there should be an intentional reason (e.g., breaking alignment to draw attention).

---

## 4 Pro Tips

### 1. Apply Perspective
Position elements to guide users through a logical sequence. Determine the user flow first, then place elements to match. On mobile: think in terms of scrolling direction (vertical) and screen-by-screen progression.

### 2. Make It Effortless
Good interfaces feel invisible. On mobile this means:
- Consistent navigation across all screens
- Clear visual feedback for every interaction (tap states, loading indicators)
- Smart defaults that reduce typing
- Autofill, autocomplete, and smart suggestions
- Minimize required inputs (ask only what you need)

### 3. Apply Shortcuts
Speed up common tasks:
- Gesture shortcuts (swipe to delete, long-press for options)
- Quick actions from home screen (3D Touch / App Shortcuts)
- Recently used / favorites for frequently accessed items
- Smart search that covers all content types

### 4. Conduct Testing
Watch real people use your app:
- Test on actual devices (not just simulators)
- Test with one hand, test while walking, test in sunlight
- Test with screen readers enabled
- Test on low-end devices (performance matters)
- Test with large/small text size settings
- Catch problems early -- every round of testing saves rework

---

## Principles in Practice

### Citymapper
Transit app that makes complex city navigation intuitive. Vibrant **color coding** per transport mode (Contrast + Hierarchy) lets users scan routes instantly. Consolidates walking, bus, subway, ride-sharing into one screen using **progressive disclosure** -- overview first, tap for details. Real-time data with clear **feedback** (delays highlighted, ETAs updating live).

**Takeaway:** Color as a functional navigation tool, not decoration. Dynamic real-time content demands clear visual hierarchy.

### Notion
All-in-one workspace (notes, tasks, databases, wikis) that avoids overwhelming users despite massive feature surface. Modular drag-and-drop blocks keep each screen focused (**progressive disclosure**). Minimalist monochrome UI with **consistent** component behavior -- every block type works the same way. Users build their own layout (**personalisation**).

**Takeaway:** Complex apps stay simple when every component follows the same interaction pattern. Let users build complexity, don't force it.

### Spotify
Music streaming giant that nails data-driven **personalisation**. Discover Weekly and Daily Mixes curate content from listening habits. Clean bottom nav with 5 tabs (**consistency**, Hick's Law). Dark-first design with high **contrast** album art as the visual hero. Search, library, and home each serve one clear purpose (**hierarchy**).

**Takeaway:** Personalisation drives retention when it surfaces genuinely relevant content. Let the content be the visual star, keep the chrome minimal.
