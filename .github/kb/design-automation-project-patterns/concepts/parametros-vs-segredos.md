# Parâmetros (`config/`) vs segredos (cofre)

> **Propósito:** Separar o que **varia por ambiente** mas não é credencial do que **nunca** deve estar em YAML versionado como texto claro.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-07

## Visão geral

| Classe | Onde | Exemplos |
|--------|------|----------|
| **Parâmetros** | `config/<env>/*.yaml` | host, porta, nome da base, timeouts de negócio, flags `debug`, nomes de tabela que diferem dev/prod |
| **Segredos** | Cofre na nuvem + facade no código | passwords, tokens OAuth, chaves privadas |

**Regra:** se só muda entre Dev e Prod **e não é segredo**, vai para YAML. O **código** permanece igual; troca-se o “mapa” carregado (`APP_ENV=prod`).

## Webhooks e zonas cinzentas

URLs de Teams podem ser tratadas como **parâmetro** em ambientes isolados ou como **segredo** se a política de segurança exigir — decidir por norma corporativa e ser **consistente** entre `dev`/`prod`.

## Bootstrap do cofre

Um ficheiro **local** (ex.: `.config` na raiz) pode conter apenas **IDs de segredo**, perfil OCI ou caminho para credencial **não commitada** — o suficiente para o **único módulo vault** obter o restante em runtime. Ver [ponto-unico-vault.md](../patterns/ponto-unico-vault.md).

## Anti-padrões

- Senha em `database.yaml` versionado no Git.
- `core` a ler `os.environ` disperso — centralizar leitura em `app` ou módulo `settings` tipado ([tipagem-fronteiras](../../dev-python-automation/concepts/tipagem-fronteiras.md)).

## Relacionado

- [config-segredos](../../dev-python-automation/patterns/config-segredos.md)
- [yaml-multi-ambiente.md](../patterns/yaml-multi-ambiente.md)
