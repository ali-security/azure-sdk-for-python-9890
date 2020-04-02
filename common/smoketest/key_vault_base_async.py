from key_vault_base import KeyVaultBase
from azure.identity.aio import DefaultAzureCredential

class KeyVaultBaseAsync(KeyVaultBase):
    credential_type = DefaultAzureCredential