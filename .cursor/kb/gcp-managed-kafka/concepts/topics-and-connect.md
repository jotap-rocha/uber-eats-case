---
domain: gcp-managed-kafka
topic: topics-and-connect
---

# Tópicos (inclusive compactados) e Connect clusters

## Tópicos

- Criados via `gcloud managed-kafka topics create`, Terraform (`google_managed_kafka_topic`)
  ou Admin API do Kafka (cliente com permissão).
- `replication_factor = 3` (cluster em 3 zonas). `partition_count` aumenta, nunca diminui.
- Configs Kafka padrão via `--configs` / `configs = {}`.

## Tópico compactado

Mantém **a última mensagem por chave** — ideal para estado/CDC/reference data.

```hcl
resource "google_managed_kafka_topic" "clientes_estado" {
  topic_id           = "clientes-estado"
  cluster            = google_managed_kafka_cluster.lab.cluster_id
  location           = var.region
  partition_count    = 3
  replication_factor = 3
  configs = {
    "cleanup.policy"            = "compact"
    "min.compaction.lag.ms"     = "60000"
    "delete.retention.ms"       = "86400000"   # tombstones
  }
}
```

Regras: toda mensagem **precisa de chave**; tombstone (`value = null`) apaga a chave após
`delete.retention.ms`. `compact,delete` combina compactação com retenção por tempo.

## Connect clusters (gerenciados)

- Recurso separado do cluster Kafka, associado a um **cluster primário** (que guarda o estado
  dos connectors). Um cluster Kafka pode ter vários Connect clusters.
- Comandos: `gcloud managed-kafka connect-clusters create|delete`,
  `gcloud managed-kafka connectors create|pause|resume|delete`.
- **Connectors suportados** (lista curada): Cloud Storage Sink, BigQuery Sink,
  Pub/Sub Sink, Pub/Sub Source, MirrorMaker 2.0, Cloud SQL for PostgreSQL Source,
  PostgreSQL Source genérico. Suporta transforms (SMT) e predicates padrão do Kafka Connect.
- **Não é possível subir plugin custom** ("You can't upload custom connector plugins").
  Consequência direta: **HDFS Sink não roda no Connect gerenciado**.
- Cobrança por hora como recurso próprio — destruir junto com o cluster.

## Self-managed Connect (quando o plugin não existe)

Kafka Connect distribuído em VM/GKE apontando para o bootstrap do Managed Kafka:

- Workers com o mesmo `SASL_SSL` + OAUTHBEARER dos clientes (prefixos `producer.`,
  `consumer.`, `admin.` no `connect-distributed.properties`).
- Tópicos internos (`config/offset/status.storage.topic`) criados no Managed Kafka,
  `cleanup.policy=compact`.
- Custo = VMs + operação. Ver `patterns/kafka-connect-sink.md` (seção HDFS — **risco a validar**).

## Escolha do sink

| Destino | Caminho |
|---|---|
| Lake GCS (raw) | Cloud Storage Sink gerenciado |
| BigQuery direto | BigQuery Sink gerenciado **ou** Dataflow template Kafka→BigQuery (`gcp-dataflow`) |
| HDFS / cluster Hadoop | Connect self-managed + plugin HDFS — **risco a validar** |
