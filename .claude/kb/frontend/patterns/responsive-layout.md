# Responsive Layout Pattern

> **Purpose**: Grid and flex layout patterns used across SisFraude pages
> **MCP Validated:** 2026-04-20

## When to Use

- Building a new page or section that must work on mobile and desktop
- Adding a grid of cards (stats, filters, case list)
- Implementing a sticky header with flex space-between layout
- Hiding or showing elements based on screen size

## Implementation

SisFraude follows a mobile-first approach. All layouts start with the narrowest viewport and expand at `sm:` (640px) and `lg:` (1024px).

```tsx
// Page shell — max-width container with responsive padding
<div className="min-h-screen bg-background">
  {/* Sticky header */}
  <header className="border-b border-border/50 bg-card/50 backdrop-blur-sm sticky top-0 z-40">
    <div className="max-w-[1600px] mx-auto px-4 sm:px-6 h-14 flex items-center justify-between">
      {/* Left: logo + context */}
      <div className="flex items-center gap-3">
        <FraudeDetectLogo size={22} />
        <span className="font-bold text-foreground tracking-tight">SisFraude</span>
        {/* Hidden on mobile, shown sm+ */}
        <span className="hidden sm:inline-flex items-center gap-1 ml-2 px-2 py-0.5 rounded bg-secondary">
          Context info
        </span>
      </div>
      {/* Right: user + actions */}
      <div className="flex items-center gap-3">
        <span className="text-sm text-muted-foreground hidden sm:block">Username</span>
        <Button variant="ghost" size="sm">Action</Button>
      </div>
    </div>
  </header>

  {/* Main content */}
  <main className="max-w-[1600px] mx-auto px-4 sm:px-6 py-6 space-y-6">

    {/* Stats row: 2-col mobile → 4-col sm+ */}
    <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
      {stats.map(s => <StatCard key={s.label} {...s} />)}
    </div>

    {/* Filter grid: 1→2→4 columns */}
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      {filters.map(f => <FilterField key={f.key} {...f} />)}
    </div>

    {/* Full-width table/list section */}
    <div>
      <h2 className="text-sm font-semibold text-foreground mb-3">Results</h2>
      <CaseTable cases={cases} onSelectCase={setSelectedCase} />
    </div>

  </main>
</div>
```

## Glass Card Usage

The `glass-card` utility is the standard container for all raised surfaces:

```tsx
// Stats card
<div className="glass-card p-4 flex items-center gap-3">
  <div className="w-9 h-9 rounded-lg flex items-center justify-center bg-primary/10">
    <Icon className="w-4 h-4 text-primary" />
  </div>
  <div>
    <p className="text-2xl font-bold text-foreground">{value}</p>
    <p className="text-xs text-muted-foreground">{label}</p>
  </div>
</div>

// Filter container
<div className="glass-card p-5 space-y-4">
  ...content...
</div>

// Modal panel (+ entry animation)
<div className="glass-card animate-slide-in w-full max-w-3xl mx-4">
  ...modal content...
</div>
```

## Modal Overlay Pattern

```tsx
// Fixed overlay + centered scrollable content
<div className="fixed inset-0 z-50 bg-background/80 backdrop-blur-sm flex items-start justify-center pt-8 overflow-y-auto">
  <div className="w-full max-w-3xl mx-4 mb-8 glass-card animate-slide-in">
    ...
  </div>
</div>
```

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| Max page width | `max-w-[1600px]` | Prevents ultra-wide stretch |
| Page padding | `px-4 sm:px-6` | 16px mobile, 24px desktop |
| Section spacing | `space-y-6` | 24px between major sections |
| Stats gap | `gap-3` | 12px between stat cards |
| Filter gap | `gap-4` | 16px between filter fields |

## Example Usage

```tsx
// New page following the SisFraude layout pattern
const ReportPage = () => (
  <div className="min-h-screen bg-background">
    <header className="sticky top-0 z-40 border-b border-border/50 bg-card/50 backdrop-blur-sm">
      <div className="max-w-[1600px] mx-auto px-4 sm:px-6 h-14 flex items-center justify-between">
        <h1 className="font-bold text-foreground">Relatórios</h1>
      </div>
    </header>
    <main className="max-w-[1600px] mx-auto px-4 sm:px-6 py-6 space-y-6">
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Content */}
      </div>
    </main>
  </div>
);
```

## See Also

- [concepts/tailwind-composition.md](../concepts/tailwind-composition.md) — cn() and custom utilities
- [patterns/icon-usage.md](icon-usage.md) — icon sizing within layout
