output "storage_account_name" {
  value = azurerm_storage_account.fase1.name
}

output "eventhub_namespace_fqdn" {
  value = "${azurerm_eventhub_namespace.fase1.name}.servicebus.windows.net"
}

output "synapse_workspace_name" {
  value = azurerm_synapse_workspace.fase1.name
}

output "service_principal_client_id" {
  value = azuread_application.fase1.client_id
}

output "unity_catalog_external_location" {
  value = databricks_external_location.bronze.url
}
