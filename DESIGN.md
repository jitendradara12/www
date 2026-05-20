---
name: "0x43"
palette_core:
  surface: "#131317"
  surface-dim: "#08080c"
  primary: "#d7baff"
  secondary: "#75d4e8"
  tertiary: "#31e368"
  border: "#282a36"
typography_core:
  headline: Space Grotesk
  body: JetBrains Mono
spacing_core:
  unit: 4px
  gutter: 24px
  margin-mobile: 16px
---

## Brand & Style

The design system is a high-fidelity "Terminal-Brutalist" framework built for developers who live in the CLI. The UI is built to feel native to power users running tiling window managers or highly customized Fedora setups, reflecting the precise workflows of tools like LazyVim. It prioritizes precision, technical density, and the aesthetic of advanced computing environments. The style utilizes heavy 1px borders, monospace-driven hierarchy, and translucent surfaces that mimic a sophisticated terminal emulator. The UI should evoke an emotional response of "controlled power"—complex but perfectly organized against a "Deep Void" background.

## Global Frame & Navigation

The entire application is framed within a simulated window or tablet bezel featuring rounded outer corners and thick grey padding. This encloses a strictly sharp-cornered internal viewport, reinforcing the brutalist aesthetic.

- **Header:** The top bar displays a cyan command prompt `ROOT@PORTFOLIO:~` on the far left.
- **Directory Navigation:** Centered navigation uses a monospaced file-path format (`~/PROJECTS`, `~/ARTICLES`, `~/ABOUT`). The active route is indicated by a primary-color underline.
- **Right Actions:** Right-aligned icons include a terminal block `>_`, code brackets `< >`, and a rectangular ghost button labeled `[ SSH_CONNECT ]` encased in a thin border.

## Textures & Backgrounds

The base layout transitions dynamically based on the viewport to emulate different hardware displays and maintain depth without relying on traditional drop shadows.

- **Desktop:** Features a subtle, low-opacity dot/graph grid overlaid on the deep void background. This grid emphasizes the "coordinate plane" structure of the application.
- **Mobile:** Introduces prominent, high-density horizontal scanlines (linear-gradient overlays) and fine film grain. This simulates a retro CRT or raw hardware monitor feel, adding tactile depth to the flat surfaces.

## Hero Modules & Metadata

Hero components utilize a flat mid-grey background and integrate structural "Metadata Tabs"—small rectangular cutouts at the corners containing strict contextual labels.

- **Profile Hero (Jitendra Dara):** Features a Laser Violet top-left tab reading `ID: 0x43`. The main subtitle uses a terminal prompt prefix (`> Software Engineer & Systems Architect`). The primary action button `[ \downarrow --resume ]` is solid purple with tiny `+` coordinate markers at all four corners, flanked by ghost buttons like `<> --github`.
- **Config Hero (Neovim Setup):** Features a dark grey top-right tab reading `TYPE: CONFIG`. Lowercase cyan breadcrumbs sit above the card (`~ / projects / dotfiles`).
- **Key-Value Lists:** Metadata is right-aligned in stacked rows with leading icons: `STATUS: STABLE` (green), `LAST_COMMIT: 2h ago` (purple), and `git://github...` (cyan link).

## Terminal & Code Blocks

A specialized black container nested within the UI serves as a dedicated code environment, acting as a window-within-a-window.

- **Faux Header:** The top edge contains macOS-style window controls (salmon, yellow, and green circles) on the far left. The exact file path (e.g., `nvim ~/.config/nvim/init.lua`) is perfectly centered in a diminutive monospace font.
- **Syntax Body:** Contains highly legible, syntax-highlighted code (specifically showcasing Lua bootstrap scripts for lazy-loading), flanked by dim, monospaced line numbers (1-9) on the left edge.
- **Tags & Highlights:** Functional tags like `#lua` or `#lsp` are wrapped in thin grey outlines. Inline code references are highlighted using subtle translucent blocks.

## Directory & List Components

Lists are strictly structured to resemble system logs, command history, or directory trees rather than traditional web lists.

- **Section Headers:** Outlined with a minimalist open-folder icon alongside tracked-out uppercase text like `SYSTEM_RESOURCES / PROJECTS`. This is anchored by a thin, full-width separator line spanning the container.
- **List Items:** Row elements use bracketed numerical indexing (e.g., `[01]`, `[02]`) in place of standard bullets.
- **Tech Chips:** Programming languages and tools are displayed as comment-style syntax tags inside dark, square-cornered chips: `// C`, `// ASM`, `// LUA`, `// BASH`.
- **Status Pings:** Live projects are marked by a solid neon green circle beside the text `ACTIVE`, cleanly right-aligned to create a rigid column across multiple rows.

## Mobile Adaptations

The rigid grid reflows specifically for smaller viewports without losing the technical, brutalist edge of the desktop version.

- **Condensed Spacing:** Container margins and heavy padding reduce drastically to maximize terminal density on smaller screens.
- **Navigation Collapse:** The top navigation directory links (`~/PROJECTS`, etc.) disappear entirely, leaving only the primary host prompt and right-side utility icons.
- **Stacking Logic:** Multi-column row layouts stack vertically. For example, tech tags (`// C`, `// ASM`) drop beneath the primary project description instead of trailing on the far right.
