# Design Tokens & Code-Ready Specs

Copy-paste-ready values for colors, typography, spacing, motion, and forms.
Use this when writing actual CSS/component code.

---

## 1. Color System

### Semantic Token Architecture (3 layers)

```
Layer 1: Reference palette  ->  raw hues (palette-blue-40, palette-neutral-90)
Layer 2: System tokens       ->  semantic roles (--color-primary, --color-surface)
Layer 3: Component tokens    ->  scoped overrides (--button-bg, --input-border)
```

**Never hardcode hex values in components. Always reference system tokens.**

### M3 Color Roles (Light + Dark)

| Token | Light | Dark | Purpose |
|-------|-------|------|---------|
| primary | #6750A4 | #D0BCFF | Key action color |
| on-primary | #FFFFFF | #381E72 | Text/icons on primary |
| primary-container | #EADDFF | #4F378B | Lower emphasis fill |
| on-primary-container | #21005D | #EADDFF | Text on primary-container |
| secondary | #625B71 | #CCC2DC | Secondary brand |
| on-secondary | #FFFFFF | #332D41 | Text on secondary |
| secondary-container | #E8DEF8 | #4A4458 | Secondary fill |
| surface | #FFFBFE | #1C1B1F | Card/sheet background |
| on-surface | #1C1B1F | #E6E1E5 | Primary text |
| surface-variant | #E7E0EC | #49454F | Alternate surface |
| on-surface-variant | #49454F | #CAC4D0 | Secondary text |
| error | #B3261E | #F2B8B5 | Error/destructive |
| on-error | #FFFFFF | #601410 | Text on error |
| outline | #79747E | #938F99 | Borders, dividers |
| outline-variant | #CAC4D0 | #49454F | Subtle dividers |
| scrim | #000000 | #000000 | Modal backdrop |

### Dark Mode Surface Elevation

Dark theme uses white tonal overlays on #121212, NOT drop shadows.

```
Elevation 0   ->  #121212  (0% overlay)
Elevation 1   ->  #1D1D1D  (5%)
Elevation 2   ->  #222222  (8%)
Elevation 3   ->  #252525  (11%)
Elevation 4   ->  #272727  (12%)
Elevation 6   ->  #2C2C2C  (14%)
Elevation 8   ->  #2E2E2E  (15%)
Elevation 12  ->  #333333  (16%)
Elevation 16  ->  #363636  (17%)
Elevation 24  ->  #3B3B3B  (18%)
```

### shadcn/ui CSS Variables (oklch, Tailwind v4)

```css
:root {
  --background:          oklch(1 0 0);
  --foreground:          oklch(0.145 0 0);
  --card:                oklch(1 0 0);
  --card-foreground:     oklch(0.145 0 0);
  --primary:             oklch(0.205 0 0);
  --primary-foreground:  oklch(0.985 0 0);
  --secondary:           oklch(0.97 0 0);
  --secondary-foreground: oklch(0.205 0 0);
  --muted:               oklch(0.97 0 0);
  --muted-foreground:    oklch(0.556 0 0);
  --destructive:         oklch(0.577 0.245 27.325);
  --border:              oklch(0.922 0 0);
  --input:               oklch(0.922 0 0);
  --ring:                oklch(0.708 0 0);
  --radius:              0.625rem;
}

.dark {
  --background:          oklch(0.145 0 0);
  --foreground:          oklch(0.985 0 0);
  --card:                oklch(0.205 0 0);
  --primary:             oklch(0.922 0 0);
  --primary-foreground:  oklch(0.205 0 0);
  --muted:               oklch(0.269 0 0);
  --muted-foreground:    oklch(0.708 0 0);
  --border:              oklch(0.269 0 0);
}
```

### Semantic Color Naming Convention

```
surface           ->  base background (lowest layer)
surface-raised    ->  cards, sheets (dp 1-2)
surface-overlay   ->  dialogs, bottom sheets (dp 3-6)
on-surface        ->  primary text
on-surface-muted  ->  secondary/hint text
primary           ->  brand action (buttons, links, FAB)
on-primary        ->  text/icons on primary
error             ->  validation errors, destructive
warning           ->  cautionary (amber/yellow)
success           ->  confirmations (green)
outline           ->  borders, dividers
scrim             ->  modal overlays (black 32-50%)
```

---

## 2. Typography Scale

### M3 Complete Type Scale

| Token | Size | Line Height | Weight | Spacing | Use |
|-------|------|-------------|--------|---------|-----|
| display-large | 57px | 64px | 400 | -0.25px | Hero/marketing |
| display-medium | 45px | 52px | 400 | 0px | Large headers |
| display-small | 36px | 44px | 400 | 0px | Section heroes |
| headline-large | 32px | 40px | 400 | 0px | Screen titles |
| headline-medium | 28px | 36px | 400 | 0px | Modal titles |
| headline-small | 24px | 32px | 400 | 0px | Card headings |
| title-large | 22px | 30px | 400 | 0px | List headers |
| title-medium | 16px | 24px | 500 | 0.15px | App bar titles |
| title-small | 14px | 20px | 500 | 0.1px | Chip labels |
| body-large | 16px | 24px | 400 | 0.5px | Primary body |
| body-medium | 14px | 20px | 400 | 0.25px | Secondary body |
| body-small | 12px | 16px | 400 | 0.4px | Captions, hints |
| label-large | 14px | 20px | 500 | 0.1px | Button text |
| label-medium | 12px | 16px | 500 | 0.5px | Tabs, chips |
| label-small | 11px | 16px | 500 | 0.5px | Badges |

### Practical Mobile Scale (Framework-Agnostic)

```
caption:      11px / 16px  400  +0.4px tracking
label:        12px / 16px  500  +0.5px tracking
body-small:   12px / 16px  400
body:         16px / 24px  400   <- golden standard for mobile
body-medium:  14px / 20px  400
title-small:  14px / 20px  600
title:        16px / 24px  600
title-large:  22px / 30px  600
heading-sm:   24px / 32px  700
heading-md:   28px / 36px  700
heading-lg:   32px / 40px  700
display-sm:   36px / 44px  400
display-lg:   57px / 64px  400
```

**Line height rules:**
- Headings: 1.2-1.3x font size
- Body: 1.5-1.6x font size (16px x 1.5 = 24px)

**Platform fonts (2025):**
- iOS: `-apple-system` / SF Pro
- Android: Roboto / Google Sans
- Cross-platform: Inter (closest match to both)

**Minimum readable:** 11px. Never below 12px for body. 14px minimum for interactive labels.

---

## 3. Spacing & Sizing System

### 4px Base Grid

```css
--space-1:   4px;    /* 0.25rem  tight gaps, icon padding */
--space-2:   8px;    /* 0.5rem   compact spacing */
--space-3:   12px;   /* 0.75rem  small component padding */
--space-4:   16px;   /* 1rem     standard spacing */
--space-5:   20px;   /* 1.25rem */
--space-6:   24px;   /* 1.5rem   section padding */
--space-8:   32px;   /* 2rem     generous spacing */
--space-10:  40px;   /* 2.5rem */
--space-12:  48px;   /* 3rem     section gaps */
--space-16:  64px;   /* 4rem     large sections */
--space-20:  80px;   /* 5rem */
--space-24:  96px;   /* 6rem     hero padding */
```

### Component Sizes

```
/* Touch targets */
touch-min:        44px (iOS) / 48px (Android)
touch-comfortable: 56px (primary actions)

/* Buttons */
button-sm:    32px height, 16px padding-x
button-md:    40px height, 24px padding-x
button-lg:    48px height, 24px padding-x
button-xl:    56px height, 24px padding-x
button-radius: 8px (rounded) / 9999px (pill)

/* Inputs */
input-sm:     40px height, 12px padding-x
input-md:     48px height, 16px padding-x  <- default
input-lg:     56px height, 16px padding-x
input-radius: 4-8px

/* Cards */
card-padding:  16px (compact) / 20px (standard) / 24px (spacious)
card-radius:   8px (subtle) / 12px (modern) / 16px (expressive)

/* Navigation */
bottom-nav:   56px (M3) / 49pt (iOS tab bar)
top-app-bar:  56px (standard) / 64px (prominent)
fab:          56px (standard) / 40px (mini) / 96px (large)
```

### Border Radius Scale

```
sharp/data:     2-4px    tables, data grids
standard:       8px      inputs, chips, small cards
modern:         12-16px  cards, bottom sheets
pill:           9999px   tags, FABs, pill buttons
circle:         50%      avatars, icon buttons
```

---

## 4. Motion & Animation

### M3 Easing Curves

```css
--ease-standard:             cubic-bezier(0.2, 0, 0, 1);
--ease-standard-decelerate:  cubic-bezier(0, 0, 0, 1);        /* enter */
--ease-standard-accelerate:  cubic-bezier(0.3, 0, 1, 1);      /* exit */
--ease-emphasized-decelerate: cubic-bezier(0.05, 0.7, 0.1, 1); /* enter prominent */
--ease-emphasized-accelerate: cubic-bezier(0.3, 0, 0.8, 0.15); /* exit prominent */
```

### M3 Duration Tokens

```
short1:     50ms     icon micro-feedback, checkmark
short2:    100ms     small state changes (hover, pressed)
short3:    150ms     fade small elements
short4:    200ms     small component transitions
medium1:   250ms     standard interactions
medium2:   300ms     most transitions (sweet spot)
medium3:   350ms     medium components
medium4:   400ms     FAB morph, card expand
long1:     450ms     list item enter, bottom sheet
long2:     500ms     navigation transitions
long3:     550ms     full-screen elements
long4:     600ms     complex layout transitions
extralong1: 700ms    page-level transitions
extralong2: 800ms    hero image transitions
```

### Animation Cheatsheet

```
Button press:           100ms  standard-accelerate  (scale 0.97)
Ripple/tap:             300ms  standard
Toast appear:           200ms  emphasized-decelerate
Toast dismiss:          150ms  emphasized-accelerate
Bottom sheet open:      400ms  emphasized-decelerate
Bottom sheet close:     300ms  emphasized-accelerate
Screen push (enter):    300ms  emphasized-decelerate
Screen pop (exit):      250ms  emphasized-accelerate
Skeleton shimmer:      1500ms  linear infinite
Checkmark draw:         200ms  standard-decelerate
Error shake:            400ms  spring (damping 0.6)
Toggle switch:          200ms  standard
Modal fade in:          250ms  standard-decelerate
Modal fade out:         200ms  standard-accelerate
Accordion expand:       300ms  standard
Skeleton -> content:    400ms  standard (stagger 50ms/item)
```

### When to Animate vs Not

**Animate:** State changes, navigation transitions, feedback, content loading, expand/collapse.

**Don't animate:** Static text, simple page loads, form field focus (at most 100ms border transition), anything where delay feels like lag.

**60fps rule:** Only animate `transform` and `opacity` (GPU-composited). Never animate `padding`, `margin`, `border-width`, `width`, `height` directly.

---

## 5. Form Design Specs

### Input Fields

```css
/* Standard input */
height: 48px;              /* 56px for prominent */
padding: 12px 16px;
font-size: 16px;           /* NEVER below 16px -- prevents iOS auto-zoom */
border: 1px solid var(--color-outline);
border-radius: 4px;        /* outlined style */
background: transparent;   /* outlined */
             var(--color-surface-variant); /* filled */

/* Focus */
border-width: 2px;
border-color: var(--color-primary);

/* Error */
border-color: var(--color-error);

/* Disabled */
opacity: 0.38;
```

### Label Placement

**Floating label (Material):**
- Resting: inside field, centered, 16px
- Active: above field, 12px, primary color
- Error: above field, 12px, error color

**Top-aligned (iOS / shadcn):**
- Label above input, 4-6px gap
- Label: 14px, weight 500, on-surface-variant
- Helper text: 12px, weight 400, 4px below field

**Never use:** placeholder-only labels, left-aligned inline labels on narrow screens, labels below input.

### Keyboard Types

```html
<input type="text" autocomplete="name" />            <!-- standard -->
<input type="email" inputmode="email" />              <!-- @ and .com keys -->
<input type="tel" inputmode="tel" />                  <!-- dialpad -->
<input type="text" inputmode="decimal" />             <!-- numbers + decimal -->
<input type="text" inputmode="numeric" />             <!-- numbers only -->
<input type="url" inputmode="url" />                  <!-- / and .com keys -->
<input type="search" enterkeyhint="search" />         <!-- search key -->
<input type="password" autocomplete="current-password" />
<input type="text" inputmode="numeric" autocomplete="one-time-code" maxlength="6" /> <!-- OTP -->
```

### Validation Patterns

- **When:** Validate on blur (field loses focus). NOT every keystroke. NOT only on submit.
- **Error display:** Inline, 4px below field. 12px text, error color. Error icon 16px leading.
- **Success:** Green checkmark trailing inside field. Border stays default.
- **Real-time exceptions:** Password strength, username availability (debounce 500ms), character count.

### Form Layout Spacing

```
field-to-field:          16px vertical
label-to-input:          4px
input-to-helper:         4px
input-to-error:          4px
section-to-section:      24-32px
form horizontal padding: 16px (phone) / 24px (tablet)
submit button margin:    24px above
submit button:           full-width, 56px height, primary color
```

---

## Quick Reference Card

```
Body text:          16px / 24px  weight 400
Small body:         14px / 20px  weight 400
Caption:            12px / 16px  weight 400
Button label:       14px / 20px  weight 500-600
Heading small:      24px / 32px  weight 700
Screen title:       22px / 30px  weight 600

Touch minimum:      44pt iOS / 48dp Android
Input height:       48px standard / 56px prominent
Input font:         16px minimum (iOS zoom prevention)
Base spacing:       4px grid (4, 8, 12, 16, 24, 32, 48)
Card radius:        8-16px
Button radius:      8px standard / 9999px pill

Animation default:  300ms standard easing
Enter elements:     emphasized-decelerate cubic-bezier(0.05, 0.7, 0.1, 1)
Exit elements:      emphasized-accelerate cubic-bezier(0.3, 0, 0.8, 0.15)
Micro-feedback:     100ms
Dark surface base:  #121212 with white tonal overlays
```
