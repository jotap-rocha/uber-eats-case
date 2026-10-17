---
domain: gcp-gcs
topic: lake-layout
---

# Layout de zonas do lake

## Bucket por zona (recomendado) vs prefixo por zona

| Opção | Prós | Contras |
|---|---|---|
| **Bucket por zona** (`<BUCKET>-raw`, `-curated`, `-ref`, `-tmp`) | IAM, lifecycle, classe e soft delete por zona; menor raio de erro | Mais buckets para gerenciar |
| Prefixo por zona num bucket | Simples | IAM é por bucket (IAM Conditions por prefixo é possível, mas frágil); lifecycle via `matchesPrefix` |

Padrão do canônico: **bucket por zona**, mesma região.

## Zonas

| Zona | Conteúdo | Escritor | Leitores | Lifecycle |
|---|---|---|---|---|
| `raw` | Cópia fiel da fonte (JSON/CSV/Avro do Kafka Connect, extrações) | Connect, ingestão | Processamento | Delete 30–90 dias |
| `curated` | Parquet tipado, deduplicado, particionado | Dataflow/Spark | BigQuery load, BigLake | Sem delete; Nearline após N dias se pouco lido |
| `ref` | Reference data (tabelas pequenas para enriquecimento) | Processo de publicação | Dataflow side input | Manter versões recentes |
| `tmp` | `staging`/`temp` do Dataflow, scratch | Jobs | Jobs | Delete 1–7 dias |

## Convenção de caminho

```
<zona>/<fonte|dominio>/<entidade>/dt=YYYY-MM-DD/[hr=HH/]<arquivo>.<ext>
```

- Particionamento estilo Hive (`dt=`) é reconhecido por BigQuery (external/`LOAD DATA`
  com partition columns) e por Spark.
- Nomes de objeto **sem PII** (sem CPF/e-mail no caminho).
- Arquivos de 100 MB–1 GB em `curated`; evite milhões de arquivos de KB (custo de operação e
  lentidão de listagem).

## Namespace hierárquico (HNS) — opcional

- GCS é namespace plano por padrão ("pastas" são prefixos). Buckets com **hierarchical
  namespace** têm pastas reais e **rename atômico de pasta** — análogo ao HNS do ADLS Gen2.
- Útil para motores que fazem commit por rename (Spark/Hadoop). Definido **na criação** do
  bucket e exige UBLA.
- Compatibilidade com cada ferramenta e custo: **a validar** antes de adotar.

## Região e classe

- **Mesma região** de BigQuery dataset, Kafka cluster e Dataflow → sem egress e com
  compatibilidade de localização no `LOAD`.
- Free tier de storage só vale em `us-central1`/`us-east1`/`us-west1`.
- `Standard` para tudo que é lido com frequência; classes frias têm **mínimo de retenção**
  (30/90/365 dias) e taxa de leitura — não use em `raw`/`tmp`.

## Terraform (uma zona)

```hcl
resource "google_storage_bucket" "raw" {
  name                        = "<BUCKET>-raw"
  location                    = var.region
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
  force_destroy               = true            # lab apenas
  soft_delete_policy { retention_duration_seconds = 0 }   # lab apenas
  lifecycle_rule {
    condition { age = 30 }
    action    { type = "Delete" }
  }
  labels = { env = "lab", zona = "raw" }
}
```
