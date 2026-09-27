# Tier Standard e obrigatorio (nao Basic) -- o Kafka Connect (Debezium + sink
# ADLS) depende de topicos internos compactados (connect-offsets/configs/status),
# so suportados a partir do Standard. Ver DESIGN, achado tecnico / Decisao 1.
resource "azurerm_eventhub_namespace" "fase1" {
  name                = "ubereats-fase1-eventhub-ns"
  location            = azurerm_resource_group.fase1.location
  resource_group_name = azurerm_resource_group.fase1.name
  sku                 = "Standard"
  capacity            = 1

  # Protocolo Kafka habilitado por padrao no tier Standard -- endpoint
  # <namespace>.servicebus.windows.net:9093, usado por Airbyte, MinIO e
  # Kafka Connect (achado tecnico do BRAINSTORM, Decisao 5 do DESIGN).
}

# 1 topico por fonte -- Postgres e Oracle sao lidos tanto pelo Stream Analytics
# (Etapa 4) quanto pelo Kafka Connect Sink Connector que alimenta o ADLS
# (Etapa 2, Decisao 1 do DESIGN: captura unica, 2 consumidores).
resource "azurerm_eventhub" "postgres" {
  name                = "postgres"
  namespace_name      = azurerm_eventhub_namespace.fase1.name
  resource_group_name = azurerm_resource_group.fase1.name
  partition_count     = 2
  message_retention   = 1
}

resource "azurerm_eventhub" "oracle" {
  name                = "oracle"
  namespace_name      = azurerm_eventhub_namespace.fase1.name
  resource_group_name = azurerm_resource_group.fase1.name
  partition_count     = 2
  message_retention   = 1
}

resource "azurerm_eventhub" "minio" {
  name                = "minio"
  namespace_name      = azurerm_eventhub_namespace.fase1.name
  resource_group_name = azurerm_resource_group.fase1.name
  partition_count     = 2
  message_retention   = 1
}

resource "azurerm_eventhub_namespace_authorization_rule" "connect" {
  name                = "kafka-connect-and-airbyte"
  namespace_name      = azurerm_eventhub_namespace.fase1.name
  resource_group_name = azurerm_resource_group.fase1.name
  listen              = true
  send                = true
  manage              = false
}
