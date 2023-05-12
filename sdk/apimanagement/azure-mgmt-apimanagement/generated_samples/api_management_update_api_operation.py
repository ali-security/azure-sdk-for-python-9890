# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.apimanagement import ApiManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-apimanagement
# USAGE
    python api_management_update_api_operation.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ApiManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.api_operation.update(
        resource_group_name="rg1",
        service_name="apimService1",
        api_id="echo-api",
        operation_id="operationId",
        if_match="*",
        parameters={
            "properties": {
                "displayName": "Retrieve resource",
                "method": "GET",
                "request": {
                    "queryParameters": [
                        {
                            "defaultValue": "sample",
                            "description": 'A sample parameter that is required and has a default value of "sample".',
                            "name": "param1",
                            "required": True,
                            "type": "string",
                            "values": ["sample"],
                        }
                    ]
                },
                "responses": [
                    {"description": "Returned in all cases.", "headers": [], "representations": [], "statusCode": 200},
                    {"description": "Server Error.", "headers": [], "representations": [], "statusCode": 500},
                ],
                "templateParameters": [],
                "urlTemplate": "/resource",
            }
        },
    )
    print(response)


# x-ms-original-file: specification/apimanagement/resource-manager/Microsoft.ApiManagement/stable/2022-08-01/examples/ApiManagementUpdateApiOperation.json
if __name__ == "__main__":
    main()
