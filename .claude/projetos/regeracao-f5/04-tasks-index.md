# 04 — Índice de tasks

Arquivos em [tasks/regeracao-f5/](../../../tasks/regeracao-f5/). Ordem de implementação = numeração.

## Feitas (retroativas, registradas em 2026-11-10)

| # | Task | Commit | Prova |
|---|---|---|---|
| 01 | Parâmetros, cidades e cálculo de dinheiro | `0ab4d66` | evidence-gate verde, em `entregas.jsonl` |
| 02 | Init dos bancos a partir do DDL aprovado | `25822d7` | waiver aprovado em 2026-11-10, em `entregas.jsonl` |
| 03 | Consultas de invariante e gate de verificação | `136d2a2` | waiver aprovado em 2026-11-10, em `entregas.jsonl` |
| 04 | Seeds de cidades, catálogo e perfis | `8a7e42a` | evidence-gate verde, em `entregas.jsonl` |
| 05 | Template do ShadowTraffic e compose da F5.2 | `8b28567` | evidence-gate verde, em `entregas.jsonl` |
| 06 | Simulador: fundação | `e8c8508` | evidence-gate verde, em `entregas.jsonl` |
| 07 | Simulador: regras de estado, prazos e reembolsos | `f2cc486` | evidence-gate verde, em `entregas.jsonl` |
| 08 | Simulador: cache de referência e escritas comuns | `c80c3f1` | evidence-gate verde, em `entregas.jsonl` |
| 09 | Simulador: compra, ciclo, frota e pós-entrega | `81ef6f6` | waiver aprovado em 2026-11-10, em `entregas.jsonl` |
| 10 | Simulador: opção `--days` e script de execução | `82f107d` | evidence-gate verde, em `entregas.jsonl` |
| 13 | Corrigir o início do histórico (`--days` ignorado) | `82f107d` | evidence-gate verde, revisor aprovado com ressalvas tratadas |
| 14 | Limpar a operação e refazer o restock em 2025-11-10 | sem commit | feita em 2026-11-10; gate do banco 47/47; waiver aprovado em 2026-11-10 (operação destrutiva rodada pelo usuário), em `entregas.jsonl` |
| 11 | Regeração F5.3: passos 0 a 3 e 6 a 8 | sem commit | waiver aprovado em 2026-11-10, em `entregas.jsonl` |
| 12 | ADR 013: snapshot inicial aceito | `fc12aec` | waiver aprovado em 2026-11-10, em `entregas.jsonl` |

## A fazer (quebra aprovada em 2026-11-10; a 15 está em execução pelo usuário)

| # | Task | Bloqueada por |
|---|---|---|
| 15 | Histórico de 1 ano de operação simulada (o usuário roda) | 14 |
| 16 | Gate do banco depois do histórico | 15 |
| 17 | Conectores Debezium e snapshot inicial (ADR 013) | 16 |
| 18 | Simulador em tempo real e gate do CDC | 17 |
| 19 | Airbyte: fonte MongoDB por change stream | 18 |
| 20 | Operação contínua e skill de operação do simulador | 19 |

## Depois (projetos próprios)

Refazer o `shared/pipeline/` (Bronze, Silver, Gold) no modelo novo e a Fase 1 (Azure).
