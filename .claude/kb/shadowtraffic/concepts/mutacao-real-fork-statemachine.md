# Mutação real: `fork` + `stateMachine` + `op: update`

> **Purpose**: Explicar o mecanismo que este projeto usa para gerar UPDATEs reais (capturados por CDC), não apenas INSERTs.
> **Confidence**: 0.9
> **MCP Validated**: 2026-09-07 — fonte: WebSearch em docs.shadowtraffic.io/fork/{maxForks,stagger}/, docs.shadowtraffic.io/functions/stateMachine/, + `.claude/sdd/reports/BUILD_REPORT_DIVERSIFICACAO_FONTES_UBEREATS_ETAPA{1,3}.md`

## Overview

Por padrão, um generator SQL só faz `INSERT`. Para simular o ciclo de vida real de uma entidade (pedido mudando de status, pagamento sendo confirmado, motorista entrando/saindo de turno) este projeto combina três mecanismos: `fork` (clona o generator em N instâncias paralelas), `stateMachine` (controla em que estado cada instância está) e `op: "update"` (faz o generator emitir um UPDATE real na linha já inserida, em vez de outro INSERT).

Validado neste repo em **Postgres** (`drivers`, Onda 1) e depois pela primeira vez em **Oracle** (`orders`, `payments`, Onda 3 Etapa 3) — confirmado via `rpk topic consume` que o Debezium captura os UPDATEs como `"op":"u"` com `before`/`after` completos.

## `fork` — identidade e ciclo de vida

| Chave | Efeito |
|---|---|
| `key` | Gera a identidade de cada fork (neste projeto sempre `sequentialInteger`, ex.: `driver_id`, `order_id`, `payment_id`) |
| `maxForks` | Teto de forks simultâneos; sem `keepAlive`, para de criar novos ao atingir o teto |
| `keepAlive: true` | Fork permanece "vivo" indefinidamente para continuar sofrendo transições de estado (usado em `orders`/`payments`) |
| `stagger` | Espaçamento mínimo (ms) entre a criação de novos forks |

## `stateMachine` — estados e transições

Três formas de declarar `transitions`: mapa (`{"a": "b", "b": "c"}`), array sequencial (`["s1","s2","s3"]`), ou array com repetição (`["s1", {"state": "s2", "times": 3}]`). Neste projeto usa-se sempre o formato **mapa**, com `initial` explícito.

Cada `states.<nome>` define o que acontece ao entrar naquele estado. Para a **primeira** entrada (estado inicial), o generator faz `INSERT` normal (`row` com todos os campos). Para os estados seguintes, usa-se:

```json
"onShift": {
  "op": "update",
  "where": {"driver_id": {"_gen": "var", "var": "forkKey"}},
  "row": { /* apenas os campos que mudam */ }
}
```

- `op: "update"` + `where` (mapeando coluna → valor, tipicamente o `forkKey`) identifica a linha a atualizar.
- Campos não mencionados em `row` **não** são tocados pelo UPDATE.
- `previousEvent` com `path` recupera um valor do evento anterior da mesma máquina de estado (ex.: preservar `total_deliveries` entre transições que não o alteram).

Transições podem ser determinísticas (`"offShift": "onShift"`) ou probabilísticas via `weightedOneOf` (ex.: 95% volta a `onShift`, 5% vai a `banned`, como em `drivers`).

## Casos reais neste config

| Generator | Connection | Estados | O que muda |
|---|---|---|---|
| `drivers` | postgres | `insertIt → onShift ⇄ offShift → banned(5%)` | status, ganhos, entregas acumuladas |
| `orders` | oracle | 9 estados (`insertIt → ... → completed`) | `status`, `updated_at` a cada transição |
| `payments` | oracle | `insertIt → {succeeded 85% / failed 10% / refunded 5%}` | `status`, `captured`, `failure_reason`, `refund_amount` |

## Gotcha real já corrigido

Ver `patterns/nome-de-campo-igual-a-coluna-real.md` — ao migrar `orders`/`payments` para Oracle (tabela pré-criada por DDL manual), os nomes de campo em `row`/`where` precisam bater **exatamente** com o nome real da coluna; um alias lógico (`*_key`) quebra o `INSERT`/`UPDATE` com `ORA-00904`.

## Related

- [conceitos-fundamentais](conceitos-fundamentais.md)
- [nome-de-campo-igual-a-coluna-real](../patterns/nome-de-campo-igual-a-coluna-real.md)
