# Key OCI KB

Base de conhecimento específica do módulo `src/utils/key_oci.py`, responsável por resolver segredos do Oracle OCI Vault para os pipelines Python e para o bridge MCP.

## Objetivo

- Documentar como o `key_oci` lê segredos do `.config`.
- Explicar o fluxo de autenticação OCI (`~/.oci/config` ou Resource Principal).
- Padronizar consumo de segredos em jobs, notebooks e integrações auxiliares.

## Navegação

| Seção | Arquivo | Uso |
|---|---|---|
| Quick reference | `quick-reference.md` | Consulta rápida do dia a dia |
| Módulo | `concepts/key-oci-module.md` | Entender funções e contrato |
| Autenticação/resolução | `concepts/authentication-and-resolution.md` | Entender fallback de auth e OCID |
| Uso em jobs | `patterns/using-return-secret.md` | Padrão oficial de consumo em pipelines |
| Uso em MCP | `patterns/mcp-integration.md` | Resolver OCID no bridge Node/Python |
| Troubleshooting | `patterns/troubleshooting.md` | Diagnóstico de falhas comuns |
| Chaves de config | `references/config-keys.md` | Mapa de chaves mais usadas |

## Fontes de verdade

- `src/utils/key_oci.py`
- `mcp/capacity-database/scripts/resolve_oci_mcp.py`
- `mcp/capacity-database/src/config.js`
- `notebooks/eda_sql_server_destino.ipynb`
- `src/jobs/00_app_servidores_sql_apex.py` e `src/jobs/01..08,10`

