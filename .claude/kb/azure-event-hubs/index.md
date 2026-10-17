---
domain: azure-event-hubs
description: Azure Event Hubs Standard como broker Kafka gerenciado — endpoint :9093, SASL_SSL PLAIN com connection string ou OAUTHBEARER/Entra ID, tópicos compactados, Kafka Connect contra Event Hubs; HDFS 2 Sink marcado como risco a validar
mcp_validated: "2026-10-16"
confidence: 0.8
---

# KB: Azure Event Hubs (endpoint Kafka)

Event Hubs expõe o **protocolo Kafka (≥ 1.0)** no namespace: cliente Kafka só troca
configuração (bootstrap + SASL), sem cluster para operar.

| Kafka | Event Hubs |
|---|---|
| Cluster | Namespace (`<NAMESPACE>.servicebus.windows.net:9093`) |
| Tópico | Event hub |
| Partição / Consumer group / Offset | iguais |

## Papel

`role: streaming` — broker de eventos com endpoint Kafka: produtores Kafka publicam,
consumidores (Kafka, Stream Analytics, Spark, Kafka Connect) leem. Tópicos compactados
servem para CDC/estado; Kafka Connect usa Event Hubs para seus tópicos internos.

## Capability map

| Pergunta | Onde achar |
|---|---|
| Tiers, cotas do Standard, o que do Kafka não existe | [concepts/kafka-on-event-hubs.md](concepts/kafka-on-event-hubs.md) |
| Log compaction, chave, tombstone | [concepts/log-compaction.md](concepts/log-compaction.md) |
| Configurar producer/consumer (SAS ou Entra ID) | [patterns/kafka-client-auth.md](patterns/kafka-client-auth.md) |
| Kafka Connect + sink (HDFS 2 = risco) | [patterns/kafka-connect-sink.md](patterns/kafka-connect-sink.md) |
| Cheatsheet | [quick-reference.md](quick-reference.md) |

## Custo e free tier

- **Sem free tier** para Standard; consome o crédito de avaliação (**US$ 200 / 30 dias**).
- Standard cobra **por TU-hora** (namespace existe = cobra, mesmo sem tráfego) +
  **por milhão de eventos de ingress**. Ordem de grandeza: 1 TU ≈ US$ 0,03/h
  (≈ US$ 22/mês) — **a validar** na calculadora da região. Capture é cobrado à parte.
- O que queima crédito: `capacity` > 1, **Auto-Inflate** ligado (sobe TUs sozinho até
  `maximum_throughput_units`), Capture ligado, tier Premium/Dedicated por engano.
- **Não existe "pausar" namespace.** Parar de pagar = **excluir** o namespace
  (`terraform destroy` ou `az eventhubs namespace delete`). `status = Disabled` no event
  hub não zera o custo do TU.
- Regra: **criar → testar → destruir o namespace no mesmo dia.** Tópicos internos do
  Kafka Connect persistem após derrubar o worker — somem com o namespace.

## SI

- Preferir **Entra ID (OAUTHBEARER)** com RBAC: `Azure Event Hubs Data Sender` /
  `Data Receiver` no escopo do event hub. Com isso dá para `local_authentication_enabled
  = false` (desliga SAS).
- Se usar connection string (SAS): policy **por event hub** com só `Send` ou `Listen` —
  **nunca** `RootManageSharedAccessKey` em aplicação. Connection string só via env/Key
  Vault; nunca em `.properties` versionado.
- Regenerar chave SAS **não** derruba conexões Kafka já abertas → reiniciar clientes ao
  rotacionar.
- TLS obrigatório (SASL_SSL); TLS 1.2 mínimo.
- Placeholders: `<NAMESPACE>`, `<EVENTHUB>`, `<TENANT_ID>`, `<CLIENT_ID>`.

## Por que este serviço

| Alternativa | Por que não (aqui) |
|---|---|
| Event Hubs **Basic** | **Sem** endpoint Kafka e sem compaction |
| Event Hubs **Premium/Dedicated** | Kafka Streams, transações e compressão gzip só aqui — custo muito maior; só se precisar |
| HDInsight Kafka / Kafka em VM | Kafka "de verdade", mas operar cluster; custo fixo alto |
| Confluent Cloud (Marketplace) | ksqlDB/Connect gerenciado; outro fornecedor e cobrança |
| Service Bus | Fila/pub-sub com DLQ; não é log particionado Kafka |

## Learning path

1. `concepts/kafka-on-event-hubs.md` — limites do Standard antes de desenhar tópicos
2. `patterns/kafka-client-auth.md` — primeiro producer/consumer
3. `concepts/log-compaction.md` — tópicos de estado/CDC
4. `patterns/kafka-connect-sink.md` — Connect (e o risco do HDFS 2)

## Quick Reference

Ver [quick-reference.md](quick-reference.md).
