# Frontend Quick Reference

> **MCP Validated:** 2026-04-20
> Fast lookup tables. For code examples, see linked concept/pattern files.

## TypeScript Utility Types

| Type | Use | Example |
|------|-----|---------|
| `Record<K, V>` | Map union keys to values | `Record<CaseStatus, { class: string }>` |
| `Partial<T>` | All props optional | `Partial<FilterState>` for overrides |
| `keyof T` | Union of keys | `keyof FilterState` for update function |
| `React.ElementType` | Any React-renderable component | Icon prop type in StatCard |

## Type vs Interface Decision

| Use `type` when | Use `interface` when |
|-----------------|----------------------|
| Union types (`"Novo" \| "Em Análise"`) | Object shape with optional extension |
| Computed/conditional types | Props interfaces |
| Aliases for primitives | Domain entities (FraudCase, User) |

## Tailwind Class Patterns

| Pattern | Classes | Where used |
|---------|---------|------------|
| Muted label | `text-xs text-muted-foreground` | FilterBar labels |
| Mono value | `font-mono text-sm` | CPF, score, case ID |
| Sticky header | `sticky top-0 z-40 bg-card/50 backdrop-blur-sm` | Dashboard header |
| Glass card | `glass-card` (custom) | FilterBar, StatCard, CaseDetail |
| Entry animation | `animate-slide-in` (custom) | CaseDetail modal |
| Icon size sm | `w-4 h-4` | Most lucide icons in buttons |
| Icon size xs | `w-3 h-3` | Inline icons in badges/labels |

## cn() Usage

| Situation | Example |
|-----------|---------|
| Conditional class | `cn("base", condition && "extra")` |
| Variant merge | `cn(defaultClass, variantClass[variant])` |
| Override Tailwind | `cn("px-4", props.className)` — merge resolves conflict |

## shadcn/ui Component Quick Map

| Need | Component | Import path |
|------|-----------|-------------|
| Trigger + dropdown | `Select` | `@/components/ui/select` |
| Text input | `Input` | `@/components/ui/input` |
| Labelled field | `Label` | `@/components/ui/label` |
| Action button | `Button` | `@/components/ui/button` |
| Multi-line input | `Textarea` | `@/components/ui/textarea` |
| Collapsible section | `Accordion` | `@/components/ui/accordion` |
| Overlay modal | `Dialog` | `@/components/ui/dialog` |
| Inline notification | `Badge` | `@/components/ui/badge` |

## Vite Env Vars

| Variable | Access in code |
|----------|---------------|
| `VITE_SUPABASE_URL` | `import.meta.env.VITE_SUPABASE_URL` |
| `VITE_SUPABASE_PUBLISHABLE_KEY` | `import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY` |
| `VITE_SUPABASE_PROJECT_ID` | `import.meta.env.VITE_SUPABASE_PROJECT_ID` |

## Responsive Breakpoints (Tailwind defaults)

| Prefix | Min-width | SisFraude usage |
|--------|-----------|----------------|
| `sm:` | 640px | Show context badge, user name |
| `md:` | 768px | General layout adjustments |
| `lg:` | 1024px | 4-column filter grid |
| (none) | 0px | Mobile-first base |

## Decision Matrix

| Use Case | Choose |
|----------|--------|
| Status mapped to display class | `Record<CaseStatus, { class: string }>` |
| Icon as component prop | `icon: React.ElementType` |
| Conditional Tailwind | `cn()` from `@/lib/utils` |
| New UI component needed | Compose from `src/components/ui/` — never install new lib |
| Access env var in component | `import.meta.env.VITE_*` |
| Import from `src/` | `@/` alias — never use relative `../../` |

## Common Pitfalls

| Don't | Do |
|-------|-----|
| `import X from '../../components/ui/button'` | `import X from '@/components/ui/button'` |
| `process.env.MY_VAR` | `import.meta.env.VITE_MY_VAR` |
| Install new UI library | Compose from existing `src/components/ui/` |
| Use `clsx` alone on Tailwind | Use `cn()` which also runs `tailwind-merge` |
| Create new types inline in component | Import from `@/types/fraud` |
| `interface` for union type | `type CaseStatus = "Novo" \| ...` |

## Related Documentation

| Topic | Path |
|-------|------|
| TypeScript patterns | `concepts/typescript-patterns.md` |
| Tailwind + cn() | `concepts/tailwind-composition.md` |
