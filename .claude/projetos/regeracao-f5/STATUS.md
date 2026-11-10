# STATUS — regeracao-f5

**Projeto:** regeração dos dados do uber-eats-case (F5.2 e F5.3 do modelo físico)  
**Tipo:** pipeline-local (fontes locais, CDC e simulador de operação)  
**Fase atual:** 5 — build (`harness-build`, task a task)  
**Adoção do harness:** 2026-11-10, retroativa. O trabalho anterior (regras, modelagem, F5.2) foi conduzido
pelo HANDOFF e pelos ADRs, antes de o projeto entrar no fluxo.

## SI assessment

Todo dado é sintético (ShadowTraffic e simulador). Sem PII real e sem `[AVISO_LGPD]`. Os bancos
locais são tratados como produção (nunca `DROP`, `TRUNCATE`, `down -v` sem confirmação). Detalhes
nos invariantes do `CLAUDE.md`.

## Checklist de fases

| Fase | Artefato | Estado |
|---|---|---|
| 0 | [00-ideia.md](00-ideia.md) | ok (aponta para CONTEXT e roadmap) |
| 1 | [01-grill.md](01-grill.md) | ok (aponta para o grill de 2026-10-17 e a revisão adversarial) |
| 2 | [02-prd.md](02-prd.md) | ok (os modelos conceitual, lógico e físico fazem o papel de PRD) |
| 3 | [03-harness.md](03-harness.md) | ok (invariantes do `CLAUDE.md` e rules) |
| 4 | [04-tasks-index.md](04-tasks-index.md) | ok; tasks 15 a 20 aprovadas em 2026-11-10 |
| 5 | build | em andamento: 14 tasks feitas, 6 por fazer |
| 6 | 05-retro.md | ao fim (`harness-ship`) |

## Tasks

Detalhe em [04-tasks-index.md](04-tasks-index.md). Resumo: 1 a 12 feitas (retroativas, ver nota), 13 e 14 feitas,
15 a 20 a fazer. A task 15 (histórico de 1 ano) está sendo rodada pelo usuário.

## Nota sobre as métricas retroativas

As tasks 1 a 12 foram registradas depois de prontas. Para elas, o gate foi **reexecutado em
2026-11-10** e a evidência é real, mas o número de tentativas até o verde, o veredito do revisor e as
intervenções humanas não foram medidos na época e ficam `null` / `nao_revisado`. O `/scorecard` não
deve tratar esses campos como dado.
