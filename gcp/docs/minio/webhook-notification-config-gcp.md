# Notificação de bucket do MinIO → Cloud Function (GCP, Fase 3)

> Equivalente GCP de `docs/minio/webhook-notification-config.md` (Fase 2/AWS). Ver `DESIGN_INGESTAO_GCP_FASE3.md`, Decisão 7.

## Configurar o destino Webhook no MinIO

```bash
mc admin config set local/ notify_webhook:gcp_pubsub_bridge \
  endpoint="<cloud_function_bridge_url>" \
  auth_token="Bearer <minio_webhook_auth_token>"

mc admin service restart local/

mc event add local/uber-eats arn:minio:sqs::gcp_pubsub_bridge:webhook --event put
```

- `<cloud_function_bridge_url>` vem do output `cloud_function_bridge_url` do Terraform (`infra/gcp/fase3-ingestao/outputs.tf`).
- `<minio_webhook_auth_token>` é o mesmo valor passado na variável `minio_webhook_auth_token` — o MinIO não assina requisições com SigV4, então a Cloud Function valida esse token estático no header `Authorization` (ver `src/gcp/cloud_function_minio_pubsub_bridge/main.py`).

## Formato do payload recebido pela Cloud Function

Mesmo formato compatível com S3 Event Notification já documentado na Fase 2/AWS:

```json
{
  "Records": [
    {
      "eventName": "s3:ObjectCreated:Put",
      "s3": {
        "bucket": { "name": "uber-eats" },
        "object": { "key": "oracle/orders/2026/09/11/obj123.json" }
      }
    }
  ]
}
```

## Validação

1. Escrever um objeto novo no bucket `uber-eats` do MinIO.
2. Confirmar que a Cloud Function recebeu a chamada (Cloud Logging).
3. Confirmar que uma mensagem apareceu no tópico Pub/Sub `pubsub_topic_minio_bridge` (`gcloud pubsub subscriptions pull ... --auto-ack`).
