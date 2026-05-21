# Mobile Design Patterns & Component Specs

Practical specs from Material Design 3 and Apple HIG. All values are code-ready.
Use this when building actual UI components.

---

## 1. Touch Targets

| Platform | Minimum Size | Spacing Between Targets |
|----------|-------------|------------------------|
| iOS (HIG) | 44 x 44 pt | 8pt recommended |
| Android (M3) | 48 x 48 dp | 8dp minimum |
| WCAG 2.5.8 (AA) | 24 x 24 CSS px | - |
| WCAG 2.5.5 (AAA) | 44 x 44 CSS px | - |

**Implementation:** `min-height: 44px; min-width: 44px` on all interactive elements. Use padding to expand small visual icons to meet the minimum.

---

## 2. iOS Safe Areas & Screen Specs

### iPhone 15 / 15 Pro Safe Area Insets
- Portrait: top 59pt, bottom 34pt, left 0, right 0
- Landscape: top 0, bottom 21pt, left 59pt, right 59pt

### Screen Sizes
| Model | Logical | Scale | Physical |
|-------|---------|-------|----------|
| iPhone 15 / 15 Pro | 393 x 852 pt | 3x | 1179 x 2556 px |
| iPhone 15 Plus / Pro Max | 430 x 932 pt | 3x | 1290 x 2796 px |

### iOS Standard Component Heights
- Status bar (Dynamic Island): ~54pt
- Navigation bar: 44pt (standard), 96pt (large title)
- Tab bar: 49pt (iPhone), 50pt (iPad)

**CSS:** `padding-top: env(safe-area-inset-top); padding-bottom: env(safe-area-inset-bottom);`

---

## 3. M3 Buttons

| Size | Height | Use |
|------|--------|-----|
| Small | 36dp | Compact contexts |
| Medium (default) | 40dp | Standard inline |
| Large | 48dp | Primary CTA |
| XL | 56dp | Hero CTA |

- Corner radius: fully rounded (half height, e.g. 20dp for Medium)
- Horizontal padding: 24dp (with icon), 16dp (text only)
- Icon inside button: 18dp, 8dp gap to label

**Types by emphasis:**
- Filled = primary CTA (highest)
- Filled Tonal = secondary (medium)
- Outlined = low emphasis
- Text = least emphasis
- Elevated = subtle shadow variant

---

## 4. M3 Text Fields

- Container height: 56dp
- Corner radius (filled): 4dp top, 0dp bottom
- Corner radius (outlined): 4dp all
- Horizontal padding: 16dp
- Label font: Body S (12sp) active, Body L (16sp) placeholder
- Helper text: Body S (12sp), 4dp below container

**Critical iOS rule:** Input font-size must be 16px+ to prevent iOS auto-zoom on focus.

---

## 5. M3 Navigation Bar (Bottom)

- Height: 80dp
- Icon size: 24dp
- Active indicator: pill 64dp x 32dp
- Label font: Label M (12sp)
- Items: 3-5 destinations max

**Real-world data:** Redbooth saw 65% DAU increase and 70% session time jump switching from hamburger to bottom tab bar.

---

## 6. M3 FAB (Floating Action Button)

| Type | Size | Corner Radius | Icon Size |
|------|------|---------------|-----------|
| Small | 40 x 40dp | 12dp | 24dp |
| Regular | 56 x 56dp | 16dp | 24dp |
| Large | 96 x 96dp | 28dp | 36dp |

Elevation: 6dp resting, 8dp pressed.

---

## 7. M3 Cards

- Corner radius: 12dp
- Content padding: 16dp all sides
- Margin between cards: 8dp
- Image aspect ratio: 16:9 or 4:3

**Types:** Filled (0dp elevation), Elevated (1dp), Outlined (0dp + border)

### List Items
- 1-line: 48dp height
- 2-line: 64dp height
- 3-line: 88dp height
- Leading avatar: 40x40dp, 16dp from edge
- Trailing element: 16dp from edge
- Divider: 1dp, starts 16dp from left (not full-bleed)

---

## 8. M3 Color System Roles

```
primary / on-primary / primary-container / on-primary-container
secondary / on-secondary / secondary-container / on-secondary-container
tertiary / on-tertiary / tertiary-container / on-tertiary-container
surface / on-surface / surface-variant / on-surface-variant
background / on-background
error / on-error / error-container / on-error-container
outline / outline-variant
scrim (modal overlays: black at 32% opacity)
```

---

## 9. M3 Spacing

- Base unit: **4dp**. All spacing = multiples of 4.
- Content margins: **16dp** (phone), **24dp** (tablet)
- Dense layouts: 8dp gaps
- Standard: 16dp
- Spacious: 24-32dp

---

## 10. Navigation Patterns

### Bottom Tab Bar (preferred 2025)
- Use for: 3-5 top-level destinations, frequent switching
- Max items: 5 iPhone, 7 iPad
- Labels: 1-2 words max
- Icons: filled = active, outlined = inactive

### Navigation Drawer / Side Drawer
- Use for: 5+ destinations, secondary nav, settings
- Width: 256-320dp (covers 75-85% of screen)
- Overlay scrim: black at 32% opacity
- Support swipe-to-close

### iOS Back Gesture
- Swipe from left edge (0-20pt) triggers back
- Never place interactive content in the left 20pt edge zone

---

## 11. Bottom Sheets

### Types
1. **Modal:** blocks background, requires scrim (black 32%)
2. **Non-modal:** floats above, background stays interactive
3. **Expandable:** starts minimized, becomes modal when fully expanded

### Specs
- Handle bar: centered, 32dp wide, 4dp tall, radius 2dp, 12dp from top
- Corner radius: 28dp top (M3), 16pt top (iOS)
- Min peek height: 56-80dp
- Snap points: 25%, 50%, 90% of screen
- Dismiss: drag below 25%, or tap scrim
- Animation: spring physics, 300-400ms, ease-out

### Anti-patterns
- Never stack two bottom sheets
- Never use for full navigation flows
- Don't put keyboard-requiring forms in short sheets

---

## 12. Loading States

### Skeleton Screens
```css
.skeleton {
  background: linear-gradient(90deg, #e0e0e0 25%, #f0f0f0 50%, #e0e0e0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite linear;
}
@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```
- Show skeleton for loads > 300ms. Under 300ms, show nothing.
- Shapes should match actual content layout.
- Use `transform` for 60fps on mobile (GPU-accelerated).

### Pull-to-Refresh
- Trigger threshold: 60-80dp drag
- Visual indicator: appears after 20-30dp drag
- Resistance: content moves at 0.5x finger speed
- Spinner: 40dp diameter, spring return ~250ms

### Infinite Scroll
- Use `IntersectionObserver` with sentinel 200-400px before bottom
- `rootMargin: "0px 0px 400px 0px"` to pre-fetch
- Error state: show inline retry button, not full-page error

---

## 13. Gesture Interactions

### Swipe Actions (List Items)
- Min swipe distance: 50-100dp
- Commit threshold: 50% of item width
- Velocity flick: 100dp/s triggers even if distance not met
- Action button: 48dp min height, 72dp width
- Full swipe delete: 300ms animate out, 250ms collapse gap
- **Always provide undo:** snackbar with 4-5 second window

### Standard Gestures
| Gesture | Action | Platform |
|---------|--------|----------|
| Swipe left edge | Back navigation | iOS |
| Swipe down top | Pull-to-refresh / dismiss | Both |
| Long press | Context menu / select | Both |
| Pinch | Zoom on media | Both |

**Rule:** Never make a gesture the ONLY way to do something. Always provide a visible button alternative.

### Advanced Gestures

| Gesture | Action | Implementation Note |
|---------|--------|---------------------|
| Drag to reorder | Rearrange list items | Haptic on pickup, shadow elevation, snap to position |
| Two-finger pinch | Zoom media/maps | Min/max zoom bounds, snap to 1x on release |
| Long press + drag | Move items between containers | Show drop targets with highlight |
| Double tap | Quick zoom / like | Context-dependent, never dual-purpose on same element |
| Three-finger swipe | Undo/redo (iOS system) | Don't override -- OS-level gesture |

### Gesture Discoverability

First-time users don't know gestures exist:
- Show a one-time animation hint on first encounter (e.g., swipe indicator on first list item)
- Use coach marks for non-obvious gestures (sparingly, max 1 per session)
- Always provide a visible button alternative (the gesture is a shortcut, not the only path)
- Haptic feedback confirms gesture recognition (light impact on start, medium on commit)

---

## 14. Responsive Breakpoints

```css
/* Mobile first -- base styles, no media query */
@media (min-width: 480px) { /* Large phones */ }
@media (min-width: 768px) { /* Tablet portrait */ }
@media (min-width: 1024px) { /* Tablet landscape */ }
@media (min-width: 1280px) { /* Desktop */ }
@media (min-width: 1536px) { /* Large desktop */ }
```

### Viewport Units (Mobile)
```css
/* NEVER use 100vh on mobile (browser chrome breaks it) */
height: 100dvh;  /* dynamic -- accounts for address bar */
height: 100svh;  /* small -- worst case (bar visible) */
height: 100lvh;  /* large -- best case (bar hidden) */
```

### Fluid Typography
```css
font-size: clamp(1rem, 0.9rem + 0.5vw, 1.25rem);     /* body: 16-20px */
font-size: clamp(1.75rem, 1.5rem + 1.5vw, 3rem);      /* h1: 28-48px */
font-size: clamp(1.5rem, 1.25rem + 1vw, 2.25rem);     /* h2: 24-36px */
```

### Layout Spacing
- Side padding: 16px (mobile), 24px (tablet), 32px+ (desktop)
- Max content width: 1200-1280px centered
- Card grid gap: 8-16px
- Section vertical spacing: 32-48px (mobile), 64-96px (desktop)

---

## 15. iOS vs Android Key Differences

| Element | iOS (HIG) | Android (M3) |
|---------|-----------|--------------|
| Primary nav | Bottom tab bar (5 max) | Navigation bar (3-5) |
| Back | Left edge swipe | System back gesture/button |
| Typography | SF Pro | Roboto / Google Sans |
| Card radius | 12-16pt | 12dp |
| Button style | Capsule/pill primary | Rounded rect, 20dp radius |
| Modal dismiss | Swipe down | Back gesture/button |
| FAB position | Bottom right, above tabs | Bottom right, above nav |
| Haptics | UIImpactFeedbackGenerator | VibrationEffect |

---

## 16. Anti-Patterns

### Navigation
- Hamburger as primary nav: engagement drops 20-30%. Use bottom tabs.
- Mixing hamburger + tab bar on same screen level
- More than 5 tab items on iPhone

### Interaction
- Touch targets below 44pt/48dp: 3x higher error rate
- No loading feedback for actions >300ms
- Gesture-only actions without visible button fallback
- Auto-playing video with sound (default muted always)

### Layout
- `100vh` on mobile (use `100dvh`)
- No safe area padding (content behind notch/home indicator)
- Fixed font sizes with no zoom support (use `rem`)
- Infinite scroll with no footer access (add "Load More" or sticky footer)
- Full-screen modals for simple actions (use bottom sheets)

---

## 17. Apple Liquid Glass (iOS 26+)

Biggest visual overhaul since iOS 7:
- Three shapes: Fixed (constant radius), Capsule (radius = height/2), Concentric (radius = parent - padding)
- Tab bar floats with blur, minimizes on scroll, re-expands on reverse scroll
- System components auto-update. Custom components need manual Liquid Glass material.
- Color: use sparingly. Let content colors dominate.

---

## 18. Design System Component Spec

When building a reusable component library, document each component with this template:

### Component Spec Template

```
Name: [PascalCase, e.g., PrimaryButton]
Variants: [size, emphasis, state variations]
Props/inputs: [what the component accepts]
Tokens used: [which design tokens it references]
States: default, hover, pressed, focused, disabled, loading
Responsive: [how it adapts across breakpoints]
Accessibility: [ARIA role, label requirements, keyboard behavior]
Platform diffs: [iOS vs Android variations, if any]
```

### Minimum Viable Design System

Define these 8 components first for any new app. Everything else builds on them:

1. **Button** -- primary, secondary, text, destructive (4 variants)
2. **Input field** -- text, select, checkbox, radio, toggle
3. **Card** -- content container with consistent padding/radius
4. **Navigation** -- bottom tabs or top bar (platform-appropriate)
5. **Modal / Bottom sheet** -- overlay for focused actions
6. **List item** -- 1-line, 2-line, 3-line with leading/trailing elements
7. **State screens** -- empty, error, loading (reusable across all features)
8. **Typography styles** -- applied heading/body/caption styles (not just tokens)

---

## 19. In-App Search

Search is one of the most useful yet often overlooked features. Users arriving with specific intent need to find it fast.

### Placement & Visibility

- Search box must be **prominent and immediately visible** (top of screen or persistent top bar)
- Use the magnifying glass icon universally -- users recognize it instantly (Jakob's Law)
- Don't hide search behind a hamburger menu or "More" tab
- On content-heavy apps, consider a persistent search bar (not just an icon)

### Search Quality

- **Relevance ranking:** Most relevant results first. Exact matches > partial matches > fuzzy matches.
- **Auto-complete / suggestions:** Show predictions as the user types. Reduces keystrokes and errors.
- **Recent searches:** Display last 5-10 searches on focus (before typing). Let users clear history.
- **Trending / popular:** Show popular searches for new users or empty query state.

### No-Results Handling

Never show a blank "No results found" page. Instead:
- Suggest alternative spellings ("Did you mean...?")
- Show related categories or popular items
- Provide a clear path forward ("Browse all [category]" CTA)

### Search UX Patterns

- **Scoped search:** Make it clear if search covers all content or just the current section. Let users change scope.
- **Filter/sort results:** Bottom sheet or inline chips for quick filtering.
- **Voice search:** Add microphone icon in search bar as accessibility + convenience option.
- **Instant results:** Begin showing results as user types (debounce 200-300ms). Don't require pressing "Search."

---

## 20. Location-Based UX

Many app features depend on location: delivery, directions, store finders, nearby search.

### Auto-Detection

- Auto-detect current location as default for location-dependent features
- User shouldn't have to enter a zip code or address when the device already knows where they are
- Show a clear indicator: "Using your current location" with an edit/change link

### Manual Override

- **Always** provide manual location entry. Users may be planning ahead (e.g., searching restaurants near tomorrow's hotel, not their couch).
- Place the manual entry option visibly -- don't bury it behind the auto-detect
- Remember recently used locations for quick re-selection

### Permission Timing

- **Never** request location permission at first launch
- Request when the user reaches a feature that benefits from it (e.g., tapping "Find nearby")
- Explain why: "Allow location access to find stores near you" beats generic "Allow location?"
- Handle denial gracefully: fall back to manual address entry, no broken screens or error states

### Caching & Performance

- Cache last-known location for instant display while GPS updates in background
- Show stale location with "Updating..." indicator rather than a loading spinner
- Respect battery: don't continuously poll GPS. Use significant-change monitoring for background updates.
