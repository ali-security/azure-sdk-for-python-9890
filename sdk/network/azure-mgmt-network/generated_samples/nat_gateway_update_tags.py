# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python nat_gateway_update_tags.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.nat_gateways.update_tags(
        resource_group_name="rg1",
        nat_gateway_name="test-natGateway",
        parameters={"tags": {"tag1": "value1", "tag2": "value2"}},
    )
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2024-01-01/examples/NatGatewayUpdateTags.json
if __name__ == "__main__":
    main()
