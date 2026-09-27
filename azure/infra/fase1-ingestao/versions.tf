terraform {
  required_version = ">= 1.5.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.100"
    }
    azuread = {
      source  = "hashicorp/azuread"
      version = "~> 2.53"
    }
    databricks = {
      source  = "databricks/databricks"
      version = "~> 1.50"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.6"
    }
  }
}

provider "azurerm" {
  features {}
}

# Databricks Free Edition: workspace fora da subscription Azure (ver DESIGN, Decisao 4).
# host/token apontam para o workspace ja existente, nao provisionado por este Terraform.
provider "databricks" {
  host  = var.databricks_workspace_host
  token = var.databricks_pat_token
}
