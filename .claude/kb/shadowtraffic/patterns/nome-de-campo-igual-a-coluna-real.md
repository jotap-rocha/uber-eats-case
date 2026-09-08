# Nome de campo em `row` deve ser igual ao nome real da coluna SQL

> **Purpose**: Prevenir a classe de bug já vivida 2x na migração para Oracle (Onda 3, Etapa 3) — `ORA-00904: invalid identifier`.
> **MCP Validated**: 2026-09-07 — fonte: docs.shadowtraffic.io/connections/oracle/ + `.claude/sdd/reports/BUILD_REPORT_DIVERSIFICACAO_FONTES_UBEREATS_ETAPA3.md`

## When to Use

- Editando ou criando um generator cujo destino é `postgres`, `oracle`, `mysql` ou `sqlServer` **e** a tabela já existe fisicamente com DDL fixo (criada por script `sql/*.sh`, não pelo ShadowTraffic).
- Renomeando qualquer chave dentro de `row` (ou `where` de um `op: update`) de um generator SQL.
- Fazendo code review de um PR que mexe em `gen/unified/uber-eats.json.template`.

## O problema

O ShadowTraffic **usa a chave do JSON em `row` como nome literal da coluna** no `INSERT`/`UPDATE` gerado — não existe camada de alias/mapeamento lógico. Se a chave não bater com o nome real da coluna, o banco rejeita a query.

## Implementation — checklist antes de commitar mudança em generator SQL

```text
1. Abra a DDL real da tabela (ex.: sql/oracle/03_create_tables_pedido_pagamento.sh).
2. Liste as colunas exatas (nome + ordem não importa, mas o NOME sim).
3. Compare 1:1 com as chaves de "row" (e "where", se houver op:update) do generator.
4. Qualquer chave com sufixo "_key" ou nome "lógico" que não apareça na DDL = bug.
```

## Incidente real (referência, não repetir)

Ao migrar `orders`/`payments`/`order_items`/`receipts` para Oracle (Etapa 3), o generator usava `user_key`/`restaurant_key`/`driver_key`/`order_key` como nomes de campo — herdados de uma época em que a tabela ainda não existia com nome fixo. A tabela real (`sql/oracle/03_create_tables_pedido_pagamento.sh`) usa `user_id`/`restaurant_id`/`driver_id`/`order_id`. Resultado:

```text
java.sql.BatchUpdateException: ORA-00904: "DRIVER_KEY": invalid identifier
```

Correção: renomear as chaves no `row` do generator **e** nos scripts Bronze/Silver que liam essas colunas (`USER_KEY`→`USER_ID` etc.) — o bug se propagava para o pipeline Databricks se não fosse pego a tempo.

## Por que `sqlHint` não ajuda aqui

`sqlHint` só sobrescreve o **tipo SQL** de uma coluna (ex.: `"stock_id": "VARCHAR2(36) PRIMARY KEY"`), nunca o **nome**. Não é uma ferramenta de aliasing.

## Nuance: `tablePolicy`

A connection Oracle aceita `tablePolicy`: `create` (padrão — cria a tabela se não existir), `dropAndCreate` (limpa antes de escrever) ou `manual` (exige tabela pré-existente). Este projeto **não define `tablePolicy` explicitamente** na connection `oracle` — como as tabelas (`orders`, `payments`, `order_items`, `receipts`, `restaurants`, `products`, `inventory`) já são criadas antes por `sql/oracle/*.sh`, o comportamento padrão (`create`) simplesmente as encontra existentes e escreve nelas; o `sqlHint` presente em vários generators só teria efeito se o ShadowTraffic precisasse criar a tabela do zero. Isso é dedução a partir da doc + config atual — não há log de execução que confirme explicitamente esse caminho de código.

## See Also

- [mutacao-real-fork-statemachine](../concepts/mutacao-real-fork-statemachine.md)
- [conexoes-sql-e-object-storage](conexoes-sql-e-object-storage.md)
