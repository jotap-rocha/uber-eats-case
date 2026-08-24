# Biblioteca de componentes — Icatu Slides

> Padrões reutilizáveis (CSS) usando **tokens Icatu**. Baseado no estilo dos componentes AIDE, com paleta substituída.

## Tags (pills)

```css
.tag {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 600;
  padding: 0.22rem 0.65rem;
  border-radius: 6px;
  letter-spacing: 0.05em;
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
}
.tag-azul   { background: var(--accent-dim); color: var(--icatu-azul-02); }
.tag-verde { background: var(--verde-dim); color: var(--icatu-verde-01); }
.tag-neutro { background: rgba(213, 219, 230, 0.12); color: var(--icatu-azul-03); }
.tag-cinza { background: rgba(147, 149, 152, 0.15); color: var(--icatu-cinza-01); }
```

## Cartão de métrica (KPI)

```css
.stat-card {
  background: rgba(27, 49, 87, 0.65);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: clamp(16px, 2.5vh, 28px);
}
.stat-card::before {
  content: '';
  display: block;
  height: 3px;
  border-radius: 14px 14px 0 0;
  margin: -16px -16px 12px -16px;
  background: linear-gradient(90deg, var(--icatu-azul-02), var(--icatu-verde-01));
}
.stat-val { font-size: clamp(32px, 5vw, 56px); font-weight: 900; color: var(--text); }
.stat-lbl { font-size: 0.72rem; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.08em; }
```

## Barra inferior (contexto)

Mesmo padrão “editorial + tags” do AIDE, com cores Icatu:

```html
<div class="icatu-foot" style="margin-top:auto;padding-top:clamp(12px,2vh,20px);border-top:1px solid var(--border);display:flex;gap:1rem;align-items:center;justify-content:space-between;">
  <p class="icatu-body" style="margin:0;color:var(--text-dim);flex:1;">
    Texto de fechamento com <strong style="color:var(--icatu-azul-02);">destaque institucional</strong>.
  </p>
  <div style="display:flex;gap:0.4rem;flex-shrink:0;">
    <span class="tag tag-azul">Etapa</span>
    <span class="tag tag-verde">Status</span>
  </div>
</div>
```

## Lista numerada (trilha)

```css
.icatu-stepnum {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 2.2rem;
  height: 2.2rem;
  border-radius: 50%;
  font-weight: 800;
  color: var(--icatu-azul-01);
  background: var(--icatu-azul-03);
  border: 2px solid var(--icatu-azul-02);
}
```

## Tabela densa

Cabeçalho com `background: var(--icatu-azul-02)` e texto `#1B3157`, linhas zebradas `rgba(213,219,230,0.06)`.
