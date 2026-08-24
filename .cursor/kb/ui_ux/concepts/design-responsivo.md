# Design responsivo

> **Purpose**: Funcionar bem de notebook a ultrawide; mobile quando aplicável.  
> **Confidence**: 0.92

## Prioridades

1. **Breakpoints conscientes** — Mobile-first ou desktop-first conforme público; SisFraude operação tende a desktop.
2. **Tabelas em telas estreitas** — Cards empilhados, colunas prioritárias, scroll horizontal *com* indicação de corte, ou “detalhe em drawer”.
3. **Touch targets** — Mínimo ~44px onde há toque (mesmo em tablets corporativos).
4. **Overflow explícito** — Evitar textos cortados sem `truncate` + tooltip.

## Layout

- Grids com `minmax` e quebras previsíveis.
- Modais: `max-h` + scroll interno em viewports baixas.

## Testes rápidos

- Zoom do navegador 125–150%.
- Largura ~1280px e ~1920px.
- Teclado apenas (ver [acessibilidade.md](acessibilidade.md)).

## Referências cruzadas

- [tabelas-dados.md](tabelas-dados.md), `.cursor/kb/frontend/patterns/responsive-layout.md`
