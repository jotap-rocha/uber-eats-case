---
domain: aws-msk
topic: topics-and-quotas
---

# Tópicos, configs e quotas (MSK Serverless)

## Configs de tópico editáveis

| Config | Default | Editável | Máximo |
|---|---|---|---|
| `cleanup.policy` | `delete` | **só na criação** | — |
| `compression.type` | `producer` | sim | — |
| `max.message.bytes` | 1048588 | sim | 8388608 (8 MiB) |
| `message.timestamp.difference.max.ms` | long.max | sim | — |
| `message.timestamp.type` | `CreateTime` | sim | — |
| `retention.bytes` | 250 GiB | sim | ilimitado (`-1`) |
| `retention.ms` | 7 dias | sim | ilimitado (`-1`) |

Qualquer outra config de tópico (e todas de broker) é **fixa**. Inclui `segment.bytes`,
`min.compaction.lag.ms`, `delete.retention.ms`, `min.insync.replicas`.

## Tópicos compactados

- Criar com `--config cleanup.policy=compact` — **não dá para converter depois**; para
  mudar, recrie o tópico e reprocesse.
- `compact,delete` (compacta e expira por tempo): **a validar** se o Serverless aceita o
  valor composto; teste com `kafka-topics --describe` após criar.
- Limites: **120 partições líderes compactadas por cluster** e **250 GB por partição
  compactada**.
- Uso típico: estado atual por chave (cadastro, CDC "last value"), offsets de connectors,
  tópicos internos do Kafka Connect self-managed (`config/offset/status` exigem compactação).
- Mensagem com `key` obrigatória; tombstone (`value = null`) apaga a chave na compactação.

```bash
kafka-topics.sh --bootstrap-server <BOOTSTRAP>:9098 --command-config client.properties \
  --create --topic cadastro.clientes --partitions 3 --config cleanup.policy=compact

kafka-configs.sh --bootstrap-server <BOOTSTRAP>:9098 --command-config client.properties \
  --entity-type topics --entity-name eventos.cliques --alter --add-config retention.ms=86400000
```

Replicação: gerenciada pelo serviço (não se escolhe `replication-factor` no Serverless —
omitir o parâmetro; **a validar** se valores explícitos são rejeitados ou ignorados).

## Quotas por cluster (validadas 2026-10-16)

| Dimensão | Quota | Ao estourar |
|---|---|---|
| Ingress / egress | 200 / 400 MBps | throttle |
| Por partição in / out | 5 / 10 MBps | throttle |
| Partições líderes | 2400 (não compactadas) · 120 (compactadas) | `INVALID_REQUEST` |
| Criação/remoção de partições | 250 a cada 5 min | `THROUGHPUT_QUOTA_EXCEEDED` |
| APIs de gestão de tópico | 2 req/s | throttle |
| Conexões / tentativas | 3000 / 100 por s | conexão fechada |
| Request rate | 15.000/s | throttle |
| Fetch por request | 55 MB | `INVALID_REQUEST` |
| Consumer groups | 500 | `JoinGroup` falha |
| VPCs clientes | 5 | — |
| Clusters por conta | 10 | — |

## Dimensionando partições

- Partições = max(throughput_in / 5 MBps, throughput_out / 10 MBps, paralelismo de consumo).
- Lab: **3 partições** por tópico (cada partição custa US$ 0,0015/h).
- Kafka Streams: tópicos internos tentam definir `segment.bytes` — configure a app conforme
  "Using Kafka Streams with MSK Serverless" (doc AWS) antes de subir.

## Naming (sugestão)

`<dominio>.<entidade>[.<versao>]` — ex.: `vendas.pedidos.v1`, `cadastro.clientes`
(compactado). Prefixo por domínio facilita policy IAM com wildcard
(`topic/<CLUSTER_NAME>/<CLUSTER_UUID>/vendas.*`).
