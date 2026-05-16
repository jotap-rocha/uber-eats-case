# Data Quality Expectations in Lakeflow

> Source: https://docs.databricks.com/aws/en/dlt/expectations

## Overview

**Apply quality constraints that validate data as it flows through ETL pipelines**

Expectations are quality checks that ensure data meets business rules and technical requirements before being written to target tables.

## Expectation Components

1. **Expectation name**: Identifier for the rule
2. **Constraint clause**: SQL boolean expression
3. **Action on violation**: What to do with invalid records

## Violation Policies

### 1. WARN (Default)
Invalid records are retained, metrics are tracked

```python
@dlt.expect("valid_age", "age >= 0")
@dlt.table()
def customers():
    return spark.read.table("raw_customers")
```

```sql
CREATE OR REFRESH STREAMING TABLE customers(
    CONSTRAINT valid_age
    EXPECT (age >= 0)
)
AS SELECT * FROM raw_customers
```

**Use cases:**
- Exploratory data analysis
- Understanding data quality issues
- Gradual quality improvement

### 2. DROP
Invalid records are dropped before data is written to the target

```python
@dlt.expect_or_drop("valid_email", "email LIKE '%@%.%'")
@dlt.table()
def customers():
    return spark.read.table("raw_customers")
```

```sql
CREATE OR REFRESH STREAMING TABLE customers(
    CONSTRAINT valid_email
    EXPECT (email LIKE '%@%.%')
    ON VIOLATION DROP ROW
)
AS SELECT * FROM raw_customers
```

**Use cases:**
- Production pipelines
- Strict data quality requirements
- Preventing bad data propagation

### 3. FAIL
Invalid records prevent the update from succeeding

```python
@dlt.expect_or_fail("critical_field", "customer_id IS NOT NULL")
@dlt.table()
def customers():
    return spark.read.table("raw_customers")
```

```sql
CREATE OR REFRESH STREAMING TABLE customers(
    CONSTRAINT critical_field
    EXPECT (customer_id IS NOT NULL)
    ON VIOLATION FAIL UPDATE
)
AS SELECT * FROM raw_customers
```

**Use cases:**
- Critical business data
- Compliance requirements
- Data integrity guarantees

## Constraint Types

### Simple Comparisons

```python
@dlt.expect("positive_amount", "amount > 0")
@dlt.expect("valid_status", "status IN ('ACTIVE', 'INACTIVE', 'PENDING')")
@dlt.expect("recent_date", "transaction_date >= '2020-01-01'")
```

### SQL Functions

```python
@dlt.expect("valid_year", "YEAR(transaction_date) >= 2020")
@dlt.expect("valid_length", "LENGTH(customer_name) >= 3")
@dlt.expect("uppercase_code", "country_code = UPPER(country_code)")
```

### CASE Statements

```python
@dlt.expect(
    "conditional_validation",
    """
    CASE
        WHEN type = 'RETAIL' THEN amount <= 10000
        WHEN type = 'WHOLESALE' THEN amount <= 100000
        ELSE TRUE
    END
    """
)
```

### Complex Boolean Logic

```python
@dlt.expect(
    "complex_rule",
    "(status = 'ACTIVE' AND last_login IS NOT NULL) OR status = 'INACTIVE'"
)
```

## Multiple Expectations

### Python: Individual Decorators

```python
@dlt.expect_or_drop("valid_id", "customer_id IS NOT NULL")
@dlt.expect_or_drop("valid_email", "email LIKE '%@%.%'")
@dlt.expect_or_drop("positive_age", "age > 0 AND age < 150")
@dlt.table()
def customers():
    return spark.read.table("raw_customers")
```

### Python: Grouped Expectations

```python
@dlt.expect_all({
    "valid_id": "customer_id IS NOT NULL",
    "valid_email": "email LIKE '%@%.%'",
    "positive_age": "age > 0 AND age < 150"
})
@dlt.table()
def customers_warn():
    return spark.read.table("raw_customers")

@dlt.expect_all_or_drop({
    "valid_id": "customer_id IS NOT NULL",
    "valid_email": "email LIKE '%@%.%'"
})
@dlt.table()
def customers_drop():
    return spark.read.table("raw_customers")

@dlt.expect_all_or_fail({
    "critical_id": "customer_id IS NOT NULL"
})
@dlt.table()
def customers_fail():
    return spark.read.table("raw_customers")
```

### SQL: Multiple Constraints

```sql
CREATE OR REFRESH STREAMING TABLE customers(
    CONSTRAINT valid_id
    EXPECT (customer_id IS NOT NULL)
    ON VIOLATION DROP ROW,

    CONSTRAINT valid_email
    EXPECT (email LIKE '%@%.%')
    ON VIOLATION DROP ROW,

    CONSTRAINT positive_age
    EXPECT (age > 0 AND age < 150)
    ON VIOLATION DROP ROW
)
AS SELECT * FROM raw_customers
```

## Complete Example: Multi-Layer Quality

```python
import dlt
from pyspark.sql import functions as F

# Bronze: Warn only, keep all data
@dlt.expect("has_data", "_rescued_data IS NULL")
@dlt.table(
    comment="Raw ingestion with quality warnings",
    table_properties={"quality": "bronze"}
)
def orders_bronze():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "json")
        .load("s3://bucket/orders/")
    )

# Silver: Drop invalid records
@dlt.expect_all_or_drop({
    "valid_id": "order_id IS NOT NULL",
    "valid_date": "order_date IS NOT NULL",
    "positive_amount": "amount > 0",
    "valid_status": "status IN ('PENDING', 'COMPLETED', 'CANCELLED')",
    "recent_order": "order_date >= '2020-01-01'"
})
@dlt.table(
    comment="Cleaned orders with quality checks",
    table_properties={"quality": "silver"}
)
def orders_silver():
    return dlt.read_stream("orders_bronze")

# Gold: Fail on critical violations
@dlt.expect_or_fail("revenue_integrity", "total_revenue >= 0")
@dlt.table(
    comment="Aggregated revenue with strict quality",
    table_properties={"quality": "gold"}
)
def daily_revenue():
    return (
        spark.read.table("orders_silver")
        .groupBy(F.date_trunc("day", "order_date").alias("date"))
        .agg(F.sum("amount").alias("total_revenue"))
    )
```

## Monitoring Expectations

### View Metrics in UI
- Pipeline dashboard shows expectation violations
- Drill down to see specific failed records
- Track trends over time

### Access Metrics Programmatically

```python
# Event logs contain expectation metrics
events = spark.read.format("delta").load("/event_log_path")
expectations = events.filter("event_type = 'flow_progress'")
```

## Limitations

❌ Only supported in streaming tables and materialized views
❌ Metrics not available in certain scenarios
❌ Cannot reference other tables in constraints (use joins first)

## Best Practices

### ✅ DO

1. **Layer quality checks**:
   - Bronze: WARN to understand issues
   - Silver: DROP to clean data
   - Gold: FAIL for critical business rules

2. **Name expectations clearly**:
   - Use descriptive names
   - Follow naming conventions
   - Document business context

3. **Test expectations**:
   - Validate with sample data
   - Test edge cases
   - Monitor failure rates

4. **Balance strictness**:
   - Too strict → pipeline failures
   - Too loose → data quality issues
   - Find the right balance

5. **Document quality rules**:
   - Explain business rationale
   - Document expected failure rates
   - Set up alerts for anomalies

### ❌ DON'T

1. **Don't fail everything**:
   - Use FAIL sparingly
   - Reserve for truly critical checks

2. **Don't ignore warnings**:
   - Review warning metrics regularly
   - Address root causes

3. **Don't create circular dependencies**:
   - Avoid referencing downstream tables

4. **Don't overcomplicate constraints**:
   - Keep rules simple and readable
   - Split complex rules into multiple expectations

## Performance Considerations

- Expectations are evaluated during data processing
- Complex constraints may impact pipeline performance
- Consider computational cost of SQL functions
- Use indexed columns when possible

## Common Patterns

### Not Null Checks
```python
@dlt.expect_or_drop("not_null", "critical_column IS NOT NULL")
```

### Range Validation
```python
@dlt.expect_or_drop("valid_range", "age BETWEEN 0 AND 150")
```

### Format Validation
```python
@dlt.expect_or_drop("valid_email", "email RLIKE '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'")
```

### Referential Integrity (via join)
```python
@dlt.table()
def orders_with_valid_customers():
    return (
        dlt.read("orders")
        .join(dlt.read("customers"), "customer_id", "inner")
    )
```

### Date Validation
```python
@dlt.expect_or_drop("valid_date_range", "start_date <= end_date")
@dlt.expect_or_drop("recent_data", "created_at >= current_date() - INTERVAL 1 YEAR")
```
