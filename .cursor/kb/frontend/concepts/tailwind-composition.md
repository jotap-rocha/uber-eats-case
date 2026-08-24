# Tailwind CSS 3 Composition

> **Purpose**: cn(), responsive design, custom utilities, and variant patterns used in SisFraude
> **Confidence**: 0.95
> **MCP Validated:** 2026-04-20

## Overview

SisFraude uses Tailwind CSS 3 with a custom theme defined in `tailwind.config.ts`. The `cn()` utility from `@/lib/utils` is the sole method for conditional class assembly. Two custom utilities are defined: `glass-card` and `animate-slide-in`.

## cn() — The Core Utility

```typescript
// src/lib/utils.ts — full implementation
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

`clsx` handles conditional logic. `twMerge` resolves Tailwind conflicts (e.g., `px-2` + `px-4` → `px-4`).

```tsx
// Basic conditional
<span className={cn("base-class", isActive && "active-class")} />

// Variant from object map
const variants = { default: "bg-secondary", primary: "bg-primary" };
<button className={cn("px-4 py-2", variants[variant], className)} />

// Override from parent — tailwind-merge picks the last winner
<Input className={cn("h-9 text-sm", props.className)} />
```

## Custom Utilities in SisFraude

```css
/* glass-card — card with backdrop blur + border */
/* Used in: FilterBar, StatCard, CaseDetail modal */
.glass-card {
  background: hsl(var(--card));
  border: 1px solid hsl(var(--border) / 0.5);
  border-radius: var(--radius);
  backdrop-filter: blur(8px);
}

/* animate-slide-in — entry animation for CaseDetail */
/* Defined in tailwind.config.ts keyframes */
@keyframes slide-in {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}
.animate-slide-in { animation: slide-in 0.3s ease-out; }
```

Apply as Tailwind utility classes:
```tsx
<div className="glass-card p-5 space-y-4">  {/* FilterBar */}
<div className="glass-card animate-slide-in"> {/* CaseDetail */}
```

## Responsive Grid Pattern

Tailwind is mobile-first. Base styles apply at all sizes; prefixed styles apply at and above the breakpoint.

```tsx
// FilterBar: 1-col mobile → 2-col tablet → 4-col desktop
<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">

// Stats: 2-col mobile → 4-col tablet up
<div className="grid grid-cols-2 sm:grid-cols-4 gap-3">

// Hide text on mobile, show on sm+
<span className="hidden sm:inline-flex">Context info</span>
```

## Custom Color Tokens

Colors are CSS variables resolved by Tailwind. All semantic colors follow the `hsl(var(--token))` convention:

```typescript
// tailwind.config.ts — risk severity scale
colors: {
  risk: {
    critical: "hsl(var(--risk-critical))",
    high:     "hsl(var(--risk-high))",
    medium:   "hsl(var(--risk-medium))",
    low:      "hsl(var(--risk-low))",
  }
}
// Usage: className="text-risk-critical bg-risk-critical/10"

// Arbitrary CSS variable (StatusBadge pattern)
className="bg-[hsl(var(--status-new)/0.15)] text-[hsl(var(--status-new))]"
```

## Common Patterns

| Pattern | Classes |
|---------|---------|
| Muted label | `text-xs text-muted-foreground` |
| Monospace value | `font-mono text-sm` |
| Sticky header | `sticky top-0 z-40 bg-card/50 backdrop-blur-sm` |
| Centered max-width | `max-w-[1600px] mx-auto px-4 sm:px-6` |
| Space between items | `space-y-4` or `space-y-6` for vertical rhythm |
| Icon + text row | `flex items-center gap-2` |

## Common Mistakes

### Wrong

```tsx
// Duplicating conditional class logic without cn()
className={`base ${condition ? "active" : ""} ${extra}`}

// Conflicting Tailwind classes without twMerge
className="px-2 px-4"  // both applied — unpredictable
```

### Correct

```tsx
// cn() handles both conditionals and conflict resolution
className={cn("base px-2", condition && "active", "px-4")}
// Result: "base active px-4" — px-4 wins via tailwind-merge
```

## Related

- [concepts/shadcn-ui.md](shadcn-ui.md) — how shadcn variants integrate with cn()
- [patterns/responsive-layout.md](../patterns/responsive-layout.md) — full page layout examples
