---
domain: gcp-bigquery
topic: cost-model
---

# Modelo de custo: on-demand vs editions

BigQuery separa **compute** (query) de **storage**. Não há cluster ligado: sem query, não há
custo de compute em on-demand. É o oposto do Synapse Dedicated Pool (pausar para economizar).

## Compute

| Modelo | Cobra por | Bom para |
|---|---|---|
| **On-demand** (default) | TiB processado (~US$ 6,25/TiB em US, **a validar**); 1 TiB/mês grátis | Lab, volumes pequenos/irregulares |
| **Editions** (Standard / Enterprise / Enterprise Plus) | slot-hora com autoscaling (baseline pode ser 0) + commitments opcionais | Carga previsível, teto de custo por slots |

- Editions só cobram se houver **reserva** criada e atribuída. Reserva esquecida = custo
  contínuo. Em lab, não crie reservas.
- Storage Write API e batch load têm regras próprias: batch load do GCS é grátis no pool
  compartilhado; streaming (Storage Write API / legacy streaming) cobra por volume.

## Storage

- Lógico ativo / long-term (90 dias sem modificação → ~metade do preço).
- Free tier: 10 GiB/mês.

## Free tier, trial e sandbox

| Programa | O que dá | Limites relevantes |
|---|---|---|
| Free Tier (sempre) | 1 TiB query + 10 GiB storage /mês | Por billing account |
| Free Trial | US$ 300 em 90 dias | Conta nova; trial fecha ao fim |
| Sandbox | Sem cartão/billing | Expira tabelas em 60 dias; **sem DML, sem streaming, sem Data Transfer** |

Consequência: o pattern `merge-scd2` **não roda no sandbox** — precisa de projeto com billing
(trial serve).

## Guardrails

1. **Dry-run** (`--dry_run`) mostra bytes antes de executar.
2. **`maximum_bytes_billed`** na query/job: falha em vez de cobrar acima do teto.
3. **Quota custom** "Query usage per day" (por projeto e por usuário) no console de quotas.
4. **`require_partition_filter`** nas tabelas grandes.
5. Selecionar colunas — formato colunar cobra só o que é lido; `SELECT *` lê tudo.
6. `LIMIT` **não** reduz bytes lidos em tabela não clusterizada.
7. Labels nos jobs (`--label=env:lab`) para atribuir custo no billing export.

## Observabilidade de custo

```sql
SELECT user_email, SUM(total_bytes_billed)/POW(1024,4) AS tib
FROM `region-<REGION>`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
WHERE creation_time > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 DAY)
GROUP BY user_email ORDER BY tib DESC;
```

Valores de preço mudam por região e ao longo do tempo: conferir
`cloud.google.com/bigquery/pricing` antes de orçar.
