# Semântica real do `lookup` e seus limites

> **Purpose**: Evitar que um agente assuma garantias que o `lookup` do ShadowTraffic **não** oferece.
> **Confidence**: 0.95
> **MCP Validated**: 2026-09-07 — fonte: https://docs.shadowtraffic.io/functions/lookup/ e https://docs.shadowtraffic.io/functions/var/

## Overview

`lookup` busca um evento/linha **já gerado** de outra collection (tabela, tópico, bucket+keyPrefix, ou outro generator por `name`) e, opcionalmente, extrai um campo com `path`. É o mecanismo usado para toda referência cruzada no config unificado (ex.: `order_items.restaurant_id` faz `lookup` em `oracle.restaurants`).

## Garantia real (o que o ShadowTraffic promete)

> "ShadowTraffic guarantees that events will only be available for lookup after they have been successfully written to the target collection."

Ou seja: nunca aparece uma referência a uma linha que ainda não existe no destino. É a base da integridade referencial deste projeto (chaves estrangeiras "lógicas" sempre apontam para algo que já foi escrito).

## Estratégias de seleção

| `strategy` | Efeito |
|---|---|
| `random` (padrão) | Amostra aleatória de qualquer evento já escrito |
| `first` | Sempre o primeiro evento gerado para aquele destino |
| `last` | O evento mais recente gerado |

`histogram` pode enviesar a distribuição (ex.: 80% das leituras caem em 20% dos registros).

## LIMITE CRÍTICO — múltiplas chamadas de `lookup` não são consistentes

> "If you need to look up multiple fields, be careful not to use `lookup` more than once in the same generator. Multiple calls are **not** consistent."

Cada chamada de `lookup` é uma amostragem **independente**. Duas chamadas ao mesmo `table`/`bucket` **podem retornar registros diferentes**, mesmo dentro do mesmo evento gerado.

**Padrão correto:** um único `lookup` guardado em `vars`/`varsOnce`, depois `var` + `path` para cada campo (ver `patterns/evitar-lookup-circular-e-multiplo.md`). A doc do `var` confirma o oposto: "If you make multiple references to the same var in a single generator, you are guaranteed to get the same value each time."

### Gotcha real já existente neste config

`gen/unified/uber-eats.json.template`, generator `kafka/route/`, campos `start_lat` e `start_lon`:

```json
"start_lat": {"_gen": "lookup", "connection": "oracle", "table": "restaurants", "path": ["row", "lat"]},
"start_lon": {"_gen": "lookup", "connection": "oracle", "table": "restaurants", "path": ["row", "lon"]}
```

São **duas chamadas de `lookup` separadas** contra a mesma tabela `restaurants` — pela regra acima, **não há garantia de que `start_lat`/`start_lon` venham do mesmo restaurante**. Isso é adicional (mais grave) ao gap já registrado no ADR de `INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC` (que discutia apenas "restaurante real, mas não necessariamente o do pedido"). Não foi corrigido nesta tarefa de KB — é um achado a considerar antes de qualquer feature que dependa de `start_lat`/`start_lon` serem coordenadas coerentes entre si.

## Lookup circular — por que não funciona

Um generator **A** não pode fazer `lookup` em **B** se a geração de **B** depende de **A** já existir (nenhum dos dois teria por onde começar). Decisão já registrada neste projeto: `orders.payment_key`/`orders.rating_key` foram **removidos** (não "corrigidos") porque criavam esse ciclo com `payments.order_key`/`ratings.order_id` — ver `.claude/sdd/archive/INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC/DESIGN_INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC.md`.

## Related

- [conceitos-fundamentais](conceitos-fundamentais.md)
- [evitar-lookup-circular-e-multiplo](../patterns/evitar-lookup-circular-e-multiplo.md)
