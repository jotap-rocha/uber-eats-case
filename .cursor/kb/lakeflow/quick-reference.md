# Lakeflow Quick Reference Guide

**Fast lookup for common Lakeflow patterns, syntax, and examples**

## 🚀 Core Syntax

### Python Decorators

| Decorator | Purpose | Example |
|-----------|---------|---------|
| `@dlt.table()` | Create materialized view or streaming table | `@dlt.table()` |
| `@dlt.view()` | Create temporary view | `@dlt.view()` |
| `@dlt.expect()` | Warn on violation | `@dlt.expect("rule", "col > 0")` |
| `@dlt.expect_or_drop()` | Drop invalid rows | `@dlt.expect_or_drop("rule", "col IS NOT NULL")` |
| `@dlt.expect_or_fail()` | Fail on violation | `@dlt.expect_or_fail("rule", "col IS NOT NULL")` |
| `@dlt.expect_all()` | Multiple expectations (warn) | `@dlt.expect_all({...})` |
| `@dlt.expect_all_or_drop()` | Multiple expectations (drop) | `@dlt.expect_all_or_drop({...})` |
| `@dlt.expect_all_or_fail()` | Multiple expectations (fail) | `@dlt.expect_all_or_fail({...})` |

### SQL Keywords

| Keyword | Purpose | Example |
|---------|---------|---------|
| `CREATE OR REFRESH STREAMING TABLE` | Create streaming table | `CREATE OR REFRESH STREAMING TABLE orders` |
| `CREATE OR REFRESH MATERIALIZED VIEW` | Create materialized view | `CREATE OR REFRESH MATERIALIZED VIEW summary` |
| `STREAM` | Streaming source | `FROM STREAM read_files(...)` |
| `CONSTRAINT ... EXPECT` | Data quality check | `CONSTRAINT valid_id EXPECT (id IS NOT NULL)` |
| `ON VIOLATION DROP ROW` | Drop invalid records | `ON VIOLATION DROP ROW` |
| `ON VIOLATION FAIL UPDATE` | Fail on invalid records | `ON VIOLATION FAIL UPDATE` |
| `APPLY CHANGES INTO` | CDC processing | `APPLY CHANGES INTO target FROM source` |
| `STORED AS SCD TYPE 1` | Current state tracking | `STORED AS SCD TYPE 1` |
| `STORED AS SCD TYPE 2` | Historical tracking | `STORED AS SCD TYPE 2` |

### Functions

| Function | Purpose | Language |
|----------|---------|----------|
| `dlt.read()` | Read table (batch) | Python |
| `dlt.read_stream()` | Read table (streaming) | Python |
| `dlt.create_streaming_table()` | Create streaming table | Python |
| `dlt.apply_changes()` | Apply CDC changes | Python |
| `dlt.create_auto_cdc_flow()` | AUTO CDC flow | Python |
| `read_files()` | Auto Loader | SQL |

## 📋 Common Patterns

### 1. Medallion Architecture

```python
import dlt
from pyspark.sql import functions as F

# Bronze: Raw ingestion
@dlt.table(comment="Raw data", table_properties={"quality": "bronze"})
def bronze_layer():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "json")
        .load("s3://bucket/raw/")
    )

# Silver: Data quality
@dlt.expect_or_drop("valid_id", "id IS NOT NULL")
@dlt.table(comment="Cleaned data", table_properties={"quality": "silver"})
def silver_layer():
    return dlt.read_stream("bronze_layer")

# Gold: Business logic
@dlt.table(comment="Aggregated data", table_properties={"quality": "gold"})
def gold_layer():
    return (
        spark.read.table("silver_layer")
        .groupBy("category")
        .agg(F.sum("amount").alias("total"))
    )
```

### 2. Change Data Capture (CDC)

```python
# SCD Type 1 (Current state)
dlt.create_streaming_table("customers_current")

dlt.apply_changes(
    target="customers_current",
    source="customers_cdc",
    keys=["customer_id"],
    sequence_by="timestamp",
    apply_as_deletes=F.expr("operation = 'DELETE'"),
    stored_as_scd_type=1
)

# SCD Type 2 (Historical tracking)
dlt.create_streaming_table("customers_history")

dlt.apply_changes(
    target="customers_history",
    source="customers_cdc",
    keys=["customer_id"],
    sequence_by="timestamp",
    stored_as_scd_type=2
)
```

### 3. Data Quality Layers

```python
# Bronze: WARN (track issues)
@dlt.expect("no_rescued_data", "_rescued_data IS NULL")
@dlt.table()
def bronze():
    return spark.readStream.load("s3://bucket/raw/")

# Silver: DROP (remove bad data)
@dlt.expect_or_drop("valid_id", "id IS NOT NULL")
@dlt.expect_or_drop("valid_amount", "amount > 0")
@dlt.table()
def silver():
    return dlt.read_stream("bronze")

# Gold: FAIL (strict validation)
@dlt.expect_or_fail("revenue_check", "total_revenue >= 0")
@dlt.table()
def gold():
    return spark.read.table("silver").groupBy("date").sum("amount")
```

### 4. Auto Loader Ingestion

```python
# Python
@dlt.table()
def incremental_load():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "json")
        .option("cloudFiles.schemaLocation", "/tmp/schema")
        .option("cloudFiles.inferColumnTypes", "true")
        .load("s3://bucket/data/")
    )
```

```sql
-- SQL
CREATE OR REFRESH STREAMING TABLE incremental_load
AS SELECT *
FROM STREAM read_files(
    "s3://bucket/data/",
    format => "json"
)
```

### 5. Parameterized Pipeline

```python
# Get parameters
CATALOG = spark.conf.get("catalog", "production")
SCHEMA = spark.conf.get("schema", "sales")
PATH = spark.conf.get("source_path")

# Use parameters
@dlt.table()
def parameterized_table():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "json")
        .load(PATH)
    )

@dlt.table()
def cross_catalog_join():
    return (
        dlt.read("parameterized_table")
        .join(
            spark.read.table(f"{CATALOG}.{SCHEMA}.customers"),
            "customer_id"
        )
    )
```

### 6. Multiple Expectations

```python
# Grouped expectations
@dlt.expect_all_or_drop({
    "valid_id": "customer_id IS NOT NULL",
    "valid_email": "email LIKE '%@%.%'",
    "valid_age": "age BETWEEN 0 AND 150",
    "recent_date": "created_at >= '2020-01-01'"
})
@dlt.table()
def validated_customers():
    return spark.read.table("raw_customers")
```

## 🔧 Configuration Snippets

### Serverless Pipeline

```json
{
  "name": "my_pipeline",
  "serverless": true,
  "target": "production.sales",
  "configuration": {
    "source_path": "s3://bucket/data/",
    "catalog": "production"
  },
  "libraries": [
    {"notebook": {"path": "/Pipelines/transformations"}}
  ],
  "continuous": false,
  "development": false,
  "channel": "CURRENT",
  "edition": "ADVANCED"
}
```

### Classic Compute Pipeline

```json
{
  "name": "my_pipeline",
  "target": "production.sales",
  "clusters": [
    {
      "label": "default",
      "autoscale": {
        "min_workers": 1,
        "max_workers": 5,
        "mode": "ENHANCED"
      },
      "node_type_id": "i3.xlarge",
      "driver_node_type_id": "i3.xlarge"
    }
  ],
  "photon": true,
  "development": false
}
```

## 🎯 Decision Matrix

### When to Use What

| Use Case | Choose |
|----------|--------|
| **Real-time data processing** | Streaming Table |
| **Batch aggregations** | Materialized View |
| **Track current state** | SCD Type 1 |
| **Track history** | SCD Type 2 |
| **Cloud storage ingestion** | Auto Loader (`cloudFiles`) |
| **Kafka/Kinesis ingestion** | Streaming source |
| **Development** | Development mode, smaller compute |
| **Production** | Serverless, triggered mode |
| **Low latency** | Continuous mode |
| **Cost optimization** | Triggered mode, serverless |
| **Data quality exploration** | `@dlt.expect()` (warn) |
| **Production data quality** | `@dlt.expect_or_drop()` |
| **Critical validation** | `@dlt.expect_or_fail()` |

## ⚠️ Common Pitfalls

### ❌ DON'T

```python
# Don't trigger actions in pipeline code
@dlt.table()
def wrong_pattern():
    df = spark.read.table("source")
    count = df.count()  # ❌ Action in pipeline code
    return df

# Don't define tables twice
@dlt.table()
def customers():
    return spark.read.table("raw")

@dlt.table()  # ❌ Error: customers already defined
def customers():
    return spark.read.table("backup")

# Don't use development mode in production
# ❌ "development": true in production config

# Don't hardcode environment values
@dlt.table()
def hardcoded():
    return spark.read.table("production.sales.customers")  # ❌ Hardcoded

# Don't skip data quality checks
@dlt.table()  # ❌ No quality checks
def unvalidated():
    return spark.read.table("raw_data")

# Don't use reserved table properties
@dlt.table(
    table_properties={
        "quality": "bronze",
        "owner": "team"  # ❌ RESERVED - Use ALTER TABLE SET OWNER TO instead
    }
)
def wrong_properties():
    return spark.read.table("source")
```

**Reserved Table Properties (DO NOT USE):**
- `owner` - Automatically set to current user
- `location` - Use `LOCATION` clause instead
- `provider` - Use `USING` clause instead
- `external` - Use `CREATE EXTERNAL TABLE` instead

### ✅ DO

```python
# Keep operations lazy
@dlt.table()
def correct_pattern():
    return spark.read.table("source")  # ✅ Lazy operation

# Use different table names
@dlt.table()
def customers_primary():
    return spark.read.table("raw")

@dlt.table()
def customers_backup():
    return spark.read.table("backup")

# Use parameters
CATALOG = spark.conf.get("catalog")

@dlt.table()
def parameterized():
    return spark.read.table(f"{CATALOG}.sales.customers")  # ✅ Parameterized

# Apply quality checks
@dlt.expect_or_drop("valid_id", "id IS NOT NULL")
@dlt.table()
def validated():
    return spark.read.table("raw_data")  # ✅ Quality checks applied
```

## 🔍 Troubleshooting Quick Lookup

| Error/Issue | Likely Cause | Solution |
|-------------|--------------|----------|
| **Permission denied** | Missing UC grants | `GRANT USE CATALOG/SCHEMA` |
| **Table already defined** | Duplicate definition | Use different table name |
| **Expectation failures** | Invalid data | Check violation policy, fix data |
| **Slow startup** | Standard serverless mode | Use performance mode if needed |
| **High costs** | Continuous mode | Switch to triggered mode |
| **Schema evolution errors** | Streaming table limitation | Use materialized view or recreate table |
| **Cannot access externally** | Materialized view limitation | Use streaming table or sink API |
| **PIVOT not working** | Not supported | Use CASE statements |
| **Identity column error** | Used with AUTO CDC | Remove identity column |
| **Concurrent update limit** | 200 updates/workspace | Schedule pipelines appropriately |

## 📊 Data Types & Conversions

### Parameters (Always Strings)

```python
# Parameters are strings - convert as needed
limit = int(spark.conf.get("limit_rows", "1000"))
sample_rate = float(spark.conf.get("sample_rate", "0.01"))
enable_feature = spark.conf.get("enable_feature", "true").lower() == "true"
```

### Common Transformations

```python
from pyspark.sql import functions as F

# Date/Time
.withColumn("date", F.to_date("timestamp_col"))
.withColumn("hour", F.hour("timestamp_col"))
.withColumn("date_trunc", F.date_trunc("day", "timestamp_col"))

# Strings
.withColumn("upper", F.upper("text_col"))
.withColumn("split", F.split("text_col", ","))
.withColumn("concat", F.concat("col1", F.lit("-"), "col2"))

# Nulls
.withColumn("coalesce", F.coalesce("col1", "col2", F.lit(0)))
.filter(F.col("col").isNotNull())

# Aggregations
.groupBy("key").agg(
    F.sum("amount").alias("total"),
    F.count("*").alias("count"),
    F.avg("value").alias("average")
)
```

## 🎓 Best Practices Checklist

### Before Production

- [ ] **Serverless enabled** (for new pipelines)
- [ ] **Unity Catalog configured**
- [ ] **Service principal** set as run-as user
- [ ] **Parameters** used for environment configs
- [ ] **Development mode disabled**
- [ ] **Data quality expectations** applied
- [ ] **Notifications** configured
- [ ] **Table comments** and properties set
- [ ] **Pipeline tested** with sample data
- [ ] **Cost monitoring** enabled
- [ ] **Permissions** reviewed (least privilege)
- [ ] **Lineage** verified in Catalog Explorer

### Code Quality

- [ ] **No actions** in dataset definitions
- [ ] **Lazy operations** only
- [ ] **Descriptive table names**
- [ ] **Comments** for complex logic
- [ ] **Error handling** where appropriate
- [ ] **No hardcoded values**
- [ ] **Quality checks** at appropriate layers
- [ ] **Proper SCD type** for CDC
- [ ] **Sequence column** for CDC

## 🔗 Quick Links to Documentation

| Topic | File |
|-------|------|
| **Getting Started** | `.claude/kb/lakeflow/02-getting-started/tutorial-pipelines.md` |
| **Python API** | `.claude/kb/lakeflow/03-development/python-development.md` |
| **SQL Syntax** | `.claude/kb/lakeflow/03-development/sql-development.md` |
| **CDC** | `.claude/kb/lakeflow/04-features/cdc.md` |
| **Expectations** | `.claude/kb/lakeflow/06-data-quality/expectations.md` |
| **Configuration** | `.claude/kb/lakeflow/05-configuration/pipeline-configuration.md` |
| **Serverless** | `.claude/kb/lakeflow/05-configuration/serverless-pipelines.md` |
| **Unity Catalog** | `.claude/kb/lakeflow/08-operations/unity-catalog.md` |
| **Parameters** | `.claude/kb/lakeflow/08-operations/parameters.md` |
| **Limitations** | `.claude/kb/lakeflow/08-operations/limitations.md` |
| **Full Index** | `.claude/kb/lakeflow/index.md` |

## 💡 Pro Tips

1. **Always use Auto Loader** for cloud storage ingestion
2. **Layer quality checks**: Warn → Drop → Fail
3. **Use views** for reusable transformations
4. **Parameterize everything** environment-specific
5. **Test in development mode** first
6. **Monitor costs** regularly
7. **Use serverless** for new pipelines
8. **Document tables** with comments
9. **Apply least privilege** permissions
10. **Review lineage** for impact analysis

---

**For detailed information, see the full documentation in `.claude/kb/lakeflow/`**
