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


class SharedAccessSignatureAuthorizationRule(Model):
    """The properties that describe the keys to access the IotHub artifacts.

    :param key_name: The name of the key.
    :type key_name: str
    :param primary_key: The primary key.
    :type primary_key: str
    :param secondary_key: The secondary key.
    :type secondary_key: str
    :param rights: The access rights. Possible values include:
     'RegistryRead', 'RegistryWrite', 'ServiceConnect', 'DeviceConnect',
     'RegistryRead, RegistryWrite', 'RegistryRead, ServiceConnect',
     'RegistryRead, DeviceConnect', 'RegistryWrite, ServiceConnect',
     'RegistryWrite, DeviceConnect', 'ServiceConnect, DeviceConnect',
     'RegistryRead, RegistryWrite, ServiceConnect', 'RegistryRead,
     RegistryWrite, DeviceConnect', 'RegistryRead, ServiceConnect,
     DeviceConnect', 'RegistryWrite, ServiceConnect, DeviceConnect',
     'RegistryRead, RegistryWrite, ServiceConnect, DeviceConnect'
    :type rights: str or :class:`AccessRights
     <azure.mgmt.iothub.models.AccessRights>`
    """ 

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'str'},
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
        'rights': {'key': 'rights', 'type': 'AccessRights'},
    }

    def __init__(self, key_name=None, primary_key=None, secondary_key=None, rights=None):
        self.key_name = key_name
        self.primary_key = primary_key
        self.secondary_key = secondary_key
        self.rights = rights
