# Databricks Quick Reference

> Fast lookup tables. For code examples, see linked concept/pattern files.
> **MCP Validated**: 2026-04-20

## Magic Commands

| Command | Language / Purpose |
|---------|-------------------|
| `%python` | Python cell |
| `%sql` | SQL cell |
| `%scala` | Scala cell |
| `%r` | R cell |
| `%md` | Markdown documentation |
| `%sh` | Shell on driver node |
| `%fs` | DBFS filesystem (alias for dbutils.fs) |
| `%run ./path/notebook` | Execute another notebook in same context |
| `%pip install pkg` | Install Python package (restarts interpreter) |
| `%conda` | Conda package management (not all runtimes) |

## dbutils API

| Call | Purpose |
|------|---------|
| `dbutils.fs.ls("/path/")` | List files |
| `dbutils.fs.cp(src, dst, recurse=True)` | Copy files |
| `dbutils.fs.rm("path", recurse=True)` | Delete files |
| `dbutils.fs.mkdirs("/path/")` | Create directory |
| `dbutils.secrets.get("scope", "key")` | Read secret (redacted in output) |
| `dbutils.secrets.list("scope")` | List secret keys |
| `dbutils.widgets.text("name", "default")` | Create text widget |
| `dbutils.widgets.get("name")` | Get widget value |
| `dbutils.widgets.removeAll()` | Remove all widgets |
| `dbutils.notebook.run("path", 600, {})` | Run child notebook (returns exit value) |
| `dbutils.notebook.exit("value")` | Exit notebook with return value |

## Spark Configurations

| Config | Recommended | Description |
|--------|-------------|-------------|
| `spark.sql.shuffle.partitions` | `2-4x cores` | Shuffle partition count |
| `spark.sql.adaptive.enabled` | `true` | Enable AQE (default DBR 7.3+) |
| `spark.sql.autoBroadcastJoinThreshold` | `10-50mb` | Broadcast join threshold |
| `spark.sql.files.maxPartitionBytes` | `128mb` | Target partition file size |
| `spark.databricks.io.cache.enabled` | `true` | Delta disk cache |
| `spark.databricks.delta.schema.autoMerge.enabled` | `false` | Schema evolution on merge |
| `spark.databricks.delta.optimizeWrite.enabled` | `true` | Auto-compact small files |
| `spark.databricks.delta.autoCompact.enabled` | `true` | Background compaction |

## Delta SQL Cheat Sheet

| Command | Syntax |
|---------|--------|
| Time travel (version) | `SELECT * FROM t VERSION AS OF 5` |
| Time travel (timestamp) | `SELECT * FROM t TIMESTAMP AS OF '2025-01-01'` |
| Show history | `DESCRIBE HISTORY catalog.schema.table` |
| Optimize | `OPTIMIZE catalog.schema.table` |
| Z-order | `OPTIMIZE catalog.schema.table ZORDER BY (col1, col2)` |
| Vacuum | `VACUUM catalog.schema.table RETAIN 168 HOURS` |
| Table details | `DESCRIBE DETAIL catalog.schema.table` |
| Enable CDF | `ALTER TABLE t SET TBLPROPERTIES (delta.enableChangeDataFeed = true)` |
| Enable liquid clustering | `ALTER TABLE t CLUSTER BY (col1, col2)` |

## Streaming Triggers

| Trigger | Code | Use Case |
|---------|------|----------|
| Fixed interval | `.trigger(processingTime="5 minutes")` | Regular micro-batch |
| Process all backlog | `.trigger(availableNow=True)` | Scheduled batch-style |
| Continuous | `.trigger(continuous="1 second")` | Ultra-low latency |
| Legacy one-shot | `.trigger(once=True)` | Deprecated — use availableNow |

## Output Modes

| Mode | Trigger | Description |
|------|---------|-------------|
| `append` | Any | Only new rows (default) |
| `complete` | Aggregations | Full result every trigger |
| `update` | Aggregations + watermark | Only changed rows |

## Unity Catalog GRANT Hierarchy

| Object | Grant Syntax |
|--------|-------------|
| Catalog | `GRANT USE_CATALOG ON CATALOG c TO group` |
| Schema | `GRANT USE_SCHEMA ON SCHEMA c.s TO group` |
| Table (read) | `GRANT SELECT ON TABLE c.s.t TO group` |
| Table (write) | `GRANT MODIFY ON TABLE c.s.t TO group` |
| Volume (read) | `GRANT READ_VOLUME ON VOLUME c.s.v TO group` |
| Volume (write) | `GRANT WRITE_VOLUME ON VOLUME c.s.v TO group` |
| All on schema | `GRANT ALL PRIVILEGES ON SCHEMA c.s TO group` |

## Cluster Type Decision Matrix

| Use Case | Choose |
|----------|--------|
| Interactive notebook development | All-purpose cluster |
| Production job / pipeline | Job cluster (auto-terminate) |
| SQL analytics / BI dashboards | Serverless SQL Warehouse |
| Frequent short jobs (< 30 min) | Instance pool + job cluster |
| SQL-heavy Delta workloads | Photon-enabled cluster |

## MLflow Model Registry Aliases

| Alias | Meaning |
|-------|---------|
| `champion` | Current production model |
| `challenger` | Candidate model being tested |
| `baseline` | Reference model for comparison |

```python
# Load by alias
model = mlflow.sklearn.load_model("models:/catalog.schema.model_name@champion")
# Load by version
model = mlflow.sklearn.load_model("models:/catalog.schema.model_name/3")
```

## DABs CLI Commands

| Command | Purpose |
|---------|---------|
| `databricks bundle validate` | Validate bundle.yml syntax |
| `databricks bundle deploy` | Deploy to default (dev) target |
| `databricks bundle deploy --target prod` | Deploy to production |
| `databricks bundle run job_name` | Trigger a job run |
| `databricks bundle summary` | Show deployed resources |
| `databricks bundle destroy` | Remove deployed resources |

## Common Pitfalls

| Don't | Do |
|-------|-----|
| Use DBFS root for data (`dbfs:/`) | Use Unity Catalog Volumes (`/Volumes/...`) |
| Use Hive metastore for new tables | Use Unity Catalog (`catalog.schema.table`) |
| Call `df.collect()` on large data | Use Spark transformations; stay distributed |
| Use Python UDFs for simple transforms | Use built-in `pyspark.sql.functions` |
| Hardcode credentials in notebooks | Use `dbutils.secrets.get()` |
| Use `trigger(once=True)` | Use `trigger(availableNow=True)` |
| Use Z-ordering on new tables (DBR 13.3+) | Use Liquid Clustering instead |
| Skip checkpoint location on streams | Always set unique `checkpointLocation` |
| All-purpose clusters for production | Use job clusters (auto-terminate) |
| Model Registry stages (Staging/Production) | Use aliases (`champion`, `challenger`) |

## Related Documentation

| Topic | Path |
|-------|------|
| Architecture & workspace | `concepts/architecture.md` |
| Delta Lake commands | `concepts/delta-lake.md` |
| Full Index | `index.md` |
