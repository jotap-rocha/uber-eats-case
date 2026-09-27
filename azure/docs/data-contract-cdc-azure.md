# Contrato de CDC — Fase 1 (Azure): sem mapeamento novo

> Extensão do contrato canônico de CDC definido na Onda 3 (`DESIGN_DIVERSIFICACAO_FONTES_UBEREATS.md`). Ver `DESIGN_INGESTAO_AZURE_FASE1.md` para o desenho completo.

**Achado favorável desta fase:** ao contrário da AWS (`docs/data-contract-cdc-aws-dms.md`) e da GCP (`docs/data-contract-cdc-gcp-datastream.md`), que precisaram mapear os metadados proprietários de ferramentas novas (DMS, Datastream), a Fase 1 **reaproveita as mesmas ferramentas já mapeadas na Onda 3** — Airbyte para Postgres, Debezium/Kafka Connect para Oracle. O mapeamento abaixo é **idêntico** ao que já roda em produção local (`pipeline/bronze/ingest_postgres_drivers.sql`, `pipeline/bronze/ingest_oracle_orders.sql`); só o meio físico muda.

| Coluna canônica | Postgres (Airbyte) | Oracle (Debezium) |
|---|---|---|
| `cdc_operation` | `_ab_cdc_deleted_at` (`NULL` → `u`, preenchido → `d`) | `payload.op` (`c`/`u`/`d`) |
| `cdc_commit_ts` | `_ab_cdc_updated_at` | `payload.source.ts_ms` |
| `cdc_sequence` | `_ab_cdc_lsn` | `payload.source.scn` |
| `cdc_source_system` | constante `'postgres-ubereats'` | constante `'oracle-ubereats'` |

## O que muda de fato: o meio físico, não o mapeamento

| Onde o dado aparece | Antes (Fase 0, local) | Agora (Fase 1, Azure) |
|---|---|---|
| Postgres — real-time | Sync direto Airbyte → tabela `uber_eats.raw.drivers`/`users` | Airbyte destino "Kafka" → tópico `postgres` do Event Hub |
| Postgres — batch/Bronze | (não existia — só a via direta acima) | Kafka Connect Sink Connector consumindo o mesmo tópico → arquivo JSON no ADLS Gen2/Bronze |
| Oracle — real-time e batch | `read_kafka()` direto do tópico Redpanda (`oracle.UBEREATS.*`) | Debezium/Kafka Connect publica no tópico `oracle` do Event Hub; o mesmo Sink Connector consome e grava no ADLS |

Em ambos os casos, o arquivo/registro pousado carrega **exatamente os mesmos campos** (`_ab_cdc_*`/`payload.*`) que a Bronze já sabe interpretar — a Silver continua sem ler o formato nativo diretamente, mesma disciplina desde a Onda 3.

## MongoDB e MinIO — sem CDC (decisão já fechada)

MongoDB é fonte estática (snapshot/full-refresh, sem CDC — decisão da Onda 3); `cdc_operation` é sempre `u` (upsert lógico) e `cdc_sequence` não resolve conflito de ordenação real, só mantém a coluna presente no schema. MinIO não tem CDC (não é motor de banco de dados) — a sync do Airbyte trata cada objeto como um registro completo, sem histórico de mutação.

## Risco não confirmado — validar no início do próximo ciclo

O comportamento do Kafka Connect HDFS 2 Sink Connector consumindo diretamente do Event Hub (protocolo Kafka) e escrevendo em `abfss://` via a interface Hadoop `FileSystem` é uma composição de dois componentes largamente documentados individualmente, mas **não testada de ponta a ponta neste projeto ainda** — mesmo padrão de risco já registrado nos Designs da Onda 3, da Fase 2/AWS e da Fase 3/GCP para suas respectivas ferramentas novas. Confirmar com um teste real (Event Hub Standard tier + sink ativo + `UPDATE` real na fonte) antes de considerar o mapeamento definitivo em produção.
