---
domain: azure-event-hubs
topic: kafka-on-event-hubs
---

# Kafka sobre Event Hubs — o que é igual e o que não é

## Suporte por tier

| Recurso | Basic | Standard | Premium | Dedicated |
|---|---|---|---|---|
| Endpoint Kafka | não | **sim** | sim | sim |
| Log compaction | não | sim (1 GB/partição) | sim (250 GB) | sim (250 GB) |
| Kafka Streams | não | não | preview | preview |
| Transações Kafka | não | não | preview | preview |
| Compressão (gzip) | não | não | sim | sim |
| Idempotent producer | — | sim | sim | sim |

Versão de protocolo: clientes Kafka **1.0+**.

## Diferenças operacionais em relação a um cluster Kafka

- **Um endpoint só** (VIP do namespace) para todas as partições — firewall libera só
  `<NAMESPACE>.servicebus.windows.net:9093`; não há lista de brokers.
- **Sem configuração de broker**: `replication.factor`, `min.insync.replicas`,
  `log.segment.bytes` etc. não se aplicam (replicação é do serviço — 3x no storage).
  Clientes que exigem RF > 1 na criação de tópico: usar 1 (ver Kafka Connect).
- **Tópico = event hub = recurso Azure.** Auto-criação via Kafka AdminClient funciona,
  mas conta no limite de **10 event hubs** do Standard. Prefira criar tópicos no
  Terraform (versionado, custo visível).
- **Partições** são fixadas na criação no Standard (não aumentam) → dimensione já
  pensando no consumidor (ex.: Stream Analytics: 1/3 SU V2 lida bem com 2 partições;
  1 SU V2 com 4–8).
- **Retenção** máx. 7 dias no Standard; para histórico use Capture → ADLS
  (`object-storage`) ou um sink.
- **Consumer group Kafka** não precisa ser pré-criado (até 1.000 por namespace);
  consumer group AMQP (Stream Analytics, Functions) **precisa** ser criado no event hub
  (até 20).
- **Entrega at-least-once**: consumidor deve ser idempotente.

## Interoperabilidade de protocolos

Kafka, AMQP e HTTPS coexistem no mesmo event hub: producer Kafka → Stream Analytics lê
via AMQP sem configuração extra. Headers Kafka viram propriedades do evento AMQP
(mapeamento de tipos pode exigir atenção — **a validar** se o consumidor depender de
headers).

## Throughput Units (Standard)

- 1 TU = ingress 1 MB/s ou 1.000 ev/s; egress 2 MB/s ou 4.096 ev/s.
- Excedeu → throttling (`ServerBusy`/latência). Auto-Inflate sobe TUs sozinho até o
  máximo configurado — **e o custo sobe junto**; em lab, deixar desligado.
- TU é do namespace, não do event hub.

## Quando o Standard não basta

Precisa de Kafka Streams, transações exactly-once, partições > 32, retenção > 7 dias,
compactação > 1 GB/partição → Premium (custo por PU) ou cluster Kafka próprio. Registre
a decisão em ADR antes de mudar de tier.
