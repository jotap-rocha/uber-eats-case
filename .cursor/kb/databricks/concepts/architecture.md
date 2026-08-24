# Databricks Platform Architecture

> **Purpose**: Understand the full Databricks platform hierarchy — workspace, clusters, Unity Catalog, DBFS, Repos, and runtime types
> **Confidence**: 0.95
> **MCP Validated**: 2026-04-20

## Overview

Databricks is a unified data intelligence platform built on Apache Spark and Delta Lake. It has two planes: the **Control Plane** (managed by Databricks — UI, job scheduler, cluster manager) and the **Data Plane** (in your cloud account — compute clusters, object storage, Delta tables). Unity Catalog provides centralized governance across all workspaces in an account.

## Workspace Hierarchy

```text
Account (Databricks account — billing, identity, metastore assignment)
  └── Workspace (isolated environment per team/project)
        ├── Catalog (Unity Catalog — top-level namespace)
        │     └── Schema (database)
        │           ├── Table / View / Materialized View
        │           ├── Volume (file storage in UC)
        │           ├── Function (UDF)
        │           └── Model (ML model)
        ├── Clusters (compute resources)
        ├── Notebooks
        ├── Jobs / Workflows
        ├── Repos (Git integration)
        └── SQL Warehouses
```

## Cluster Types

| Type | Use Case | Cost | Lifecycle |
|------|----------|------|-----------|
| All-purpose | Interactive notebooks, development | Higher (runs idle) | Manual start/stop |
| Job cluster | Production jobs, pipelines | Lower (terminates after job) | Auto-terminated |
| SQL Warehouse (serverless) | DBSQL queries, dashboards | Pay-per-query | Auto-suspend |
| Instance Pool | Pre-warm VMs for faster startup | Pool idle cost | Always available |

**Rule:** Use all-purpose for development; job clusters for production to minimize cost.

## DBFS vs Unity Catalog Volumes

```python
# DBFS — LEGACY, avoid for new workloads (deprecated path)
df = spark.read.csv("dbfs:/FileStore/my-data.csv")

# Unity Catalog Volumes — RECOMMENDED (DBR 13.3+)
df = spark.read.csv("/Volumes/catalog/schema/volume/my-data.csv")

# dbutils with Volumes
dbutils.fs.ls("/Volumes/catalog/schema/volume/")
```

| Feature | DBFS | UC Volumes |
|---------|------|-----------|
| Governance | None | Full UC ACLs |
| Cross-workspace | No | Yes |
| Audit logs | No | Yes |
| Recommended | No (legacy) | Yes |

## Databricks Repos (Git Integration)

```python
# Repos mount a Git repository into the workspace
# Path: /Repos/{user_or_folder}/{repo_name}/

# Files in repos are version-controlled
# Supports: GitHub, GitLab, Bitbucket, Azure DevOps

# Best practice: use Databricks Asset Bundles (DABs)
# for CI/CD deployment instead of Repos alone
```

## Runtime Versions

| Runtime | Description | Use When |
|---------|-------------|----------|
| DBR (e.g., 15.4 LTS) | Standard Spark + Python | General workloads |
| DBR ML (e.g., 15.4 LTS ML) | + MLflow, sklearn, TensorFlow, PyTorch | ML training |
| Photon Runtime | DBR + Photon C++ engine | SQL-heavy, Delta reads/writes |
| DBR for Genomics | + bioinformatics libs | Life sciences |

**LTS versions** (Long-Term Support): recommended for production — 2-year support window.

## Control vs Data Plane

```text
Control Plane (Databricks-managed, in Databricks cloud account)
  ├── Web Application (UI)
  ├── Cluster Manager
  ├── Job Scheduler
  ├── Notebook Server
  └── REST API Gateway

Data Plane (Customer cloud account — AWS/Azure/GCP)
  ├── Compute Clusters (EC2/VMs)
  ├── Object Storage (S3/ADLS/GCS)
  ├── Delta Tables
  └── Network (VPC/VNET)
```

**Security implication:** Customer data never leaves the data plane. Databricks only sends orchestration commands from the control plane.

## Common Mistakes

### Wrong
```python
# Storing data in DBFS root (unmanaged, no governance)
df.write.save("dbfs:/user/hive/warehouse/my_table")
```

### Correct
```python
# Use Unity Catalog managed tables (UC handles storage location)
df.write.format("delta").saveAsTable("catalog.schema.my_table")
```

## Related

- [concepts/unity-catalog.md](unity-catalog.md)
- [concepts/clusters.md](clusters.md)
- [patterns/medallion-architecture.md](../patterns/medallion-architecture.md)
