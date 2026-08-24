# Icon Usage Pattern

> **Purpose**: lucide-react icon patterns including React.ElementType prop type for SisFraude
> **MCP Validated:** 2026-04-20

## When to Use

- Adding icons to buttons, labels, tabs, or badges
- Passing an icon as a prop to a component (StatCard, nav items)
- Sizing icons consistently with the surrounding text
- Building icon+text rows with proper alignment

## Implementation

```tsx
// Standard lucide-react import — named exports
import { Search, RotateCcw, LogOut, Building2, AlertTriangle,
         CheckCircle, Clock, XCircle, X, FileText } from "lucide-react";

// Direct usage — className controls size and color
<Search className="w-4 h-4 text-primary" />
<RotateCcw className="w-3 h-3 mr-1" />
<X className="w-5 h-5" />

// Icon + text row (standard alignment pattern)
<div className="flex items-center gap-2">
  <Search className="w-4 h-4 text-primary" />
  <span>Filtros de Busca</span>
</div>

// Icon in Button (left-aligned with text)
<Button>
  <Search className="w-4 h-4 mr-2" /> Buscar Casos
</Button>
```

## React.ElementType — Icon as Prop

Use `React.ElementType` when passing a lucide icon (or any component constructor) as a prop:

```tsx
// Dashboard.tsx — StatCard with icon prop
const StatCard = ({
  icon: Icon,       // rename destructuring: `icon` prop used as `Icon` JSX tag
  label,
  value,
  accent,
}: {
  icon: React.ElementType;
  label: string;
  value: number;
  accent?: string;
}) => (
  <div className="glass-card p-4 flex items-center gap-3">
    <div className={cn(
      "w-9 h-9 rounded-lg flex items-center justify-center",
      accent === "destructive" ? "bg-destructive/10" :
      accent === "primary"     ? "bg-primary/10"     : "bg-secondary"
    )}>
      <Icon className={cn(
        "w-4 h-4",
        accent === "destructive" ? "text-destructive" :
        accent === "primary"     ? "text-primary"     : "text-muted-foreground"
      )} />
    </div>
    <div>
      <p className="text-2xl font-bold text-foreground">{value}</p>
      <p className="text-xs text-muted-foreground">{label}</p>
    </div>
  </div>
);

// Call site — pass the icon class directly (no JSX, no angle brackets)
<StatCard icon={AlertTriangle} label="Total de Casos" value={stats.total} />
<StatCard icon={Clock}         label="Novos"          value={stats.new} accent="primary" />
<StatCard icon={XCircle}       label="Alto Risco"     value={stats.highRisk} accent="destructive" />
```

## Tab Icon Pattern

```tsx
// CaseDetail.tsx — tabs with icons
const tabs = [
  { key: "details"  as const, label: "Detalhes",   icon: FileText },
  { key: "evidence" as const, label: "Evidências",  icon: AlertTriangle },
  { key: "history"  as const, label: "Histórico",   icon: Clock },
];

{tabs.map((t) => (
  <button
    key={t.key}
    onClick={() => setActiveTab(t.key)}
    className={cn(
      "flex items-center gap-2 px-5 py-3 text-sm font-medium transition-colors border-b-2",
      activeTab === t.key
        ? "border-primary text-primary"
        : "border-transparent text-muted-foreground hover:text-foreground"
    )}
  >
    <t.icon className="w-4 h-4" />
    {t.label}
  </button>
))}
```

## Configuration

| Size class | px | Use case |
|------------|----|---------|
| `w-3 h-3` | 12px | Inline in badges, micro-labels |
| `w-4 h-4` | 16px | Standard button/tab icon |
| `w-5 h-5` | 20px | Close buttons, prominent actions |
| `w-9 h-9` | 36px | Stat card icon container |

## Example Usage

```tsx
// New nav item with icon
import { BarChart2 } from "lucide-react";

const NavItem = ({ icon: Icon, label }: { icon: React.ElementType; label: string }) => (
  <button className="flex items-center gap-2 text-sm text-muted-foreground hover:text-foreground">
    <Icon className="w-4 h-4" />
    {label}
  </button>
);

<NavItem icon={BarChart2} label="Relatórios" />
```

## See Also

- [concepts/typescript-patterns.md](../concepts/typescript-patterns.md) — React.ElementType definition
- [patterns/responsive-layout.md](responsive-layout.md) — StatCard usage in page layout
