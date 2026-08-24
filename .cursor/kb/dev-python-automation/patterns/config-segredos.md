# Configuração e segredos em jobs Python

> **Propósito:** Separar parâmetros operacionais de credenciais; evitar vazamentos em repo e logs.
> **MCP Validated:** 2026-05-07

## Quando usar

- Qualquer job que leia connection strings, tokens ou chaves.

## Implementação

| Fonte | Uso |
|-------|-----|
| Variáveis de ambiente | CI/CD e containers |
| Vault / OCI Secrets / Azure Key Vault | Produção — ler no arranque, não cachear em ficheiro plano |
| Ficheiros locais | `.env` **fora** do git; `.config` com OCIDs, não passwords |

Carregue valores num modelo validado (ver `tipagem-fronteiras.md`). **Nunca** `print(connection_string)`.

```python
import os
from pydantic import BaseModel, SecretStr


class Settings(BaseModel):
    sql_connection_secret_key: str  # nome da chave no vault
    log_level: str = "INFO"


def load_settings() -> Settings:
    return Settings.model_validate(os.environ)
```

Em runtime, resolver o segredo via cliente oficial e montar a string ODBC só em memória.

## Boas práticas

- Rotacionar segredos sem alterar código — só mapping env/vault.
- Mascarar outputs em **logging** (últimos 4 caracteres se necessário para debug).

## Veja também

- [injecao-dependencias.md](injecao-dependencias.md) — passar resolvedores e loggers, não instanciar tudo no meio da regra
- [../concepts/sql-server-conexao.md](../concepts/sql-server-conexao.md)
- Repositório exemplo interno com `key_oci` — alinhar política corporativa
