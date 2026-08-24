# Tabelas bem desenhadas (aplicações de dados)

> **Purpose**: Em apps analíticos/operacionais, a tabela é Peça Crítica™.  
> **Confidence**: 0.94

## Checklist de produto

- **Paginação** — Offset ou cursor; sempre indicar página e total aproximado quando possível.
- **Ordenação** — Por colunas relevantes; estado visual claro (↑↓).
- **Filtros** — Globais na barra; por coluna quando útil (popover).
- **Busca** — Texto livre com escopo explícito (“buscar em CPF/nome”).
- **Congelar colunas** — Identidade (ID, CPF mascarado, nome) fixa à esquerda em grids largos.
- **Exportação** — CSV/XLS com nome de arquivo datado; aviso se truncado por limite.
- **Quantidade de registros** — “Mostrando X–Y de Z” ou “Z registros (filtrados)”.
- **Nomes de colunas claros** — Rótulos de negócio; tooltips para siglas.
- **Valores nulos** — Placeholder consistente (`—`, “N/D”), não célula vazia ambígua.
- **Largura** — `minWidth` / truncamento + tooltip para textos longos.

## Densidade e leitura

- Zebrado leve ou `hover` na linha; destaque para outliers (ex.: score alto).
- Não misturar **ações destrutivas** na mesma linha sem affordance clara.

## Performance

Virtualização quando milhares de linhas *sem* paginação server-side.

## Projeto local

- `CaseTable`, Lab PRD: alinhar badges de risco, máscara de CPF e paginação ao mesmo vocabulário visual.

## Referências cruzadas

- [consistencia-design-system.md](consistencia-design-system.md), [empty-states.md](empty-states.md)
