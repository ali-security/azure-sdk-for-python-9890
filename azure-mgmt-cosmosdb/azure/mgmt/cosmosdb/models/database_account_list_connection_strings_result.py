# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DatabaseAccountListConnectionStringsResult(Model):
    """The connection strings for the given database account.

    :param connection_strings: An array that contains the connection strings
     for the Cosmos DB account.
    :type connection_strings:
     list[~azure.mgmt.cosmosdb.models.DatabaseAccountConnectionString]
    """

    _attribute_map = {
        'connection_strings': {'key': 'connectionStrings', 'type': '[DatabaseAccountConnectionString]'},
    }

    def __init__(self, connection_strings=None):
        super(DatabaseAccountListConnectionStringsResult, self).__init__()
        self.connection_strings = connection_strings
