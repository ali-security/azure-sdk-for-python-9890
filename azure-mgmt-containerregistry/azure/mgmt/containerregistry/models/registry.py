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

from .resource import Resource


class Registry(Resource):
    """An object that represents a container registry.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: The location of the resource. This cannot be changed
     after the resource is created.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict
    :ivar login_server: The URL that can be used to log into the container
     registry.
    :vartype login_server: str
    :ivar creation_date: The creation date of the container registry in
     ISO8601 format.
    :vartype creation_date: datetime
    :param admin_user_enabled: The value that indicates whether the admin user
     is enabled. This value is false by default. Default value: False .
    :type admin_user_enabled: bool
    :param storage_account: The properties of the storage account for the
     container registry. If specified, the storage account must be in the same
     physical location as the container registry.
    :type storage_account: :class:`StorageAccountProperties
     <azure.mgmt.containerregistry.models.StorageAccountProperties>`
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'login_server': {'readonly': True},
        'creation_date': {'readonly': True},
        'storage_account': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'login_server': {'key': 'properties.loginServer', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
        'admin_user_enabled': {'key': 'properties.adminUserEnabled', 'type': 'bool'},
        'storage_account': {'key': 'properties.storageAccount', 'type': 'StorageAccountProperties'},
    }

    def __init__(self, location, storage_account, tags=None, admin_user_enabled=False):
        super(Registry, self).__init__(location=location, tags=tags)
        self.login_server = None
        self.creation_date = None
        self.admin_user_enabled = admin_user_enabled
        self.storage_account = storage_account
