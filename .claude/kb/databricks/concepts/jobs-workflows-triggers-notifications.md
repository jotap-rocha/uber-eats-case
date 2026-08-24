# Jobs — triggers, reparação, notificações e parâmetros

> **Purpose**: Extensão de [jobs-workflows.md](jobs-workflows.md).  
> **Confidence**: 0.95  
> **MCP Validated**: 2026-04-20

## Triggers

```yaml
trigger:
  pause_status: UNPAUSED
  periodic:
    interval: 1
    unit: HOURS

schedule:
  quartz_cron_expression: "0 0 6 * * ?"
  timezone_id: "America/Sao_Paulo"

trigger:
  file_arrival:
    url: "s3://my-bucket/landing-zone/"
    min_time_between_triggers_seconds: 60

trigger:
  pause_status: UNPAUSED
  continuous:
    pause_status: UNPAUSED
```

## Repair and Re-Run

```python
import requests
response = requests.post(
    f"{DATABRICKS_URL}/api/2.1/jobs/runs/repair",
    headers={"Authorization": f"Bearer {TOKEN}"},
    json={"run_id": 12345, "rerun_tasks": ["failed_task_key"]},
)
```

## Notifications

```yaml
email_notifications:
  on_start: ["team@company.com"]
  on_success: ["team@company.com"]
  on_failure: ["oncall@company.com", "manager@company.com"]
  no_alert_for_skipped_runs: true

webhook_notifications:
  on_failure:
    - id: "webhook_destination_id"
```

## Job Parameters and Dynamic Values

```yaml
parameters:
  - name: run_date
    default: "{{start_date}}"
  - name: environment
    default: "prod"
```

## Common Mistakes

### Wrong

```yaml
tasks:
  - task_key: heavy_etl
    existing_cluster_id: "shared-dev-cluster"
```

### Correct

```yaml
tasks:
  - task_key: heavy_etl
    new_cluster:
      spark_version: "15.4.x-scala2.12"
      node_type_id: "i3.2xlarge"
      num_workers: 8
```

## Related

- [jobs-workflows.md](jobs-workflows.md)
- [patterns/databricks-asset-bundles-cli-cicd.md](../patterns/databricks-asset-bundles-cli-cicd.md)
