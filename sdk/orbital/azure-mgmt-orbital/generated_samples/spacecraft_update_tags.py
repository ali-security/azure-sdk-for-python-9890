# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.orbital import AzureOrbital

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-orbital
# USAGE
    python spacecraft_update_tags.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AzureOrbital(
        credential=DefaultAzureCredential(),
        subscription_id="c1be1141-a7c9-4aac-9608-3c2e2f1152c3",
    )

    response = client.spacecrafts.begin_update_tags(
        resource_group_name="contoso-Rgp",
        spacecraft_name="CONTOSO_SAT",
        parameters={"tags": {"tag1": "value1", "tag2": "value2"}},
    ).result()
    print(response)


# x-ms-original-file: specification/orbital/resource-manager/Microsoft.Orbital/stable/2022-11-01/examples/SpacecraftUpdateTags.json
if __name__ == "__main__":
    main()
