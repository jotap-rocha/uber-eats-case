# shadcn/ui Component Patterns

> **Purpose**: Component usage, Radix UI primitives, theming, and variant patterns in SisFraude
> **Confidence**: 0.95
> **MCP Validated:** 2026-04-20

## Overview

shadcn/ui components are copied directly into `src/components/ui/` during installation. They are NOT an npm dependency — they are your code. Never install alternative UI libraries; compose all UI from the existing 50+ components in `src/components/ui/`. Components are built on Radix UI primitives and styled with Tailwind.

## Installed Components in Use

```
src/components/ui/
├── button.tsx        — variant: default | destructive | outline | ghost | link
├── input.tsx         — controlled text input
├── label.tsx         — accessible label
├── select.tsx        — SelectTrigger + SelectContent + SelectItem (Radix)
├── textarea.tsx      — multi-line input
├── badge.tsx         — status/label chip
├── accordion.tsx     — collapsible section (Radix)
├── dialog.tsx        — modal overlay (Radix)
├── tabs.tsx          — tabbed content (Radix)
└── ... (50+ total)
```

## Select Pattern (Radix Compound Component)

```tsx
import {
  Select, SelectContent, SelectItem,
  SelectTrigger, SelectValue
} from "@/components/ui/select";

// FilterBar pattern — controlled Select
<Select value={filters.status} onValueChange={(v) => update("status", v)}>
  <SelectTrigger className="bg-secondary border-border h-9 text-sm">
    <SelectValue placeholder="Todos" />
  </SelectTrigger>
  <SelectContent>
    <SelectItem value="all">Todos</SelectItem>
    {allStatuses.map((s) => (
      <SelectItem key={s} value={s}>{s}</SelectItem>
    ))}
  </SelectContent>
</Select>
```

## Button Variants

```tsx
import { Button } from "@/components/ui/button";

// Primary action
<Button className="bg-primary hover:bg-primary/90 text-primary-foreground">
  <Search className="w-4 h-4 mr-2" /> Buscar
</Button>

// Ghost — secondary/destructive action
<Button variant="ghost" size="sm" className="text-muted-foreground hover:text-foreground">
  <RotateCcw className="w-3 h-3 mr-1" /> Limpar
</Button>

// Sizes: default | sm | lg | icon
```

## CSS Variable Theming

shadcn/ui uses CSS variables for all colors. Override per-token in `src/index.css`:

```css
:root {
  --background: 222 47% 11%;
  --foreground: 213 31% 91%;
  --primary: 210 100% 60%;
  --card: 222 47% 14%;
  --border: 216 34% 25%;
  --radius: 0.5rem;
  /* Risk severity — SisFraude custom tokens */
  --risk-critical: 0 84% 60%;
  --risk-high: 25 95% 53%;
  --risk-medium: 45 96% 64%;
  --risk-low: 142 71% 45%;
}
```

All Tailwind color utilities (`bg-primary`, `text-foreground`, `border-border`) read these variables.

## Variant Pattern with Record

```tsx
// StatusBadge.tsx — exhaustive Record over discriminated union
import type { CaseStatus } from "@/types/fraud";

const statusConfig: Record<CaseStatus, { class: string }> = {
  "Novo":           { class: "bg-[hsl(var(--status-new)/0.15)] ..." },
  "Em Análise":     { class: "bg-[hsl(var(--status-analysis)/0.15)] ..." },
  "Confirmado":     { class: "bg-[hsl(var(--status-confirmed)/0.15)] ..." },
  "Falso Positivo": { class: "..." },
};

export const StatusBadge = ({ status }: { status: CaseStatus }) => (
  <span className={cn(
    "inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium border",
    statusConfig[status].class
  )}>
    {status}
  </span>
);
```

## Accessibility via Radix

Radix UI primitives (used by Select, Dialog, Accordion) provide:
- ARIA roles and attributes automatically
- Keyboard navigation (Arrow, Enter, Escape)
- Focus trapping in modals
- Screen reader announcements

```tsx
// Dialog — Radix handles focus trap + Escape key automatically
import { Dialog, DialogContent, DialogHeader } from "@/components/ui/dialog";
```

## Common Mistakes

### Wrong

```tsx
// Installing a new UI library for a missing component
npm install @mui/material  // NEVER — compose from existing ui/
```

### Correct

```tsx
// Build from primitives already in src/components/ui/
// If a Dialog is needed: use ui/dialog.tsx
// If tabs are needed: use ui/tabs.tsx
// Check src/components/ui/ first — 50+ components installed
```

## Related

- [concepts/tailwind-composition.md](tailwind-composition.md) — cn() and class variant patterns
- [concepts/typescript-patterns.md](typescript-patterns.md) — Record<CaseStatus, ...> variant type
