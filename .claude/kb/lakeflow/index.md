# Databricks Lakeflow Knowledge Base

**Comprehensive documentation for Lakeflow Declarative Pipelines (formerly Delta Live Tables)**

## 📚 Documentation Structure

### [01 - Core Concepts](01-core-concepts/)
- **[concepts.md](01-core-concepts/concepts.md)** - Fundamental concepts: Flows, Streaming Tables, Materialized Views, Sinks, Pipelines

### [02 - Getting Started](02-getting-started/)
- **[tutorial-pipelines.md](02-getting-started/tutorial-pipelines.md)** - Complete ETL tutorial with CDC, Medallion architecture

### [03 - Development](03-development/)
- **[python-development.md](03-development/python-development.md)** - Python API, decorators, data loading patterns
- **[sql-development.md](03-development/sql-development.md)** - SQL syntax, Auto Loader, constraints

### [04 - Features](04-features/)
- **[cdc.md](04-features/cdc.md)** - Change Data Capture, SCD Type 1/2, sequencing

### [05 - Configuration](05-configuration/)
- **[pipeline-configuration.md](05-configuration/pipeline-configuration.md)** - Compute, parameters, notifications, editions
- **[serverless-pipelines.md](05-configuration/serverless-pipelines.md)** - Serverless compute, performance modes

### [06 - Data Quality](06-data-quality/)
- **[expectations.md](06-data-quality/expectations.md)** - Data quality constraints, violation policies

### [07 - Advanced](07-advanced/)
- **[stateful-processing.md](07-advanced/stateful-processing.md)** - Watermarks, windows, stream-stream joins, state stores
- **[materialized-views-optimization.md](07-advanced/materialized-views-optimization.md)** - Incremental refresh, performance optimization

### [08 - Operations](08-operations/)
- **[unity-catalog.md](08-operations/unity-catalog.md)** - Unity Catalog integration, permissions
- **[parameters.md](08-operations/parameters.md)** - Pipeline parameterization
- **[limitations.md](08-operations/limitations.md)** - Known limitations and constraints

## 🚀 Quick Start

### Create Your First Pipeline (Python)

```python
import dlt

# Bronze: Raw ingestion
@dlt.table()
def customers_bronze():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "json")
        .load("s3://bucket/customers/")
    )

# Silver: Data quality
@dlt.expect_or_drop("valid_id", "id IS NOT NULL")
@dlt.table()
def customers_silver():
    return dlt.read_stream("customers_bronze")

# Gold: Business logic
@dlt.table()
def customer_metrics():
    return (
        spark.read.table("customers_silver")
        .groupBy("country")
        .count()
    )
```

### Create Your First Pipeline (SQL)

```sql
-- Bronze: Raw ingestion
CREATE OR REFRESH STREAMING TABLE customers_bronze
AS SELECT *
FROM STREAM read_files("s3://bucket/customers/", format => "json")

-- Silver: Data quality
CREATE OR REFRESH STREAMING TABLE customers_silver(
    CONSTRAINT valid_id EXPECT (id IS NOT NULL) ON VIOLATION DROP ROW
)
AS SELECT * FROM STREAM customers_bronze

-- Gold: Business logic
CREATE OR REFRESH MATERIALIZED VIEW customer_metrics
AS SELECT country, COUNT(*) as count
FROM customers_silver
GROUP BY country
```

## 🎯 Common Patterns

### Pattern 1: Medallion Architecture
```
Bronze (Raw) → Silver (Cleaned) → Gold (Business)
```

### Pattern 2: Change Data Capture
```python
dlt.apply_changes(
    target="customers",
    source="customers_cdc",
    keys=["id"],
    sequence_by="timestamp",
    stored_as_scd_type=1
)
```

### Pattern 3: Data Quality Layers
```
Bronze: WARN  → Track issues
Silver: DROP  → Remove bad data
Gold:   FAIL  → Strict validation
```

## 🔑 Key Concepts

| Concept | Description |
|---------|-------------|
| **Flow** | Data processing unit with source, logic, and destination |
| **Streaming Table** | Incrementally processes new data |
| **Materialized View** | Batch-refreshed aggregate table |
| **Sink** | External streaming destination (Kafka, EventHubs) |
| **Expectation** | Data quality constraint |
| **AUTO CDC** | Automatic change data capture processing |
| **SCD** | Slowly Changing Dimension (Type 1 or 2) |

## 💡 Best Practices

### ✅ DO
1. **Use serverless** for new pipelines
2. **Apply expectations** at silver layer
3. **Use Auto Loader** for cloud storage
4. **Parameterize** configurations
5. **Enable Unity Catalog** for governance
6. **Use service principals** for run-as identity
7. **Monitor** pipeline metrics

### ❌ DON'T
1. **Don't trigger actions** (`.count()`, `.collect()`) in pipeline code
2. **Don't use development mode** in production
3. **Don't hardcode** environment values
4. **Don't skip** data quality checks
5. **Don't ignore** cost monitoring

## 🎓 Learning Path

### Beginner
1. Read [concepts.md](01-core-concepts/concepts.md)
2. Follow [tutorial-pipelines.md](02-getting-started/tutorial-pipelines.md)
3. Learn [python-development.md](03-development/python-development.md) or [sql-development.md](03-development/sql-development.md)

### Intermediate
4. Master [expectations.md](06-data-quality/expectations.md)
5. Understand [cdc.md](04-features/cdc.md)
6. Configure [serverless-pipelines.md](05-configuration/serverless-pipelines.md)

### Advanced
7. Learn [stateful-processing.md](07-advanced/stateful-processing.md)
8. Optimize [materialized-views-optimization.md](07-advanced/materialized-views-optimization.md)
9. Implement [unity-catalog.md](08-operations/unity-catalog.md) governance
10. Optimize [pipeline-configuration.md](05-configuration/pipeline-configuration.md)
11. Know [limitations.md](08-operations/limitations.md)

## 🔍 MCP Integration

This knowledge base is designed to work with Claude Code's MCP capabilities:

### Local KB Search (Primary)
```bash
# Grep for specific topics
grep -r "AUTO CDC" .claude/kb/lakeflow/
```

### MCP Fallback (Real-time Updates)
- `mcp__ref-tools__ref_search_documentation` - Latest Databricks docs
- `mcp__exa__get_code_context_exa` - Real-world examples
- `mcp__upstash-context-7-mcp` - Library documentation

### Search Strategy
1. **Local first** - Fast, comprehensive, offline-capable
2. **MCP validation** - Verify latest updates
3. **Web search** - Community solutions, blog posts

## 📊 Quick Reference

### Decorators (Python)
```python
@dlt.table()                              # Create table
@dlt.view()                               # Create temp view
@dlt.expect()                             # Warn on violation
@dlt.expect_or_drop()                     # Drop on violation
@dlt.expect_or_fail()                     # Fail on violation
@dlt.expect_all({...})                    # Multiple expectations
```

### Keywords (SQL)
```sql
CREATE OR REFRESH STREAMING TABLE         # Streaming table
CREATE OR REFRESH MATERIALIZED VIEW       # Materialized view
STREAM                                    # Streaming source
CONSTRAINT ... EXPECT                     # Data quality check
ON VIOLATION DROP ROW                     # Drop invalid records
ON VIOLATION FAIL UPDATE                  # Fail on invalid records
APPLY CHANGES INTO                        # CDC processing
STORED AS SCD TYPE 1/2                    # SCD type
```

### Functions
```python
dlt.read()                                # Read table (batch)
dlt.read_stream()                         # Read table (streaming)
dlt.create_streaming_table()              # Create streaming table
dlt.apply_changes()                       # Apply CDC changes
dlt.create_auto_cdc_flow()                # AUTO CDC flow
```

## 🌐 External Resources

- [Official Databricks Docs](https://docs.databricks.com/aws/en/dlt/index.html)
- [Databricks Lakeflow Product Page](https://www.databricks.com/product/data-engineering#related-products)
- [Community Forums](https://community.databricks.com/)

## 📝 Version Info

- **Last Updated**: 2025-01-06
- **Databricks Runtime**: Current channel
- **Coverage**: 35+ documentation pages
- **Focus**: AWS deployment

---

**For questions or issues, use MCP tools to search latest documentation or community resources.**
