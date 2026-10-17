---
domain: gcp-dataflow
topic: streaming-jobs-and-cost
---

# Jobs streaming, workers e custo

## Modelo

- Um **job** = pipeline Beam executado pelo runner Dataflow numa **região**, com workers
  (VMs Compute gerenciadas) numa subnet.
- **Streaming** (fonte ilimitada: Kafka, Pub/Sub) roda até ser **drenado/cancelado**.
  Batch termina sozinho.
- **Streaming Engine** (default em jobs streaming recentes) move estado/shuffle para o
  backend do Google → workers menores, autoscaling mais rápido.
- **Autoscaling** horizontal por backlog/CPU; limite com `maxNumWorkers`.
- Garantia default **exactly-once**; modo **at-least-once** é mais barato/latência menor
  quando o destino tolera duplicata (BigQuery Storage Write API at-least-once).

## Componentes de custo

| Componente | Unidade | Referência `us-central1` (**a validar**) |
|---|---|---|
| vCPU streaming | vCPU-hora | ~US$ 0,069 |
| Memória | GiB-hora | ~US$ 0,0036 |
| Disco do worker | GB-hora | pequeno (PD por worker) |
| Streaming Engine | Compute Unit-hora (ou dados processados, legado) | ~US$ 0,089 |
| Shuffle (batch) | dados processados | só batch |

Cobrança **por segundo**, enquanto o job estiver ativo. Recursos externos (BigQuery storage/
writes, GCS, Kafka) cobram à parte. Sem free tier do Dataflow.

## Dimensionar o lab

- `--max-workers=1` ou `2`, máquina pequena (`n1-standard-2`/`e2` conforme suporte — **a
  validar** tipos aceitos em streaming), Streaming Engine ligado.
- Um job streaming mínimo **ligado 24 h** ≈ 1 worker × 24 h (vCPU + memória) + SECUs — conta
  na casa de alguns dólares/dia; ligado o mês inteiro, ordem de US$ 100+. Calcular na
  calculadora oficial antes de deixar rodando.

## Parar: drain vs cancel

| | Drain | Cancel |
|---|---|---|
| Aplica a | Só streaming | Batch e streaming |
| Comportamento | Para de ler; processa e grava o que está em buffer; fecha janelas abertas com resultado parcial | Para imediatamente; descarta buffer |
| Perda de dados | Não (no pipeline) | Pode perder in-flight |
| Custo | Continua cobrando até terminar o buffer | Libera recursos o mais rápido possível |
| Comando | `gcloud dataflow jobs drain <JOB_ID>` | `gcloud dataflow jobs cancel <JOB_ID>` |

- **Force cancel** (`--force`) só para job preso em cancel há ≥ 30 min; pode vazar VMs
  (consomem quota, não custo do job).
- Drain não resolve pipeline travado — corrigir código e usar `update`/cancel.
- Fonte Kafka: offsets commitados no grupo de consumidores permitem retomar num novo job.

## Update de job

`--update` (mesmo `job_name`) troca o código mantendo estado, se o grafo for compatível
(`--transform_name_mapping` para renomes). Flex templates suportam update — **a validar**
por template.

## Observabilidade

- Job graph, data freshness, system lag, backlog no console/Cloud Monitoring.
- Alertas: `job/data_watermark_age` e `job/system_lag` altos.
- Logs de worker no Cloud Logging — **sem PII** em `logging.info`.
