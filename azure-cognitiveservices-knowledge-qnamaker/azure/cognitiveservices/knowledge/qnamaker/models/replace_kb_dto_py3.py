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


class ReplaceKbDTO(Model):
    """Post body schema for Replace KB operation.

    All required parameters must be populated in order to send to Azure.

    :param qn_alist: Required. List of Q-A (QnADTO) to be added to the
     knowledgebase. Q-A Ids are assigned by the service and should be omitted.
    :type qn_alist:
     list[~azure.cognitiveservices.knowledge.qnamaker.models.QnADTO]
    """

    _validation = {
        'qn_alist': {'required': True},
    }

    _attribute_map = {
        'qn_alist': {'key': 'qnAList', 'type': '[QnADTO]'},
    }

    def __init__(self, *, qn_alist, **kwargs) -> None:
        super(ReplaceKbDTO, self).__init__(**kwargs)
        self.qn_alist = qn_alist
