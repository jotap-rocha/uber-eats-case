# Visuais avançados — Icatu Slides

> Diagramas, fluxos e camadas visuais complexas — **sempre** com tokens [icatu-palette.md](icatu-palette.md).

## Princípios

1. **SVG** para arquiteturas e pipelines (como no PDF de trilha: etapas numeradas e setas).
2. Nós: preenchimento `var(--icatu-azul-01)` ou `rgba(27,49,87,0.85)` com borda `2px solid var(--icatu-azul-02)`.
3. Setas / conectores: `stroke: var(--icatu-azul-02)` com `opacity` 0.5–0.9.
4. Destaque de etapa atual: anel `stroke: var(--icatu-verde-01)` ou `animation: pulse-icatu` de [animation-patterns.md](animation-patterns.md).

## Glassmorphism discreto

```css
.icatu-glass {
  background: linear-gradient(135deg, rgba(27,49,87,0.82), rgba(106,162,185,0.08));
  border: 1px solid var(--border-bright);
  border-radius: 16px;
  backdrop-filter: blur(10px);
}
```

Evite blur excessivo que prejudique leitura em projetores.

## Referência cruzada

Para padrões adicionais (fitas, orbitais, etc.), consulte [../aide-slides/advanced-visuals.md](../aide-slides/advanced-visuals.md) e **substitua** todas as referências a `--accent` / `--gold` por tokens `--icatu-*`.
