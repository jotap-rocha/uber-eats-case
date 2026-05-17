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
- **CDC** (`APPLY CHANGES`) para Postgres via Airbyte
- **Expectations** para qualidade de dados
- **Unity Catalog** para governança

---

## Estrutura Atual

```
pipeline/
├── bronze/          # ODS Postgres (CDC): users, drivers
├── silver/          # Limpeza e tipagem (18 scripts)
└── gold/            # Métricas de negócio (3 scripts)
```

---

## Fontes de dados: o que o Docker sobe vs. o que está no MinIO

| Tipo | Onde vive | Como acessar |
|------|-----------|--------------|
| **Postgres OLTP** | Container `postgres-ubereats` | DBeaver em `localhost:5432` ou Airbyte → Databricks `raw` |
| **MySQL, MongoDB, Kafka (lógicos)** | **Embarcados no MinIO** | Bucket `uber-eats`, prefixos S3 (ex.: `kafka/orders/`, `mysql/restaurants/`, `mongodb/items/`) |

> **Importante:** Os scripts Silver com nomes `ingestion_kafka_*`, `ingestion_mysql_*` ou `ingestion_mongodb_*` **não exigem** instalar MySQL, MongoDB ou Kafka no Docker. Eles modelam a **origem lógica** dos JSONs que o ShadowTraffic já grava no MinIO (`gen/minio/uber-eats.json`). Em produção, esses dados viriam de sistemas reais; no projeto local, o MinIO concentra todas essas “fontes” simuladas.

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
