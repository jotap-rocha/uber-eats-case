---
name: visual-explainer
description: Generate beautiful, self-contained HTML pages that visually explain systems, code changes, plans, and data. Use when the user asks for a diagram, architecture overview, diff review, plan review, project recap, comparison table, or any visual explanation of technical concepts. Also use proactively when you are about to render a complex ASCII table (4+ rows or 3+ columns) — present it as a styled HTML page instead.
license: MIT
compatibility: Requires a browser to view generated HTML files. Optional surf-cli for AI image generation.
metadata:
  author: nicobailon
  version: "0.5.1"
  vendored_by: "agent-harness-canonico, adapted from agentspec (Luan Moreno)"
---

# Visual Explainer

Generate self-contained HTML files for technical diagrams, visualizations, and data tables. Always
open the result in the browser. Never fall back to ASCII art when this skill is loaded.

**Proactive table rendering.** When about to present tabular data as an ASCII box-drawing table
(comparisons, audits, feature matrices, status reports, any structured rows/columns), generate an
HTML page instead. Threshold: 4+ rows or 3+ columns belongs in the browser. Don't wait for the user
to ask — render it and tell them the file path. A brief text summary in chat is fine, but the table
itself should be the HTML page.

## Available Commands

Commands live in `.claude/commands/visual-explainer/`, invoked directly (e.g. `/generate-web-diagram`).

| Command | What it does |
|---------|-------------|
| `/generate-web-diagram` | Generate an HTML diagram for any topic |
| `/generate-visual-plan` | Generate a visual implementation plan for a feature |
| `/generate-slides` | Generate a magazine-quality slide deck |
| `/diff-review` | Visual diff review with architecture comparison and code review |
| `/plan-review` | Compare a plan against the codebase with risk assessment |
| `/project-recap` | Mental model snapshot for context-switching back to a project |
| `/fact-check` | Verify accuracy of a document against actual code |

## Workflow

### 1. Think (5 seconds, not 5 minutes)

Commit to a direction before writing HTML. Don't default to "dark theme with blue accents."
**Visual is always default** — even essays and articles get card/diagram/grid treatment; prose
patterns (lead paragraphs, pull quotes, callouts) are accent elements within a visual page, not a
separate mode (see "Prose Page Elements" in `./references/css-patterns.md`).

Ask: **Who is looking?** (developer / PM / reviewer — shapes density). **What content type?**
(architecture, flowchart, sequence, data flow, schema/ER, state machine, mind map, class diagram,
C4, table, timeline, dashboard, prose) — see `./references/diagram-types.md` for per-type rules.
**What aesthetic?** Pick one of 4 constrained directions (Blueprint, Editorial, Paper/ink,
Monochrome terminal) or, with more discipline, a flexible one (IDE-inspired, Data-dense). Full
palette/font lists and forbidden combinations: `./references/aesthetics.md`. Vary the choice each
generation — the swap test: if a generic dark theme would look the same, you haven't designed
anything.

### 2. Structure

**Read the reference material each time** — don't rely on memory.
- Text-heavy architecture overviews: `./templates/architecture.html`
- Flowcharts, sequence, ER, state machines, mind maps, class diagrams, C4: `./templates/mermaid-flowchart.html`
- Data tables, comparisons, audits: `./templates/data-table.html`
- Slide decks (`--slides` flag or `/generate-slides`): `./templates/slide-deck.html` + `./references/slide-patterns.md`
- Prose-heavy pages (READMEs, articles): "Prose Page Elements" in `./references/css-patterns.md`
- CSS/layout patterns, SVG connectors: `./references/css-patterns.md`
- Pages with 4+ sections: `./references/responsive-nav.md` (sticky sidebar TOC / mobile scroll bar)

**Choosing a rendering approach:**

| Content type | Approach | Why |
|---|---|---|
| Architecture (text-heavy) | CSS Grid cards + flow arrows | Rich card content needs CSS control |
| Architecture (topology) / flowchart / sequence / data flow / ER / state machine / mind map / class diagram / C4 | **Mermaid** | Automatic node positioning and edge routing |
| Data table | HTML `<table>` | Semantic markup, accessibility, copy-paste |
| Timeline | CSS (central line + cards) | Simple linear layout doesn't need a layout engine |
| Dashboard | CSS Grid + Chart.js | Card grid with embedded charts |

**Mermaid essentials** (full theming guide in `./references/libraries.md`): always `theme: 'base'`
with custom `themeVariables`; never bare `<pre class="mermaid">` — use the full `diagram-shell` >
`.mermaid-wrap` > zoom-controls pattern from `templates/mermaid-flowchart.html` (copy wholesale, it
has zoom/pan/fit JS); prefer `flowchart TD` over `LR` for anything but 3-4 node linear flows; `<br/>`
for line breaks in labels, never `\n`; never define page-level `.node` CSS (Mermaid uses it
internally) — use `.ve-card` instead.

**AI-generated illustrations (optional).** If `surf-cli` is available (`which surf`), generate
images via Gemini for hero banners or concepts Mermaid can't express: `surf gemini "prompt"
--generate-image /tmp/ve-img.png --aspect-ratio 16:9`, then base64-embed and clean up. Skip
gracefully if unavailable — the page must stand on CSS/typography alone. Image container styles in
`./references/css-patterns.md`.

### 3. Style

Typography, color palette, surface depth, and animation rules are exhaustive in
`./references/aesthetics.md` — read it before finalizing colors/fonts. Core rules to hold in mind:
**typography is the diagram** (distinctive pairing, never Inter/Roboto/Arial as body font); **color
tells a story** (CSS custom properties, semantic names, no indigo/violet/neon-gradient); **surfaces
whisper** (2-4% lightness shifts, low-opacity borders, not dramatic contrast); **animation earns its
place** (staggered fade-ins, respect `prefers-reduced-motion`, nothing glows or pulses on its own).

### 4. Deliver

Write to `~/.agent/diagrams/` with a descriptive filename (`modem-architecture.html`,
`pipeline-flow.html`). Open it: `open ~/.agent/diagrams/filename.html` (macOS) or `xdg-open
~/.agent/diagrams/filename.html` (Linux). Tell the user the file path.

## File Structure

Every diagram is a single self-contained `.html` file — no external assets except CDN links (fonts,
optional libraries):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Descriptive Title</title>
  <link href="https://fonts.googleapis.com/css2?family=...&display=swap" rel="stylesheet">
  <style>/* CSS custom properties, theme, layout, components — all inline */</style>
</head>
<body>
  <!-- Semantic HTML: sections, headings, lists, tables, inline SVG -->
  <!-- Optional: <script> for Mermaid, Chart.js, or anime.js when used -->
</body>
</html>
```

## Quality Checks

Before delivering, verify: **squint test** (blur eyes — hierarchy still perceivable?); **swap test**
(generic dark theme would look the same? push the aesthetic further); **both themes** look
intentional; **information completeness** (pretty but incomplete is a failure); **no overflow** at
any browser width (every grid/flex child needs `min-width: 0`; see Overflow Protection in
`./references/css-patterns.md`); **Mermaid zoom controls** present on every diagram; **no console
errors**. Full anti-pattern checklist and the 7-point Slop Test: `./references/aesthetics.md`.
