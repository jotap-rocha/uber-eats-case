# Módulo `key_oci`

## Escopo

O arquivo `src/utils/key_oci.py` centraliza o acesso a segredos para todo o projeto.

## Responsabilidades

- Ler `.config` e descobrir ambiente ativo via `DEFAULT.env`.
- Localizar a chave solicitada na seção do ambiente.
- Resolver OCID no OCI Vault e decodificar Base64 do `secret_bundle_content`.
- Fornecer funções utilitárias para valores literais e resolução híbrida (OCID ou texto puro).

## API atual

| Função | Entrada | Saída | Uso típico |
|---|---|---|---|
| `return_config_int(key)` | chave em `DEFAULT` | string | obter `env` |
| `read_secret_value(secret_client, secret_id)` | client OCI + OCID | string | leitura low-level |
| `_get_secrets_client()` | - | `oci.secrets.SecretsClient` | auth OCI com fallback |
| `resolve_credential_value(value)` | valor bruto | valor resolvido | bridge MCP e integrações |
| `return_secret(secret)` | nome da chave | string/None | jobs/notebooks |
| `return_config(key)` | nome da chave | string | valor não secreto |

## Contratos importantes

- `return_secret` espera que `.config` exista e que a seção de ambiente esteja válida.
- Se o secret vier vazio, retorna `None` com warning no logger.
- Falhas de leitura/autenticação são logadas e re-lançadas.

