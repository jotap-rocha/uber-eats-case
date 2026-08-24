# Autenticação e Resolução de Segredos

## Estratégia de autenticação OCI

No `_get_secrets_client()`:

1. **Primário:** `~/.oci/config` com profile `DEFAULT`.
2. **Fallback:** `Resource Principal` (`oci.auth.signers.get_resource_principals_signer()`).
3. **Erro final:** `RuntimeError` explicando as duas tentativas.

## Resolução por tipo de entrada

### `return_secret(secret_key)`

- Lê `.config`.
- Busca `env` em `[DEFAULT]`.
- Acessa seção `[env]`.
- Obtém OCID da chave.
- Consulta OCI Vault.
- Decodifica base64 e retorna o segredo.

### `resolve_credential_value(value)`

- `None` -> `None`
- string vazia -> string vazia
- **não** começa com `ocid1.` -> devolve valor original
- começa com `ocid1.` -> resolve no OCI Vault e retorna valor secreto

Essa função permite operar com configurações mistas (valor literal ou OCID), sem duplicar lógica em outros módulos.

## Contextos onde isso é usado

- Jobs PySpark (`src/jobs/*`): `return_secret("...")`
- Notebook EDA: `notebooks/eda_sql_server_destino.ipynb`
- Bridge MCP: `mcp/capacity-database/scripts/resolve_oci_mcp.py`

