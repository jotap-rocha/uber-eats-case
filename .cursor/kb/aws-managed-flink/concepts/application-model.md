---
domain: aws-managed-flink
topic: application-model
---

# Modelo de aplicação do Managed Flink

## Dois modos

| Modo | O que é | Runtime | Uso |
|---|---|---|---|
| **Aplicação** (streaming) | jar Java/Scala ou zip PyFlink no S3, roda continuamente | Flink **1.20** (recomendado) | produção e lab "de verdade" |
| **Studio notebook** | Zeppelin com Flink SQL/Python/Scala interativo | Flink **1.15** apenas | exploração; pode ser "deployado" como aplicação |

Studio é o mais próximo da experiência "escreve SQL e roda" do Stream Analytics, mas
fica preso em 1.15 (aguarda upgrade do interpretador do Zeppelin) e custa +2 KPUs.
Para o harness: **prototipar no Studio é opcional**; o entregável é uma aplicação 1.20.

## APIs dentro da aplicação

| API | Quando |
|---|---|
| **Flink SQL / Table API** | joins, janelas, agregações declarativas — default |
| DataStream API | estado custom, broadcast, timers, lógica imperativa |
| PyFlink | time Python; mesmas APIs, empacota jars de connectors no zip |

Uma aplicação PyFlink/SQL típica: `main.py` executa `CREATE TABLE ...` (fontes/sinks) e
`INSERT INTO sink SELECT ...`. Propriedades (bootstrap, paths) chegam via
`environment_properties` (property groups) — lidas no runtime, não hardcoded.

## KPU e paralelismo

- 1 **KPU** = 1 vCPU + 4 GB de memória + 50 GB de running storage.
- `parallelism` = slots totais; `parallelism_per_kpu` = slots por KPU.
- KPUs cobradas = `ceil(parallelism / parallelism_per_kpu)` **+ 1** de orquestração.
- Autoscaling (`auto_scaling_enabled`) ajusta paralelismo por CPU — desligue em lab para
  custo previsível.

| parallelism | per_kpu | KPU cobradas | US$/h |
|---|---|---|---|
| 1 | 1 | 2 | 0,22 |
| 4 | 2 | 3 | 0,33 |
| 4 | 1 | 5 | 0,55 |

## Ciclo de vida

```
create ──> READY ──start──> STARTING ──> RUNNING ──stop──> STOPPING ──> READY
                                   │                        ▲
                                   └── update (código/config) ┘ (reinicia a partir de snapshot)
```

- Só `RUNNING` consome KPU. `READY` = parada.
- `stop-application` tira snapshot (se habilitado) — o próximo `start` pode restaurar
  estado (`ApplicationRestoreConfiguration`).
- `--force` no stop pula snapshot (perde estado; use só se travou).

## Estado, checkpoints e snapshots

| Mecanismo | Gerenciado por | Para |
|---|---|---|
| Checkpoint | serviço (automático, `DEFAULT`) | recuperação de falha |
| Snapshot | serviço, no stop/update ou manual | upgrade, restart com estado |

Joins com reference data guardam estado (ver `patterns/reference-data.md`) — defina
`table.exec.state.ttl` quando aplicável para não crescer sem limite.

## Observabilidade

- CloudWatch Logs (log group da app) + métricas `AWS/KinesisAnalytics`
  (`KPUs`, `uptime`, `lastCheckpointDuration`, `numRecordsInPerSecond`, `millisBehindLatest`).
- Flink Dashboard acessível pelo console (somente leitura).
- Alarme de `KPUs > N` como guard-rail extra de custo.

## Versões e upgrade

- In-place version upgrade preserva ARN, snapshots, logs e configs.
- Runtimes antigos (1.6/1.8/1.11/1.13) foram ou estão sendo descontinuados — não crie
  aplicações novas neles.
- Flink 2.x no serviço: **a validar** (não confirmado na doc consultada).
