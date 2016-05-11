# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CloudServiceConfiguration(Model):
    """
    The configuration for nodes in a pool based on the Azure Cloud Services
    platform.

    :param os_family: The Azure Guest OS family to be installed on the
     virtual machines in the pool.
    :type os_family: str
    :param target_os_version: The Azure Guest OS version to be installed on
     the virtual machines in the pool. The default value is * which specifies
     the latest operating system version for the specified OS family.
    :type target_os_version: str
    :param current_os_version: The Azure Guest OS Version currently installed
     on the virtual machines in the pool. This may differ from
     TargetOSVersion if the pool state is Upgrading.
    :type current_os_version: str
    """ 

    _validation = {
        'os_family': {'required': True},
    }

    _attribute_map = {
        'os_family': {'key': 'osFamily', 'type': 'str'},
        'target_os_version': {'key': 'targetOSVersion', 'type': 'str'},
        'current_os_version': {'key': 'currentOSVersion', 'type': 'str'},
    }

    def __init__(self, os_family, target_os_version=None, current_os_version=None):
        self.os_family = os_family
        self.target_os_version = target_os_version
        self.current_os_version = current_os_version
