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

from .sub_resource import SubResource


class ApplicationGatewayPathRule(SubResource):
    """Path rule of URL path map of application gateway.

    :param id: Resource Id
    :type id: str
    :param paths: Gets or sets the path rules of URL path map
    :type paths: list of str
    :param backend_address_pool: Gets or sets backend address pool resource
     of URL path map
    :type backend_address_pool: :class:`SubResource
     <azure.mgmt.network.models.SubResource>`
    :param backend_http_settings: Gets or sets backend http settings resource
     of URL path map
    :type backend_http_settings: :class:`SubResource
     <azure.mgmt.network.models.SubResource>`
    :param provisioning_state: Gets or sets path rule of URL path map
     resource Updating/Deleting/Failed
    :type provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated
    :type etag: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'paths': {'key': 'properties.paths', 'type': '[str]'},
        'backend_address_pool': {'key': 'properties.backendAddressPool', 'type': 'SubResource'},
        'backend_http_settings': {'key': 'properties.backendHttpSettings', 'type': 'SubResource'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, paths=None, backend_address_pool=None, backend_http_settings=None, provisioning_state=None, name=None, etag=None):
        super(ApplicationGatewayPathRule, self).__init__(id=id)
        self.paths = paths
        self.backend_address_pool = backend_address_pool
        self.backend_http_settings = backend_http_settings
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
