# UI/UX — Base de conhecimento (frontend)

> **Propósito**: Princípios e padrões de interface para aplicações web (especialmente dashboards e apps de dados), com checklist de release e vínculo ao stack SisFraude quando aplicável.  
> **Stack de referência local**: React 18, TypeScript, Vite, Tailwind, shadcn/ui, React Query.

## Navegação rápida

### Conceitos (foco em decisão de produto e UX)

| Arquivo | Tema |
|---------|------|
| [concepts/clareza-de-tela.md](concepts/clareza-de-tela.md) | Objetivo da tela, linguagem, densidade |
| [concepts/hierarquia-visual.md](concepts/hierarquia-visual.md) | Título, escaneabilidade, ênfase |
| [concepts/fluxo-simples.md](concepts/fluxo-simples.md) | Menos passos, caminho feliz, reversibilidade |
| [concepts/feedback-constante.md](concepts/feedback-constante.md) | Estados de sistema visíveis |
| [concepts/tratamento-erro-amigavel.md](concepts/tratamento-erro-amigavel.md) | Mensagens acionáveis |
| [concepts/consistencia-design-system.md](concepts/consistencia-design-system.md) | Botões, cores, menus, tabelas, mensagens |
| [concepts/design-responsivo.md](concepts/design-responsivo.md) | Layouts adaptativos |
| [concepts/percepcao-de-performance.md](concepts/percepcao-de-performance.md) | Operação lenta × sensação de rapidez |
| [concepts/tabelas-dados.md](concepts/tabelas-dados.md) | Apps de dados: grid como peça central |
| [concepts/acessibilidade.md](concepts/acessibilidade.md) | WCAG-minded em sistemas internos |
| [concepts/seguranca-experiencia.md](concepts/seguranca-experiencia.md) | Confirmação em ações críticas |
| [concepts/observabilidade-usuario.md](concepts/observabilidade-usuario.md) | Transparência técnica para o usuário |
| [concepts/empty-states.md](concepts/empty-states.md) | Listas vazias e primeiros passos |
| [concepts/ux-para-ia.md](concepts/ux-para-ia.md) | Agentes, evidências, confiança |
| [concepts/menos-e-mais.md](concepts/menos-e-mais.md) | Progressivo: decisão × investigação |
| [concepts/microcopy-i18n.md](concepts/microcopy-i18n.md) | Tom de voz, pluralização, preparação i18n |
| [concepts/movimento-reduzido.md](concepts/movimento-reduzido.md) | `prefers-reduced-motion`, animações seguras |

### Padrões (como aplicar)

| Arquivo | Uso |
|---------|-----|
| [patterns/loading-etapas-e-cache.md](patterns/loading-etapas-e-cache.md) | Skeleton, progresso, etapas, cache, paginação, lazy |
| [patterns/confirmacao-acoes-criticas.md](patterns/confirmacao-acoes-criticas.md) | Diálogos e texto de confirmação |
| [patterns/alinhamento-projeto-sisfraude.md](patterns/alinhamento-projeto-sisfraude.md) | `glass-card`, badges, Sonner, Lab PRD |
| [patterns/tailwind-motion-reduced.md](patterns/tailwind-motion-reduced.md) | `motion-reduce:` / `motion-safe:` no Tailwind 3.4 |

### Specs (máquina + revisão)

| Arquivo | Uso |
|---------|-----|
| [specs/ui-checklist.yaml](specs/ui-checklist.yaml) | Checklist versionável por severidade (required/recommended/optional) |

---

## Referência rápida

- [quick-reference.md](quick-reference.md) — checklist pré-release e mapa técnico curto
- [specs/ui-checklist.yaml](specs/ui-checklist.yaml) — mesmo conteúdo estruturado para agentes/scripts

---

## Trilha de aprendizado

| Nível | Leia primeiro |
|-------|----------------|
| **Base** | clareza-de-tela, hierarquia-visual, feedback-constante, tratamento-erro-amigavel |
| **Apps de dados** | tabelas-dados, percepcao-de-performance, patterns/loading-etapas-e-cache |
| **Confiança e risco** | seguranca-experiencia, observabilidade-usuario, ux-para-ia |
| **Polimento** | microcopy-i18n, movimento-reduzido, patterns/tailwind-motion-reduced |

---

## Agentes sugeridos

| Agente / papel | Arquivos principais |
|----------------|---------------------|
| Implementação React | patterns/alinhamento-projeto-sisfraude.md, `.claude/kb/frontend/` |
| Fluxos longos (Databricks etc.) | patterns/loading-etapas-e-cache.md, concepts/percepcao-de-performance.md |
| Revisão de PR / release de tela | specs/ui-checklist.yaml, quick-reference.md |
| Agente Cursor dedicado | `.claude/agents/sisfraude/ui-ux-specialist.md` |
