# Databricks Asset Bundles — CLI e CI/CD

> **Purpose**: Continuação de [databricks-asset-bundles.md](databricks-asset-bundles.md).  
> **MCP Validated**: 2026-04-20

## CLI Commands

```bash
pip install databricks-cli
curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh
databricks configure --token
databricks auth login --host https://workspace.azuredatabricks.net
databricks bundle validate
databricks bundle deploy
databricks bundle deploy --target staging
databricks bundle deploy --target production
databricks bundle run orders_etl_job
databricks bundle run orders_etl_job --target production
databricks bundle destroy --target dev
databricks bundle summary
```

## CI/CD with GitHub Actions

```yaml
name: Deploy Databricks Bundle
on:
  push:
    branches: [main]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: databricks/setup-cli@main
      - run: databricks bundle validate
```

## Variable Substitution Reference

| Variable | Example | Description |
|----------|---------|-------------|
| `${var.my_var}` | `${var.catalog}` | Bundle variable |
| `${workspace.host}` | `https://...` | Current workspace URL |
| `${workspace.current_user.userName}` | `user@co.com` | Current user email |
| `{{start_date}}` | `2025-01-01` | Job dynamic value (at runtime) |
| `{{job_id}}` | `12345` | Current job ID |

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `mode: development` | N/A | Prefixes resource names with `[dev username]` |
| `mode: production` | N/A | Deploys with exact resource names |
| `pause_status` | `UNPAUSED` | `PAUSED` to deploy without scheduling |

## See Also

- [databricks-asset-bundles.md](databricks-asset-bundles.md)
