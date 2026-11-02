resource "azurerm_storage_account" "asartfstate2026" {
  name                     = "asartfstate2026"
  resource_group_name      = azurerm_resource_group.rg-tfstate.name
  location                 = azurerm_resource_group.rg-tfstate.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = {
    environment = "shared"
  }
}

resource "azurerm_storage_container" "tfstate" {
  name                  = "tfstate"
  storage_account_id    = azurerm_storage_account.asartfstate2026.id
  container_access_type = "private"
}
