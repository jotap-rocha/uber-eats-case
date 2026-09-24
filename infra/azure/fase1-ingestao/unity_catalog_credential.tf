# Storage credential + external location do Unity Catalog, via Service
# Principal (DESIGN, Decisao 4 -- Access Connector for Databricks nao se
# aplica: workspace Free Edition fica fora da subscription Azure).
resource "databricks_storage_credential" "adls_bronze" {
  name = "adls-bronze-fase1-credential"

  azure_service_principal {
    directory_id   = var.azure_tenant_id
    application_id = azuread_application.fase1.client_id
    client_secret  = azuread_application_password.fase1.value
  }

  comment = "Fase 1/Azure -- ingestao consolidada (DESIGN_INGESTAO_AZURE_FASE1.md)"
}

resource "databricks_external_location" "bronze" {
  name            = "adls-bronze-fase1"
  url             = "abfss://bronze@${azurerm_storage_account.fase1.name}.dfs.core.windows.net/"
  credential_name = databricks_storage_credential.adls_bronze.name
  comment         = "Landing unico consolidado: postgres/, oracle/, mongodb/, minio/ -- ver Decisao 1/3 do DESIGN"
}

resource "databricks_grants" "bronze_external_location" {
  external_location = databricks_external_location.bronze.id

  grant {
    principal  = "account users"
    privileges = ["READ_FILES"]
  }
}
