# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ActionGroupList
    from ._models_py3 import ActionGroupPatchBody
    from ._models_py3 import ActionGroupResource
    from ._models_py3 import AutomationRunbookReceiver
    from ._models_py3 import AzureAppPushReceiver
    from ._models_py3 import AzureFunctionReceiver
    from ._models_py3 import DynamicMetricCriteria
    from ._models_py3 import DynamicThresholdFailingPeriods
    from ._models_py3 import EmailReceiver
    from ._models_py3 import EnableRequest
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ItsmReceiver
    from ._models_py3 import LogicAppReceiver
    from ._models_py3 import MetricAlertAction
    from ._models_py3 import MetricAlertCriteria
    from ._models_py3 import MetricAlertMultipleResourceMultipleMetricCriteria
    from ._models_py3 import MetricAlertResource
    from ._models_py3 import MetricAlertResourceCollection
    from ._models_py3 import MetricAlertResourcePatch
    from ._models_py3 import MetricAlertSingleResourceMultipleMetricCriteria
    from ._models_py3 import MetricAlertStatus
    from ._models_py3 import MetricAlertStatusCollection
    from ._models_py3 import MetricAlertStatusProperties
    from ._models_py3 import MetricCriteria
    from ._models_py3 import MetricDimension
    from ._models_py3 import MultiMetricCriteria
    from ._models_py3 import Resource
    from ._models_py3 import SmsReceiver
    from ._models_py3 import VoiceReceiver
    from ._models_py3 import WebhookReceiver
    from ._models_py3 import WebtestLocationAvailabilityCriteria
except (SyntaxError, ImportError):
    from ._models import ActionGroupList  # type: ignore
    from ._models import ActionGroupPatchBody  # type: ignore
    from ._models import ActionGroupResource  # type: ignore
    from ._models import AutomationRunbookReceiver  # type: ignore
    from ._models import AzureAppPushReceiver  # type: ignore
    from ._models import AzureFunctionReceiver  # type: ignore
    from ._models import DynamicMetricCriteria  # type: ignore
    from ._models import DynamicThresholdFailingPeriods  # type: ignore
    from ._models import EmailReceiver  # type: ignore
    from ._models import EnableRequest  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ItsmReceiver  # type: ignore
    from ._models import LogicAppReceiver  # type: ignore
    from ._models import MetricAlertAction  # type: ignore
    from ._models import MetricAlertCriteria  # type: ignore
    from ._models import MetricAlertMultipleResourceMultipleMetricCriteria  # type: ignore
    from ._models import MetricAlertResource  # type: ignore
    from ._models import MetricAlertResourceCollection  # type: ignore
    from ._models import MetricAlertResourcePatch  # type: ignore
    from ._models import MetricAlertSingleResourceMultipleMetricCriteria  # type: ignore
    from ._models import MetricAlertStatus  # type: ignore
    from ._models import MetricAlertStatusCollection  # type: ignore
    from ._models import MetricAlertStatusProperties  # type: ignore
    from ._models import MetricCriteria  # type: ignore
    from ._models import MetricDimension  # type: ignore
    from ._models import MultiMetricCriteria  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import SmsReceiver  # type: ignore
    from ._models import VoiceReceiver  # type: ignore
    from ._models import WebhookReceiver  # type: ignore
    from ._models import WebtestLocationAvailabilityCriteria  # type: ignore

from ._monitor_client_enums import (
    AggregationType,
    CriterionType,
    DynamicThresholdOperator,
    DynamicThresholdSensitivity,
    Odatatype,
    Operator,
    ReceiverStatus,
)

__all__ = [
    'ActionGroupList',
    'ActionGroupPatchBody',
    'ActionGroupResource',
    'AutomationRunbookReceiver',
    'AzureAppPushReceiver',
    'AzureFunctionReceiver',
    'DynamicMetricCriteria',
    'DynamicThresholdFailingPeriods',
    'EmailReceiver',
    'EnableRequest',
    'ErrorResponse',
    'ItsmReceiver',
    'LogicAppReceiver',
    'MetricAlertAction',
    'MetricAlertCriteria',
    'MetricAlertMultipleResourceMultipleMetricCriteria',
    'MetricAlertResource',
    'MetricAlertResourceCollection',
    'MetricAlertResourcePatch',
    'MetricAlertSingleResourceMultipleMetricCriteria',
    'MetricAlertStatus',
    'MetricAlertStatusCollection',
    'MetricAlertStatusProperties',
    'MetricCriteria',
    'MetricDimension',
    'MultiMetricCriteria',
    'Resource',
    'SmsReceiver',
    'VoiceReceiver',
    'WebhookReceiver',
    'WebtestLocationAvailabilityCriteria',
    'AggregationType',
    'CriterionType',
    'DynamicThresholdOperator',
    'DynamicThresholdSensitivity',
    'Odatatype',
    'Operator',
    'ReceiverStatus',
]
