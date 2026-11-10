# Limpar a operação gerada e refazer o restock inicial

**Status:** done  
**Blocked by:** tasks/regeracao-f5/13-corrigir-inicio-do-historico.md

## What to build

Voltar o Postgres ao estado "carga pronta, sem operação" com o restock inicial em **2025-11-10 00:00** (hoje menos
365 dias), para o histórico de 1 ano começar certo. Preserva `cities`, `restaurants`, `products`, `stock_items` e
`product_recipes`; esvazia as 22 tabelas de operação do simulador (com `RESTART IDENTITY`), zera
`stock_items.quantity_on_hand` e refaz o restock com `python -m simulator.seed catalog --start-day 2025-11-10`.
Oracle e Mongo não são tocados (o simulador só lê neles). Dado sintético, mas o `CLAUDE.md` manda confirmar cada
`TRUNCATE`.

## Acceptance criteria

- [x] `ac1` As 22 tabelas de operação com 0 linha e `cities`, `restaurants`, `products`, `stock_items` e `product_recipes` com as contagens anteriores (5, 250, 2.850, 3.870 e 5.091).
- [x] `ac2` Um movimento `restock` por item de estoque, todos em 2025-11-10 00:00, e `quantity_on_hand` igual ao restock.
- [x] `ac3` `python -m simulator.gate` com 47 de 47 e 0 linha.
