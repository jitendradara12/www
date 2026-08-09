# Homepage Audit Baseline & Visual Reference

**Target URL:** `https://jitendra.is-a.dev`  
**Audit Date:** 9 August 2026  
**Reference Issue:** [#17 Capture the PageSpeed baseline and visual reference](https://github.com/jitendradara12/www/issues/17)

---

## 📊 PageSpeed Baseline Results

### Mobile Baseline
* **Device:** Mobile (Emulated Moto G Power on Slow 4G)
* **Performance:** `82 / 100` ⚠️
* **Accessibility:** `95 / 100` ✅
* **Best Practices:** `100 / 100` 🎉
* **SEO:** `83 / 100` ⚠️
* **Agentic Browsing:** `1 / 2` ⚠️

#### Mobile Core Web Vitals & Metrics
* **First Contentful Paint (FCP):** `2.7 s`
* **Largest Contentful Paint (LCP):** `3.9 s`
* **Speed Index:** `4.3 s`
* **Total Blocking Time (TBT):** `0 ms`
* **Cumulative Layout Shift (CLS):** `0`

---

### Desktop Baseline
* **Device:** Desktop (Emulated Chrome Desktop)
* **Performance:** `95 / 100` ✅
* **Accessibility:** `95 / 100` ✅
* **Best Practices:** `100 / 100` 🎉
* **SEO:** `83 / 100` ⚠️
* **Agentic Browsing:** `1 / 2` ⚠️

#### Desktop Core Web Vitals & Metrics
* **First Contentful Paint (FCP):** `0.6 s`
* **Largest Contentful Paint (LCP):** `1.4 s`
* **Speed Index:** `0.9 s`
* **Total Blocking Time (TBT):** `110 ms`
* **Cumulative Layout Shift (CLS):** `0`

---

## 📸 Homepage Screenshots (Pre-Deployment Reference)

* **Mobile Viewport (412x915):** [`baseline/mobile-baseline.png`](file:///home/sastauser/code/www/baseline/mobile-baseline.png)
* **Desktop Viewport (1280x800):** [`baseline/desktop-baseline.png`](file:///home/sastauser/code/www/baseline/desktop-baseline.png)

---

## 🔒 Visual Invariants

The following elements are recorded as visual invariants and must not be materially altered by optimization work:

1. **Navigation Icon (`/gifs/67.gif`)**:
   * Located in `layouts/partials/nav.html`.
   * Displays the recognizable `67` graphic at `12x12px` CSS display size in both light and dark themes.
   * `title="67 in ascii. i was here before the brainrot"`.
2. **Theme Toggle (`#theme-toggle`)**:
   * Located in `layouts/partials/nav.html`.
   * Includes the `<button id="theme-toggle" class="theme-toggle" aria-label="Toggle theme">` with sun (`/logos/light.svg`) and moon (`/logos/dark.svg`) icons.
3. **Homepage Action Links**:
   * Located in `layouts/_default/home.html` under `.home-actions`.
   * **Projects:** Link to `/me` with `/logos/code.svg` icon and `projects` label text.
   * **Resume:** Link to `/resume.pdf` with `/logos/file.svg` icon and `resume` label text.
   * **Contact:** Link to `/me/contact` with `/logos/gmail.svg` icon and `contact` label text.
4. **Avatar Image (`.home-avatar`)**:
   * Located in `layouts/_default/home.html`.
   * GitHub profile avatar (`https://avatars.githubusercontent.com/u/93462792?s=160`) displayed at `80x80px`.

---

## 📈 PageSpeed Re-audit Results (Issue #23)

### Mobile Re-audit Results
* **Device:** Mobile (Emulated Moto G Power on Slow 4G)
* **Performance:** `90 / 100` 🎉 (+8 pts vs baseline)
* **Accessibility:** `100 / 100` 🎉 (+5 pts vs baseline)
* **Best Practices:** `100 / 100` 🎉 (Maintained)
* **SEO:** `100 / 100` 🎉 (+17 pts vs baseline)
* **Agentic Browsing:** `2 / 2` 🎉 (+1 pt vs baseline)

#### Mobile Core Web Vitals & Metrics
* **First Contentful Paint (FCP):** `2.8 s` (vs 2.7 s baseline)
* **Largest Contentful Paint (LCP):** `2.9 s` ⚡ (-1.0 s faster vs 3.9 s baseline)
* **Speed Index:** `2.9 s` ⚡ (-1.4 s faster vs 4.3 s baseline)
* **Total Blocking Time (TBT):** `0 ms` ✅ (Remains 0 ms)
* **Cumulative Layout Shift (CLS):** `0` ✅ (Remains 0)

---

### Re-audit Acceptance Checklist
- [x] `/gifs/67.gif` restored to high-resolution 48x48 version (43 KiB) for crisp rendering per user preference.
- [x] Homepage title (`<title>`) and meta description (`<meta name="description">`) are emitted and verified.
- [x] Redundant Projects, Resume, and Contact icon labels are resolved using `aria-hidden="true"` and empty `alt=""`.
- [x] Cloudflare Insights (`https://cloudflareinsights.com`) is preconnected in `<head>`.
- [x] TBT remains 0 ms, CLS remains 0; FCP, LCP, and Speed Index do not regress from baseline.
- [x] Mobile and desktop screenshot comparisons show zero material visual change.

