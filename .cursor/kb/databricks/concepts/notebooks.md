# Databricks Notebooks

> **Purpose**: Master notebook features — magic commands, widgets, dbutils, display(), %run, and Databricks Connect
> **Confidence**: 0.95
> **MCP Validated**: 2026-04-20

## Overview

Databricks notebooks are the primary interactive development environment. They support multiple languages per cell via magic commands, parameterization via widgets, notebook chaining via `%run`, and rich data visualization via `display()`. Databricks Connect allows running notebook code from a local IDE against a remote cluster.

## Language Magic Commands

```python
# %python — switch cell to Python (default in Python notebooks)
# %sql    — switch cell to SQL
# %scala  — switch cell to Scala
# %r      — switch cell to R
# %md     — Markdown (documentation cells)
# %sh     — Shell commands (runs on driver only)
# %fs     — DBFS filesystem operations (alias for dbutils.fs)
# %run    — Execute another notebook
# %pip    — Install Python packages (restarts Python interpreter)
# %conda  — Use conda to manage packages (not available on all runtimes)

# Example: SQL cell in a Python notebook
```

```sql
-- %sql
SELECT catalog_name, schema_name, table_name
FROM system.information_schema.tables
WHERE table_schema = 'my_schema'
LIMIT 10;
```

```bash
# %sh — shell on driver node
ls -la /databricks/
cat /etc/databricks/spark.conf
```

```python
# %pip — install packages
# %pip install pandas==2.0.3 requests
# Note: restarts Python kernel — run in first cell
```

## Widgets

```python
# Widgets parameterize notebooks (used by Jobs, %run, and DLT)

# Text widget
dbutils.widgets.text("environment", "dev", "Environment")
env = dbutils.widgets.get("environment")

# Dropdown widget
dbutils.widgets.dropdown("log_level", "INFO", ["DEBUG", "INFO", "WARN", "ERROR"])
log_level = dbutils.widgets.get("log_level")

# Combobox (dropdown + free text)
dbutils.widgets.combobox("catalog", "main", ["main", "dev", "prod"])

# Multiselect
dbutils.widgets.multiselect("regions", "US", ["US", "EU", "APAC"])
regions = dbutils.widgets.get("regions").split(",")

# Remove all widgets
dbutils.widgets.removeAll()
```

## %run for Notebook Chaining

```python
# %run executes another notebook in the same interpreter context
# All variables, functions, imports defined in the called notebook
# are available in the calling notebook

# Call notebook by relative path
# %run ./utils/data_helpers

# Call with parameters (passed as widgets)
# %run ./config/setup $environment="prod" $catalog="main"

# Note: %run is synchronous — waits for the called notebook to finish
# For parallel execution, use dbutils.notebook.run() instead
```

## dbutils — Databricks Utilities

```python
# dbutils.fs — filesystem operations
dbutils.fs.ls("/Volumes/catalog/schema/volume/")
dbutils.fs.cp("source_path", "dest_path", recurse=True)
dbutils.fs.rm("path", recurse=True)
dbutils.fs.mkdirs("/Volumes/catalog/schema/volume/new_dir/")

# Read file content
content = dbutils.fs.head("/Volumes/catalog/schema/volume/config.json", 1000)

# dbutils.secrets — access secret scopes
token = dbutils.secrets.get(scope="my-scope", key="api-token")
# Note: secret values are redacted in notebook output

# List secrets (shows key names, NOT values)
dbutils.secrets.list("my-scope")

# dbutils.notebook — notebook orchestration
result = dbutils.notebook.run("./child_notebook", timeout_seconds=600, arguments={
    "environment": "prod",
    "run_date": "2025-01-01"
})
# Returns: exit value from dbutils.notebook.exit("success")

# Exit current notebook with a value
dbutils.notebook.exit("Job completed successfully")

# dbutils.library (legacy — prefer %pip)
# dbutils.library.installPyPI("mlflow")
```

## display(), Databricks Connect e IPython

Continuação: [notebooks-display-connect.md](notebooks-display-connect.md).

## Related

- [concepts/clusters.md](clusters.md)
- [concepts/jobs-workflows.md](jobs-workflows.md)
- [concepts/security.md](security.md)
