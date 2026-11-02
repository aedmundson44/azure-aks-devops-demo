# Create a resource group
resource "azurerm_resource_group" "rg-tfstate" {
  name     = "rg-tfstate"
  location = "eastus"
}
