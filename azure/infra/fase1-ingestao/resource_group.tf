resource "azurerm_resource_group" "fase1" {
  name     = "rg-ubereats-fase1-ingestao"
  location = var.azure_location

  tags = {
    projeto = "uber-eats-case"
    fase    = "fase1-azure"
  }
}
