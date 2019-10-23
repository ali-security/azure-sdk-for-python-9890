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

from .update_resource import UpdateResource


class MachineUpdate(UpdateResource):
    """Describes a hybrid machine Update.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param tags: Resource tags
    :type tags: dict[str, str]
    :param type: The identity type.
    :type type: str
    :ivar principal_id: The identity's principal id.
    :vartype principal_id: str
    :ivar tenant_id: The identity's tenant id.
    :vartype tenant_id: str
    :param physical_location: Resource's Physical Location
    :type physical_location: str
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'type': {'key': 'identity.type', 'type': 'str'},
        'principal_id': {'key': 'identity.principalId', 'type': 'str'},
        'tenant_id': {'key': 'identity.tenantId', 'type': 'str'},
        'physical_location': {'key': 'properties.physicalLocation', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MachineUpdate, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.principal_id = None
        self.tenant_id = None
        self.physical_location = kwargs.get('physical_location', None)
