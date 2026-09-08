# Evitar lookup circular e lookup múltiplo inconsistente

> **Purpose**: Dar ao agente um padrão pronto para campos que dependem de mais de um valor do mesmo registro referenciado, e um checklist para não desenhar dependências circulares entre generators.
> **MCP Validated**: 2026-09-07 — fonte: docs.shadowtraffic.io/functions/{lookup,var}/ + `.claude/sdd/archive/INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC/`

## When to Use

- Um novo campo precisa de **dois ou mais valores do mesmo registro** referenciado (ex.: `lat` e `lon` do mesmo restaurante).
- Está avaliando adicionar um `lookup` de A para B, e B (ou algo que B depende) já faz `lookup` de volta para A.
- Está revisando um generator existente que usa `lookup` mais de uma vez contra a mesma tabela/bucket.

## Implementation — padrão correto (single lookup + var/path)

```json
{
  "vars": {
    "restaurant_ref": {
      "_gen": "lookup",
      "connection": "oracle",
      "table": "restaurants"
    }
  },
  "data": {
    "start_lat": {
      "_gen": "var",
      "var": "restaurant_ref",
      "path": ["row", "lat"]
    },
    "start_lon": {
      "_gen": "var",
      "var": "restaurant_ref",
      "path": ["row", "lon"]
    }
  }
}
```

`vars` roda uma vez por evento gerado (valor fresco a cada iteração); `varsOnce` roda uma única vez para a vida do generator. Múltiplas referências ao **mesmo** `var` dentro do mesmo evento são garantidamente consistentes — ao contrário de múltiplas chamadas de `lookup`.

**Nota:** este exemplo é ilustrativo (reescreve o padrão correto para o caso de `kafka/route.start_lat/start_lon` descrito em `concepts/lookup-semantica-e-limites.md`). Não foi aplicado automaticamente ao `gen/unified/uber-eats.json.template` — decidir a correção do generator real é uma tarefa separada, não desta KB.

## Configuration

| Chave | Default | Description |
|---|---|---|
| `vars` | — | Reavaliado a cada evento; usar quando o valor pode variar por linha |
| `varsOnce` | — | Avaliado uma única vez; usar para valores fixos por generator (ex.: seed de config) |
| `path` (em `var`) | — | Array de chaves/índices para navegar dentro do valor guardado |

## Checklist anti-circularidade

1. Antes de adicionar `lookup` de A→B, confirme que B **não** depende (direta ou indiretamente) de A já existir.
2. Se dois generators precisam um do outro, escolha **um único sentido** e aceite que o campo do lado "de trás" não pode existir (ver decisão de remover `orders.payment_key`/`orders.rating_key` no ADR de `INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC` — a relação já existe pelo lado oposto, via `payments.order_key`/`ratings.order_id`).
3. Prefira expor a FK apenas no lado "mais novo" da relação (quem é criado depois pode olhar para trás; quem é criado antes não pode olhar para frente).

## Example Usage

Ver os generators `order_items` (fork com `key` = `lookup` em `orders.order_id`) e `receipts` (lookup direto em `orders`+`payments`) no config atual — ambos seguem o sentido correto (criados depois de `orders`/`payments` já existirem).

## See Also

- [lookup-semantica-e-limites](../concepts/lookup-semantica-e-limites.md)
- [conceitos-fundamentais](../concepts/conceitos-fundamentais.md)
