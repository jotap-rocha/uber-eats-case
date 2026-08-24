# Ponto único de resgate de segredos (cloud vault facade)

> **Propósito:** Toda leitura de senha/token na nuvem passa por **um** módulo — legibilidade, auditoria e troca de provedor localizada.
> **MCP Validated:** 2026-05-07

## Quando usar

- Projeto usa **OCI Vault**, **Azure Key Vault**, **AWS Secrets Manager**, etc.
- Vários integradores precisam da mesma credencial ou políticas de cache consistentes.

## Padrão

Colocar a facade em **`integrations/cloud/`** (ex.: `oci_vault.py`, `azure_keyvault.py`). As demais camadas chamam só métodos estáveis:

```python
# integrations/cloud/vault.py — exemplo genérico
class SecretVault(Protocol):
    def get_secret(self, logical_name: str) -> str: ...
```

Implementação concreta lê `.config` / env para **OCIDs ou URIs**, nunca passwords embutidos.

**Neste repositório (Sentinela):** segredos via **`src/utils/key_oci.py`** e `.config` na raiz do clone (localizada por **`src/utils/repo_root.py`**), sem pasta `integrations/cloud/` dedicada.

## Sinais no código

- Presença de `vault.get_secret("database_password")` (ou nome da API do projeto) indica **consumo sensível** — útil em revisão e static checks.

## Fluxo típico (OCI)

1. `.config` na raiz (gitignored ou só com placeholders): perfil, OCIDs de segundos níveis.
2. Facade inicializa cliente OCI uma vez (ou lazy).
3. `integrations/database/` pede strings ao facade, não duplica `oci.secrets` espalhado.

## Anti-padrões

- `oci.SecretsClient` instanciado em cinco módulos diferentes.
- Segredo lido em `core` — manter IO na **integrations** e injetar **valores já resolvidos** ou um **port** estreito.

## Veja também

- [parametros-vs-segredos.md](../concepts/parametros-vs-segredos.md)
- [injecao-dependencias](../../dev-python-automation/patterns/injecao-dependencias.md)
