# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.eventhub.aio import EventHubManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestEventHubManagementDisasterRecoveryConfigsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(EventHubManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_authorization_rules(self, resource_group):
        response = self.client.disaster_recovery_configs.list_authorization_rules(
            resource_group_name=resource_group.name,
            namespace_name="str",
            alias="str",
            api_version="2017-04-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get_authorization_rule(self, resource_group):
        response = await self.client.disaster_recovery_configs.get_authorization_rule(
            resource_group_name=resource_group.name,
            namespace_name="str",
            alias="str",
            authorization_rule_name="str",
            api_version="2017-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_keys(self, resource_group):
        response = await self.client.disaster_recovery_configs.list_keys(
            resource_group_name=resource_group.name,
            namespace_name="str",
            alias="str",
            authorization_rule_name="str",
            api_version="2017-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_check_name_availability(self, resource_group):
        response = await self.client.disaster_recovery_configs.check_name_availability(
            resource_group_name=resource_group.name,
            namespace_name="str",
            parameters={"name": "str"},
            api_version="2017-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list(self, resource_group):
        response = self.client.disaster_recovery_configs.list(
            resource_group_name=resource_group.name,
            namespace_name="str",
            api_version="2017-04-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_create_or_update(self, resource_group):
        response = await self.client.disaster_recovery_configs.create_or_update(
            resource_group_name=resource_group.name,
            namespace_name="str",
            alias="str",
            parameters={
                "alternateName": "str",
                "id": "str",
                "name": "str",
                "partnerNamespace": "str",
                "pendingReplicationOperationsCount": 0,
                "provisioningState": "str",
                "role": "str",
                "type": "str",
            },
            api_version="2017-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_delete(self, resource_group):
        response = await self.client.disaster_recovery_configs.delete(
            resource_group_name=resource_group.name,
            namespace_name="str",
            alias="str",
            api_version="2017-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.disaster_recovery_configs.get(
            resource_group_name=resource_group.name,
            namespace_name="str",
            alias="str",
            api_version="2017-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_break_pairing(self, resource_group):
        response = await self.client.disaster_recovery_configs.break_pairing(
            resource_group_name=resource_group.name,
            namespace_name="str",
            alias="str",
            api_version="2017-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_fail_over(self, resource_group):
        response = await self.client.disaster_recovery_configs.fail_over(
            resource_group_name=resource_group.name,
            namespace_name="str",
            alias="str",
            api_version="2017-04-01",
        )

        # please add some check logic here by yourself
        # ...
