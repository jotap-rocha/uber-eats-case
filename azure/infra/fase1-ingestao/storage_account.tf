# ADLS Gen2 (Storage Account com hierarchical namespace habilitado).
# Container unico "bronze", com prefixos por fonte/tabela (postgres/, oracle/,
# mongodb/, minio/) — mesmo landing unico ja usado no padrao das Fases 2/3
# (S3/Bronze na AWS, GCS/Bronze na GCP).
resource "azurerm_storage_account" "fase1" {
  name                     = "ubereatsfase1bronze"
  resource_group_name      = azurerm_resource_group.fase1.name
  location                 = azurerm_resource_group.fase1.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind             = "StorageV2"
  is_hns_enabled           = true # habilita ADLS Gen2 (hierarchical namespace)

  min_tls_version                = "TLS1_2"
  public_network_access_enabled  = true # Free Edition (fora da subscription) acessa via internet, ver Decisao 4
}

# azurerm_storage_data_lake_gen2_filesystem (nao azurerm_storage_container) --
# o Synapse workspace (synapse.tf) exige especificamente um ID neste formato
# para storage_data_lake_gen2_filesystem_id. Mesmo objeto fisico no Azure
# (HNS habilitado), so muda o resource type usado pelo provider.
resource "azurerm_storage_data_lake_gen2_filesystem" "bronze" {
  name               = "bronze"
  storage_account_id = azurerm_storage_account.fase1.id
}
