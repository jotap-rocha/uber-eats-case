---
domain: gcp-managed-kafka
topic: quick-reference
---

# Managed Kafka — Quick Reference

### Criar / descrever / apagar

```bash
gcloud managed-kafka clusters create <CLUSTER> --location=<REGION> \
  --cpu=3 --memory=3GiB \
  --subnets=projects/<GCP_PROJECT_ID>/regions/<REGION>/subnetworks/<SUBNET> --async

gcloud managed-kafka clusters describe <CLUSTER> --location=<REGION> \
  --format="value(bootstrapAddress)"
# bootstrap.<CLUSTER>.<REGION>.managedkafka.<GCP_PROJECT_ID>.cloud.goog:9092

gcloud managed-kafka clusters delete <CLUSTER> --location=<REGION>
```

### Tópico compactado

```bash
gcloud managed-kafka topics create <TOPIC> --cluster=<CLUSTER> --location=<REGION> \
  --partitions=3 --replication-factor=3 --configs=cleanup.policy=compact
```

### Limites de capacidade

| Item | Valor |
|---|---|
| vCPU mínimo | 3 |
| RAM por vCPU | 1–8 GiB |
| Subnets | 1–10, uma por rede, mesma região |
| Porta bootstrap | 9092 (TLS) |

### Auth do cliente

| Mecanismo | Uso |
|---|---|
| `SASL_SSL` + `OAUTHBEARER` + `GcpLoginCallbackHandler` | Padrão (ADC) |
| `SASL_SSL` + `PLAIN` (user = e-mail da SA, password = access token) | Cliente sem handler Google |
| `SASL_SSL` + `PLAIN` (password = chave JSON base64) | Só teste; secret fora do git |
| mTLS | Suportado (config `tls_config`) — detalhes **a validar** |

### IAM

| Quem | Papel |
|---|---|
| Produtor/consumidor | `roles/managedkafka.client` |
| Operador | `roles/managedkafka.admin` (lab) |
| Service agent do Connect → bucket | `roles/storage.objectUser` (doc oficial) |
| SA do Dataflow | `roles/managedkafka.client` |

### Connect (gerenciado)

Connectors suportados: Cloud Storage Sink, BigQuery Sink, Pub/Sub Source/Sink,
MirrorMaker 2.0, Cloud SQL PostgreSQL Source, PostgreSQL Source. **Sem plugin custom.**

```bash
gcloud managed-kafka connectors create <CONNECTOR> --location=<REGION> \
  --connect-cluster=<CONNECT_CLUSTER> --config-file=gcs-sink.yaml
```

### Custo

Sem free tier. Mínimo ~2,1 DCU/h (~US$ 0,19/h, **a validar**) 24/7 + Connect cluster.
Criar → testar → destruir no mesmo dia.
