---
domain: gcp-managed-kafka
topic: kafka-connect-sink
---

# Pattern: Kafka Connect sink (GCS gerenciado; HDFS = risco a validar)

## Problema

Levar eventos dos tópicos para o lake (`gcp-gcs`) — e, no briefing de paridade com o Azure,
também para HDFS — sem escrever consumidor próprio.

## Solução

1. **GCS:** Connect cluster **gerenciado** + connector **Cloud Storage Sink** (validado na doc).
2. **HDFS:** Connect gerenciado **não** aceita plugin custom → exige Kafka Connect
   **self-managed** (VM/GKE) com o plugin HDFS. **Risco a validar** — nunca testado contra o
   Managed Kafka real.

## A. Sink GCS (gerenciado)

### 1. Permissão do service agent no bucket

```bash
PROJECT_NUMBER=$(gcloud projects describe <GCP_PROJECT_ID> --format="value(projectNumber)")
gcloud storage buckets add-iam-policy-binding gs://<BUCKET> \
  --member="serviceAccount:service-${PROJECT_NUMBER}@gcp-sa-managedkafka.iam.gserviceaccount.com" \
  --role="roles/storage.objectUser"
```

A doc oficial concede no **projeto** (`objectUser` no guia do connector; `objectCreator` no
tutorial). Aqui no **bucket** = menor privilégio — **a validar** que basta.

### 2. Connect cluster

```bash
gcloud managed-kafka connect-clusters create <CONNECT_CLUSTER> \
  --location=<REGION> --cpu=12 --memory=12GiB \
  --primary-subnet=projects/<GCP_PROJECT_ID>/regions/<REGION>/subnetworks/<SUBNET> \
  --kafka-cluster=<CLUSTER> --async
```

O tutorial usa 12 vCPU / 12 GiB (criação até ~30 min). Tamanho mínimo aceito **a validar** —
tente 3 vCPU em lab; Connect cobra por hora como o cluster.

### 3. Connector (`gcs-sink.yaml`)

```yaml
connector.class: "io.aiven.kafka.connect.gcs.GcsSinkConnector"
topics: "<TOPIC>"
tasks.max: "3"
gcs.bucket.name: "<BUCKET>"
gcs.credentials.default: "true"          # usa a identidade do serviço, sem chave
file.name.prefix: "raw/kafka/<TOPIC>/"
format.output.type: "json"               # parquet/avro exigem converter com schema
file.max.records: "10000"
key.converter: "org.apache.kafka.connect.storage.StringConverter"
value.converter: "org.apache.kafka.connect.json.JsonConverter"
value.converter.schemas.enable: "false"
```

```bash
gcloud managed-kafka connectors create gcs-sink-<TOPIC> \
  --location=<REGION> --connect-cluster=<CONNECT_CLUSTER> --config-file=gcs-sink.yaml
gcloud managed-kafka connectors describe gcs-sink-<TOPIC> \
  --location=<REGION> --connect-cluster=<CONNECT_CLUSTER>
gcloud storage ls gs://<BUCKET>/raw/kafka/<TOPIC>/   # 1º arquivo leva alguns minutos
```

`file.name.prefix` com layout por zona: **a validar** se aceita `/` e placeholders de data;
o default do connector gera `<topic>-<partition>-<offset>`.

## B. Sink HDFS (self-managed) — **risco a validar**

Contexto: mesmo risco do briefing Azure ("HDFS 2 Sink nunca testado contra o Event Hub real").

Esboço (não validado):

```properties
# connect-distributed.properties (workers em VM/GKE na VPC do cluster)
bootstrap.servers=bootstrap.<CLUSTER>.<REGION>.managedkafka.<GCP_PROJECT_ID>.cloud.goog:9092
group.id=connect-hdfs
config.storage.topic=_connect-configs
offset.storage.topic=_connect-offsets
status.storage.topic=_connect-status
security.protocol=SASL_SSL
sasl.mechanism=OAUTHBEARER
sasl.login.callback.handler.class=com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler
sasl.jaas.config=org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;
# repetir os 4 de segurança com prefixos producer. / consumer. / admin.
plugin.path=/opt/connect/plugins
```

Connector: `io.confluent.connect.hdfs.HdfsSinkConnector` com `hdfs.url=hdfs://<NAMENODE>:8020`.

Pontos a validar antes de assumir que funciona:

| Risco | Como testar |
|---|---|
| Licença do plugin HDFS (Confluent Community License) e compatibilidade com Kafka 3.7+ | Subir worker e listar plugins (`GET /connector-plugins`) |
| Handler OAUTHBEARER no classpath do worker | Log de inicialização sem `ClassNotFound` |
| Rede worker → brokers (9092) **e** worker → NameNode/DataNodes | `nc`/`kafka-topics --list` + `hdfs dfs -ls` da VM |
| Kerberos no HDFS (se houver) | Keytab via Secret Manager, nunca no git |
| Alternativa sem HDFS | Dataproc lendo do GCS (sink A) |

Se algum item falhar: adotar sink GCS + Dataproc/BigQuery lendo do GCS.

## Teardown (mesmo dia)

```bash
gcloud managed-kafka connectors delete gcs-sink-<TOPIC> --location=<REGION> --connect-cluster=<CONNECT_CLUSTER>
gcloud managed-kafka connect-clusters delete <CONNECT_CLUSTER> --location=<REGION> --async
```

## Anti-patterns

- `gcs.credentials.json` com chave de SA no YAML.
- `objectAdmin` no projeto para o service agent.
- Deixar Connect cluster ligado "para o próximo teste".
