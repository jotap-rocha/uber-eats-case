---
domain: gcp-dataflow
topic: kafka-to-bigquery-template
---

# Pattern: Managed Kafka → BigQuery com template Google

## Problema

Colocar eventos de um tópico do Managed Kafka numa tabela BigQuery com o mínimo de código,
para validar o fluxo ponta a ponta (streaming → stream-processing → warehouse).

## Solução

Flex template `Kafka_to_BigQuery` com `kafkaReadAuthenticationMode=APPLICATION_DEFAULT_CREDENTIALS`
— o job lê o Kafka como a worker SA, sem segredo.

## 1. Pré-requisitos

| Item | KB |
|---|---|
| Cluster + tópico | `gcp-managed-kafka` |
| Dataset de destino | `gcp-bigquery` |
| Bucket `tmp` para staging/temp | `gcp-gcs` |
| APIs `dataflow`, `managedkafka`, `bigquery`, `compute` | `gcp-terraform/concepts/project-apis.md` |

## 2. Worker SA

```bash
SA=<SA_EMAIL>
for r in roles/dataflow.worker roles/managedkafka.client roles/bigquery.jobUser; do
  gcloud projects add-iam-policy-binding <GCP_PROJECT_ID> --member="serviceAccount:$SA" --role="$r"
done
bq add-iam-policy-binding --member="serviceAccount:$SA" \
  --role="roles/bigquery.dataEditor" <GCP_PROJECT_ID>:<DATASET>
gcloud storage buckets add-iam-policy-binding gs://<BUCKET>-tmp \
  --member="serviceAccount:$SA" --role="roles/storage.objectUser"
```

`bq add-iam-policy-binding` em dataset: **a validar** na versão do `bq`; alternativa é
`google_bigquery_dataset_iam_member` no Terraform.

## 3. Rodar

```bash
gcloud dataflow flex-template run kafka-to-bq-lab \
  --region=<REGION> \
  --template-file-gcs-location=gs://dataflow-templates-<REGION>/latest/flex/Kafka_to_BigQuery \
  --service-account-email=<SA_EMAIL> \
  --subnetwork=regions/<REGION>/subnetworks/<SUBNET> --disable-public-ips \
  --max-workers=2 \
  --staging-location=gs://<BUCKET>-tmp/dataflow/staging \
  --temp-location=gs://<BUCKET>-tmp/dataflow/temp \
  --parameters=\
readBootstrapServerAndTopic=projects/<GCP_PROJECT_ID>/locations/<REGION>/clusters/<CLUSTER>/topics/<TOPIC>,\
kafkaReadAuthenticationMode=APPLICATION_DEFAULT_CREDENTIALS,\
kafkaReadOffset=earliest,\
persistKafkaKey=false,\
messageFormat=JSON,\
writeMode=SINGLE_TABLE_NAME,\
outputTableSpec=<GCP_PROJECT_ID>:<DATASET>.eventos,\
useBigQueryDLQ=true,\
outputDeadletterTable=<GCP_PROJECT_ID>:<DATASET>.eventos_dlq
```

- A doc oficial usa `gs://dataflow-templates/latest/flex/Kafka_to_BigQuery`; o caminho
  regional é equivalente e evita leitura cross-region.
- Tabela DLQ: tutorial diz que o pipeline cria; referência do template diz criar vazia sem
  schema — **a validar**.

## 4. Testar

```bash
# produzir (cliente com client.properties do gcp-managed-kafka)
echo '{"pedido_id":"p1","produto_id":"x1","valor":10.5}' | \
  kafka-console-producer.sh --bootstrap-server "$BOOTSTRAP" \
  --producer.config client.properties --topic <TOPIC>
```

```sql
SELECT * FROM `<GCP_PROJECT_ID>.<DATASET>.eventos` LIMIT 10;
SELECT COUNT(*) FROM `<GCP_PROJECT_ID>.<DATASET>.eventos_dlq`;
```

Data freshness no console do job deve ficar em segundos.

## 5. Encerrar (mesmo dia)

```bash
JOB_ID=$(gcloud dataflow jobs list --region=<REGION> --status=active \
  --filter="name=kafka-to-bq-lab" --format="value(id)")
gcloud dataflow jobs drain "$JOB_ID" --region=<REGION>     # ou cancel
gcloud dataflow jobs list --region=<REGION> --status=active  # esperado: vazio
```

Depois: destruir Connect/cluster Kafka (`gcp-managed-kafka`) e dataset de lab.

## Limites

- Enriquecimento com reference data **não** cabe no template → `patterns/reference-data.md`.
- UDF opcional do template (se disponível) só para transformações simples por mensagem.

## Anti-patterns

- Rodar com a SA default do Compute (Editor no projeto).
- Sem `--max-workers` (autoscaling pode subir vários workers).
- Deixar o job ativo "para ver amanhã".
