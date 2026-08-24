# Databricks Asset Bundles (DABs)

> **Purpose**: CI/CD deployment for Databricks — bundle.yml structure, environments, variable substitution, GitHub Actions
> **MCP Validated**: 2026-04-20

## When to Use

- Deploying Databricks jobs, pipelines, and models via CI/CD
- Managing dev/staging/production environment configurations
- Versioning Databricks resources alongside application code
- Automated testing and promotion of data pipelines

## bundle.yml Structure

```yaml
# databricks.yml (root bundle configuration)
bundle:
  name: orders-pipeline
  git:
    origin_url: https://github.com/company/orders-pipeline
    branch: main

# Global variables (overridable per environment)
variables:
  catalog:
    description: Unity Catalog catalog name
    default: dev_catalog
  env:
    description: Deployment environment
    default: dev
  job_cluster_size:
    description: Worker node instance type
    default: i3.xlarge

# Artifact configuration (built Python wheel, etc.)
artifacts:
  orders_whl:
    type: whl
    path: ./src/

# Resources: jobs, pipelines, models, experiments, serving endpoints
resources:
  jobs:
    orders_etl_job:
      name: "Orders ETL — ${var.env}"
      tags:
        team: "data-engineering"
        environment: "${var.env}"

      # Job-level email notifications
      email_notifications:
        on_failure:
          - "data-team@company.com"

      # Schedule (cron)
      schedule:
        quartz_cron_expression: "0 0 5 * * ?"
        timezone_id: "America/Sao_Paulo"
        pause_status: UNPAUSED

      tasks:
        - task_key: bronze_ingest
          job_cluster_key: default_cluster
          notebook_task:
            notebook_path: /Repos/${workspace.current_user.userName}/orders-pipeline/notebooks/01_bronze
            base_parameters:
              catalog: "${var.catalog}"
              env: "${var.env}"

        - task_key: silver_transform
          depends_on:
            - task_key: bronze_ingest
          job_cluster_key: default_cluster
          python_wheel_task:
            package_name: orders_pipeline
            entry_point: silver_transform
            parameters:
              - "--catalog=${var.catalog}"
              - "--date={{start_date}}"

        - task_key: gold_aggregate
          depends_on:
            - task_key: silver_transform
          job_cluster_key: default_cluster
          sql_task:
            query:
              query_id: "12345-abcdef"
            warehouse_id: "${var.warehouse_id}"

      job_clusters:
        - job_cluster_key: default_cluster
          new_cluster:
            spark_version: "15.4.x-scala2.12"
            node_type_id: "${var.job_cluster_size}"
            num_workers: 4
            spark_conf:
              spark.databricks.delta.preview.enabled: "true"
            aws_attributes:
              availability: SPOT_WITH_FALLBACK

  pipelines:
    orders_dlt:
      name: "Orders DLT Pipeline — ${var.env}"
      target: "${var.catalog}.orders_pipeline"
      catalog: "${var.catalog}"
      continuous: false
      development: "${var.env == 'dev'}"
      configuration:
        catalog: "${var.catalog}"
        env: "${var.env}"
      libraries:
        - notebook:
            path: /Repos/${workspace.current_user.userName}/orders-pipeline/pipelines/orders_pipeline
      clusters:
        - label: "default"
          num_workers: 4
          node_type_id: "${var.job_cluster_size}"

  experiments:
    fraud_detection_experiment:
      name: "/Shared/fraud-detection-${var.env}"
      description: "Fraud detection model experiments"

# Target environments
targets:
  # Development environment
  dev:
    mode: development   # Adds [dev username] prefix to resources
    default: true
    workspace:
      host: https://dev-workspace.azuredatabricks.net
    variables:
      catalog: dev_catalog
      env: dev
      job_cluster_size: i3.xlarge

  # Staging environment
  staging:
    mode: production
    workspace:
      host: https://staging-workspace.azuredatabricks.net
    variables:
      catalog: staging_catalog
      env: staging
      job_cluster_size: i3.xlarge

  # Production environment
  production:
    mode: production
    workspace:
      host: https://prod-workspace.azuredatabricks.net
    variables:
      catalog: prod_catalog
      env: production
      job_cluster_size: i3.2xlarge
```

## CLI, GitHub Actions e variáveis

Ver [databricks-asset-bundles-cli-cicd.md](databricks-asset-bundles-cli-cicd.md).

## See Also

- [patterns/dlt-pipeline.md](dlt-pipeline.md)
- [concepts/jobs-workflows.md](../concepts/jobs-workflows.md)
- [concepts/security.md](../concepts/security.md)
