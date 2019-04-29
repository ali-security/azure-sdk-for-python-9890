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


class P2SVpnGateway(Resource):
    """P2SVpnGateway Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param virtual_hub: The VirtualHub to which the gateway belongs
    :type virtual_hub: ~azure.mgmt.network.v2019_02_01.models.SubResource
    :param provisioning_state: The provisioning state of the resource.
     Possible values include: 'Succeeded', 'Updating', 'Deleting', 'Failed'
    :type provisioning_state: str or
     ~azure.mgmt.network.v2019_02_01.models.ProvisioningState
    :param vpn_gateway_scale_unit: The scale unit for this p2s vpn gateway.
    :type vpn_gateway_scale_unit: int
    :param p2_svpn_server_configuration: The P2SVpnServerConfiguration to
     which the p2sVpnGateway is attached to.
    :type p2_svpn_server_configuration:
     ~azure.mgmt.network.v2019_02_01.models.SubResource
    :param vpn_client_address_pool: The reference of the address space
     resource which represents Address space for P2S VpnClient.
    :type vpn_client_address_pool:
     ~azure.mgmt.network.v2019_02_01.models.AddressSpace
    :param custom_routes: The reference of the address space resource which
     represents the custom routes specified by the customer for P2SVpnGateway
     and P2S VpnClient.
    :type custom_routes: ~azure.mgmt.network.v2019_02_01.models.AddressSpace
    :ivar vpn_client_connection_health: All P2S VPN clients' connection health
     status.
    :vartype vpn_client_connection_health:
     ~azure.mgmt.network.v2019_02_01.models.VpnClientConnectionHealth
    :ivar etag: Gets a unique read-only string that changes whenever the
     resource is updated.
    :vartype etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'vpn_client_connection_health': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'virtual_hub': {'key': 'properties.virtualHub', 'type': 'SubResource'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'vpn_gateway_scale_unit': {'key': 'properties.vpnGatewayScaleUnit', 'type': 'int'},
        'p2_svpn_server_configuration': {'key': 'properties.p2SVpnServerConfiguration', 'type': 'SubResource'},
        'vpn_client_address_pool': {'key': 'properties.vpnClientAddressPool', 'type': 'AddressSpace'},
        'custom_routes': {'key': 'properties.customRoutes', 'type': 'AddressSpace'},
        'vpn_client_connection_health': {'key': 'properties.vpnClientConnectionHealth', 'type': 'VpnClientConnectionHealth'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(P2SVpnGateway, self).__init__(**kwargs)
        self.virtual_hub = kwargs.get('virtual_hub', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.vpn_gateway_scale_unit = kwargs.get('vpn_gateway_scale_unit', None)
        self.p2_svpn_server_configuration = kwargs.get('p2_svpn_server_configuration', None)
        self.vpn_client_address_pool = kwargs.get('vpn_client_address_pool', None)
        self.custom_routes = kwargs.get('custom_routes', None)
        self.vpn_client_connection_health = None
        self.etag = None
