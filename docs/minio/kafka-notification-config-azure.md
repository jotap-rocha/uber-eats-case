# Notificação de bucket do MinIO → Event Hub (Azure, Fase 1)

> Diferente de `docs/minio/webhook-notification-config.md` (AWS) e `docs/minio/webhook-notification-config-gcp.md` (GCP): aqui o destino é do tipo **Kafka**, não Webhook — o Event Hub fala protocolo Kafka nativamente, então não existe função-ponte customizada nesta fase (Lambda/Cloud Function). Ver `DESIGN_INGESTAO_AZURE_FASE1.md`, Decisão 5.

## Configurar o destino Kafka no MinIO

```bash
mc admin config set local/ notify_kafka:eventhub \
  brokers="${AZURE_EVENTHUB_NAMESPACE}.servicebus.windows.net:9093" \
  topic="minio" \
  sasl="on" \
  sasl_mechanism="PLAIN" \
  sasl_username='$ConnectionString' \
  sasl_password="${AZURE_EVENTHUB_CONNECTION_STRING}" \
  tls="on"

mc admin service restart local/

mc event add local/uber-eats arn:minio:sqs::eventhub:kafka --event put,delete
```

- `AZURE_EVENTHUB_NAMESPACE` e `AZURE_EVENTHUB_CONNECTION_STRING` vêm de `gen/.env` (ver `gen/.env.template`, seção "Azure (Fase 1)") — a connection string é a do Event Hubs Namespace (não de um Event Hub individual), com permissão `Send` no mínimo (ver `azurerm_eventhub_namespace_authorization_rule.connect` em `infra/azure/fase1-ingestao/event_hubs.tf`).
- `sasl_username='$ConnectionString'` é literal — é o nome de usuário fixo exigido pelo endpoint Kafka do Event Hubs, não uma variável a substituir.

## Formato da mensagem publicada no tópico `minio`

MinIO publica o evento no formato nativo compatível com S3 Event Notification, direto como valor da mensagem Kafka:

```json
{
  "Records": [
    {
      "eventName": "s3:ObjectCreated:Put",
      "s3": {
        "bucket": { "name": "uber-eats" },
        "object": { "key": "kafka/gps/2026/09/12/obj123.json" }
      }
    }
  ]
}
```

O Stream Analytics (input `minio-input`, ver `infra/azure/fase1-ingestao/stream_analytics.tf`) lê esse payload diretamente do tópico — sem tradução de protocolo, sem componente intermediário.

## Validação

1. Escrever um objeto novo no bucket `uber-eats` do MinIO.
2. Confirmar no Azure Portal (Event Hubs → `minio` → Métricas) que uma mensagem chegou.
3. Confirmar que o job Stream Analytics (se já implantado) processou o evento — métrica "Input Events" do job.
