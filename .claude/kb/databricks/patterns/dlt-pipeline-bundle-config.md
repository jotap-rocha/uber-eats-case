# DLT pipeline — `bundle.yml` e parâmetros

> **Purpose**: Continuação de [dlt-pipeline.md](dlt-pipeline.md).  
> **MCP Validated**: 2026-04-20

## Pipeline Configuration (bundle.yml)

```yaml
resources:
  pipelines:
    orders_medallion_pipeline:
      name: "Orders Medallion Pipeline"
      target: prod_catalog.orders_pipeline
      catalog: prod_catalog
      channel: "CURRENT"
      continuous: false
      development: false
      configuration:
        spark.databricks.delta.schema.autoMerge.enabled: "true"
      clusters:
        - label: "default"
          num_workers: 4
          node_type_id: "i3.xlarge"
          spark_version: "15.4.x-scala2.12"
      libraries:
        - notebook:
            path: /Repos/main/pipelines/orders_pipeline.py
      notifications:
        - email_recipients:
            - "data-team@company.com"
          alerts:
            - on-update-failure
            - on-flow-failure
```

## Configuration

| Setting | Value | Description |
|---------|-------|-------------|
| `continuous` | `false` | Triggered (batch) vs continuous (streaming) |
| `development` | `false` | Production mode (no _dev suffix on tables) |
| `channel` | `"CURRENT"` | Use current DLT runtime |
| `target` | UC schema | Where pipeline tables are created |

## See Also

- [dlt-pipeline.md](dlt-pipeline.md)
