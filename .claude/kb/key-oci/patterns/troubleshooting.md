# Troubleshooting do `key_oci`

## Erros frequentes

| Sintoma | Causa provável | Ação |
|---|---|---|
| `Arquivo .config não encontrado ou vazio` | execução fora da raiz ou `.config` ausente | executar na raiz do repo e validar arquivo |
| `Seção '<env>' não encontrada` | `DEFAULT.env` inválido | corrigir seção no `.config` |
| `Chave '<X>' não encontrada` | nome da chave errado | revisar chave usada no código |
| `ConfigFileNotFound` OCI | `~/.oci/config` ausente | configurar OCI local ou usar Resource Principal |
| erro de autenticação Resource Principal | execução fora de ambiente com RP | rodar com `~/.oci/config` válido |
| retorno `None` para segredo | secret vazio no Vault | revisar valor no OCI Secret |

## Checklist de diagnóstico

1. Confirmar CWD na raiz do projeto.
2. Validar `DEFAULT.env` e seção correspondente no `.config`.
3. Conferir se o valor da chave é um OCID válido (`ocid1...`).
4. Testar autenticação OCI local.
5. Reexecutar fluxo com logs habilitados.

## Snippet de validação rápida

```python
from src.utils import key_oci
print(key_oci.return_config_int("env"))
print(key_oci.return_secret("SQL_SERVER_HOSTNAME_DESTINATION"))
```

