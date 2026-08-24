# Frontend Knowledge Base

> **Purpose**: TypeScript 5, Tailwind CSS 3, shadcn/ui, Vite 5, and frontend performance patterns for SisFraude
> **MCP Validated:** 2026-04-20
> **Scope**: Complements `kb/react/` — covers tooling and styling layers, not React component patterns

## Quick Navigation

### Concepts (< 150 lines each)

| File | Purpose |
|------|---------|
| [concepts/typescript-patterns.md](concepts/typescript-patterns.md) | Generics, utility types, discriminated unions, type guards |
| [concepts/tailwind-composition.md](concepts/tailwind-composition.md) | cn(), responsive design, custom utilities, variants |
| [concepts/shadcn-ui.md](concepts/shadcn-ui.md) | Component usage, Radix primitives, theming, variants |
| [concepts/vite-config.md](concepts/vite-config.md) | Build config, path aliases, env vars with VITE_ prefix |

### Patterns (< 200 lines each)

| File | Purpose |
|------|---------|
| [patterns/responsive-layout.md](patterns/responsive-layout.md) | Grid/flex patterns used across SisFraude pages |
| [patterns/icon-usage.md](patterns/icon-usage.md) | lucide-react icon patterns with React.ElementType |

---

## Quick Reference

- [quick-reference.md](quick-reference.md) — Fast lookup tables for all topics

---

## Boundary with react KB

| Topic | KB to use |
|-------|-----------|
| useState, useEffect, useMemo hooks | `kb/react/` |
| React Query data fetching | `kb/react/` |
| React Router v6 navigation | `kb/react/` |
| TypeScript types and utility types | **this KB** |
| Tailwind classes and cn() | **this KB** |
| shadcn/ui component APIs | **this KB** |
| Vite config, path aliases, env vars | **this KB** |
| Bundle splitting, lazy loading | **this KB** |
| lucide-react icon patterns | **this KB** |

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **`cn()`** | `clsx` + `tailwind-merge` — resolves class conflicts from conditional Tailwind |
| **`@/` alias** | Maps to `src/` — configured in both `vite.config.ts` and `tsconfig.json` |
| **`VITE_` prefix** | Required for env vars to be exposed to browser code |
| **discriminated union** | Union type with a shared literal field used as type narrowing key |
| **shadcn/ui** | Component library installed locally in `src/components/ui/` — never install alternatives |
| **`glass-card`** | Custom Tailwind utility: card with backdrop-blur and border |
| **`animate-slide-in`** | Custom keyframe entry animation defined in `tailwind.config.ts` |

---

## Learning Path

| Level | Files |
|-------|-------|
| **Start here** | concepts/vite-config.md → concepts/typescript-patterns.md |
| **Styling** | concepts/tailwind-composition.md → patterns/responsive-layout.md |
| **Components** | concepts/shadcn-ui.md → patterns/icon-usage.md |

---

## Agent Usage

| Agent | Primary Files | Use Case |
|-------|---------------|----------|
| `react-specialist` | All files here + `kb/react/` | Component implementation with correct types and styles |
| `sisfraude-specialist` | concepts/typescript-patterns.md, concepts/shadcn-ui.md | Domain component building |
| `kb-architect` | index.md, quick-reference.md | KB maintenance |
