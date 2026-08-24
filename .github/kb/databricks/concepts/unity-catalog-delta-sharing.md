# Unity Catalog — Delta Sharing e erros comuns

> **Purpose**: Extensão de [unity-catalog.md](unity-catalog.md).  
> **Confidence**: 0.95  
> **MCP Validated**: 2026-04-20

## Delta Sharing

```sql
CREATE SHARE partner_share;
ALTER SHARE partner_share
ADD TABLE prod_catalog.sales.orders;
CREATE RECIPIENT external_partner
USING ID 'databricks_account_id_of_partner';
GRANT SELECT ON SHARE partner_share TO RECIPIENT external_partner;
```

## Common Mistakes

### Wrong

```sql
SELECT * FROM sales.orders;
```

### Correct

```sql
SELECT * FROM prod_catalog.sales.orders;
```

## Related

- [unity-catalog.md](unity-catalog.md)
