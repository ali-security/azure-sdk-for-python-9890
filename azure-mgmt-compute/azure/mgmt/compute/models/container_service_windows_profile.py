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


class ContainerServiceWindowsProfile(Model):
    """Profile for Windows VMs.

    :param admin_username: The administrator username to use for Windows VMs
    :type admin_username: str
    :param admin_password: The administrator password to use for Windows VMs
    :type admin_password: str
    """ 

    _validation = {
        'admin_username': {'required': True},
        'admin_password': {'required': True},
    }

    _attribute_map = {
        'admin_username': {'key': 'adminUsername', 'type': 'str'},
        'admin_password': {'key': 'adminPassword', 'type': 'str'},
    }

    def __init__(self, admin_username, admin_password):
        self.admin_username = admin_username
        self.admin_password = admin_password
