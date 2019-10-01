from __future__ import unicode_literals
from mmj import client, error, env
from mmj.resource import MMJFacilityResource
from mmj.resource.base import (
    Facility
)
from mmj.util import (
    cached_property,
)

import time

class Package(MMJFacilityResource):

    @classmethod
    def list_url(cls, facility_id):
        return super(Package, cls).list_url(facility_id) + 'packages/'

    @classmethod
    def get_url(cls, facility_id, id):
        return super(Package, cls).list_url(facility_id) + 'packages/' + id + '/'

    def refresh_from(self, **kwargs):
        self.Id = kwargs['Id']
        self.Label = kwargs['Label']
        self.PackageType = kwargs['PackageType']
        self.SourceHarvestNames = kwargs['SourceHarvestNames']
        self.RoomId = kwargs['RoomId']
        self.RoomName = kwargs['RoomName']
        self.Quantity = kwargs['Quantity']
        self.UnitOfMeasureName = kwargs['UnitOfMeasureName']
        self.UnitOfMeasureAbbreviation = kwargs['UnitOfMeasureAbbreviation']
        self.PatientLicenseNumber = kwargs['PatientLicenseNumber']
        self.ProductId = kwargs['ProductId']
        self.ProductName = kwargs['ProductName']
        self.ProductCategoryName = kwargs['ProductCategoryName']
        self.ItemStrainName = kwargs['ItemStrainName']
        self.ItemUnitCbdPercent = kwargs['ItemUnitCbdPercent']
        self.ItemUnitCbdContent = kwargs['ItemUnitCbdContent']
        self.ItemUnitCbdContentUnitOfMeasureName = kwargs['ItemUnitCbdContentUnitOfMeasureName']
        self.ItemUnitThcPercent = kwargs['ItemUnitThcPercent']
        self.ItemUnitThcContent = kwargs['ItemUnitThcContent']
        self.ItemUnitThcContentUnitOfMeasureName = kwargs['ItemUnitThcContentUnitOfMeasureName']
        self.ItemUnitVolume = kwargs['ItemUnitVolume']
        self.ItemUnitVolumeUnitOfMeasureName = kwargs['ItemUnitVolumeUnitOfMeasureName']
        self.ItemUnitWeight = kwargs['ItemUnitWeight']
        self.ItemUnitWeightUnitOfMeasureName = kwargs['ItemUnitWeightUnitOfMeasureName']
        self.ItemServingSize = kwargs['ItemServingSize']
        self.ItemSupplyDurationDays = kwargs['ItemSupplyDurationDays']
        self.ItemUnitQuantity = kwargs['ItemUnitQuantity']
        self.ItemUnitQuantityUnitOfMeasureName = kwargs['ItemUnitQuantityUnitOfMeasureName']
        self.Note = kwargs['Note']
        self.PackagedDate = kwargs['PackagedDate']
        self.InitialLabTestingState = kwargs['InitialLabTestingState']
        self.LabTestingState = kwargs['LabTestingState']
        self.LabTestingStateDate = kwargs['LabTestingStateDate']
        self.IsProductionBatch = kwargs['IsProductionBatch']
        self.ProductionBatchNumber = kwargs['ProductionBatchNumber']
        self.IsTradeSample = kwargs['IsTradeSample']
        self.IsTestingSample = kwargs['IsTestingSample']
        self.IsProcessValidationTestingSample = kwargs['IsProcessValidationTestingSample']
        self.ProductRequiresRemediation = kwargs['ProductRequiresRemediation']
        self.ContainsRemediatedProduct = kwargs['ContainsRemediatedProduct']
        self.RemediationDate = kwargs['RemediationDate']
        self.ReceivedFromManifestNumber = kwargs['ReceivedFromManifestNumber']
        self.ReceivedFromFacilityLicenseNumber = kwargs['ReceivedFromFacilityLicenseNumber']
        self.ReceivedFromFacilityName = kwargs['ReceivedFromFacilityName']
        self.ReceivedDateTime = kwargs['ReceivedDateTime']
        self.IsOnHold = kwargs['IsOnHold']
        self.ArchivedDate = kwargs['ArchivedDate']
        self.FinishedDate = kwargs['FinishedDate']
        self.LastModified = kwargs['LastModified']

    def to_any_object(self):
        return {
            "Id": self.Id,
            "Label": self.Label,
            "PackageType": self.PackageType,
            "SourceHarvestNames": self.SourceHarvestNames,
            "RoomId": self.RoomId,
            "RoomName": self.RoomName,
            "Quantity": self.Quantity,
            "UnitOfMeasureName": self.UnitOfMeasureName,
            "UnitOfMeasureAbbreviation": self.UnitOfMeasureAbbreviation,
            "PatientLicenseNumber": self.PatientLicenseNumber,
            "ProductId": self.ProductId,
            "ProductName": self.ProductName,
            "ProductCategoryName": self.ProductCategoryName,
            "ItemStrainName": self.ItemStrainName,
            "ItemUnitCbdPercent": self.ItemUnitCbdPercent,
            "ItemUnitCbdContent": self.ItemUnitCbdContent,
            "ItemUnitCbdContentUnitOfMeasureName": self.ItemUnitCbdContentUnitOfMeasureName,
            "ItemUnitThcPercent": self.ItemUnitThcPercent,
            "ItemUnitThcContent": self.ItemUnitThcContent,
            "ItemUnitThcContentUnitOfMeasureName": self.ItemUnitThcContentUnitOfMeasureName,
            "ItemUnitVolume": self.ItemUnitVolume,
            "ItemUnitVolumeUnitOfMeasureName": self.ItemUnitVolumeUnitOfMeasureName,
            "ItemUnitWeight": self.ItemUnitWeight,
            "ItemUnitWeightUnitOfMeasureName": self.ItemUnitWeightUnitOfMeasureName,
            "ItemServingSize": self.ItemServingSize,
            "ItemSupplyDurationDays": self.ItemSupplyDurationDays,
            "ItemUnitQuantity": self.ItemUnitQuantity,
            "ItemUnitQuantityUnitOfMeasureName": self.ItemUnitQuantityUnitOfMeasureName,
            "Note": self.Note,
            "PackagedDate": self.PackagedDate,
            "InitialLabTestingState": self.InitialLabTestingState,
            "LabTestingState": self.LabTestingState,
            "LabTestingStateDate": self.LabTestingStateDate,
            "IsProductionBatch": self.IsProductionBatch,
            "ProductionBatchNumber": self.ProductionBatchNumber,
            "IsTradeSample": self.IsTradeSample,
            "IsTestingSample": self.IsTestingSample,
            "IsProcessValidationTestingSample": self.IsProcessValidationTestingSample,
            "ProductRequiresRemediation": self.ProductRequiresRemediation,
            "ContainsRemediatedProduct": self.ContainsRemediatedProduct,
            "RemediationDate": self.RemediationDate,
            "ReceivedFromManifestNumber": self.ReceivedFromManifestNumber,
            "ReceivedFromFacilityLicenseNumber": self.ReceivedFromFacilityLicenseNumber,
            "ReceivedFromFacilityName": self.ReceivedFromFacilityName,
            "ReceivedDateTime": self.ReceivedDateTime,
            "IsOnHold": self.IsOnHold,
            "ArchivedDate": self.ArchivedDate,
            "FinishedDate": self.FinishedDate,
            "LastModified": self.LastModified,
        }
