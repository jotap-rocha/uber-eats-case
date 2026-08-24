# Databricks Knowledge Base

> **Purpose**: Comprehensive reference for the Databricks Data Intelligence Platform — architecture, Spark, Delta Lake, Unity Catalog, MLflow, DLT/Lakeflow, streaming, jobs, security, and CI/CD
> **MCP Validated**: 2026-04-20

## Quick Navigation

### Concepts (core platform knowledge)

| File | Purpose |
|------|---------|
| [concepts/architecture.md](concepts/architecture.md) | Workspace hierarchy, cluster types, DBFS vs Volumes, Repos, runtimes |
| [concepts/spark-core.md](concepts/spark-core.md) | SparkSession, DataFrame API, lazy eval, DAG, transformations, actions |
| [concepts/delta-lake.md](concepts/delta-lake.md) | Delta format, ACID, time travel, schema evolution, Z-ordering, CDF |
| [concepts/unity-catalog.md](concepts/unity-catalog.md) | 3-level namespace, metastore, grants, lineage, volumes, Delta Sharing |
| [concepts/clusters.md](concepts/clusters.md) | All-purpose vs job clusters, autoscaling, pools, Photon, spot, policies |
| [concepts/notebooks.md](concepts/notebooks.md) | Magic commands, widgets, dbutils, display(), %run, Databricks Connect |
| [concepts/jobs-workflows.md](concepts/jobs-workflows.md) | Task types, dependencies, triggers, notifications, repair/re-run |
| [concepts/lakeflow.md](concepts/lakeflow.md) | DLT / Lakeflow: streaming tables, materialized views, expectations, CDC |
| [concepts/mlflow.md](concepts/mlflow.md) | Experiments, runs, autologging, model flavors, Registry (UC), serving |
| [concepts/feature-store.md](concepts/feature-store.md) | Feature tables, point-in-time lookups, training sets, online store |
| [concepts/sql-warehouse.md](concepts/sql-warehouse.md) | Serverless SQL, DBSQL, dashboards, alerts, Lakehouse Federation |
| [concepts/streaming.md](concepts/streaming.md) | Structured Streaming, triggers, watermarks, checkpoints, Kafka, Auto Loader |
| [concepts/security.md](concepts/security.md) | PAT/OAuth, secrets, cluster policies, PrivateLink, audit logs, UC grants |

**Continuações (arquivos extra, por baixo do limite de linhas da KB):**  
`spark-core-dataframe-operations`, `delta-lake-maintenance-advanced`, `unity-catalog-delta-sharing`, `clusters-policies-init-scripts`, `notebooks-display-connect`, `jobs-workflows-triggers-notifications`, `lakeflow-pipeline-modes-cdc`, `mlflow-registry-serving`, `feature-store-training-online`, `sql-warehouse-federation-views`, `streaming-kafka-autoloader-stateful`, `security-network-audit-uc` — listados em [`_index.yaml`](../_index.yaml) no domínio `databricks`.

**Genie (sala conversacional):** ver domínio dedicado [../databricks_genie/index.md](../databricks_genie/index.md) — Genie Space, knowledge store, instruções, limites e Agent mode.

### Patterns (production-ready implementations)

| File | Purpose |
|------|---------|
| [patterns/medallion-architecture.md](patterns/medallion-architecture.md) | Bronze/Silver/Gold full pipeline with Delta MERGE + SCD Type 1 & 2 |
| [patterns/etl-pipeline.md](patterns/etl-pipeline.md) | PySpark ETL: schema, multi-source read, transforms, window funcs, UDFs |
| [patterns/incremental-load.md](patterns/incremental-load.md) | Auto Loader, MERGE INTO upserts, watermarks, CDC (Debezium → Kafka) |
| [patterns/dlt-pipeline.md](patterns/dlt-pipeline.md) | Complete DLT pipeline: Bronze→Silver→Gold, expectations, CDC, config |
| [patterns/spark-optimization.md](patterns/spark-optimization.md) | Partitioning, caching, broadcast joins, AQE, skew salting, Z-ordering |
| [patterns/mlops-pipeline.md](patterns/mlops-pipeline.md) | Feature Store → MLflow training → Registry → serving → monitoring |
| [patterns/databricks-asset-bundles.md](patterns/databricks-asset-bundles.md) | DABs: bundle.yml, environments, CI/CD with GitHub Actions |

**Patterns (continuação):** `etl-pipeline-windows-udfs`, `incremental-load-cdc-kafka`, `dlt-pipeline-bundle-config`, `spark-optimization-skew-clustering`, `mlops-pipeline-registry-serving`, `databricks-asset-bundles-cli-cicd` — ver `_index.yaml`.

---

## Capability Map

```text
Databricks Platform
│
├── Data Ingestion
│     ├── Auto Loader (cloudFiles)  → streaming/incremental file ingest
│     ├── Lakeflow Connect          → enterprise connectors (SaaS, DBs)
│     └── Kafka / Event Hubs       → streaming message buses
│
├── Storage & Format
│     ├── Delta Lake                → ACID, time travel, schema evolution
│     ├── Unity Catalog Volumes     → unstructured files (not tables)
│     └── External Locations        → cloud storage paths
│
├── Processing
│     ├── PySpark / Scala Spark     → distributed batch processing
│     ├── Structured Streaming      → micro-batch and continuous streaming
│     ├── Lakeflow (DLT)            → declarative pipeline framework
│     └── SQL Warehouses            → SQL analytics (serverless + classic)
│
├── Governance
│     ├── Unity Catalog             → GRANT/REVOKE, lineage, discovery
│     ├── Delta Sharing             → cross-organization data sharing
│     └── Audit Logs (system.access) → who accessed what, when
│
├── Machine Learning
│     ├── MLflow Tracking           → experiments, runs, metrics
│     ├── Model Registry (UC)       → versioning, aliases, governance
│     ├── Mosaic AI Feature Store   → feature tables, point-in-time
│     └── Model Serving             → REST API endpoints
│
├── Orchestration
│     ├── Databricks Jobs           → multi-task workflows, scheduling
│     └── Databricks Asset Bundles  → CI/CD, IaC for Databricks resources
│
└── Security
      ├── Unity Catalog RBAC        → table/schema/catalog grants
      ├── Databricks Secrets        → credential management
      ├── Network Isolation         → VPC injection, PrivateLink
      └── Cluster Policies          → guardrails for compute
```

---

## Key Concepts Summary

| Concept | Description |
|---------|-------------|
| **Delta Lake** | Open-source storage layer: Parquet + `_delta_log/` = ACID on data lakes |
| **Unity Catalog** | Centralized governance: `catalog.schema.table` 3-level namespace |
| **Lakeflow DLT** | Declarative pipelines: declare what data looks like, not how to compute it |
| **Medallion** | Bronze (raw) → Silver (cleaned) → Gold (aggregated) layered architecture |
| **Auto Loader** | `cloudFiles` format for incremental, scalable file ingestion |
| **Photon** | Native C++ vectorized engine for SQL/Delta workloads (2-12x speedup) |
| **Liquid Clustering** | Modern alternative to Z-ordering: incremental, auto-maintained |
| **AQE** | Adaptive Query Execution: runtime plan optimization (enabled by default) |
| **MLflow Registry** | UC-backed model versioning with aliases (champion/challenger) |
| **DABs** | Databricks Asset Bundles: YAML-based IaC for jobs, pipelines, models |

---

## Learning Path

| Level | Files |
|-------|-------|
| **Beginner** | concepts/architecture.md → concepts/spark-core.md → concepts/delta-lake.md → concepts/notebooks.md |
| **Intermediate** | concepts/unity-catalog.md → concepts/clusters.md → concepts/jobs-workflows.md → patterns/medallion-architecture.md |
| **Advanced** | concepts/lakeflow.md → concepts/streaming.md → patterns/dlt-pipeline.md → patterns/mlops-pipeline.md → patterns/databricks-asset-bundles.md |

---

## Deprecated Features to Avoid

| Deprecated | Replacement | Notes |
|-----------|-------------|-------|
| DBFS root (`dbfs:/`) | Unity Catalog Volumes | No governance |
| Hive metastore | Unity Catalog | Per-workspace, no lineage |
| Model Registry stages (Staging/Production) | Aliases (`champion`, `challenger`) | UC registry uses aliases |
| `%pip dbutils.library.installPyPI` | `%pip install` | Legacy API |
| `trigger(once=True)` | `trigger(availableNow=True)` | More efficient |
| Z-ordering (new tables) | Liquid Clustering (DBR 13.3+) | Better for high-cardinality |

---

## Quick Reference

- [quick-reference.md](quick-reference.md) — Magic commands, Spark configs, SQL cheat sheet

---

## Agent Usage

| Agent | Primary Files | Use Case |
|-------|---------------|----------|
| ai-data-engineer | All | Data pipeline design and implementation |
| kb-architect | All | KB creation and maintenance |
