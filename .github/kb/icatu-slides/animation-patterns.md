# Animações — Icatu Slides

> Mesma filosofia de easing do AIDE (`cubic-bezier(0.16,1,0.3,1)`), com **cores da marca Icatu**.

## Shimmer em título

Use **Azul #02** e **Verde #01** no gradiente (não usar gold AIDE):

```css
@keyframes shimmer-icatu {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}
.shimmer-icatu {
  background: linear-gradient(135deg, var(--icatu-azul-02) 0%, #fff 35%, var(--icatu-verde-01) 65%, var(--icatu-azul-02) 100%);
  background-size: 280% 280%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: shimmer-icatu 7s ease infinite;
}
```

## Pulse (acento institucional)

```css
@keyframes pulse-icatu {
  0%, 100% { box-shadow: 0 0 14px rgba(106, 162, 185, 0.2); }
  50% { box-shadow: 0 0 26px rgba(95, 187, 72, 0.35); }
}
```

## Reveal escalonado

Reutilize as regras `.slide .reveal` de [../aide-slides/slide-engine.md](../aide-slides/slide-engine.md#reveal-animation-system).
