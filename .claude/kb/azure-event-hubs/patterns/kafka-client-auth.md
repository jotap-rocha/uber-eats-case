---
domain: azure-event-hubs
topic: kafka-client-auth
---

# Pattern — kafka-client-auth (producer/consumer contra Event Hubs)

Dois caminhos, ambos com `security.protocol=SASL_SSL` na porta **9093**:

| Caminho | Mecanismo | Quando |
|---|---|---|
| A. Connection string (SAS) | `PLAIN`, user `$ConnectionString` | lab, ferramentas que só falam PLAIN (Kafka Connect padrão, CLI) |
| B. Entra ID (OAuth 2.0) | `OAUTHBEARER` | produção; permite desligar SAS no namespace |

Tokens SAS **gerados** (assinatura com expiração) **não** funcionam no endpoint Kafka —
use a connection string da policy.

## A. Connection string (SAS)

### 1. Policy mínima por event hub

```hcl
resource "azurerm_eventhub_authorization_rule" "app_send" {
  name                = "app-send"
  namespace_name      = azurerm_eventhub_namespace.ns.name
  eventhub_name       = azurerm_eventhub.pedidos.name
  resource_group_name = azurerm_resource_group.base.name
  send   = true
  listen = false
  manage = false
}
# Guardar a connection string no Key Vault, não em output
resource "azurerm_key_vault_secret" "eh_send" {
  name         = "eh-pedidos-send"
  value        = azurerm_eventhub_authorization_rule.app_send.primary_connection_string
  key_vault_id = var.key_vault_id
}
```

Policy no **namespace** (`azurerm_eventhub_namespace_authorization_rule`) dá acesso a
todos os tópicos — usar só para Kafka Connect (que cria tópicos internos).

### 2. Java / Kafka CLI — sem segredo no arquivo

Kafka ≥ 3.5 tem `EnvVarConfigProvider`; o arquivo versionado só referencia a variável:

```properties
bootstrap.servers=<NAMESPACE>.servicebus.windows.net:9093
security.protocol=SASL_SSL
sasl.mechanism=PLAIN
config.providers=env
config.providers.env.class=org.apache.kafka.common.config.provider.EnvVarConfigProvider
sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="$ConnectionString" password="${env:EH_CONNECTION_STRING}";
request.timeout.ms=60000
```

Versão do Kafka < 3.5: gerar o `.properties` em runtime (template + env) em pasta
gitignored. Suporte do `config.providers` na CLI/cliente específico: **a validar**.

### 3. Python (confluent-kafka / librdkafka)

```python
import os
from confluent_kafka import Producer

conf = {
    "bootstrap.servers": f"{os.environ['EH_NAMESPACE']}.servicebus.windows.net:9093",
    "security.protocol": "SASL_SSL",
    "sasl.mechanism": "PLAIN",
    "sasl.username": "$ConnectionString",
    "sasl.password": os.environ["EH_CONNECTION_STRING"],   # nunca logar
    "client.id": "pedidos-producer",
}
p = Producer(conf)
p.produce("pedidos", key=b"pedido-1", value=b'{"valor": 10}')
p.flush(10)
```

## B. Entra ID (OAUTHBEARER)

### 1. RBAC

```hcl
resource "azurerm_role_assignment" "producer" {
  scope                = azurerm_eventhub.pedidos.id
  role_definition_name = "Azure Event Hubs Data Sender"
  principal_id         = var.app_principal_id   # MI ou SP da aplicação
}
```

Consumer: `Azure Event Hubs Data Receiver`. Com todos os clientes em Entra ID:
`local_authentication_enabled = false` no namespace.

### 2. Python com azure-identity

```python
import os
from azure.identity import DefaultAzureCredential
from confluent_kafka import Consumer

NS = os.environ["EH_NAMESPACE"]
cred = DefaultAzureCredential()   # MI em Azure; az login no laptop; SP via env no CI

def oauth_cb(_config):
    tok = cred.get_token(f"https://{NS}.servicebus.windows.net/.default")
    return tok.token, tok.expires_on

c = Consumer({
    "bootstrap.servers": f"{NS}.servicebus.windows.net:9093",
    "security.protocol": "SASL_SSL",
    "sasl.mechanism": "OAUTHBEARER",
    "oauth_cb": oauth_cb,
    "group.id": "pedidos-etl",
    "auto.offset.reset": "earliest",
})
c.subscribe(["pedidos"])
```

Escopo do token: `https://<NAMESPACE>.servicebus.windows.net/.default` (amostras
oficiais em github.com/Azure/azure-event-hubs-for-kafka `tutorials/oauth`).

### 3. Java

```properties
security.protocol=SASL_SSL
sasl.mechanism=OAUTHBEARER
sasl.jaas.config=org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;
sasl.login.callback.handler.class=<pacote>.CustomAuthenticateCallbackHandler
```

O handler é código do projeto (usa `azure-identity`); base nas amostras oficiais.

## Ajustes recomendados de cliente (Microsoft)

| Propriedade | Valor sugerido | Motivo |
|---|---|---|
| `request.timeout.ms` | 60000 | latência do serviço gerenciado |
| `metadata.max.age.ms` | 180000 | evitar desconexão por inatividade (a validar) |
| `connections.max.idle.ms` | 180000 | idem |
| `enable.idempotence` | true | at-least-once sem duplicar no producer |

## Checklist SI

- [ ] Nenhuma connection string em arquivo versionado, log ou output Terraform
- [ ] Policy por event hub com só `Send` ou `Listen`
- [ ] `RootManageSharedAccessKey` nunca usada por aplicação
- [ ] Rotação de chave seguida de restart dos clientes (conexões abertas não caem)
- [ ] Produção: Entra ID + `local_authentication_enabled = false`
