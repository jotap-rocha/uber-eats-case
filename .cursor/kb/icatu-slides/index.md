# Icatu Slides — Knowledge Base

> Design system, layouts corporativos e regras de qualidade para **HTML slide decks** alinhados à identidade **Icatu**, derivados dos PDFs oficiais em `templates/ppts/ICATU/`.

## Quando usar

Consulte esta KB quando:

- Criar ou revisar slides HTML para trilhas, auditorias ou comunicações **Icatu**.
- Precisar harmonizar **cores**, **tipografia**, **logo**, **formas de fundo** e **tipos de página** com o template corporativo.
- O requisito for **não usar pesquisa na internet** para marca: use **somente** esta KB + PDFs + assets versionados no repositório.

**Fluxo dos agentes (planner → builder → reviewer → fixer → reviewer):** ver [fluxo-agentes.md](fluxo-agentes.md).

## Fontes normativas (ordem de prioridade)

1. `templates/ppts/ICATU/template_ppt_Icatu.pdf` — paleta, fontes, categorias de slide.
2. `templates/ppts/ICATU/ppt_trilha_de_auditoria_jan_2026.pdf` — referência de aplicação.
3. `templates/ppts/ICATU/assets/*` — logo e imagens exportadas da Vitrine de Marketing.
4. Arquivos desta pasta `.cursor/kb/icatu-slides/`.

## Arquivos deste domínio

| Arquivo | Finalidade |
|---------|------------|
| [sources-and-logo.md](sources-and-logo.md) | Caminhos dos PDFs, logo, Vitrine / Guia da Marca (sem internet). |
| [icatu-palette.md](icatu-palette.md) | **Cores oficiais** (RGB/HEX/Pantone) extraídas do template PDF. |
| [design-system.md](design-system.md) | Variáveis CSS, tipografia Roboto + Arial, superfícies. |
| [layout-and-geometry.md](layout-and-geometry.md) | Capas, sub-capas, faixas diagonais e planos de fundo geométricos. |
| [slide-types.md](slide-types.md) | Tipos de página espelhando o template Icatu. |
| [component-library.md](component-library.md) | Componentes CSS reutilizáveis (tags, cards, barras). |
| [quality-rules.md](quality-rules.md) | Regras de densidade, PT-BR, contraste e marca. |
| [slide-engine.md](slide-engine.md) | Motor JS, navegação e scroll (igual padrão Kurv/AIDE). |
| [animation-patterns.md](animation-patterns.md) | Animações usando tokens Icatu. |
| [advanced-visuals.md](advanced-visuals.md) | SVG, fluxos e painéis com marca Icatu. |
| [template.md](template.md) | Esqueleto HTML inicial com barra Icatu + logo. |
| [fluxo-agentes.md](fluxo-agentes.md) | **Usabilidade:** ordem dos agentes Icatu, diagrama e quando saltar etapas. |

## Convenção de pastas (sugestão)

```
presentation/icatu-{codigo}/
├── {codigo}-slide-spec.md
├── {codigo}-slides.html
└── assets/   # imagens locais, diagramas
```

O `slide-spec.md` continua sendo a **fonte da verdade** do roteiro de slides (espelhando a ideia do KB AIDE Slides).

## Agentes

- **Planear (sem HTML):** `@.cursor/agents/communication/icatu-slide-planner.md` — slide-map com tipos `slide--icatu-*`, chunks e layout alinhados ao PDF.
- **Gerar:** `@.cursor/agents/communication/icatu-slide-builder.md` + KB **`@.cursor/kb/icatu-slides/`** (ou `index.md`).
- **Rever (read-only):** `@.cursor/agents/communication/icatu-slide-reviewer.md` no ficheiro HTML — valida paleta, marca, motor e checklist frente aos PDFs em `templates/ppts/ICATU/`.
- **Corrigir (mecânico):** `@.cursor/agents/communication/icatu-slide-fixer.md` com base no relatório do revisor (diff mínimo); reestruturação → builder.

## Paleta rápida (referência)

| Token | Hex | Uso |
|-------|-----|-----|
| `--icatu-azul-01` | `#1B3157` | Fundos escuros, faixas principais |
| `--icatu-azul-02` | `#6AA2B9` | Destaque, gráficos, links |
| `--icatu-azul-03` | `#D5DBE6` | Fundos claros, áreas “ar” |
| `--icatu-verde-01` | `#5FBB48` | Acento institucional positivo |
| `--icatu-cinza-01` | `#939598` | Texto secundário, grids |

Detalhes e CMYK em [icatu-palette.md](icatu-palette.md).
