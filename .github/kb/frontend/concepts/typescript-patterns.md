# TypeScript 5 Patterns

> **Purpose**: Generics, utility types, discriminated unions, and type guards as used in SisFraude
> **Confidence**: 0.95
> **MCP Validated:** 2026-04-20

## Overview

SisFraude centralizes all domain types in `src/types/fraud.ts`. The project uses `type` for union aliases and `interface` for object shapes. Type guards and `Record<>` mapped types appear throughout the component layer.

## Discriminated Unions

A union type where one shared literal field acts as the discriminant key.

```typescript
// src/types/fraud.ts — canonical pattern
export type CaseStatus = "Novo" | "Em Análise" | "Confirmado" | "Falso Positivo";
export type BusinessLine = "Vida" | "Previdência";
export type UserRole = "analyst" | "manager" | "admin";

// Discriminant used in Record mapping (StatusBadge.tsx)
const statusConfig: Record<CaseStatus, { class: string }> = {
  "Novo":           { class: "bg-[hsl(var(--status-new)/0.15)] ..." },
  "Em Análise":     { class: "bg-[hsl(var(--status-analysis)/0.15)] ..." },
  "Confirmado":     { class: "bg-[hsl(var(--status-confirmed)/0.15)] ..." },
  "Falso Positivo": { class: "bg-[hsl(var(--status-false-positive)/0.15)] ..." },
};
// TypeScript errors if any CaseStatus key is missing from the Record
```

## Utility Types in SisFraude

```typescript
// keyof — typed update function (FilterBar.tsx)
const update = (key: keyof FilterState, value: string | number) =>
  onFilterChange({ ...filters, [key]: value });

// Record — exhaustive status-to-class mapping
const statusConfig: Record<CaseStatus, { class: string }> = { ... };

// React.ElementType — icon prop pattern (Dashboard.tsx)
const StatCard = ({ icon: Icon, label, value, accent }: {
  icon: React.ElementType;
  label: string;
  value: number;
  accent?: string;
}) => <Icon className="w-4 h-4" />;
```

## Interface vs Type

```typescript
// Use `interface` for object shapes that describe entities
export interface FraudCase {
  id: string;
  cpf: string;
  status: CaseStatus;        // references union type
  businessLine: BusinessLine;
  evidences: Evidence[];     // array of another interface
  riskScore: number;
}

// Use `type` for union aliases and computed types
export type CaseStatus = "Novo" | "Em Análise" | "Confirmado" | "Falso Positivo";
export type ActiveTab = "details" | "evidence" | "history"; // local to CaseDetail
```

## Type Guard Pattern

```typescript
// Inline type narrowing with `as const` literal
const isHighRisk = (score: number): boolean => score >= 80;

// Exhaustive tab key union (CaseDetail.tsx)
const [activeTab, setActiveTab] = useState<"details" | "evidence" | "history">("details");

// tabs array with `as const` key type
const tabs = [
  { key: "details" as const, label: "Detalhes", icon: FileText },
  { key: "evidence" as const, label: "Evidências", icon: AlertTriangle },
  { key: "history" as const, label: "Histórico", icon: Clock },
];
```

## Quick Reference

| Pattern | Example | File |
|---------|---------|------|
| `Record<Union, V>` | `Record<CaseStatus, {class: string}>` | `StatusBadge.tsx` |
| `keyof T` | `key: keyof FilterState` | `FilterBar.tsx` |
| `React.ElementType` | `icon: React.ElementType` | `Dashboard.tsx` |
| Discriminated union | `CaseStatus = "Novo" \| ...` | `types/fraud.ts` |
| `useState<T>` | `useState<CaseStatus>(...)` | `CaseDetail.tsx` |

## Common Mistakes

### Wrong

```typescript
// Re-declaring types that already exist in types/fraud.ts
type MyStatus = "Novo" | "Em Análise"; // duplicate
interface LocalCase { id: string; status: MyStatus } // should use FraudCase
```

### Correct

```typescript
import type { FraudCase, CaseStatus } from "@/types/fraud";
// Use the centralized types everywhere
```

## Related

- [concepts/shadcn-ui.md](shadcn-ui.md) — Record pattern used for variant mappings
- [patterns/icon-usage.md](../patterns/icon-usage.md) — React.ElementType in practice
