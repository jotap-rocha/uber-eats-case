# Quick Reference - key_oci

## Funções principais

- `return_secret(secret_key)`: recebe nome da chave no `.config` e devolve valor do secret resolvido no OCI Vault.
- `return_config(key)`: devolve valor literal da seção de ambiente ativa no `.config`.
- `resolve_credential_value(value)`: se `value` começar com `ocid1.`, resolve no Vault; caso contrário, devolve o próprio valor.

## Fluxo de autenticação OCI

1. Tenta `oci.config.from_file(profile_name="DEFAULT")`.
2. Se não houver arquivo, tenta `get_resource_principals_signer()`.
3. Se ambos falharem, lança `RuntimeError`.

## Exemplo rápido

```python
from src.utils import key_oci

host = key_oci.return_secret("SQL_SERVER_HOSTNAME_DESTINATION")
user = key_oci.return_secret("SQL_SERVER_CAPACITY_USER")
pwd = key_oci.return_secret("SQL_SERVER_CAPACITY_PASS")
db = key_oci.return_secret("SQL_SERVER_DATABASE_CAPACITY")
```

## Regras

- Não commitar valores de segredo em código.
- Guardar no `.config` apenas OCID ou identificadores esperados.
- Sempre usar chave por nome (`return_secret("...")`), nunca hardcode de secret.

