# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.sql.aio import SqlManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSqlManagementManagedDatabaseSecurityAlertPoliciesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(SqlManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.managed_database_security_alert_policies.get(
            resource_group_name=resource_group.name,
            managed_instance_name="str",
            database_name="str",
            security_alert_policy_name="str",
            api_version="2020-11-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_create_or_update(self, resource_group):
        response = await self.client.managed_database_security_alert_policies.create_or_update(
            resource_group_name=resource_group.name,
            managed_instance_name="str",
            database_name="str",
            security_alert_policy_name="str",
            parameters={
                "creationTime": "2020-02-20 00:00:00",
                "disabledAlerts": ["str"],
                "emailAccountAdmins": bool,
                "emailAddresses": ["str"],
                "id": "str",
                "name": "str",
                "retentionDays": 0,
                "state": "str",
                "storageAccountAccessKey": "str",
                "storageEndpoint": "str",
                "type": "str",
            },
            api_version="2020-11-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_database(self, resource_group):
        response = self.client.managed_database_security_alert_policies.list_by_database(
            resource_group_name=resource_group.name,
            managed_instance_name="str",
            database_name="str",
            api_version="2020-11-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
