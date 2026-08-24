# Unity Catalog

> **Purpose**: Master Unity Catalog — 3-level namespace, metastore, privilege model, data lineage, volumes, and Delta Sharing
> **Confidence**: 0.95
> **MCP Validated**: 2026-04-20

## Overview

Unity Catalog (UC) is Databricks' centralized governance layer for all data and AI assets. It provides a 3-level namespace (`catalog.schema.table`), fine-grained access control via GRANT/REVOKE, automatic column and table lineage, and cross-workspace sharing. One metastore per cloud region is assigned to all workspaces in an account.

## 3-Level Namespace

```sql
-- Full reference: catalog.schema.object
SELECT * FROM prod_catalog.sales.orders;
SELECT * FROM dev_catalog.analytics.daily_summary;

-- Create assets
CREATE CATALOG dev_catalog;
CREATE SCHEMA dev_catalog.analytics;
CREATE TABLE dev_catalog.analytics.daily_summary (
    date     DATE,
    revenue  DOUBLE,
    orders   BIGINT
) USING DELTA;
```

## Metastore Architecture

```text
Account
  └── Metastore (1 per region — shared across workspaces)
        ├── Workspace A (assigned to metastore)
        ├── Workspace B (assigned to metastore)
        └── Catalogs
              ├── main (default catalog)
              ├── prod_catalog
              └── dev_catalog
```

## Privilege Model

```sql
-- Account admin → Metastore admin → Catalog owner → Schema owner → Table owner

-- GRANT permissions
GRANT USE_CATALOG ON CATALOG prod_catalog TO `analyst-group`;
GRANT USE_SCHEMA  ON SCHEMA  prod_catalog.sales TO `analyst-group`;
GRANT SELECT      ON TABLE   prod_catalog.sales.orders TO `analyst-group`;

-- Grant on schema (inherits to all tables)
GRANT SELECT ON SCHEMA prod_catalog.sales TO `data-science-team`;

-- Revoke
REVOKE SELECT ON TABLE prod_catalog.sales.orders FROM `analyst-group`;

-- Show grants
SHOW GRANTS ON TABLE prod_catalog.sales.orders;

-- Privilege levels (most to least)
-- CREATE, MODIFY, SELECT, READ_VOLUME, WRITE_VOLUME, USE_SCHEMA, USE_CATALOG
```

## Data Lineage

```python
# Lineage is automatic — no code required
# Databricks captures column-level lineage for:
#   - Spark DataFrame operations
#   - SQL queries in notebooks and SQL warehouses
#   - DLT pipelines

# View lineage in Databricks UI:
# Catalog Explorer → select table → Lineage tab

# Lineage API (REST)
# GET /api/2.0/lineage-tracking/table-lineage?table_name=catalog.schema.table
```

## External Locations and Storage Credentials

```sql
-- Storage credential (IAM role / service principal)
CREATE STORAGE CREDENTIAL my_s3_cred
WITH IAM_ROLE 'arn:aws:iam::123456789:role/databricks-s3-role';

-- External location (maps cloud path to UC path)
CREATE EXTERNAL LOCATION my_external_loc
URL 's3://my-bucket/external-data/'
WITH (STORAGE CREDENTIAL my_s3_cred);

-- External table using external location
CREATE TABLE catalog.schema.ext_orders
USING DELTA
LOCATION 's3://my-bucket/external-data/orders/';
```

## Volumes vs External Tables

```python
# Volumes — for unstructured / semi-structured files (not tables)
# Managed volume — UC manages storage
CREATE VOLUME catalog.schema.my_volume;

# Access files
dbutils.fs.ls("/Volumes/catalog/schema/my_volume/")
df = spark.read.csv("/Volumes/catalog/schema/my_volume/data.csv")

# External volume — points to existing cloud storage
CREATE EXTERNAL VOLUME catalog.schema.ext_volume
URL 's3://my-bucket/raw-files/'
WITH (STORAGE CREDENTIAL my_s3_cred);
```

| Feature | Managed Table | External Table | Volume |
|---------|--------------|----------------|--------|
| Storage managed by UC | Yes | No | Yes (managed vol) |
| Governed by UC | Yes | Yes | Yes |
| For tabular data | Yes | Yes | No |
| For files (CSV, images, etc.) | No | No | Yes |
| DROP deletes data | Yes | No (just metadata) | Yes (managed) |

## Delta Sharing e erros comuns

Ver continuação: [unity-catalog-delta-sharing.md](unity-catalog-delta-sharing.md).

## Related

- [concepts/architecture.md](architecture.md)
- [concepts/security.md](security.md)
- [concepts/clusters.md](clusters.md)
