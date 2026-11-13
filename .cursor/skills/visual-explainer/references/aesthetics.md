# Aesthetics reference — typography, color, surfaces, animation, anti-patterns

Exhaustive lists behind the condensed rules in `SKILL.md`'s "Style" section. Read before finalizing
colors/fonts, or when the Quality Checks slop test flags something.

## Typography

**Forbidden as `--font-body`:** Inter, Roboto, Arial, Helvetica, system-ui alone. These are AI slop signals.

**Good pairings (use these, vary each generation):**
- DM Sans + Fira Code (technical, precise)
- Instrument Serif + JetBrains Mono (editorial, refined)
- IBM Plex Sans + IBM Plex Mono (reliable, readable)
- Bricolage Grotesque + Fragment Mono (bold, characterful)
- Plus Jakarta Sans + Azeret Mono (rounded, approachable)

Load via `<link>` in `<head>`. Include a system font fallback in the `font-family` stack for offline resilience.

## Color

**Color tells a story.** Use CSS custom properties for the full palette. Define at minimum: `--bg`, `--surface`, `--border`, `--text`, `--text-dim`, and 3-5 accent colors. Each accent should have a full and a dim variant (for backgrounds). Name variables semantically when possible (`--pipeline-step` not `--blue-3`). Support both themes.

**Forbidden accent colors:** `#8b5cf6` `#7c3aed` `#a78bfa` (indigo/violet), `#d946ef` (fuchsia), the cyan-magenta-pink combination (`#06b6d4` → `#d946ef` → `#f472b6`). These are Tailwind defaults that signal zero design intent.

**Good accent palettes (use these):**
- Terracotta + sage (`#c2410c`, `#65a30d`) — warm, earthy
- Teal + slate (`#0891b2`, `#0369a1`) — technical, precise
- Rose + cranberry (`#be123c`, `#881337`) — editorial, refined
- Amber + emerald (`#d97706`, `#059669`) — data-focused
- Deep blue + gold (`#1e3a5f`, `#d4a73a`) — premium, sophisticated

Or derive from real IDE themes (Dracula, Nord, Solarized, Gruvbox, Catppuccin).

```css
/* Light-first (editorial, paper/ink, blueprint): */
:root { /* light values */ }
@media (prefers-color-scheme: dark) { :root { /* dark values */ } }

/* Dark-first (neon, IDE-inspired, terminal): */
:root { /* dark values */ }
@media (prefers-color-scheme: light) { :root { /* light values */ } }
```

**Forbidden color effects:** gradient text on headings (`background: linear-gradient(...); background-clip: text;`), animated glowing box-shadows, multiple overlapping radial glows creating a "neon haze".

## Aesthetic directions

**Constrained (prefer these — harder to mess up, have specific requirements that prevent generic output):**
- Blueprint — technical drawing feel, subtle grid background, deep slate/blue palette, monospace labels, precise borders
- Editorial — serif headlines (Instrument Serif, Crimson Pro), generous whitespace, muted earth tones or deep navy + gold
- Paper/ink — warm cream `#faf7f5` background, terracotta/sage accents, informal feel
- Monochrome terminal — green/amber on near-black, monospace everything, CRT glow optional

**Flexible (use with caution — require more discipline):**
- IDE-inspired — borrow a real, named color scheme (Dracula, Nord, Catppuccin Mocha/Latte, Solarized Dark/Light, Gruvbox, One Dark, Rosé Pine); commit to the actual palette, don't approximate
- Data-dense — small type, tight spacing, maximum information, muted colors

**Explicitly forbidden:** Neon dashboard (cyan + magenta + purple on dark), gradient mesh (pink/purple/cyan blobs), any combination of Inter font + violet/indigo accents + gradient text.

Vary the choice each time. The swap test: if you replaced your styling with a generic dark theme and nobody would notice the difference, you haven't designed anything.

## Surfaces, depth, hierarchy

**Surfaces whisper, they don't shout.** Build depth through subtle lightness shifts (2-4% between levels), not dramatic color changes. Borders should be low-opacity rgba (`rgba(255,255,255,0.08)` dark, `rgba(0,0,0,0.08)` light) — visible when you look, invisible when you don't.

**Backgrounds create atmosphere.** Don't use flat solid colors for the page background. Subtle gradients, faint grid patterns via CSS, or gentle radial glows behind focal areas.

**Visual weight signals importance.** Executive summaries and key metrics should dominate the viewport on load (larger type, more padding, subtle accent-tinted background zone). Reference sections (file maps, dependency lists, decision logs) should be compact. Use `<details>/<summary>` for useful-but-not-primary sections (see `./references/css-patterns.md`).

**Surface depth creates hierarchy.** Hero sections get elevated shadows and accent-tinted backgrounds (`ve-card--hero`). Body content stays flat (`.ve-card`). Code blocks and secondary content feel recessed (`ve-card--recessed`). Don't make everything elevated — when everything pops, nothing does.

## Animation

**Animation earns its place.** Staggered fade-ins on page load are almost always worth it. Mix animation types by role: `fadeUp` for cards, `fadeScale` for KPIs/badges, `drawIn` for SVG connectors, `countUp` for hero numbers. Hover transitions on interactive-feeling elements. Always respect `prefers-reduced-motion`. For orchestrated multi-element sequences, anime.js via CDN is available (see `./references/libraries.md`).

**Forbidden:** animated glowing box-shadows (`@keyframes glow`), pulsing/breathing effects on static content, continuous animations that run after page load (except progress indicators).

## Anti-Patterns (AI Slop) — full checklist

Review every generated page against this before delivering.

**Section headers — forbidden:** emoji icons (🏗️ ⚙️ 📁 💻 📅 🔗 ⚡ 🔧 📦 🚀), all sections using the same icon-in-rounded-box pattern. **Required:** styled monospace labels with colored dot indicators (`.section-label`), numbered badges (`section__num`), or asymmetric dividers. If an icon is genuinely needed, inline SVG matching the palette — not emoji.

**Layout & hierarchy — forbidden:** perfectly centered everything with uniform padding, all cards styled identically, every section getting equal visual treatment, symmetric mirrored layouts. **Required:** vary visual weight (hero → elevated → default → recessed), asymmetric layouts.

**Template patterns — forbidden:** three-dot window chrome (red/yellow/green) on code blocks, KPI cards with identical gradient text on every metric, "Neon Dashboard" aesthetic, gradient meshes with pink/purple/cyan blobs. **Required:** code blocks use a simple header with filename/language label; KPI cards vary by importance.

**The Slop Test:** would a developer looking at this page immediately think "AI generated this"? Telltale signs — (1) Inter/Roboto + purple/violet gradient accents, (2) every heading has gradient-text, (3) emoji icons leading every section, (4) glowing cards with animated shadows, (5) cyan-magenta-pink on dark, (6) perfectly uniform card grid with no hierarchy, (7) three-dot code block chrome. Two or more present = regenerate with a different aesthetic direction (Editorial, Blueprint, Paper/ink, or a specific IDE theme).
