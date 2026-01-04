# SQL Development for Lakeflow Pipelines

> Source: https://docs.databricks.com/aws/en/dlt/sql-dev

## Pipeline Creation Syntax

### Streaming Tables

```sql
CREATE OR REFRESH STREAMING TABLE table_name
AS SELECT * FROM source
```

### Materialized Views

```sql
CREATE OR REFRESH MATERIALIZED VIEW view_name
AS SELECT * FROM source
```

## Data Loading Methods

### Using Auto Loader (read_files)

```sql
CREATE OR REFRESH STREAMING TABLE orders AS
SELECT *
FROM STREAM read_files(
    "/path/to/data",
    format => "json"
)
```

### Supported Formats

- JSON
- CSV
- Parquet
- Avro
- Delta
- Text

### Read Files Options

```sql
CREATE OR REFRESH STREAMING TABLE customers AS
SELECT *
FROM STREAM read_files(
    "s3://bucket/customers/",
    format => "json",
    schemaLocation => "/tmp/schema/customers",
    cloudFiles.inferColumnTypes => "true"
)
```

## Data Quality Expectations

### Basic Constraints

```sql
CREATE OR REFRESH STREAMING TABLE orders(
    CONSTRAINT valid_date
    EXPECT (order_datetime IS NOT NULL)
)
AS SELECT * FROM source
```

### Drop Invalid Rows

```sql
CREATE OR REFRESH STREAMING TABLE clean_orders(
    CONSTRAINT valid_id
    EXPECT (order_id IS NOT NULL)
    ON VIOLATION DROP ROW,

    CONSTRAINT positive_amount
    EXPECT (amount > 0)
    ON VIOLATION DROP ROW
)
AS SELECT * FROM raw_orders
```

### Fail on Violation

```sql
CREATE OR REFRESH STREAMING TABLE critical_data(
    CONSTRAINT required_field
    EXPECT (critical_column IS NOT NULL)
    ON VIOLATION FAIL UPDATE
)
AS SELECT * FROM source
```

## Complete Example: Medallion Architecture

### Bronze Layer

```sql
-- Raw data ingestion
CREATE OR REFRESH STREAMING TABLE customers_bronze
COMMENT "Raw customer data from cloud storage"
TBLPROPERTIES (
    "quality" = "bronze",
    "source_system" = "s3"
)
AS
SELECT *
FROM STREAM read_files(
    "s3://bucket/customers/",
    format => "json"
)
```

**Note:** Do NOT use reserved table properties in TBLPROPERTIES:
- `owner` - Automatically set to current user (use `ALTER TABLE SET OWNER TO` instead)
- `location` - Use `LOCATION` clause instead
- `provider` - Use `USING` clause instead
- `external` - Use `CREATE EXTERNAL TABLE` instead

### Silver Layer

```sql
-- Cleaned and validated data
CREATE OR REFRESH STREAMING TABLE customers_silver(
    CONSTRAINT valid_id
    EXPECT (customer_id IS NOT NULL)
    ON VIOLATION DROP ROW,

    CONSTRAINT valid_email
    EXPECT (email LIKE '%@%.%')
    ON VIOLATION DROP ROW
)
COMMENT "Cleaned customer data"
TBLPROPERTIES ("quality" = "silver")
AS
SELECT
    customer_id,
    name,
    email,
    CURRENT_TIMESTAMP() as processed_at
FROM STREAM customers_bronze
```

### Gold Layer

```sql
-- Business aggregations
CREATE OR REFRESH MATERIALIZED VIEW customer_domains
COMMENT "Customer email domains summary"
TBLPROPERTIES ("quality" = "gold")
AS
SELECT
    SPLIT(email, '@')[1] as domain,
    COUNT(*) as customer_count
FROM customers_silver
GROUP BY SPLIT(email, '@')[1]
```

## Parameterization

### Define Parameters

```sql
-- Set configuration values
SET catalog_name = "production";
SET schema_name = "sales";
SET source_path = "s3://bucket/data/";
```

### Use Parameters with String Interpolation

```sql
CREATE OR REFRESH STREAMING TABLE ${catalog_name}.${schema_name}.orders
AS
SELECT *
FROM STREAM read_files(
    "${source_path}orders/",
    format => "json"
)
```

## Change Data Capture (CDC)

### Apply Changes Example

```sql
-- Create target streaming table
CREATE OR REFRESH STREAMING TABLE customers;

-- Apply CDC changes
APPLY CHANGES INTO
    customers
FROM
    STREAM customers_cdc
KEYS
    (customer_id)
SEQUENCE BY
    timestamp
COLUMNS * EXCEPT (operation, timestamp)
STORED AS
    SCD TYPE 1
```

### SCD Type 2 (Historical Tracking)

```sql
CREATE OR REFRESH STREAMING TABLE customers_history;

APPLY CHANGES INTO
    customers_history
FROM
    STREAM customers_cdc
KEYS
    (customer_id)
SEQUENCE BY
    timestamp
STORED AS
    SCD TYPE 2
```

## Advanced Features

### Joins Between Tables

```sql
CREATE OR REFRESH MATERIALIZED VIEW order_details AS
SELECT
    o.order_id,
    o.order_date,
    c.customer_name,
    c.email
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
```

### Window Functions

```sql
CREATE OR REFRESH MATERIALIZED VIEW customer_rankings AS
SELECT
    customer_id,
    total_orders,
    RANK() OVER (ORDER BY total_orders DESC) as rank
FROM (
    SELECT
        customer_id,
        COUNT(*) as total_orders
    FROM orders
    GROUP BY customer_id
)
```

### Aggregations

```sql
CREATE OR REFRESH MATERIALIZED VIEW daily_sales AS
SELECT
    DATE(order_date) as sale_date,
    SUM(amount) as total_sales,
    COUNT(*) as order_count,
    AVG(amount) as avg_order_value
FROM orders
GROUP BY DATE(order_date)
```

## Limitations

### Not Supported

❌ **PIVOT clause** - Not supported in Lakeflow pipelines

❌ **CREATE OR REFRESH LIVE TABLE** - Deprecated syntax (use STREAMING TABLE or MATERIALIZED VIEW)

### Key Differences from Traditional SQL

1. **Dataflow Graph Evaluation** - Evaluates dataset definitions across all source files before execution
2. **Streaming Semantics** - Different behavior for streaming vs batch tables
3. **Incremental Processing** - Automatically handles incremental data

## Best Practices

### ✅ DO

1. **Use STREAMING TABLE** for real-time data
2. **Use MATERIALIZED VIEW** for batch aggregations
3. **Apply expectations** for data quality
4. **Parameterize** pipeline configurations
5. **Document tables** with comments and properties
6. **Use read_files** for cloud storage ingestion

### ❌ DON'T

1. **Don't use PIVOT** (not supported)
2. **Don't mix deprecated syntax** (LIVE TABLE)
3. **Don't skip schema evolution** planning
4. **Don't ignore data quality** expectations

## Performance Tips

1. **Partition large tables** for better query performance
2. **Use Z-ordering** on commonly filtered columns
3. **Leverage Auto Loader** schema inference caching
4. **Monitor pipeline** update durations
5. **Optimize expectations** to avoid unnecessary data scans
