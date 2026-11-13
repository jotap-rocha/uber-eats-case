# Diagram Types — detailed guidance per content type

Read the section for the content type you're generating. Not needed for every invocation — the
"Choosing a rendering approach" table in `SKILL.md` already tells you Mermaid vs CSS vs table; this
file has the deeper per-type rules.

## Architecture / System Diagrams
Three approaches depending on complexity:

**Simple topology (under 10 elements):** Use Mermaid. A `graph TD` with custom `themeVariables` produces readable diagrams with automatic edge routing.

**Text-heavy overviews (under 15 elements):** CSS Grid with explicit row/column placement. Sections as rounded cards with colored borders and monospace labels. Vertical flow arrows between sections. The reference template at `./templates/architecture.html` demonstrates this pattern. Use when cards need descriptions, code references, tool lists, or other rich content that Mermaid nodes can't hold.

**Complex architectures (15+ elements):** Use the **hybrid pattern** — a simple Mermaid overview (5-8 nodes showing module relationships) followed by detailed CSS Grid cards for each module's internals. This gives you visual topology AND readable details. The overview diagram uses module names with `<small>` tags for key function names. The cards below show full function lists with new/modified badges. Never try to cram 15+ elements into a single Mermaid diagram — it will render unreadably small even with zoom controls.

## Flowcharts / Pipelines
**Use Mermaid.** Automatic node positioning and edge routing produces proper diagrams with connecting lines, decision diamonds, and parallel branches — dramatically better than CSS flexbox with arrow characters. Prefer `graph TD` (top-down); use `graph LR` only for simple 3-4 node linear flows. Color-code node types with Mermaid's `classDef` or rely on `themeVariables` for automatic styling.

## Sequence Diagrams
**Use Mermaid.** Lifelines, messages, activation boxes, notes, and loops all need automatic layout. Use Mermaid's `sequenceDiagram` syntax. Style actors and messages via CSS overrides on `.actor`, `.messageText`, `.activation` classes.

## Data Flow Diagrams
**Use Mermaid.** Data flow diagrams emphasize connections over boxes — exactly what Mermaid excels at. Use `graph TD` (or `graph LR` for simple linear flows) with edge labels for data descriptions. Thicker, colored edges for primary flows. Source/sink nodes styled differently from transform nodes via Mermaid's `classDef`.

## Schema / ER Diagrams
**Use Mermaid.** Relationship lines between entities need automatic routing. Use Mermaid's `erDiagram` syntax with entity attributes. Style via `themeVariables` and CSS overrides on `.er.entityBox` and `.er.relationshipLine`.

## State Machines / Decision Trees
**Use Mermaid.** Use `stateDiagram-v2` for states with labeled transitions. Supports nested states, forks, joins, and notes. Decision trees can use `graph TD` with diamond decision nodes.

**`stateDiagram-v2` label caveat:** Transition labels have a strict parser — colons, parentheses, `<br/>`, HTML entities, and most special characters cause silent parse failures ("Syntax error in text"). If your labels need any of these (e.g., `cancel()`, `curate: true`, multi-line labels), use `flowchart TD` instead with rounded nodes and quoted edge labels (`|"label text"|`). Flowcharts handle all special characters and support `<br/>` for line breaks. Reserve `stateDiagram-v2` for simple single-word or plain-text labels.

## Mind Maps / Hierarchical Breakdowns
**Use Mermaid.** Use `mindmap` syntax for hierarchical branching from a root node. Mermaid handles the radial layout automatically. Style with `themeVariables` to control node colors at each depth level.

## Class Diagrams
**Use Mermaid.** Use `classDiagram` syntax for domain modeling, OOP design, and entity relationships with typed properties and methods. Supports relationships: association (`-->`), composition (`*--`), aggregation (`o--`), and inheritance (`<|--`). Add multiplicity labels (e.g., `"1" --> "*"`) and abstract/interface markers (`<<interface>>`, `<<abstract>>`). For simple entity boxes without OOP semantics (no methods, no inheritance), prefer `erDiagram` instead — it produces cleaner output for pure data modeling.

## C4 Architecture Diagrams
**Use Mermaid flowchart syntax — NOT native C4.** Use `graph TD` with `subgraph` blocks for C4 boundaries. Native `C4Context` hardcodes sharp corners, its own font, blue icons, and inline SVG colors that ignore `themeVariables` — it always clashes with custom palettes.

**Flowchart-as-C4 pattern:** Persons → rounded nodes `(("Name"))`, systems → rectangles `["Name"]`, databases → cylinders `[("Name")]`, boundaries → `subgraph` blocks, relationships → labeled arrows `-->|"protocol"|`. Use `classDef` + `:::className` to visually differentiate external systems (e.g., dashed borders). This inherits `themeVariables`, `fontFamily`, and CSS overrides like every other Mermaid diagram.

## Data Tables / Comparisons / Audits
Use a real `<table>` element — not CSS Grid pretending to be a table. Tables get accessibility, copy-paste behavior, and column alignment for free. The reference template at `./templates/data-table.html` demonstrates all patterns below.

**Use proactively.** Any time you'd render an ASCII box-drawing table in the terminal, generate an HTML table instead. This includes: requirement audits (request vs plan), feature comparisons, status reports, configuration matrices, test result summaries, dependency lists, permission tables, API endpoint inventories — any structured rows and columns.

Layout patterns:
- Sticky `<thead>` so headers stay visible when scrolling long tables
- Alternating row backgrounds via `tr:nth-child(even)` (subtle, 2-3% lightness shift)
- First column optionally sticky for wide tables with horizontal scroll
- Responsive wrapper with `overflow-x: auto` for tables wider than the viewport
- Column width hints via `<colgroup>` or `th` widths — let text-heavy columns breathe
- Row hover highlight for scanability

Status indicators (use styled `<span>` elements, never emoji):
- Match/pass/yes: colored dot or checkmark with green background
- Gap/fail/no: colored dot or cross with red background
- Partial/warning: amber indicator
- Neutral/info: dim text or muted badge

Cell content:
- Wrap long text naturally — don't truncate or force single-line
- Use `<code>` for technical references within cells
- Secondary detail text in `<small>` with dimmed color
- Keep numeric columns right-aligned with `tabular-nums`

## Timeline / Roadmap Views
Vertical or horizontal timeline with a central line (CSS pseudo-element). Phase markers as circles on the line. Content cards branching left/right (alternating) or all to one side. Date labels on the line. Color progression from past (muted) to future (vivid).

## Dashboard / Metrics Overview
Card grid layout. Hero numbers large and prominent. Sparklines via inline SVG `<polyline>`. Progress bars via CSS `linear-gradient` on a div. For real charts (bar, line, pie), use **Chart.js via CDN** (see `./references/libraries.md`). KPI cards with trend indicators (up/down arrows, percentage deltas).

## Implementation Plans

For visualizing implementation plans, extension designs, or feature specifications. The goal is **understanding the approach**, not reading the full source code.

**Don't dump full files.** Displaying entire source files inline overwhelms the page and defeats the purpose of a visual explanation. Instead:
- Show **file structure with descriptions** — list functions/exports with one-line explanations
- Show **key snippets only** — the 5-10 lines that illustrate the core logic
- Use **collapsible sections** for full code if truly needed

**Code blocks require explicit formatting.** Without `white-space: pre-wrap`, code runs together into an unreadable wall. See the "Code Blocks" section in `./references/css-patterns.md` for the correct pattern.

**Structure for implementation plans:**
1. Overview/purpose (what problem does this solve?)
2. Flow diagram (Mermaid or CSS cards)
3. File structure with descriptions (not full code)
4. Key implementation details (snippets)
5. API/interface summary
6. Usage examples

## Documentation (READMEs, Library Docs, API References)

When visualizing documentation, extract structure into visual elements:

| Content | Visual Treatment |
|---------|------------------|
| Features | Card grid (2-3 columns) |
| Install/setup steps | Numbered cards or vertical flow |
| API endpoints/commands | Table with sticky header |
| Config options | Table |
| Architecture | Mermaid diagram or CSS card layout |
| Comparisons | Side-by-side panels or table |
| Warnings/notes | Callout boxes |

Don't just format the prose — transform it. A feature list becomes a card grid. Install steps become a numbered flow. An API reference becomes a table.

## Prose Accent Elements

Use these sparingly within visual pages to highlight key points or provide breathing room. See "Prose Page Elements" in `./references/css-patterns.md` for CSS patterns.

- **Lead paragraph** — larger intro text to set context before diving into cards/grids
- **Pull quote** — highlight a key insight; one per page maximum
- **Callout box** — warnings, tips, important notes
- **Section divider** — visual break between major sections

**When to use:** A visual page explaining an essay might use a lead paragraph for the thesis, then cards for key arguments. A README visualization might use callout boxes for warnings but otherwise stay card/table-focused.

## Slide Deck Mode

An alternative output format for presenting content as a magazine-quality slide presentation instead of a scrollable page. **Opt-in only** — generate slides when the user invokes `/generate-slides`, passes `--slides` to an existing prompt (e.g., `/diff-review --slides`), or explicitly asks for a slide deck. Never auto-select slide format.

**Before generating slides**, read `./references/slide-patterns.md` (engine CSS, slide types, transitions, nav chrome, presets) and `./templates/slide-deck.html` (reference template showing all 10 types). Also read `./references/css-patterns.md` for shared patterns and `./references/libraries.md` for Mermaid/Chart.js theming.

**Slides are not pages reformatted.** They're a different medium. Each slide is exactly one viewport tall (100dvh) with no scrolling. Typography is 2–3× larger. Compositions are bolder. Compose a narrative arc (impact → context → deep dive → resolution) rather than mechanically paginating the source.

**Content completeness.** Changing the medium does not mean dropping content. Follow the "Planning a Deck from a Source Document" process in `slide-patterns.md` before writing any HTML: inventory the source, map every item to slides, verify coverage. Every section, decision, data point, specification, and collapsible detail from the source must appear in the deck. If a plan has 7 sections, the deck covers all 7. If there are 6 decisions, present all 6 — not the 2 that fit on one slide. Collapsible details in the source become their own slides. Add more slides rather than cutting content. A 22-slide deck that covers everything beats a 13-slide deck that looks polished but is missing 40% of the source.

**Slide types (10):** Title, Section Divider, Content, Split, Diagram, Dashboard, Table, Code, Quote, Full-Bleed. Each has a defined layout in `slide-patterns.md`. Content that exceeds a slide's density limit splits across multiple slides — never scrolls within a slide.

**Visual richness:** Check `which surf` at the start. If surf-cli is available, generate 2–4 images (title slide background, full-bleed background, optional content illustrations) before writing HTML — see the Proactive Imagery section in `slide-patterns.md` for the workflow. Also use SVG decorative accents, per-slide background gradients, inline sparklines, and small Mermaid diagrams. Visual-first, text-second.

**Compositional variety:** Consecutive slides must vary spatial approach — centered, left-heavy, right-heavy, split, edge-aligned, full-bleed. Three centered slides in a row means push one off-axis.

**Curated presets:** Four slide-specific presets as starting points (Midnight Editorial, Warm Signal, Terminal Mono, Swiss Clean) plus the existing 8 aesthetic directions adapted for slides. Pick one and commit. See `slide-patterns.md` for preset CSS values.

**`--slides` flag on existing prompts:** When a user passes `--slides` to `/diff-review`, `/plan-review`, `/project-recap`, or other prompts, gather data using the prompt's normal data-gathering instructions, then present the content as a slide deck instead of a scrollable page. The slide version tells the same story with different structure and pacing — but the same breadth of coverage. Don't use the slide format as an excuse to summarize or skip sections that the scrollable version would have included.
