resource "azurerm_stream_analytics_job" "kappa" {
  name                                     = "ubereats-fase1-kappa"
  resource_group_name                     = azurerm_resource_group.fase1.name
  location                                = azurerm_resource_group.fase1.location
  compatibility_level                     = "1.2"
  data_locale                             = "en-US"
  events_out_of_order_policy              = "Adjust"
  output_error_policy                     = "Drop"
  events_out_of_order_max_delay_in_seconds = 5
  events_late_arrival_max_delay_in_seconds = 60
  transformation_query                    = file("${path.module}/../../../sql/azure/stream_analytics_query.sql")

  streaming_units = 1 # ajustar no build real conforme volume (Open Question do DEFINE)
}

# 3 inputs de stream -- 1 por topico do Event Hub (postgres/oracle/minio),
# sem componente-ponte (Decisao 5 do DESIGN).
resource "azurerm_stream_analytics_stream_input_eventhub" "postgres" {
  name                     = "postgres-input"
  stream_analytics_job_name = azurerm_stream_analytics_job.kappa.name
  resource_group_name      = azurerm_resource_group.fase1.name
  eventhub_consumer_group_name = "$Default"
  eventhub_name            = azurerm_eventhub.postgres.name
  servicebus_namespace     = azurerm_eventhub_namespace.fase1.name
  shared_access_policy_key  = azurerm_eventhub_namespace_authorization_rule.connect.primary_key
  shared_access_policy_name = azurerm_eventhub_namespace_authorization_rule.connect.name

  serialization {
    type     = "Json"
    encoding = "UTF8"
  }
}

resource "azurerm_stream_analytics_stream_input_eventhub" "oracle" {
  name                     = "oracle-input"
  stream_analytics_job_name = azurerm_stream_analytics_job.kappa.name
  resource_group_name      = azurerm_resource_group.fase1.name
  eventhub_consumer_group_name = "$Default"
  eventhub_name            = azurerm_eventhub.oracle.name
  servicebus_namespace     = azurerm_eventhub_namespace.fase1.name
  shared_access_policy_key  = azurerm_eventhub_namespace_authorization_rule.connect.primary_key
  shared_access_policy_name = azurerm_eventhub_namespace_authorization_rule.connect.name

  serialization {
    type     = "Json"
    encoding = "UTF8"
  }
}

resource "azurerm_stream_analytics_stream_input_eventhub" "minio" {
  name                     = "minio-input"
  stream_analytics_job_name = azurerm_stream_analytics_job.kappa.name
  resource_group_name      = azurerm_resource_group.fase1.name
  eventhub_consumer_group_name = "$Default"
  eventhub_name            = azurerm_eventhub.minio.name
  servicebus_namespace     = azurerm_eventhub_namespace.fase1.name
  shared_access_policy_key  = azurerm_eventhub_namespace_authorization_rule.connect.primary_key
  shared_access_policy_name = azurerm_eventhub_namespace_authorization_rule.connect.name

  serialization {
    type     = "Json"
    encoding = "UTF8"
  }
}

# Reference data input -- join contra o snapshot particionado por data do
# MongoDB no ADLS (Decisao 6 do DESIGN). Path pattern com tokens {date}/{time}
# -- o ASA atualiza automaticamente para a versao mais recente disponivel.
resource "azurerm_stream_analytics_reference_input_blob" "mongodb_perfil_restaurante" {
  name                      = "mongodb-perfil-restaurante-refdata"
  stream_analytics_job_name = azurerm_stream_analytics_job.kappa.name
  resource_group_name       = azurerm_resource_group.fase1.name
  storage_account_name      = azurerm_storage_account.fase1.name
  storage_account_key       = azurerm_storage_account.fase1.primary_access_key
  storage_container_name    = azurerm_storage_data_lake_gen2_filesystem.bronze.name
  path_pattern              = "mongodb/perfil_restaurante/{date}/perfil_restaurante.json"
  date_format               = "yyyy/MM/dd"

  serialization {
    type     = "Json"
    encoding = "UTF8"
  }
}

# Output placeholder -- destino final do stream enriquecido ainda a decidir
# (mesma pendencia que a AWS/GCP carregaram ate o proprio Build, ver
# BUILD_REPORT_INGESTAO_AWS_FASE2.md). Escreve no ADLS por enquanto, so para
# o job ser valido; reavaliar destino real (novo Event Hub, Lakebase, etc).
resource "azurerm_stream_analytics_output_blob" "enriched_placeholder" {
  name                      = "enriched-output-placeholder"
  stream_analytics_job_name = azurerm_stream_analytics_job.kappa.name
  resource_group_name       = azurerm_resource_group.fase1.name
  storage_account_name      = azurerm_storage_account.fase1.name
  storage_account_key       = azurerm_storage_account.fase1.primary_access_key
  storage_container_name    = azurerm_storage_data_lake_gen2_filesystem.bronze.name
  path_pattern              = "kappa-enriched/{date}/{time}"
  date_format                = "yyyy/MM/dd"
  time_format                = "HH"

  serialization {
    type     = "Json"
    encoding = "UTF8"
    format   = "LineSeparated"
  }
}
