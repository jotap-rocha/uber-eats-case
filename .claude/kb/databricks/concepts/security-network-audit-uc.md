# Segurança — rede, auditoria e Unity Catalog

> **Purpose**: Extensão de [security.md](security.md).  
> **Confidence**: 0.95  
> **MCP Validated**: 2026-04-20

## Network: VPC/VNET Injection, PrivateLink, IP Access Lists

```python
import requests

requests.post(
    f"{WORKSPACE_URL}/api/2.0/ip-access-lists",
    headers={"Authorization": f"Bearer {TOKEN}"},
    json={
        "label": "Corporate VPN",
        "list_type": "ALLOW",
        "ip_addresses": ["10.0.0.0/8", "203.0.113.0/24"],
    },
)
```

## Audit Logs

```sql
SELECT event_time, user_identity.email AS user, action_name,
       request_params.full_name_arg AS table_accessed
FROM system.access.audit
WHERE action_name IN ('getTable', 'executeStatement')
  AND event_time > CURRENT_TIMESTAMP - INTERVAL 7 DAYS
ORDER BY event_time DESC;
```

## Unity Catalog Permission Hierarchy

```sql
GRANT USE_CATALOG ON CATALOG prod_catalog TO `analyst-group`;
GRANT USE_SCHEMA ON SCHEMA prod_catalog.sales TO `analyst-group`;
GRANT SELECT ON TABLE prod_catalog.sales.orders TO `analyst-group`;
```

## Common Mistakes

### Wrong

```python
api_key = "sk-1234567890abcdef"
```

### Correct

```python
api_key = dbutils.secrets.get(scope="production-secrets", key="external-api-key")
```

## Related

- [security.md](security.md)
