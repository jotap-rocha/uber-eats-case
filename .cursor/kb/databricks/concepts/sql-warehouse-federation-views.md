# SQL Warehouse — alertas, federation e *materialized views*

> **Purpose**: Extensão de [sql-warehouse.md](sql-warehouse.md).  
> **Confidence**: 0.95  
> **MCP Validated**: 2026-04-20

## Alerts

```sql
-- Alertas executam query agendada e notificam quando o limiar é atingido
```

## Lakehouse Federation (Query External Databases)

```sql
CREATE CONNECTION my_postgres_conn
TYPE POSTGRESQL
OPTIONS (
    host 'mydb.example.com',
    port '5432',
    user 'databricks_user',
    password secret('my-scope', 'pg-password')
);

CREATE FOREIGN CATALOG my_postgres_catalog
USING CONNECTION my_postgres_conn
OPTIONS (database 'production_db');

SELECT * FROM my_postgres_catalog.public.customers LIMIT 100;

SELECT c.customer_id, c.name AS external_name, d.total_spend AS databricks_metric
FROM my_postgres_catalog.public.customers c
JOIN prod_catalog.analytics.customer_metrics d ON c.customer_id = d.customer_id;
```

## Materialized Views in DBSQL (DBR 13.3+)

```sql
CREATE MATERIALIZED VIEW prod_catalog.analytics.daily_revenue
AS
SELECT DATE(order_ts) AS order_date, SUM(amount) AS total_revenue, COUNT(*) AS num_orders
FROM prod_catalog.sales.orders
GROUP BY DATE(order_ts);

REFRESH MATERIALIZED VIEW prod_catalog.analytics.daily_revenue;

SELECT * FROM prod_catalog.analytics.daily_revenue
WHERE order_date >= CURRENT_DATE - INTERVAL 30 DAYS;
```

## Decision Matrix

| Use Case | Choose |
|----------|--------|
| Ad-hoc SQL exploration | DBSQL SQL Editor + serverless warehouse |
| BI dashboards | AI/BI Dashboards + dedicated warehouse |
| ETL jobs with SQL tasks | SQL task in Databricks Jobs |
| Querying external DB | Lakehouse Federation |
| Precomputed aggregations | Materialized views |
| Real-time KPI alerts | DBSQL Alerts |

## Related

- [sql-warehouse.md](sql-warehouse.md)
