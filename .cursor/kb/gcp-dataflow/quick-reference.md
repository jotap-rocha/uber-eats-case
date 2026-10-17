---
domain: gcp-dataflow
topic: quick-reference
---

# Dataflow — Quick Reference

### Template Kafka → BigQuery (Managed Kafka, sem código)

```bash
gcloud dataflow flex-template run kafka-to-bq-lab \
  --region=<REGION> \
  --template-file-gcs-location=gs://dataflow-templates-<REGION>/latest/flex/Kafka_to_BigQuery \
  --service-account-email=<SA_EMAIL> --max-workers=2 --disable-public-ips \
  --subnetwork=regions/<REGION>/subnetworks/<SUBNET> \
  --parameters=readBootstrapServerAndTopic=projects/<GCP_PROJECT_ID>/locations/<REGION>/clusters/<CLUSTER>/topics/<TOPIC>,kafkaReadAuthenticationMode=APPLICATION_DEFAULT_CREDENTIALS,messageFormat=JSON,writeMode=SINGLE_TABLE_NAME,outputTableSpec=<GCP_PROJECT_ID>:<DATASET>.<TABLE>,useBigQueryDLQ=true,outputDeadletterTable=<GCP_PROJECT_ID>:<DATASET>.<TABLE>_dlq
```

### Operar

| Ação | Comando |
|---|---|
| Listar ativos | `gcloud dataflow jobs list --region=<REGION> --status=active` |
| Detalhe | `gcloud dataflow jobs describe <JOB_ID> --region=<REGION>` |
| Drain (streaming, sem perda) | `gcloud dataflow jobs drain <JOB_ID> --region=<REGION>` |
| Cancel (imediato) | `gcloud dataflow jobs cancel <JOB_ID> --region=<REGION>` |
| Force cancel (preso > 30 min) | `gcloud dataflow jobs cancel <JOB_ID> --force --region=<REGION>` |

Drain não existe para batch.

### Pipeline Python (opções)

```bash
python pipeline.py --runner=DataflowRunner --project=<GCP_PROJECT_ID> \
  --region=<REGION> --streaming --enable_streaming_engine \
  --temp_location=gs://<BUCKET>-tmp/dataflow/temp \
  --staging_location=gs://<BUCKET>-tmp/dataflow/staging \
  --service_account_email=<SA_EMAIL> --max_num_workers=2 --no_use_public_ips
```

### Side input slowly-changing (esqueleto)

```
PeriodicImpulse(fire_interval=600) → Map(load_ref_from_gcs)
  → WindowInto(GlobalWindows, Repeatedly(AfterProcessingTime(1)), DISCARDING)
  → beam.pvalue.AsSingleton(...)
```

Ver `patterns/reference-data.md`.

### IAM

| Quem | Papel |
|---|---|
| Worker SA | `dataflow.worker`, `managedkafka.client`, `bigquery.jobUser`, `bigquery.dataEditor` (dataset), `storage.objectViewer` (ref), `storage.objectUser` (tmp) |
| Quem lança | `dataflow.developer`, `iam.serviceAccountUser` (na SA) |

### Custo

Sem free tier; por segundo de vCPU/memória/disco + Streaming Engine. Streaming = 24/7.
`--max-workers` sempre. Drain/cancel no mesmo dia.
