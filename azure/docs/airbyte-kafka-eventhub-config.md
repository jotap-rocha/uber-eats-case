# Airbyte — destino Kafka (Event Hub) para Postgres CDC real-time (Azure, Fase 1)

> Complementa `docs/airbyte/README.md` (que documenta o destino "Databricks Lakehouse" já usado hoje na Fase 0). Este destino é **novo**, exclusivo do trilho real-time desta fase — ver `DESIGN_INGESTAO_AZURE_FASE1.md`, Decisão 1.

## Configurar o destino "Kafka"

1. Destinations → + New destination → **Kafka**
2. Preencha:
   - **Bootstrap servers**: `<AZURE_EVENTHUB_NAMESPACE>.servicebus.windows.net:9093`
   - **Topic pattern**: `postgres.{namespace}.{stream}` (gera `postgres.public.drivers`, `postgres.public.users` — mesmo padrão de nome de tópico esperado pelo Kafka Connect Sink Connector, ver `debezium/adls-sink-connector.json.template`)
   - **Protocol**: `SASL_SSL`
   - **SASL mechanism**: `PLAIN`
   - **SASL JAAS config**: `org.apache.kafka.common.security.plain.PlainLoginModule required username="$ConnectionString" password="<AZURE_EVENTHUB_CONNECTION_STRING>";`
3. Test connection → Set up

## Criar a conexão (Postgres → Kafka/Event Hub)

1. Connections → + New connection
2. Selecione: PostgreSQL (a mesma source já configurada em `docs/airbyte/README.md`) → Kafka
3. Configure:
   - **Sync mode**: `Incremental | Append` com **CDC** habilitado (replication slot dedicado — usar um nome de slot diferente do já usado pela sync direta Postgres→Databricks da Fase 0, ex. `ubereats_airbyte_azure_slot`)
   - **Frequency**: contínua (CDC), não agendada
4. Selecione tabelas: `drivers`, `users`
5. Set up connection

## Validação

1. Fazer um `UPDATE` real em `drivers`/`users` no Postgres.
2. Confirmar no Azure Portal (Event Hubs → `postgres` → Métricas) que uma mensagem chegou em poucos segundos.
3. Confirmar que a mensagem carrega os campos `_ab_cdc_operation`/`_ab_cdc_updated_at`/`_ab_cdc_lsn` — ver `docs/data-contract-cdc-azure.md`.

## Atenção — replication slot dedicado

Este é um **novo** replication slot no Postgres, adicional ao já usado pela sync direta Airbyte→Databricks da Fase 0 (que continua rodando, sem ser desligada por esta feature). São 2 replication slots simultâneos nesta fonte — aceitável, dado que o Postgres suporta múltiplos slots concorrentes nativamente (diferente do Oracle/LogMiner, mais sensível a concorrência — ver `docs/data-contract-cdc-azure.md` e `BUILD_REPORT_INGESTAO_AZURE_FASE1.md`).
