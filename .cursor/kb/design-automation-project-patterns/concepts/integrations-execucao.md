# `src/integrations/` — execução (“mão na massa”)

> **Propósito:** Todo IO e SDKs externos; implementações concretas das portas que `core` utiliza.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-07

## Regra

**`integrations/`** concentra o código que **efetivamente** fala com o mundo exterior:

| Subpasta | Exemplos |
|----------|----------|
| `database/` | Conexões, repositórios pyodbc/SQLAlchemy, queries parametrizadas |
| `messaging/` | Webhook Teams, SMTP, filas |
| `cloud/` | Facade de vault (OCI/Azure), clientes de API cloud |

Cada integração deve expor **classes** com métodos claros (públicos para uso por `core`, `_privados` para detalhe interno). **Não** importar `core` a partir de `integrations` (evitar ciclo).

## Contrato com `core`

`core` depende de **Protocolos** / ABCs / tipos definidos em `core` ou `src/utils/contracts.py`, e recebe **instâncias** construídas na composição (tipicamente montadas antes do `start` em `main.py` ou factory dedicada em `src/utils/`).

## Relacionado

- [core-orquestracao.md](core-orquestracao.md)
- [ponto-unico-vault.md](../patterns/ponto-unico-vault.md)
