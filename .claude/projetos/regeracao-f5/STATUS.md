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
| 5 | build | **PAUSADO** em 2026-11-20: 16 tasks feitas, 17 a 20 aguardam a revisão das arquiteturas (ver "Pausa") |
| 6 | 05-retro.md | ao fim (`harness-ship`) |

## Tasks

Detalhe em [04-tasks-index.md](04-tasks-index.md). Resumo: 1 a 12 feitas (retroativas, ver nota), 13 e 14 feitas,
15 e 16 feitas em 2026-11-20 (histórico de 1 ano com 400.743 pedidos; gate do banco 47/47), 17 a 20 pausadas.

## Pausa (2026-11-20): retomar aqui

**Não executar as tasks 17 a 20 como estão escritas.** Elas planejam Redpanda, Kafka Connect e conectores Debezium
para o batch, o que a [ADR 014](../../../docs/adr/014-ingestao-batch-pelo-airbyte-e-debezium-so-no-kappa.md) substituiu:
Airbyte no batch de Warehouse e Lakehouse, Debezium e Kafka Connect só no Kappa, registrados na fase dele. A ADR 014
vive na branch `feat/planejamento-conta-azure` e ainda não chegou à `main`; a [ADR 013](../../../docs/adr/013-snapshot-inicial-aceito-na-regeracao.md)
(conectores depois do gate) fica sem objeto para o batch e precisa de nota de revisão ou de uma ADR nova.

Combinado com o usuário:

1. O usuário refina as arquiteturas **Lakehouse** e **Kappa** (o Warehouse já tem grill) na janela do `azure-warehouse` e
   commita lá a ADR 014 e o resto da Azure.
2. Quando terminar, volta a **esta janela** (projeto `regeracao-f5`) para o avanço prático.
3. **Só com o ok explícito dele**, rodar `harness-iterate` para reescrever as tasks 17 a 20 conforme a ADR 014 e
   propor a revisão da ADR 013. Nada disso antes.

Ao retomar: confirmar que a ADR 014 já está na `main`, reler as tasks 17 a 20 e o impacto de cada uma
(17 e 18 dependem de conectores Debezium; 19, Airbyte MongoDB e desativar a conexão antiga do Postgres, passa a ser o
centro; 20 continua com escopo ajustado). Pendência pequena e independente: `shm_size` do `postgres-ubereats`
(o gate só rodou com `max_parallel_workers_per_gather=0` por causa dos 64 MB de `/dev/shm`).

## Nota sobre as métricas retroativas

As tasks 1 a 12 foram registradas depois de prontas. Para elas, o gate foi **reexecutado em
2026-11-10** e a evidência é real, mas o número de tentativas até o verde, o veredito do revisor e as
intervenções humanas não foram medidos na época e ficam `null` / `nao_revisado`. O `/scorecard` não
deve tratar esses campos como dado.
