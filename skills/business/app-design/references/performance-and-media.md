# Performance & Media

Load speed, image optimization, screen density, and app icon design.
Companion to `design-tokens.md` (code specs) and `design-patterns.md` (component specs).

---

## 1. Load Speed & Perceived Performance

### The Numbers

- **1 second** is the gold standard for page load (Google PageSpeed Insights)
- **3 seconds:** 53% of users abandon a mobile page that takes longer
- Every 100ms of added latency costs ~1% in conversions

### What Slows Apps Down

1. **Too many HTTP requests** -- each image, script, stylesheet is a round trip
2. **Unoptimized images** -- largest single culprit on mobile
3. **Render-blocking resources** -- CSS/JS that prevents first paint
4. **Excessive redirects** -- each redirect adds a full round trip
5. **No caching** -- re-downloading assets the user already has

### Speed Optimization Checklist

**Reduce requests:**
- Combine CSS/JS bundles (code splitting for route-based chunks, not one mega-bundle)
- Use CSS sprites or icon fonts for multiple small icons
- Inline critical CSS (above-the-fold styles in `<head>`)

**Optimize delivery:**
- CDN for static assets (images, fonts, scripts)
- Gzip/Brotli compression on server
- Resource hints: `<link rel="preload">` for critical assets, `<link rel="prefetch">` for next-page assets
- HTTP/2 or HTTP/3 for multiplexed requests

**Perceived performance (feels fast even if it isn't):**
- Skeleton screens for loads >300ms (see `design-patterns.md` section 12)
- Optimistic UI: update immediately, confirm in background
- Progressive rendering: show content as it arrives, don't wait for everything
- Placeholder blur (blurhash/thumbhash) for images while full resolution loads

**Lazy loading:**
- `loading="lazy"` on below-fold images
- `IntersectionObserver` for deferred component mounting
- Route-based code splitting: only load JS for the current screen

---

## 2. Image Optimization

### The Balance

High-resolution images are essential for visual appeal but are the #1 cause of slow mobile load times. The goal: sharp images, fast loads.

### Format Selection

| Format | Best For | Savings vs JPEG |
|--------|----------|----------------|
| WebP | Photos, illustrations | 25-35% smaller |
| AVIF | Photos (modern browsers) | 50%+ smaller |
| SVG | Icons, logos, illustrations | Infinitely scalable, tiny file size |
| PNG | Screenshots, transparency | Use only when transparency needed |
| JPEG | Fallback for older devices | Baseline |

**Quality sweet spot:** 80-85% for WebP/AVIF. Below 75% artifacts become visible.

### Responsive Images

Serve the right size for each device. Never send a 4000px image to a 375px phone screen.

```html
<img
  src="photo-800.webp"
  srcset="photo-400.webp 400w,
          photo-800.webp 800w,
          photo-1200.webp 1200w"
  sizes="(max-width: 480px) 100vw,
         (max-width: 1024px) 50vw,
         33vw"
  alt="Product photo"
  loading="lazy"
  decoding="async"
/>
```

### Progressive Loading (Image Slicing)

Load images progressively so users see content building rather than waiting for a blank space:

1. **Progressive JPEG:** Image renders blurry-to-sharp (built into format, no extra work)
2. **Blurhash / Thumbhash:** Tiny encoded placeholder (20-30 bytes) shown instantly, replaced by full image
3. **Low-quality image placeholder (LQIP):** Tiny thumbnail (1-2KB) scaled up with CSS blur, swapped for full image on load

### Aspect Ratios

Never stretch or distort images. Always maintain correct proportions.

| Ratio | Use Case | CSS |
|-------|----------|-----|
| 16:9 | Hero images, video thumbnails | `aspect-ratio: 16/9` |
| 4:3 | Product photos, cards | `aspect-ratio: 4/3` |
| 1:1 | Avatars, thumbnails, app icons | `aspect-ratio: 1/1` |
| 3:2 | Landscape photos, feature cards | `aspect-ratio: 3/2` |
| 9:16 | Stories, vertical video | `aspect-ratio: 9/16` |

**Responsive containers:** Use CSS `aspect-ratio` or the padding-bottom trick to reserve space before the image loads (prevents layout shift).

```css
.image-container {
  aspect-ratio: 16 / 9;
  overflow: hidden;
}
.image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover; /* crops to fill */
  /* or object-fit: contain for no crop */
}
```

---

## 3. Screen Density & Resolution

### Apple Devices

Coordinate system uses **points (pt)**. Actual pixels = points x scale factor.

| Scale | Name | Example Devices |
|-------|------|-----------------|
| 1x | Standard | Older iPads, non-Retina Macs |
| 2x | Retina | iPhone SE, iPad Air, MacBook |
| 3x | Super Retina | iPhone 15, iPhone 15 Pro Max |

**Asset workflow:** Design at 1x. Export at 1x, 2x, 3x. Xcode selects the right one automatically.

### Android Devices

Uses **density-independent pixels (dp)**. Actual pixels = dp x (dpi / 160).

| Bucket | DPI | Scale | Pixel Equivalent of 48dp |
|--------|-----|-------|--------------------------|
| LDPI | 120 | 0.75x | 36px |
| MDPI | 160 | 1x | 48px |
| HDPI | 240 | 1.5x | 72px |
| XHDPI | 320 | 2x | 96px |
| XXHDPI | 480 | 3x | 144px |
| XXXHDPI | 640 | 4x | 192px |

### CSS Resolution Switching

```css
.hero {
  background-image: url('hero-1x.webp');
}
@media (min-resolution: 2dppx) {
  .hero { background-image: url('hero-2x.webp'); }
}
@media (min-resolution: 3dppx) {
  .hero { background-image: url('hero-3x.webp'); }
}
```

Or use `image-set()`:
```css
.hero {
  background-image: image-set(
    url('hero-1x.webp') 1x,
    url('hero-2x.webp') 2x,
    url('hero-3x.webp') 3x
  );
}
```

---

## 4. App Icon Design

The icon is the first thing users see in the app store and on their home screen. It carries outsized brand weight for a tiny square.

### Core Rules

- **One idea, minimal design.** Don't squeeze an entire scene into a square centimetre. Pick one central concept.
- **Focal point in the center.** The primary design element must sit in the innermost circle of the icon. Outer edges get cropped at small sizes and on different platforms (rounded rect on iOS, circle on some Android launchers).
- **No text in icons.** Text becomes illegible below ~64px. If your brand name is crucial, design a wordmark that reads as a shape, not text.
- **Test at every size.** Your icon renders at 1024px in the App Store, 60px on the home screen, 29px in notifications. It must be recognizable at all sizes.
- **Test on light and dark backgrounds.** Home screens vary. An icon that looks great on white may disappear on dark mode.

### Platform Specs

| Platform | Master Size | Shape | Notes |
|----------|------------|-------|-------|
| iOS | 1024 x 1024px | Rounded superellipse (auto-masked) | Submit square; iOS applies the mask. No transparency. |
| Android | 512 x 512px | Adaptive (foreground + background layers) | Foreground 108dp in 72dp safe zone. Background can be color or image. Launchers apply masks (circle, squircle, rounded rect). |

### Adaptive Icon Safe Zone (Android)

```
Total canvas:      108 x 108 dp
Safe zone:          72 x 72 dp (centered)
Visible mask area:  Varies by launcher (circle = 66dp diameter)
```

Keep all critical design elements within the 72dp safe zone. The outer 18dp on each side may be masked.

### Notification Icon Sizes

Push notification icons render very small. Test that your icon is still recognizable at:
- 16 x 16px (Android status bar)
- 24 x 24px (notification shade)
- 32 x 32px (larger displays)

Android requires a separate monochrome silhouette icon for notifications (white on transparent).

### Background Considerations

- Use a solid background color if the icon's foreground is simple or thin (improves readability)
- Skip the background if the icon itself is bold and distinctive enough (Tinder's flame works standalone)
- Avoid gradients that look washed out at small sizes
- Avoid pure white backgrounds (invisible on light home screens)
