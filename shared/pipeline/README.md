# Pipeline Databricks - Delta Live Tables (Lakeflow)

Scripts SQL de processamento para o Databricks Lakehouse utilizando **Lakeflow Spark Declarative Pipelines** (DLT).

---

## Visão Geral

Esta pasta implementa a **Arquitetura Medalhão**:

```
Bronze Layer → Silver Layer → Gold Layer
(Raw/ODS)      (Cleaned)       (Aggregated)
```

Recursos utilizados:
- **Auto Loader** / streaming tables para ingestão incremental
- **CDC** (`APPLY CHANGES`) para Postgres via Airbyte, e para Oracle via Debezium/Kafka Connect (lido direto de tópico Kafka com `read_kafka()`)
- **Expectations** para qualidade de dados
- **Unity Catalog** para governança

Tabelas Silver/Bronze são nomeadas por **domínio de negócio** (ex.: `silver_orders`), não por sistema de origem — ver `docs/MODELO_CONCEITUAL_UBER_EATS.md` e `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md` (Onda 3) para o histórico da convenção.

---

## Estrutura Atual

```
pipeline/
├── bronze/          # ODS: users/drivers (Postgres, CDC via Airbyte); restaurants/products/inventory/orders/payments/order_items/receipts (Oracle, CDC via Debezium/Kafka Connect)
├── silver/          # Limpeza e tipagem, nomeada por domínio
└── gold/            # Métricas de negócio
```

---

## Fontes de dados: o que o Docker sobe vs. o que está no MinIO

| Tipo | Onde vive | Como acessar |
|------|-----------|--------------|
| **Postgres OLTP** | Container `postgres-ubereats` | DBeaver em `localhost:5432` ou Airbyte → Databricks `raw` |
| **Oracle OLTP** | Container `oracle-ubereats` (sob demanda — ver `docker-compose.yml`) | SQL*Plus/DBeaver em `localhost:1521/FREEPDB1`, ou Debezium/Kafka Connect → tópicos no Redpanda → Bronze via `read_kafka()` |
| **MySQL, MongoDB, Kafka (lógicos, o que sobrou)** | **Embarcados no MinIO** | Bucket `uber-eats`, prefixos S3 (ex.: `kafka/route/`, `mysql/menu/`, `mongodb/support/`, `kafka/gps/`) — Pedido, Pagamento, Item de Pedido e Recibo saíram daqui na Onda 3/Etapa 3 e agora vivem no Oracle |
| **MongoDB (satélite documental)** | Container `mongo-ubereats` (sob demanda) | Cadastro estático "Perfil de Restaurante" (menu + horários), lido via Lakehouse Federation |

> **Importante:** os scripts Silver com nomes `ingestion_kafka_*`, `ingestion_mysql_*` ou `ingestion_mongodb_*` que restam **não exigem** instalar MySQL, MongoDB ou Kafka no Docker — modelam a **origem lógica** dos JSONs que o ShadowTraffic grava no MinIO. Já os scripts `ingestion_oracle_*`/`ingest_oracle_*` leem de um Oracle **real**, via CDC real.

Lista de prefixos no bucket: veja [docs/minio/README.md](../docs/minio/README.md).

---

## Como Usar no Lakeflow

1. Acesse o Databricks Workspace
2. **Workflows → Lakeflow / ETL Pipeline** → novo pipeline (SQL)
3. Anexe os scripts nesta ordem: `bronze/` → `silver/` → `gold/`
4. Configure o **target** (catalog/schema, ex.: `uber_eats`)
5. Garanta que o Airbyte (ou ingestão equivalente) populou o schema `raw` antes de executar Bronze/Silver que leem `uber_eats.raw.*`
6. Execute o pipeline

---

## Referências no Repositório

- `.cursor/kb/how_construct_dlt.md` — tutorial DLT, CDC e Auto Loader
- `.cursor/kb/project_architecture.md` — arquitetura end-to-end
- `docs/airbyte/README.md` — ingestão Postgres e MinIO → Databricks

---

## Links Externos

- [Delta Live Tables](https://docs.databricks.com/delta-live-tables/)
- [Auto Loader](https://docs.databricks.com/ingestion/auto-loader/)
- [Unity Catalog](https://docs.databricks.com/data-governance/unity-catalog/)
- [Arquitetura Medalhão](https://www.databricks.com/glossary/medallion-architecture)
