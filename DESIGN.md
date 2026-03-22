```markdown
# Design System Strategy: The Editorial Developer

## 1. Overview & Creative North Star

**Creative North Star: "The Digital Lithograph"**

This design system rejects the "template-driven" nature of modern portfolio sites. It draws inspiration from high-end architectural monographs and legacy print journals, where code is treated as poetry and whitespace is as functional as the content itself.

The system moves beyond standard UI by treating the screen as a canvas of physical layers. We achieve a "premium" feel not through decoration, but through **intentional asymmetry** and **tonal depth**. By utilizing a sophisticated typographic scale and a "No-Line" philosophy, the interface feels less like software and more like a curated exhibition of technical craft.

---

## 2. Colors: A Warm, Intellectual Foundation

The palette is rooted in warm neutrals that mimic archival paper (`#fffcf7`) and charcoal ink (`#383831`). Accents are used with surgical precision to denote interactivity or technical metadata.

### Surface Hierarchy & Nesting

To create depth without shadows, use the **Surface Tiering** method. Treat the UI as stacked sheets of fine paper:

- **Baseline:** Use `surface` (`#fffcf7`) for the primary background.

- **Structural Nesting:** Place a `surface_container_low` (`#fcf9f3`) section to denote a secondary area. For an inner card or interactive module, use `surface_container_lowest` (`#ffffff`) to create a "highlighted" lift.

- **The "No-Line" Rule:** 1px solid borders are strictly prohibited for sectioning. Boundaries must be defined solely through background color shifts. If a visual break is needed, use a `surface_container` transition.

### The Glass & Gradient Rule

To prevent a "flat" appearance, apply **Glassmorphism** for floating navigation or overlays:

- Use `surface` at 80% opacity with a `backdrop-blur` of 12px.

- **Signature Textures:** For primary CTAs, apply a subtle linear gradient from `primary` (`#5f5e5e`) to `primary_dim` (`#535252`) at a 145-degree angle. This adds a tactile, "satin" finish to the UI.

---

## 3. Typography: The Editorial Voice

Typography is the primary vehicle for the brand’s "Intellectual" personality. We pair the romanticism of a serif with the clinical precision of a monospaced font.

- **Display & Headlines (Newsreader):** Use these for high-level storytelling. The high contrast of the serif reflects a sophisticated, print-magazine aesthetic.

- **Body (Inter):** Reserved for long-form reading. The clean, neutral sans-serif ensures the "Developer" side of the persona remains efficient and modern.

- **Technical Metadata (Space Grotesk):** Use for "Label" roles (dates, tech stacks, git hashes). This provides the "Terminal" feel without being heavy-handed.

**The Typographic Hierarchy:**

- **display-lg (3.5rem):** Reserved for Hero titles only. Use asymmetrical alignment (e.g., 15% left margin) to break the grid.

- **headline-md (1.75rem):** Section headers. Pair with a `secondary` (`#845c32`) monospace label above it for a "masthead" look.

- **label-sm (0.6875rem):** All-caps, tracked out (10-15%) for technical metadata.

---

## 4. Elevation & Depth: Tonal Layering

We do not use elevation to "pop" elements; we use it to "place" them.

- **The Layering Principle:** Depth is achieved by stacking. A `surface_container_highest` element should never sit directly on `surface_bright`. It must follow the natural progression: `surface` -> `low` -> `high`.

- **Ambient Shadows:** Only for floating menus. Use `on_surface` at 5% opacity with a 32px blur and 16px Y-offset. This mimics natural light hitting a page.

- **The "Ghost Border" Fallback:** If accessibility requires a container boundary, use `outline_variant` (`#babab0`) at **15% opacity**. This creates a "hairline" feel common in premium print.

- **Linearity:** Use the `spacing-16` (5.5rem) or `spacing-24` (8.5rem) to create dramatic vertical gaps, forcing the user to focus on one "article" or "code block" at a time.

---

## 5. Components

### Buttons

- **Primary:** Rectangle with `0px` radius. Background: `primary`. Text: `on_primary` (Inter, Bold).

- **Secondary:** Transparent background, Ghost Border (15% opacity `outline`).

- **Interactive State:** On hover, transition to `secondary` (`#845c32`) to provide a "warm" amber glow inspired by vintage terminal highlights.

### Cards & Projects

- **Style:** No borders, no shadows. Use `surface_container_low` as the card base.

- **Separation:** Forbid dividers. Use `spacing-10` (3.5rem) between list items to let the content breathe.

- **The "Code-Stamp":** Every project card should feature a `label-sm` technical tag in `tertiary` (`#3d6d5d`) to signify its "Developer" origin.

### Input Fields

- **Design:** A single bottom-border using `outline_variant`. The label should use `label-md` (Space Grotesk) and sit 0.5rem above the input.

- **Focus:** The bottom border transitions to `secondary` (amber) with a 2px thickness.

### Additional Component: The "Code Fragment"

- A dedicated container for code snippets using `surface_container_highest`.

- No syntax highlighting that uses neon colors. Use a custom theme based on the system colors: `secondary_fixed_dim` for strings and `tertiary_fixed_dim` for functions.

---

## 6. Do’s and Don’ts

### Do:

- **Use Asymmetry:** Place a large serif headline on the left and a small monospaced paragraph on the right.

- **Embrace the 0px Radius:** Everything is sharp. Sharp corners imply precision and technical rigor.

- **Respect the Spacing Scale:** Use `spacing-20` for section transitions to maintain the "High-End Magazine" feel.

### Don't:

- **Don't use Divider Lines:** If you feel the need for a line, increase the whitespace instead.

- **Don't use Rounded Corners:** No exceptions. Even buttons and tags must be strictly rectangular.

- **Don't use Pure Black:** Use `on_background` (`#383831`) for text. Pure black is too harsh for the warm cream palette and breaks the "Editorial" softness.

- **Don't Center-Align Everything:** Use left-aligned grids with generous, uneven gutters to create visual interest.
```
