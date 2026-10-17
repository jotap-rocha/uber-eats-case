---
domain: azure-event-hubs
topic: quick-reference
---

# Azure Event Hubs (Kafka) — Quick Reference

### Cliente Kafka — SAS (connection string)

```properties
bootstrap.servers=<NAMESPACE>.servicebus.windows.net:9093
security.protocol=SASL_SSL
sasl.mechanism=PLAIN
sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="$ConnectionString" password="<EH_CONNECTION_STRING>";
```

`username` é o literal `$ConnectionString`. Valor real injetado em runtime (env/Key
Vault) — ver `patterns/kafka-client-auth.md`.

### Cliente Kafka — Entra ID (OAuth)

```properties
bootstrap.servers=<NAMESPACE>.servicebus.windows.net:9093
security.protocol=SASL_SSL
sasl.mechanism=OAUTHBEARER
sasl.jaas.config=org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;
sasl.login.callback.handler.class=<CallbackHandler que obtém token Entra ID>
```

### Standard — limites que mais mordem

| Limite | Standard |
|---|---|
| Event hubs (tópicos) por namespace | **10** |
| Partições por event hub | 32 (não muda depois no Standard; nunca diminui) |
| Consumer groups por event hub | 20 (Kafka: 1.000 por namespace) |
| Retenção máxima | 7 dias |
| Evento/publicação máx. | 1 MB |
| Compacted event hub | **1 GB por partição** |
| Throughput por TU | in 1 MB/s ou 1.000 ev/s · out 2 MB/s |
| Conexões | 5.000 por namespace |

### Só Premium/Dedicated (não conte com isso no Standard)

Kafka Streams (preview) · transações Kafka (preview) · compressão gzip ·
alterar nº de partições.

### Terraform mínimo

```hcl
resource "azurerm_eventhub_namespace" "ns" {
  name                = "<NAMESPACE>"
  location            = azurerm_resource_group.base.location
  resource_group_name = azurerm_resource_group.base.name
  sku                 = "Standard"
  capacity            = 1
  auto_inflate_enabled = false
}
resource "azurerm_eventhub" "pedidos" {
  name              = "pedidos"
  namespace_id      = azurerm_eventhub_namespace.ns.id
  partition_count   = 4
  message_retention = 1
}
```

### az CLI

```bash
az eventhubs eventhub create -g <RG> --namespace-name <NAMESPACE> -n pedidos \
  --partition-count 4 --retention-time-in-hours 24 --cleanup-policy Delete
az eventhubs eventhub authorization-rule create -g <RG> --namespace-name <NAMESPACE> \
  --eventhub-name pedidos -n app-send --rights Send
az eventhubs namespace delete -g <RG> -n <NAMESPACE>      # único jeito de parar de pagar
```

(Flags `--retention-time-in-hours`/`--cleanup-policy` — **a validar** na versão do az.)

### RBAC (Entra ID)

| Role | Para |
|---|---|
| `Azure Event Hubs Data Sender` | producer |
| `Azure Event Hubs Data Receiver` | consumer |
| `Azure Event Hubs Data Owner` | Kafka Connect (cria tópicos internos) |

### Troubleshooting

| Sintoma | Causa provável |
|---|---|
| Timeout no bootstrap | porta 9093 bloqueada / tier Basic |
| `SaslAuthenticationException` | `username` diferente de `$ConnectionString`; string do event hub errado |
| `TopicAuthorizationException` | policy só `Listen` para producer (ou vice-versa) |
| Erro ao criar 11º tópico | limite de 10 event hubs no Standard |
