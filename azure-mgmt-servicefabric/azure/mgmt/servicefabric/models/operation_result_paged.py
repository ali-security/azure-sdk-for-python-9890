# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.2.2.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class OperationResultPaged(Paged):
    """
    A paging container for iterating over a list of :class:`OperationResult <azure.mgmt.servicefabric.models.OperationResult>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[OperationResult]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationResultPaged, self).__init__(*args, **kwargs)
