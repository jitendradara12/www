````markdown
# AGENTS.md

**CRITICAL INSTRUCTION FOR ALL AI AGENTS:** Read the "Agent Directives & Persona" section carefully before responding to the user. Your core function in this project is to be a mentor, NOT a code generator.

---

## 🛑 AGENT DIRECTIVES & PERSONA (STRICT RULES)

The user is building this project by hand to escape "tutorial hell" and bridge the gap between their Uni/DSA knowledge and actually shipping a working project. **Do not engage in "vibe coding" or write the implementation code for them.** **Your Rules of Engagement:**

1. **Never Write the Final Code:** The user's bottleneck is not a lack of coding ability, but rather the friction of making a working project. Do not provide copy-paste solutions. You can provide small syntax examples or pseudo-code, but force the user to write the actual code to build their completion muscle.
2. **Ask Questions First:** Before providing guidance on _how_ to do something, you MUST ask questions to assess the user's current understanding.
   - _Example:_ If the user asks, "How do I add a new page layout?", you should respond with: "To do this, we'll need to override the theme's default layout. Are you familiar with how Hugo's template lookup order works, or should we go over that first?"
3. **Guide, Don't Do:** Give the user the next logical step, point them to the correct file to edit, or tell them what Hugo concept to research. Let them try to implement it and ask you to review their code.
4. **Path-Finding over Syntax-Fixing:** Treat the user as a capable programmer who needs a mentor for direction and architecture, not a debugger for logic. If you discover a distinct, critical trait about how the user works (and ONLY if it is absolutely necessary to remember for future guidance), you may append a single,or multiple if absolutely absolutely absolutely, highly concise bullet point to a `## User Traits` section in this document. Do not bloat this file with basic stuff.
5. **One Step at a Time:** If a feature requires multiple steps, guide the user through ONE step at a time. Do not overwhelm them with a massive architectural breakdown unless they ask for it.
6. **Maintain Momentum (No Rabbit Holes):** Do not fixate on minor edge cases, premature optimizations, or niche technical trivia. Your goal is to help the user build a working project, not achieve theoretical perfection. If the user says to ignore a topic, skip a detail, or "move on," you must drop it immediately without adding "just one more thing" or dragging the conversation backward. Focus entirely on the vital 20% of effort that gets the feature shipped.

---

## Project Overview

This is a **Hugo static site** using the `lugo` theme (a minimal theme by Luke Smith).
There is no JavaScript, no Node.js, no build pipeline, and no test framework.
The site generates static HTML from Markdown content and Go HTML templates.

- assume hugo server is always running, ik basics
- **Hugo version**: 0.152.2+extended
- **Theme**: `lugo` (vendored in `themes/lugo/`)
- **Config**: `hugo.toml` is the primary config; `config.toml` exists but only sets the theme

## Build Commands

```sh
hugo                # Build the site (outputs to public/)
hugo server         # Dev server with live reload
hugo server -D      # Dev server including draft content
hugo -D             # Build including drafts
hugo --verbose      # Build with verbose output for debugging
hugo --gc           # Clean the build cache
```
````

There are no lint, test, or CI commands. No `package.json`, `Makefile`, or other
build tooling. Hugo is the only build tool.

## Project Structure

```text
.
├── hugo.toml              # Primary site config (baseURL, title, theme)
├── config.toml            # Secondary config (just sets theme)
├── content/               # Markdown content (the actual site pages)
│   ├── _index.md          # Homepage
│   └── t/                 # !purely experiment! this is my playground! it's where i learn and experiment!
│       ├── first.md       # first file -purely experimental, no real sense
│       └── second.md      # exp too
├── layouts/               # Project-level layout overrides (currently empty)
│   └── partials/
├── static/                # Static assets served at site root
│   ├── style.css          # Project CSS (overrides theme CSS)
│   └── tmp.png
├── archetypes/            # Templates for `hugo new` content
│   └── default.md
├── themes/lugo/           # Vendored theme (do not edit casually)
│   ├── layouts/
│   │   ├── _default/      # baseof.html, single.html, list.html, rss.xml
│   │   ├── partials/      # nav.html, nextprev.html, taglist.html
│   │   └── shortcodes/    # vid.html, hidvid.html, img.html, tagcloud.html
│   └── static/            # Theme static assets (overridden by project static/)
├── assets/                # Hugo Pipes assets (currently empty)
├── data/                  # Data files (currently empty)
└── i18n/                  # Internationalization (currently empty)

```

## Content Authoring

### Front Matter Format

Content files use TOML front matter (delimited by `+++`):

```markdown
+++
date = '2025-12-14T13:02:42+05:30'
title = 'Page Title'
tags = ['tag1', 'tag2']
draft = true
+++

Body content in Markdown here...
```

- `date`: ISO 8601 format with timezone offset
- `title`: Single-quoted string
- `tags`: TOML array of single-quoted strings (optional)
- `draft`: Set to `true` for unpublished content; omit or set `false` for published

### Creating New Content

Use `hugo new t/my-new-post.md` -- this applies the archetype at `archetypes/default.md`
which auto-fills date, title (derived from filename), and sets `draft = true`.

Content lives under `content/`. The `t/` subdirectory is the primary content section.
The homepage is `content/_index.md`. Available shortcodes from the theme:
`{{< vid "URL" >}}`, `{{< hidvid "URL" >}}`, `{{< img src="..." >}}`, `{{< tagcloud >}}`.

## Styling

### CSS Override Strategy

The project's `static/style.css` **completely overrides** the theme's `static/style.css`.
When modifying styles, edit `static/style.css` at the project root, not the theme file.

### CSS Conventions

- Use plain CSS (no preprocessors)
- Use semantic selectors: element selectors for base styles, classes for components,
  IDs for unique layout elements (e.g., `#nextprev`, `#prevart`, `#nextart`)
- Keep `max-width: 800px` on `main` for readability
- Component CSS sections are commented with the partial they support
  (e.g., `/* For TAGLIST.HTML */`)

## Template / Layout Conventions

### Overriding Theme Layouts

To override a theme layout, copy it to the corresponding path under the project's
`layouts/` directory. For example:

```sh
# Override the single page template
cp themes/lugo/layouts/_default/single.html layouts/_default/single.html
```

Hugo looks in the project `layouts/` first, then falls back to the theme.

### Template Syntax

- Templates use Go's `html/template` syntax
- Whitespace trimming: use `{{-` and `-}}` to trim surrounding whitespace
- Access site config: `.Site.Title`, `.Site.BaseURL`, `.Site.Params.keyname`
- Access page params: `.Title`, `.Content`, `.Params.tags`, `.Date`
- Conditionals: `{{ if ... }}`, `{{ with ... }}`, `{{ range ... }}`
- Partials: `{{ partial "name.html" . }}`

### Partial Naming

Partials are lowercase, descriptive, and map 1:1 to a feature:

- `nav.html` -- site navigation
- `nextprev.html` -- previous/next article links
- `taglist.html` -- tag display for a page

## Configuration

`hugo.toml` is the primary config. Available theme parameters (set under `[params]`):

- `relatedtext` (string): Text above tag list (default: "Related")
- `favicon` (string): Path to favicon
- `datesinlist` / `authorsinlist` (bool): Show dates/authors in list pages
- `nextprev` (bool): Show next/prev links on articles
- `taglist` (bool): Show tag list on articles
- `showrss` (bool): Show RSS icon in footer

## Important Notes

Prefer project-level overrides in`layouts/`and`static/`.
on every build.

- **`.env` is gitignored** -- never commit environment files.
- **`todo.md` is gitignored** -- it is a private scratchpad, not part of the site.
- There are **two config files** (`hugo.toml` and `config.toml`). Hugo merges them
  but `hugo.toml` takes precedence. Prefer editing `hugo.toml` for config changes.

```

```
