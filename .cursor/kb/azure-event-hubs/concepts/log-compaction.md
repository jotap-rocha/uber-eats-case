---
domain: azure-event-hubs
topic: log-compaction
---

# Log compaction em Event Hubs

Retenção **por chave** em vez de por tempo: o serviço mantém pelo menos o último evento
de cada chave. Equivalente ao `cleanup.policy=compact` do Kafka.

## Regras

| Ponto | Comportamento |
|---|---|
| Tier | Standard, Premium, Dedicated (Basic **não**) |
| Nível | por event hub (tópico); definido **na criação** — mudar política recria o recurso |
| Chave de compactação | a **partition key** do evento (no Kafka: a `key` do record) |
| Tombstone | evento com chave existente e **payload `null`** → chave removida na compactação |
| Visibilidade do tombstone | consumidores ainda veem o tombstone por `tombstone_retention_time_in_hours` |
| Quando roda | o serviço decide (não determinístico, não controlável) |
| Tamanho máx. (Standard) | **1 GB por partição** |

## Garantias

- Ordem preservada por chave e partição; offsets e sequence numbers não mudam.
- Quem lê do início vê **pelo menos** o estado final de cada chave.
- Entre execuções da compactação podem existir **várias versões** da mesma chave →
  consumidor trata como upsert (último vence), nunca assume unicidade.

## Usos

- CDC (estado atual por chave primária).
- Tabelas de estado/lookup para processamento de stream.
- Tópicos internos do **Kafka Connect** (`config`, `offset`, `status`) — **devem** ser
  compactados.

## Terraform

```hcl
resource "azurerm_eventhub" "clientes_cdc" {
  name            = "clientes-cdc"
  namespace_id    = azurerm_eventhub_namespace.ns.id
  partition_count = 2

  retention_description {
    cleanup_policy                    = "Compact"   # "Delete" = retenção por tempo
    tombstone_retention_time_in_hours = 24
  }
}
```

Não setar `message_retention` junto com `Compact` (retenção por tempo só vale para
`Delete`) — combinação exata **a validar** no `plan`.

## Producer: requisitos

- Todo evento **precisa de key** — sem key não há o que compactar.
- Deleção = enviar `key` + `value = null`.
- Mesma key sempre na mesma partição (particionador padrão por hash da key garante).

```python
# confluent-kafka: deleção lógica (tombstone)
producer.produce("clientes-cdc", key=b"cliente-123", value=None)
```

## Armadilhas

| Sintoma | Causa |
|---|---|
| Event hub "encheu" (1 GB/partição) | muitas chaves distintas no Standard → mais partições na criação ou Premium |
| Duplicatas da mesma chave na leitura | compactação ainda não rodou (esperado) |
| Chave deletada "volta" | tombstone expirou antes do consumidor ler → aumentar retenção do tombstone |
