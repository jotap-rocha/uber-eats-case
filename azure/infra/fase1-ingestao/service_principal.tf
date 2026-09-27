# Service Principal usado pela storage credential do Unity Catalog (DESIGN,
# Decisao 4) e pelo Kafka Connect Sink Connector (autenticacao OAuth contra
# o ADLS Gen2, ver debezium/adls-sink-connector.json.template).
resource "azuread_application" "fase1" {
  display_name = "ubereats-fase1-adls-bronze"
}

resource "azuread_application_password" "fase1" {
  application_id = azuread_application.fase1.id
  display_name   = "adls-bronze-access"
  end_date_relative = "17520h" # 24 meses -- rotacionar manualmente antes disso (ver DESIGN, Decisao 4, Consequencias)
}

resource "azuread_service_principal" "fase1" {
  client_id = azuread_application.fase1.client_id
}

resource "azurerm_role_assignment" "fase1_sp_storage" {
  # Escopo no Storage Account (nao no filesystem) -- azurerm_storage_data_lake_gen2_filesystem
  # nao expoe um resource_manager_id proprio; "Storage Blob Data Contributor"
  # no account inteiro e suficiente para este projeto de portfolio.
  scope                = azurerm_storage_account.fase1.id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = azuread_service_principal.fase1.object_id
}
