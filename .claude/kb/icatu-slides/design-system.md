# Design System — Icatu Slides

> Tokens visuais para decks HTML **Icatu**, alinhados a `template_ppt_Icatu.pdf` e [icatu-palette.md](icatu-palette.md).

## Variáveis CSS (`:root`)

```css
:root {
  /* Marca — ver icatu-palette.md */
  --icatu-azul-01: #1B3157;
  --icatu-azul-02: #6AA2B9;
  --icatu-azul-03: #D5DBE6;
  --icatu-verde-01: #5FBB48;
  --icatu-cinza-01: #939598;

  /* Aliases de uso em componentes (espelham AIDE, sem misturar paleta AIDE) */
  --bg: var(--icatu-azul-01);
  --surface: rgba(27, 49, 87, 0.92);
  --surface-elevated: #243a5c;
  --accent: var(--icatu-azul-02);
  --accent-positive: var(--icatu-verde-01);
  --text: #f0f3f7;
  --text-dim: rgba(213, 219, 230, 0.82);
  --text-muted: var(--icatu-cinza-01);
  --border: rgba(106, 162, 185, 0.25);
  --border-bright: rgba(106, 162, 185, 0.45);

  --accent-dim: rgba(106, 162, 185, 0.12);
  --verde-dim: rgba(95, 187, 72, 0.15);

  /* Código / dados */
  --code-bg: #0f1729;
  --code-text: #d5dbe6;

  /* Tipografia — Roboto + fallback Arial (PDF) */
  --font-display: "Roboto", Arial, sans-serif;
  --font-body: "Roboto", Arial, sans-serif;
  --font-mono: ui-monospace, "Cascadia Code", "Source Code Pro", Menlo, monospace;
}
```

## Tipografia

| Papel | Peso Roboto | Uso |
|-------|-------------|-----|
| Título hero | Black (900) | Capa e números de seção |
| Subtítulo / destaque | Medium (500–600) | Sub-capas, labels |
| Corpo | Regular (400) | Texto corrido |
| Apoio / notas | Light (300) | Legendas discretas |

Escala sugerida (ajuste por viewport):

```css
.icatu-display { font-size: clamp(40px, 8vw, 96px); font-weight: 900; letter-spacing: -0.02em; }
.icatu-heading { font-size: clamp(28px, 4.5vw, 52px); font-weight: 600; }
.icatu-body   { font-size: clamp(16px, 2vw, 22px); font-weight: 400; line-height: 1.45; }
.icatu-label  { font-size: clamp(11px, 1.2vw, 14px); font-weight: 500; letter-spacing: 0.04em; text-transform: uppercase; color: var(--icatu-azul-03); }
```

## Fundo e textura

- Base: `--icatu-azul-01` sólido ou gradiente **linear** discreto para `#243a5c` (não usar cores fora da paleta).
- Grain / ruído: opcional, opacidade **≤ 0.04** para não sujar a marca.

## Barra institucional

Ver [template.md](template.md): barra fixa ou superior com **logo** + título curto da trilha (ex.: “Trilha de Auditoria 2026”).

## O que não fazer

- Misturar paleta **AIDE** (cyan `#00b4ff`, gold Kurv) com slides Icatu.
- Carregar **Google Fonts** em ambiente restrito: preferir `@font-face` local com arquivos da Vitrine.
