# Synapse Dedicated SQL Pool (nao Serverless -- suporta DML/MERGE/SCD2, ver
# roadmap v1.4). Le do ADLS Gen2/Bronze via COPY INTO (sql/azure/synapse_copy_merge.sql).
resource "azurerm_synapse_workspace" "fase1" {
  name                                 = "ubereats-fase1-synapse"
  resource_group_name                 = azurerm_resource_group.fase1.name
  location                            = azurerm_resource_group.fase1.location
  storage_data_lake_gen2_filesystem_id = azurerm_storage_data_lake_gen2_filesystem.bronze.id
  sql_administrator_login             = "ubereatssqladmin"
  sql_administrator_login_password    = random_password.synapse_admin.result

  identity {
    type = "SystemAssigned"
  }
}

resource "random_password" "synapse_admin" {
  length  = 24
  special = true
}

resource "azurerm_synapse_sql_pool" "fase1" {
  name                 = "ubereatswarehouse"
  synapse_workspace_id = azurerm_synapse_workspace.fase1.id
  sku_name             = "DW100c" # menor SKU Dedicated -- ajustar no build real conforme volume (Open Question do DEFINE)
  create_mode          = "Default"
}

resource "azurerm_role_assignment" "synapse_storage_access" {
  scope                = azurerm_storage_account.fase1.id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = azurerm_synapse_workspace.fase1.identity[0].principal_id
}
