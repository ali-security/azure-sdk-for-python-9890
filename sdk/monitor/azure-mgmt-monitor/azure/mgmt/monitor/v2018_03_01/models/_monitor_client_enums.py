# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class AggregationType(str, Enum):
    """the criteria time aggregation types.
    """

    average = "Average"
    count = "Count"
    minimum = "Minimum"
    maximum = "Maximum"
    total = "Total"

class CriterionType(str, Enum):
    """Specifies the type of threshold criteria
    """

    static_threshold_criterion = "StaticThresholdCriterion"
    dynamic_threshold_criterion = "DynamicThresholdCriterion"

class DynamicThresholdOperator(str, Enum):
    """The operator used to compare the metric value against the threshold.
    """

    greater_than = "GreaterThan"
    less_than = "LessThan"
    greater_or_less_than = "GreaterOrLessThan"

class DynamicThresholdSensitivity(str, Enum):
    """The extent of deviation required to trigger an alert. This will affect how tight the threshold
    is to the metric series pattern.
    """

    low = "Low"
    medium = "Medium"
    high = "High"

class Odatatype(str, Enum):
    """specifies the type of the alert criteria.
    """

    microsoft_azure_monitor_single_resource_multiple_metric_criteria = "Microsoft.Azure.Monitor.SingleResourceMultipleMetricCriteria"
    microsoft_azure_monitor_multiple_resource_multiple_metric_criteria = "Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria"
    microsoft_azure_monitor_webtest_location_availability_criteria = "Microsoft.Azure.Monitor.WebtestLocationAvailabilityCriteria"

class Operator(str, Enum):
    """the criteria operator.
    """

    equals = "Equals"
    not_equals = "NotEquals"
    greater_than = "GreaterThan"
    greater_than_or_equal = "GreaterThanOrEqual"
    less_than = "LessThan"
    less_than_or_equal = "LessThanOrEqual"

class ReceiverStatus(str, Enum):
    """Indicates the status of the receiver. Receivers that are not Enabled will not receive any
    communications.
    """

    not_specified = "NotSpecified"
    enabled = "Enabled"
    disabled = "Disabled"
