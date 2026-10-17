---
domain: gcp-dataflow
topic: templates
---

# Templates

Template = pipeline empacotado e parametrizado; quem lança não precisa de SDK nem código.

## Tipos

| Tipo | Como é | Quando |
|---|---|---|
| **Flex template** | Imagem de container + spec JSON no GCS; grafo construído no launch | Padrão atual (Google e custom) |
| Classic template | Grafo serializado no GCS; parâmetros via `ValueProvider` | Legado; não criar novos |
| Job builder / Beam YAML | Pipeline declarativo no console/YAML | Protótipo rápido — **a validar** recursos para Kafka |

## Templates Google relevantes (paridade Stream Analytics)

| Template | Fonte → destino |
|---|---|
| `Kafka_to_BigQuery` (flex) | Kafka / **Managed Kafka** → BigQuery |
| `Kafka_to_Gcs` (flex) | Kafka → arquivos no GCS — **a validar** nome atual |
| `PubSub_to_BigQuery` (flex) | Pub/Sub → BigQuery (alternativa não-Kafka) |
| `GCS_Text_to_BigQuery` | batch de arquivos → BigQuery |

Localização: `gs://dataflow-templates-<REGION>/latest/flex/<Nome>` (regional, preferido) ou
`gs://dataflow-templates/latest/flex/<Nome>`. `latest` muda — em produção, fixar versão
(`.../<VERSAO>/flex/...`).

## `Kafka_to_BigQuery` com Managed Kafka

Parâmetros principais (doc oficial):

| Parâmetro | Valor |
|---|---|
| `readBootstrapServerAndTopic` | `projects/<GCP_PROJECT_ID>/locations/<REGION>/clusters/<CLUSTER>/topics/<TOPIC>` |
| `kafkaReadAuthenticationMode` | `APPLICATION_DEFAULT_CREDENTIALS` (identidade da worker SA) |
| `kafkaReadOffset` | `earliest` / `latest` |
| `messageFormat` | `JSON`, `AVRO_CONFLUENT_WIRE_FORMAT`, `AVRO_BINARY_ENCODING` |
| `writeMode` | `SINGLE_TABLE_NAME` (ou dinâmico por tópico) |
| `outputTableSpec` | `<GCP_PROJECT_ID>:<DATASET>.<TABLE>` |
| `useBigQueryDLQ` / `outputDeadletterTable` | Fila de erros em tabela BigQuery |
| `persistKafkaKey` | grava a chave da mensagem |

Requisitos: worker SA com `roles/managedkafka.client`; workers na subnet que alcança o
cluster. O template também suporta SASL/PLAIN para Kafka não-Google.

Divergência na doc: o tutorial diz para **não** criar a tabela DLQ (o pipeline cria); a
referência do template diz para criar tabela vazia sem schema — **a validar** na versão usada.

## Template custom (flex)

```bash
gcloud dataflow flex-template build gs://<BUCKET>-tmp/templates/enrich.json \
  --image-gcr-path=<REGION>-docker.pkg.dev/<GCP_PROJECT_ID>/<REPO>/enrich:latest \
  --sdk-language=PYTHON --flex-template-base-image=PYTHON3 \
  --py-path=. --env=FLEX_TEMPLATE_PYTHON_PY_FILE=pipeline.py \
  --metadata-file=metadata.json
```

Use template custom quando precisar de side input/janela/lógica que o template Google não
cobre (ver `patterns/reference-data.md`).

## Limites de template Google

- Transformação limitada a UDF JavaScript/Python opcional (quando o template oferece).
- Sem side input arbitrário → enriquecimento com reference data exige pipeline custom.
