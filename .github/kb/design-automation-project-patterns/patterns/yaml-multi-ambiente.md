# YAML por ambiente (`config/dev` vs `config/prod`)

> **Propósito:** Mapas de negócio segregados sem alterar código entre ambientes.
> **MCP Validated:** 2026-05-07

## Quando usar

- Mesmo job corre em **homologação** e **produção** com hosts, bases ou feature flags diferentes.
- Equipa quer **diff** legível só nos YAML, não em `.py`.

## Estrutura

```text
config/
├── dev/
│   ├── database.yaml
│   ├── teams.yaml
│   └── app.yaml
└── prod/
    ├── database.yaml
    ├── teams.yaml
    └── app.yaml
```

**Domínios sugeridos:**

| Ficheiro | Conteúdo típico |
|----------|-----------------|
| `database.yaml` | servidor, database, timeouts, schema |
| `teams.yaml` | webhook URL ou ID de canal **conforme política** |
| `app.yaml` | `debug`, limites de lote, nomes de tabelas de log |

## Carregamento

1. Variável `APP_ENV` ou argumento CLI escolhe `dev` | `prod`.
2. Carregar e validar com modelo tipado (pydantic ou equivalente) — falhar no arranque se faltar chave.

```python
def load_db_settings(env: str) -> DatabaseSettings:
    path = Path("config") / env / "database.yaml"
    ...
```

## Boas práticas

- **Um domínio por ficheiro** — evita YAML gigante.
- **Defaults** só onde fizer sentido; ambientes críticos devem ser explícitos.
- **Não** misturar segredos — ver [parametros-vs-segredos.md](../concepts/parametros-vs-segredos.md).

## Veja também

- [ponto-unico-vault.md](ponto-unico-vault.md)
