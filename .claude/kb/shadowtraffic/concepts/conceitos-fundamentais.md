# Conceitos fundamentais do ShadowTraffic

> **Purpose**: Vocabulário mínimo para ler/editar `gen/unified/uber-eats.json.template` sem depender de tentativa e erro.
> **Confidence**: 0.95
> **MCP Validated**: 2026-09-07 — fonte: https://docs.shadowtraffic.io/overview/ e https://docs.shadowtraffic.io/cheatsheet/

## Overview

ShadowTraffic é uma ferramenta em container que gera dados sintéticos "de produção" para múltiplos backends (Kafka, Postgres, MySQL, Oracle, S3/MinIO, SQL Server, Databricks, webhooks, etc.) a partir de **um único arquivo de configuração JSON**. Em vez de escrever código, o usuário substitui valores concretos por funções marcadas com a chave `_gen` — "replace concrete values with functions. That is all that's happening here" (doc oficial).

Neste repositório existe **um config unificado** (`gen/unified/uber-eats.json.template`), não um por conexão, porque os `lookup`s cruzam Postgres ↔ Oracle ↔ MinIO no mesmo processo (ver `concepts/lookup-semantica-e-limites.md`).

## Os três blocos de um config

```json
{
  "generators": [ /* array de objetos — um por tabela/tópico/bucket-prefix */ ],
  "connections": { /* mapa nome→config de backend */ }
}
```

- **`connections`** — mapeia um nome lógico (`"postgres"`, `"oracle"`, `"minio"`) para `kind` + `connectionConfigs` (host, porta, credenciais). Um generator referencia a connection pelo nome em `"connection": "..."`.
- **`generators`** — cada item descreve o destino (`table` para SQL, `bucket`+`bucketConfigs` para S3, `topic` para Kafka) e o formato do dado (`row` para SQL, `data` para object storage/Kafka).
- **Funções `_gen`** — qualquer valor de campo pode ser substituído por `{"_gen": "<nome>", ...params}`. Podem ser aninhadas (uma função dentro de outra) para espelhar a complexidade do dado.

## Categorias de função usadas neste projeto

| Categoria | Exemplos usados aqui |
|---|---|
| Escalar | `uuid`, `sequentialInteger`, `sequentialString`, `string` (com `expr` tipo Faker `#{Name.fullName}`), `boolean`, `uniformDistribution`, `normalDistribution` |
| Data/hora | `formatDateTime`, `now` |
| Seleção | `lookup`, `var`, `oneOf`, `weightedOneOf`, `stateMachine`, `previousEvent` |
| Math | `math` (fórmulas com variáveis nomeadas via `names`) |
| Geo | `geoWander` (simulação de movimento GPS em `kafka/gps/`) |

Categorias existentes na doc oficial mas **não usadas** neste config: Easing, Transformation (`map`/`merge`/`cycle`), Preprocessing (`env`/`loadJsonFile`), `ai`/`customFunction`.

## `localConfigs` — controle de throughput por generator

| Chave | Efeito |
|---|---|
| `maxEvents` | Número exato de eventos/linhas; o generator finaliza sozinho ao atingir (comportamento normal, não é erro) |
| `throttleMs` | Atraso entre eventos — menor = mais rápido |

Generators sem `maxEvents` (ex.: os que usam `fork`+`stateMachine`) rodam continuamente até `maxForks` ser atingido e as máquinas de estado ficarem ociosas.

## Related

- [lookup-semantica-e-limites](lookup-semantica-e-limites.md)
- [mutacao-real-fork-statemachine](mutacao-real-fork-statemachine.md)
- [conexoes-sql-e-object-storage](../patterns/conexoes-sql-e-object-storage.md)
