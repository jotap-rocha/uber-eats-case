# Histórico de 1 ano de operação simulada

**Status:** not started (rascunho a aprovar)  
**Blocked by:** tasks/regeracao-f5/14-limpar-operacao-e-refazer-restock.md

## What to build

Rodar `run-simulator.ps1 -Days 365 -Seed 42` (executado pelo usuário), só histórico, sem conectores.

## Acceptance criteria

- [ ] `ac1` `orders` entre 250 mil e 330 mil e `ultimo_pedido` próximo de agora.
- [ ] `ac2` Log sem `falha em` e sem parada por erro do banco.
