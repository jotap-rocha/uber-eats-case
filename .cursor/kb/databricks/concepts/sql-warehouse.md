# SQL Warehouses and Databricks SQL

> **Purpose**: Master SQL Warehouses — serverless vs classic, DBSQL, dashboards, alerts, Lakehouse Federation, and materialized views
> **Confidence**: 0.95
> **MCP Validated**: 2026-04-20

## Overview

Databricks SQL (DBSQL) provides a lakehouse SQL experience with serverless SQL Warehouses, a SQL Editor, dashboards, alerts, and AI-assisted queries. Serverless warehouses eliminate infrastructure management — you pay only for query compute. Lakehouse Federation lets you query external databases (PostgreSQL, MySQL, Snowflake) directly from DBSQL.

## Serverless vs Classic Warehouses

| Feature | Serverless | Classic |
|---------|-----------|---------|
| Infrastructure | Databricks-managed | Customer cloud account |
| Start time | ~1 second | ~2-5 minutes |
| Scaling | Instant (no provisioning) | Minutes |
| Cost model | Pay per DBU while running | Pay per DBU + cloud VM cost |
| Networking | Databricks-managed | Requires VPC/VNET setup |
| Recommended | Yes (for most workloads) | When network isolation required |

## Warehouse Sizes and Auto-Stop

```sql
-- Warehouse sizes map to vCPU allocation per cluster
-- XSmall: 4 vCPU / Small: 8 vCPU / Medium: 16 vCPU / Large: 32 vCPU / XLarge: 64 vCPU

-- Multi-cluster scaling: 1 cluster per ~10 concurrent queries (rule of thumb)
-- Auto-stop: warehouse stops after N minutes of inactivity (default: 10 min)
```

```python
# Create warehouse via API
import requests
response = requests.post(
    f"{DATABRICKS_URL}/api/2.0/sql/warehouses",
    headers={"Authorization": f"Bearer {TOKEN}"},
    json={
        "name": "analytics-warehouse",
        "cluster_size": "Small",
        "min_num_clusters": 1,
        "max_num_clusters": 3,
        "auto_stop_mins": 15,
        "warehouse_type": "PRO",  # CLASSIC or PRO (enables serverless features)
        "enable_serverless_compute": True,
    }
)
```

## SQL Editor and Queries

```sql
-- DBSQL SQL Editor supports:
-- - Full ANSI SQL + Databricks SQL extensions
-- - Query parameters using {{ param_name }} syntax
-- - Results visualization (table, bar, line, pie charts)
-- - Saved queries and query folders

-- Example with parameters (DBSQL query parameter syntax)
SELECT
    order_date,
    SUM(amount) AS daily_revenue,
    COUNT(*) AS num_orders
FROM prod_catalog.sales.orders
WHERE
    order_date BETWEEN '{{ start_date }}' AND '{{ end_date }}'
    AND status = '{{ status }}'
GROUP BY order_date
ORDER BY order_date;
```

## DBSQL Dashboards

```python
# Dashboards in Databricks SQL (AI/BI Dashboards — DBR 14.3+)
# Modern dashboard builder with natural language data exploration
# AI/BI Dashboards recommended for new dashboards; Genie para NL queries
```

## Alertas, Lakehouse Federation e *materialized views*

Continuação: [sql-warehouse-federation-views.md](sql-warehouse-federation-views.md).

## Related

- [concepts/unity-catalog.md](unity-catalog.md)
- [concepts/delta-lake.md](delta-lake.md)
- [concepts/clusters.md](clusters.md)
