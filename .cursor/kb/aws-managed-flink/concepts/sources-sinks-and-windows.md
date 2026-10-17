---
domain: aws-managed-flink
topic: sources-sinks-and-windows
---

# Fontes, sinks e janelas

## Fonte MSK (Kafka) com IAM

Flink SQL — as propriedades `properties.*` vão direto para o cliente Kafka:

```sql
CREATE TABLE pedidos (
  pedido_id   BIGINT,
  loja_id     STRING,
  valor       DECIMAL(12,2),
  ts_evento   TIMESTAMP(3),
  proc_time   AS PROCTIME(),
  WATERMARK FOR ts_evento AS ts_evento - INTERVAL '10' SECOND
) WITH (
  'connector' = 'kafka',
  'topic' = 'vendas.pedidos.v1',
  'properties.bootstrap.servers' = '<BOOTSTRAP>:9098',
  'properties.group.id' = 'flink-vendas',
  'properties.security.protocol' = 'SASL_SSL',
  'properties.sasl.mechanism' = 'AWS_MSK_IAM',
  'properties.sasl.jaas.config' = 'software.amazon.msk.auth.iam.IAMLoginModule required;',
  'properties.sasl.client.callback.handler.class' = 'software.amazon.msk.auth.iam.IAMClientCallbackHandler',
  'scan.startup.mode' = 'latest-offset',
  'format' = 'json',
  'json.ignore-parse-errors' = 'true'
);
```

- Empacote `flink-sql-connector-kafka` (versão compatível com 1.20) **e** `aws-msk-iam-auth`
  no zip/uber-jar. **A validar** a versão exata do connector para 1.20.
- A **service execution role** precisa das ações `kafka-cluster:*` mínimas (ver
  `aws-msk/patterns/kafka-client-auth.md`) — o plugin IAM usa a role da aplicação.
- `<BOOTSTRAP>` vem de `environment_properties`; em PyFlink, monte o DDL com a string lida.

## Fonte Kinesis Data Streams

```sql
CREATE TABLE cliques (...) WITH (
  'connector' = 'kinesis',
  'stream.arn' = 'arn:aws:kinesis:<REGION>:<AWS_ACCOUNT_ID>:stream/<STREAM>',
  'aws.region' = '<REGION>',
  'source.init.position' = 'LATEST',
  'format' = 'json'
);
```

Opções do connector Kinesis mudaram entre versões (`stream` × `stream.arn`,
`scan.stream.initpos` × `source.init.position`) — **a validar** contra a versão do
`flink-connector-aws-kinesis-streams` empacotada.

## Sink S3 (filesystem)

```sql
CREATE TABLE vendas_5min (
  window_start TIMESTAMP(3), window_end TIMESTAMP(3), loja_id STRING,
  regiao STRING, pedidos BIGINT, dt STRING
) PARTITIONED BY (dt) WITH (
  'connector' = 'filesystem',
  'path' = 's3://<BUCKET>/curated/vendas_5min/',
  'format' = 'parquet',
  'sink.rolling-policy.rollover-interval' = '10 min'
);
```

- Arquivos só são **commitados no checkpoint** — sem checkpoint, nada aparece no S3.
- Esquema `s3://` funciona no Managed Flink (plugin S3 incluso no runtime).

## Janelas (equivalente às do Stream Analytics)

| Stream Analytics | Flink SQL (TVF) |
|---|---|
| `TumblingWindow(minute, 5)` | `TUMBLE(TABLE t, DESCRIPTOR(ts), INTERVAL '5' MINUTES)` |
| `HoppingWindow(minute, 10, 5)` | `HOP(TABLE t, DESCRIPTOR(ts), INTERVAL '5' MINUTES, INTERVAL '10' MINUTES)` (slide, size) |
| `SlidingWindow` | `OVER (... RANGE BETWEEN INTERVAL ... PRECEDING AND CURRENT ROW)` |
| `SessionWindow` | `SESSION(TABLE t PARTITION BY k, DESCRIPTOR(ts), INTERVAL '5' MINUTES)` (TVF em streaming: 1.19+, a validar) |
| `TIMESTAMP BY ts` | `WATERMARK FOR ts AS ts - INTERVAL 'n' SECOND` |

```sql
INSERT INTO vendas_5min
SELECT window_start, window_end, loja_id, CAST(NULL AS STRING), COUNT(*),
       DATE_FORMAT(window_start, 'yyyy-MM-dd')
FROM TABLE(TUMBLE(TABLE pedidos, DESCRIPTOR(ts_evento), INTERVAL '5' MINUTES))
GROUP BY window_start, window_end, loja_id;
```

## Tempo de evento × processamento

- Event time (`WATERMARK`) = resultado determinístico, tolera atraso até o limite.
- Processing time (`PROCTIME()`) = necessário para **lookup join**.
- Eventos além do watermark são descartados nas janelas — monitore `numLateRecordsDropped`.

## Path pattern (paralelo com o ASA)

O "path pattern" `{date}/{time}` do Stream Analytics não existe no Flink. Equivalentes:

- **Saída:** `PARTITIONED BY (dt)` + coluna derivada → `.../dt=2026-10-16/`.
- **Reference data por data:** apontar `path` para prefixo e reler (restart) ou usar
  `source.monitor-interval` para descobrir arquivos novos (ver `patterns/reference-data.md`).
