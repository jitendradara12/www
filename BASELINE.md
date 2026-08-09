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
