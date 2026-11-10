# Corrigir o início do histórico (--days ignorado)

**Status:** done (aguarda commit)  
**Blocked by:** tasks/regeracao-f5/12-adr-013-snapshot-inicial.md

## What to build

Hoje o simulador "retoma" de qualquer evento já gravado, inclusive o restock inicial do seed de catálogo, e por isso
ignora `--days`: o `-Days 365` rodou como 30 dias (início em 2026-10-11, não em 2025-11-10). A correção faz o
simulador só retomar quando já existem pedidos, e recusa começar um histórico anterior ao restock inicial dos itens
de estoque (que daria saldo negativo e violaria T6).

Bug achado em 2026-11-10 ao acompanhar a execução do histórico (task 15 em rascunho). Vira teste de regressão.

## Acceptance criteria

- [x] `ac1` Sem pedidos no banco, o início vem de `--days` (ou de `clock.backfill_days`), mesmo que existam movimentos de estoque do seed.
- [x] `ac2` Com pedidos no banco, o simulador retoma do último evento gravado (comportamento atual preservado).
- [x] `ac3` Sem pedidos e com restock inicial **posterior** ao início do histórico, o CLI recusa com mensagem que manda refazer o seed com `--start-day`; com restock anterior ou igual ao início, segue.
- [x] `ac4` `ruff`, `mypy simulator` e `pytest` em `shared/gen` passam; `revisor-codigo` sem bloqueante.
- [x] `ac5` Sem pedidos mas com eventos além do restock inicial (execução que parou antes do 1º pedido), o CLI recusa com mensagem que manda limpar a operação (task 14).
- [x] `ac6` `--days` só aceita inteiro >= 1; com pedidos no banco o CLI avisa que `--days` foi ignorado.

Achados do `revisor-codigo` tratados nesta task: operação parcial sem pedidos (ac5), comparação do restock por dia
e mensagem do erro, validação do `--days` (ac6), e no `scripts/simulator/run-simulator.ps1`: propagação do código
de saída, stderr do Python no PowerShell 5.1, log em UTF-8 e `-Status` sem exigir os sais.

## Evidência

Teste de regressão em `shared/gen/tests/test_default_start.py` e o gate de `/validar` (seção "Neste projeto").
