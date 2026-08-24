# Databricks Security

> **Purpose**: Master Databricks security — authentication, secrets, cluster policies, networking, audit logs, and UC permission hierarchy
> **Confidence**: 0.95
> **MCP Validated**: 2026-04-20

## Overview

Databricks security operates at multiple layers: authentication (who can access), authorization (what they can do via Unity Catalog GRANT/REVOKE), secrets management (credentials), network isolation (VPC/VNET), and audit logging (what was done). Service principals are preferred over PAT tokens for production automation.

## Authentication

```python
# 1. Personal Access Tokens (PAT) — user-based, for development
# Generate in Databricks UI: Settings → Developer → Access Tokens
TOKEN = dbutils.secrets.get("my-scope", "databricks-token")

# 2. OAuth (M2M) — machine-to-machine, preferred for CI/CD
# Service principal → OAuth client credentials flow
# Managed in Databricks Account Console → Service Principals

# 3. Azure AD / Okta SSO — for human users via browser
# Configured at Account level

# Best practice for production:
# - CI/CD pipelines: service principal + OAuth
# - Human users: SSO (no PAT tokens)
# - PAT tokens: only for development / quick prototyping
```

## Secrets Management

```python
# Secret scopes: Databricks-backed or Azure Key Vault-backed

# --- DATABRICKS-BACKED SCOPE ---
# Create scope via CLI:
# databricks secrets create-scope --scope my-scope

# Add secret:
# databricks secrets put --scope my-scope --key api-key

# Read secret in notebook (value is NEVER displayed in output)
api_key = dbutils.secrets.get(scope="my-scope", key="api-key")

# List secrets (shows key names only — values are redacted)
dbutils.secrets.list("my-scope")

# List all scopes
dbutils.secrets.listScopes()

# --- AZURE KEY VAULT-BACKED SCOPE ---
# Links Databricks scope to Azure Key Vault
# No need to sync secrets — reads from AKV directly
# More secure: rotation handled by AKV

# Use in code: same API as Databricks-backed
azure_secret = dbutils.secrets.get("akv-scope", "my-azure-secret")
```

## Cluster Policies

```python
# Cluster policies restrict what users can configure
# Defined as JSON — each attribute can be: fixed, allowlist, range, regex

policy = {
    # Force job cluster type
    "cluster_type": {
        "type": "fixed",
        "value": "job"
    },
    # Limit max workers
    "autoscale.max_workers": {
        "type": "range",
        "maxValue": 20,
        "defaultValue": 5,
        "hidden": False
    },
    # Restrict instance types
    "node_type_id": {
        "type": "allowlist",
        "values": ["i3.xlarge", "i3.2xlarge"],
        "defaultValue": "i3.xlarge"
    },
    # Force specific runtime
    "spark_version": {
        "type": "regex",
        "pattern": "15\\.[0-9]+\\..*-scala2\\.12",
        "defaultValue": "15.4.x-scala2.12"
    },
    # Force spot workers
    "aws_attributes.availability": {
        "type": "fixed",
        "value": "SPOT_WITH_FALLBACK"
    }
}
```

## Rede, auditoria e hierarquia UC

Continuação: [security-network-audit-uc.md](security-network-audit-uc.md).

## Related

- [concepts/unity-catalog.md](unity-catalog.md)
- [concepts/clusters.md](clusters.md)
- [concepts/notebooks.md](notebooks.md)
