from __future__ import unicode_literals
from mmj import client, error
from mmj.resource import MMJFacilityResource
from mmj.resource.base import (
    Facility
)
from mmj.util import (
    cached_property,
)

import time

class Item(MMJFacilityResource):

    @classmethod
    def list_url(cls, facility_id):
        return super(Item, cls).list_url(facility_id) + 'items/'

    @classmethod
    def get_url(cls, facility_id, id):
        return super(Item, cls).list_url(facility_id) + 'items/' + id + '/'

    def refresh_from(self, **kwargs):
        self.Id = kwargs['Id']
        self.Name = kwargs['Name']
        self.ProductCategoryName = kwargs['ProductCategoryName']
        self.ProductCategoryType = kwargs['ProductCategoryType']
        self.QuantityType = kwargs['QuantityType']
        self.DefaultLabTestingState = kwargs['DefaultLabTestingState']
        self.UnitOfMeasureName = kwargs['UnitOfMeasureName']
        self.ApprovalStatus = kwargs['ApprovalStatus']
        self.StrainId = kwargs['StrainId']
        self.StrainName = kwargs['StrainName']
        self.AdministrationMethod = kwargs['AdministrationMethod']
        self.UnitCbdPercent = kwargs['UnitCbdPercent']
        self.UnitCbdContent = kwargs['UnitCbdContent']
        self.UnitCbdContentUnitOfMeasureName = kwargs['UnitCbdContentUnitOfMeasureName']
        self.UnitThcPercent = kwargs['UnitThcPercent']
        self.UnitThcContent = kwargs['UnitThcContent']
        self.UnitThcContentUnitOfMeasureName = kwargs['UnitThcContentUnitOfMeasureName']
        self.UnitVolume = kwargs['UnitVolume']
        self.UnitVolumeUnitOfMeasureName = kwargs['UnitVolumeUnitOfMeasureName']
        self.UnitWeight = kwargs['UnitWeight']
        self.UnitWeightUnitOfMeasureName = kwargs['UnitWeightUnitOfMeasureName']
        self.ServingSize = kwargs['ServingSize']
        self.SupplyDurationDays = kwargs['SupplyDurationDays']
        self.UnitQuantity = kwargs['UnitQuantity']
        self.UnitQuantityUnitOfMeasureName = kwargs['UnitQuantityUnitOfMeasureName']
        self.Ingredients = kwargs['Ingredients']
        self.IsUsed = kwargs['IsUsed']

    def to_any_object(self):
        return {
            "Id": self.Id,
            "Name": self.Name,
            "ProductCategoryName": self.ProductCategoryName,
            "ProductCategoryType": self.ProductCategoryType,
            "QuantityType": self.QuantityType,
            "DefaultLabTestingState": self.DefaultLabTestingState,
            "UnitOfMeasureName": self.UnitOfMeasureName,
            "ApprovalStatus": self.ApprovalStatus,
            "StrainId": self.StrainId,
            "StrainName": self.StrainName,
            "AdministrationMethod": self.AdministrationMethod,
            "UnitCbdPercent": self.UnitCbdPercent,
            "UnitCbdContent": self.UnitCbdContent,
            "UnitCbdContentUnitOfMeasureName": self.UnitCbdContentUnitOfMeasureName,
            "UnitThcPercent": self.UnitThcPercent,
            "UnitThcContent": self.UnitThcContent,
            "UnitThcContentUnitOfMeasureName": self.UnitThcContentUnitOfMeasureName,
            "UnitVolume": self.UnitVolume,
            "UnitVolumeUnitOfMeasureName": self.UnitVolumeUnitOfMeasureName,
            "UnitWeight": self.UnitWeight,
            "UnitWeightUnitOfMeasureName": self.UnitWeightUnitOfMeasureName,
            "ServingSize": self.ServingSize,
            "SupplyDurationDays": self.SupplyDurationDays,
            "UnitQuantity": self.UnitQuantity,
            "UnitQuantityUnitOfMeasureName": self.UnitQuantityUnitOfMeasureName,
            "Ingredients": self.Ingredients,
            "IsUsed": self.IsUsed,
        }
