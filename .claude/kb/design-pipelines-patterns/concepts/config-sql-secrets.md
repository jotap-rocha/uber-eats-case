# Config, SQL e segredos

> **Propósito:** Manter **ligações e queries fora do código** e segredos no **Vault OCI**.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-15

## Overview

`config/config.yaml` descreve **o quê** ligar (nomes lógicos, ambientes). `sql/*.sql` versiona **como** interrogar o destino. `src/utils/key_oci.py` (obrigatório) resolve segredos a partir de `.config`. `src/utils/logger.py` (obrigatório) uniformiza logs para `logs/`.

## O Pattern

```yaml
# config/config.yaml (exemplo ilustrativo — sem segredos)
environments:
  dev:
    sql_server:
      server: "sql-dev.example.internal"
      database: "BI_STAGING"
  prd:
    sql_server:
      server: "sql-prd.example.internal"
      database: "BI"
```

Queries longas ou parametrizáveis vivem em `sql/extract_source_1.sql`; o código Python referencia o ficheiro por caminho relativo à raiz do repositório.

## Quick Reference

| Ficheiro | Contém | Não contém |
|----------|---------|------------|
| `config.yaml` | URLs lógicas, timeouts, batch sizes | passwords, private keys |
| `.config` | OCIDs / metadados Vault | valores secretos em claro |
| `sql/*.sql` | SELECT/merge parametrizáveis | credenciais embutidas |

## Common Mistakes

### Wrong

Copiar connection string completa com user/password para `config.yaml` committed.

### Correct

User no YAML se for **não sensível**; password só via Vault em runtime (`key_oci.py`).

## Related

- [obrigatoriedade-arvore.md](obrigatoriedade-arvore.md)
- [../patterns/scaffold-projeto-dados.md](../patterns/scaffold-projeto-dados.md)
- [../../dev-python-automation/patterns/config-segredos.md](../../dev-python-automation/patterns/config-segredos.md)
