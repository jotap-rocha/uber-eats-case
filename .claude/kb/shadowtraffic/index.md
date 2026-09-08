# ShadowTraffic KB

> **Purpose**: Apoiar decisões de agentes sobre o gerador de dados sintéticos ShadowTraffic (`gen/unified/uber-eats.json.template`) — semântica real dos `_gen`, limites conhecidos e incidentes já vividos neste projeto.
> **MCP Validated**: 2026-09-07 (WebFetch/WebSearch em docs.shadowtraffic.io + shadowtraffic.io/pricing.html + código/artefatos deste repo)

Base de conhecimento específica do ShadowTraffic **como usado neste repositório** (Postgres + Oracle + MinIO/S3 num único config unificado). Não substitui a doc oficial (https://docs.shadowtraffic.io/) — complementa com o que a doc não deixa óbvio e com incidentes reais já corrigidos aqui.

## Objetivo

- Impedir que um agente repita bugs já corrigidos (ex.: nome de campo ≠ nome de coluna real).
- Deixar explícito o que o mecanismo de `lookup` garante e o que **não** garante (referências cruzadas, múltiplas chamadas).
- Registrar a discrepância entre `docs/shadowtraffic/README.md` (howto humano, parcialmente desatualizado) e o `.env.template` real.

## Navegação

| Seção | Arquivo | Uso |
|---|---|---|
| Quick reference | `quick-reference.md` | Consulta rápida (funções, connections, env, comandos) |
| Conceitos fundamentais | `concepts/conceitos-fundamentais.md` | O que é ShadowTraffic, `_gen`, generators, connections |
| Semântica de `lookup` | `concepts/lookup-semantica-e-limites.md` | Garantias reais, estratégias, limite de chamadas múltiplas |
| Mutação real (fork+stateMachine) | `concepts/mutacao-real-fork-statemachine.md` | Como o projeto gera UPDATE real capturado por CDC |
| Licenciamento e `.env` | `concepts/licenciamento-e-env.md` | Variáveis reais vs. README desatualizado |
| Evitar lookup circular/múltiplo | `patterns/evitar-lookup-circular-e-multiplo.md` | Padrão `vars`+`var`+`path` para campos correlacionados |
| Campo = coluna real (SQL) | `patterns/nome-de-campo-igual-a-coluna-real.md` | Classe de bug já ocorrida 2x no Oracle |
| Restart seguro (`startingFrom`) | `patterns/restart-seguro-startingFrom.md` | Colisão de PK ao religar o gerador com dado pré-existente — trava o pipeline inteiro |
| Conexões SQL e object storage | `patterns/conexoes-sql-e-object-storage.md` | Config de `oracle`, `postgres`, `s3`/MinIO |
| Mapa de geradores atual | `specs/generator-targets-uber-eats.yaml` | Tabela machine-readable dos 17 geradores do config unificado |

## Fontes de verdade

- `scripts/toggle-shadowtraffic.ps1` — liga/desliga `gen-unified` manualmente sem colidir PK (ver `patterns/restart-seguro-startingFrom.md`)
- `gen/unified/uber-eats.json.template` — config real (17 geradores, 3 connections)
- `gen/.env.template` — variáveis de ambiente reais (licença, credenciais)
- `docs/shadowtraffic/README.md` — howto operacional humano (start/stop, troubleshooting) — **não** é fonte de decisão de agente, ver `concepts/licenciamento-e-env.md`
- `.claude/sdd/archive/INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC/DESIGN_...md` — ADRs sobre limites reais do `lookup` (Onda 1)
- `.claude/sdd/reports/BUILD_REPORT_DIVERSIFICACAO_FONTES_UBEREATS_ETAPA{1,2,3}.md` — incidentes reais de migração para Oracle com mutação (Onda 3)
- https://docs.shadowtraffic.io/ (overview, functions/lookup, functions/stateMachine, functions/var, connections/s3, connections/oracle, cheatsheet)

## Como agentes devem usar esta KB

Antes de **criar ou editar** qualquer generator em `gen/unified/uber-eats.json.template`: ler `concepts/lookup-semantica-e-limites.md` e `patterns/nome-de-campo-igual-a-coluna-real.md`. Ambos documentam classes de erro que já quebraram o pipeline em produção local (ver Etapa 3).
