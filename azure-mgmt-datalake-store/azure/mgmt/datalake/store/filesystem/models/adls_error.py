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
from msrest.exceptions import HttpOperationError


class AdlsError(Model):
    """
    Data Lake Store filesystem error containing a specific WebHDFS exception.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar remote_exception: Gets the object representing the actual WebHDFS
     exception being returned.
    :vartype remote_exception: :class:`AdlsRemoteException
     <azure.mgmt.datalake.store.filesystem.models.AdlsRemoteException>`
    """ 

    _validation = {
        'remote_exception': {'readonly': True},
    }

    _attribute_map = {
        'remote_exception': {'key': 'RemoteException', 'type': 'AdlsRemoteException'},
    }

    def __init__(self):
        self.remote_exception = None


class AdlsErrorException(HttpOperationError):
    """Server responsed with exception of type: 'AdlsError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(AdlsErrorException, self).__init__(deserialize, response, 'AdlsError', *args)
