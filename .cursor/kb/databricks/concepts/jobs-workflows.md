# Jobs and Workflows

> **Purpose**: Master Databricks Jobs — task types, dependencies, triggers, job clusters, repair/re-run, notifications, and parameters
> **Confidence**: 0.95
> **MCP Validated**: 2026-04-20

## Overview

Databricks Jobs (also called Workflows) orchestrate multi-task data pipelines with dependencies, scheduling, and monitoring. Each job can contain multiple tasks of different types (notebook, Python script, JAR, SQL, DLT pipeline, dbt) with linear, fan-out, fan-in, or conditional branching between tasks.

## Task Types

| Task Type | Use Case | Runtime |
|-----------|----------|---------|
| Notebook | Interactive notebook execution | All-purpose or job cluster |
| Python script | `.py` file from Repo/Workspace | Job cluster |
| JAR | Compiled JVM code | Job cluster |
| SQL | SQL queries or alerts | SQL Warehouse |
| DLT Pipeline | Delta Live Tables pipeline | Managed by DLT |
| dbt | dbt project execution | Serverless / SQL Warehouse |
| Spark Submit | Low-level Spark submission | Job cluster |
| Run job | Trigger another job | N/A |

## Task Dependencies

```yaml
# bundle.yml — job with task dependencies
resources:
  jobs:
    my_pipeline:
      name: "My Data Pipeline"
      tasks:
        - task_key: ingest_bronze
          notebook_task:
            notebook_path: /Repos/main/notebooks/01_bronze_ingest

        - task_key: transform_silver
          depends_on:
            - task_key: ingest_bronze
          notebook_task:
            notebook_path: /Repos/main/notebooks/02_silver_transform

        - task_key: aggregate_gold_sales
          depends_on:
            - task_key: transform_silver
          notebook_task:
            notebook_path: /Repos/main/notebooks/03_gold_sales

        - task_key: aggregate_gold_marketing
          depends_on:
            - task_key: transform_silver   # Fan-out from silver
          notebook_task:
            notebook_path: /Repos/main/notebooks/03_gold_marketing
```

## Conditional Branching (If/Else)

```yaml
tasks:
  - task_key: validate_data
    notebook_task:
      notebook_path: /notebooks/validate

  - task_key: process_valid
    condition_task:
      op: EQUAL_TO
      left: "{{tasks.validate_data.values.status}}"
      right: "success"

  - task_key: run_pipeline
    depends_on:
      - task_key: process_valid
        outcome: "true"
    notebook_task:
      notebook_path: /notebooks/pipeline

  - task_key: alert_failure
    depends_on:
      - task_key: process_valid
        outcome: "false"
    notebook_task:
      notebook_path: /notebooks/alert
```

## Job Clusters vs All-Purpose Clusters

```python
# Job cluster config in job definition — terminates after job
{
  "new_cluster": {
    "spark_version": "15.4.x-scala2.12",
    "node_type_id": "i3.xlarge",
    "num_workers": 4,
    "spark_conf": {
      "spark.databricks.delta.preview.enabled": "true"
    }
  }
}

# Existing cluster (all-purpose) — cluster must be running
{
  "existing_cluster_id": "0123-456789-abcdef"
}

# Rule: job clusters for production (cheaper, isolated)
#        all-purpose only for development
```

## Triggers, reparação, notificações e parâmetros

Continuação: [jobs-workflows-triggers-notifications.md](jobs-workflows-triggers-notifications.md).

## Related

- [concepts/lakeflow.md](lakeflow.md)
- [concepts/clusters.md](clusters.md)
- [patterns/databricks-asset-bundles.md](../patterns/databricks-asset-bundles.md)
