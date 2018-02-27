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


class MeterInfo(Model):
    """Detailed information about the meter.

    :param meter_id: The unique identifier of the resource.
    :type meter_id: str
    :param meter_name: The name of the meter, within the given meter category
    :type meter_name: str
    :param meter_category: The category of the meter, e.g., 'Cloud services',
     'Networking', etc..
    :type meter_category: str
    :param meter_sub_category: The subcategory of the meter, e.g., 'A6 Cloud
     services', 'ExpressRoute (IXP)', etc..
    :type meter_sub_category: str
    :param unit: The unit in which the meter consumption is charged, e.g.,
     'Hours', 'GB', etc.
    :type unit: str
    :param meter_tags: Provides additional meter data. 'Third Party' indicates
     a meter with no discount. Blanks indicate First Party.
    :type meter_tags: list[str]
    :param meter_region: The region in which the Azure service is available.
    :type meter_region: str
    :param meter_rates: The list of key/value pairs for the meter rates, in
     the format 'key':'value' where key = the meter quantity, and value = the
     corresponding price
    :type meter_rates: dict[str, float]
    :param effective_date: Indicates the date from which the meter rate is
     effective.
    :type effective_date: datetime
    :param included_quantity: The resource quantity that is included in the
     offer at no cost. Consumption beyond this quantity will be charged.
    :type included_quantity: float
    """

    _attribute_map = {
        'meter_id': {'key': 'MeterId', 'type': 'str'},
        'meter_name': {'key': 'MeterName', 'type': 'str'},
        'meter_category': {'key': 'MeterCategory', 'type': 'str'},
        'meter_sub_category': {'key': 'MeterSubCategory', 'type': 'str'},
        'unit': {'key': 'Unit', 'type': 'str'},
        'meter_tags': {'key': 'MeterTags', 'type': '[str]'},
        'meter_region': {'key': 'MeterRegion', 'type': 'str'},
        'meter_rates': {'key': 'MeterRates', 'type': '{float}'},
        'effective_date': {'key': 'EffectiveDate', 'type': 'iso-8601'},
        'included_quantity': {'key': 'IncludedQuantity', 'type': 'float'},
    }

    def __init__(self, meter_id=None, meter_name=None, meter_category=None, meter_sub_category=None, unit=None, meter_tags=None, meter_region=None, meter_rates=None, effective_date=None, included_quantity=None):
        super(MeterInfo, self).__init__()
        self.meter_id = meter_id
        self.meter_name = meter_name
        self.meter_category = meter_category
        self.meter_sub_category = meter_sub_category
        self.unit = unit
        self.meter_tags = meter_tags
        self.meter_region = meter_region
        self.meter_rates = meter_rates
        self.effective_date = effective_date
        self.included_quantity = included_quantity
