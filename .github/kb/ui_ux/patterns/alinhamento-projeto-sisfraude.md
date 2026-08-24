# Padrão — Alinhamento ao Fraud Investigator Hub (SisFraude)

> **Purpose**: Traduzir princípios de UI/UX para o stack e componentes deste repositório.  
> **Confidence**: 0.95 (específico do projeto)

## Stack de referência

React 18, TypeScript 5, Vite 5, Tailwind, shadcn/ui, React Query, Supabase (roadmap).

## Superfícies visuais

| Elemento | Convenção local |
|----------|------------------|
| Cards | Classe utilitária `glass-card` para superfícies principais |
| Badges de risco/status | `RiskBadge`, `StatusBadge` — não reinventar cores por tela |
| Modais | `CaseDetail` como referência de tabs e densidade |
| Toasts | Sonner (`@/components/ui/sonner`) para feedback pós-ação |
| Formulários | React Hook Form + Zod + componentes shadcn |

## Tabelas e dados

- `CaseTable` / Lab PRD: paginação, ordenação, filtros com vocabulário único.
- CPF mascarado e score normalizado para badge — consistência com [tabelas-dados.md](../concepts/tabelas-dados.md).

## Feedback sem novo request

Quando a lógica é só client-side (ex.: “Buscar casos” no Lab):

- Spinner + `aria-busy` no botão  
- Realce temporário na área de resultados (ring/overlay leve)  
- Toast de “lista atualizada” com contagem  

Isso implementa [feedback-constante.md](../concepts/feedback-constante.md) sem mentir sobre rede.

## Polimento

- Microcopy e futuro i18n: [concepts/microcopy-i18n.md](../concepts/microcopy-i18n.md)  
- Animações e `prefers-reduced-motion`: [patterns/tailwind-motion-reduced.md](tailwind-motion-reduced.md)  
- Checklist de release: [specs/ui-checklist.yaml](../specs/ui-checklist.yaml)

## Onde aprofundar

- `.github/kb/sisfraude/` — domínio de casos e sessão multi-empresa  
- `.github/kb/frontend/` — Tailwind, shadcn, TypeScript  
- `.github/kb/react/` — hooks, estado derivado, providers  
