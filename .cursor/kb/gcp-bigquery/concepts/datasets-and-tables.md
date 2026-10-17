---
domain: gcp-bigquery
topic: datasets-and-tables
---

# Datasets, localização e tabelas

## Hierarquia

`projeto → dataset → tabela/view/rotina`. Dataset é a unidade de **localização**, de
**IAM** e de **expiração default**. Equivale ao schema do Synapse.

## Localização

- Definida na criação do dataset e **imutável** (`US`, `EU` multi-região ou região como
  `<REGION>`).
- `LOAD DATA`/`bq load` exige bucket **compatível** com a localização do dataset
  (mesma região, ou bucket regional dentro da multi-região). Erro típico:
  `Cannot read and write in different locations`.
- Regra prática: bucket, dataset, cluster Kafka e job Dataflow na **mesma região**.

## Layout por zona (paridade com o lake)

| Dataset | Conteúdo |
|---|---|
| `raw` | carga 1:1 do GCS, tipos frouxos, append |
| `staging` | limpeza/tipagem, deduplicação, `row_hash` |
| `dw` | dimensões (SCD2) e fatos |

## Tipos de tabela

| Tipo | Quando |
|---|---|
| Nativa (gerenciada) | Padrão. DML completo (`MERGE`, `UPDATE`), time travel |
| Externa / BigLake sobre GCS | Ler o lake sem copiar; DML limitado |
| View / materialized view | Camada semântica; MV para agregados recorrentes |

## Partição e cluster

- **Partição** por coluna `DATE`/`TIMESTAMP` (diária), por tempo de ingestão ou por range
  inteiro. Elimina bytes lidos → custo direto em on-demand.
- `require_partition_filter = TRUE` bloqueia query sem filtro de partição.
- **Cluster** (até 4 colunas) ordena dentro da partição; bom para colunas de filtro/join
  frequentes (`cliente_id`).
- Dimensões pequenas (< ~1 GB) normalmente **não** precisam de partição; cluster pela chave
  de negócio já ajuda o `MERGE`.

## Storage

- Lógico (default) ou físico (comprimido) — escolha por dataset.
- Partição/tabela sem modificação por 90 dias vira **long-term** (preço ~50% menor).
- Time travel (default 7 dias) + fail-safe ocupam storage físico.

## Expiração (labs)

- `default_table_expiration_ms` no dataset ou `expiration_timestamp` na tabela.
- `default_partition_expiration_ms` para descartar partições antigas de `raw`.

## Terraform

```hcl
resource "google_bigquery_dataset" "dw" {
  dataset_id                  = "dw"
  location                    = var.region
  default_table_expiration_ms = 86400000   # lab: 1 dia
  delete_contents_on_destroy  = true       # lab apenas
  labels = { env = "lab" }
}
```
