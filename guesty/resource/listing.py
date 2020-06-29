from __future__ import unicode_literals
from guesty.resource import GuestyAccountResource
import json


class Listing(GuestyAccountResource):

    @classmethod
    def list_url(cls):
        return super(Listing, cls).list_url(None) + 'listings'

    @classmethod
    def get_url(cls, id):
        return super(Listing, cls).list_url(None) + 'listings/' + id + '/'

    def refresh_from(self, **kwargs):
        # print('Guesty Listing: {}'.format(json.dumps(kwargs, indent=4, sort_keys=True)))
        self.id = kwargs['_id']
        self.accommodates = kwargs['accommodates']
        self.accountId = kwargs['accountId']
        self.accountTaxes = kwargs['accountTaxes']
        self.active = kwargs['active']
        self.address = Address(self.account_id, **kwargs['address'])
        self.amenities = kwargs['amenities']
        self.amenitiesNotIncluded = kwargs['amenitiesNotIncluded']
        self.bathrooms = kwargs['bathrooms']
        self.bedrooms = kwargs['bedrooms']
        self.beds = kwargs['beds']
        # TODO -> Is Object or Array
        self.calendarRules = kwargs['calendarRules']
        self.commissionFormula = kwargs['commissionFormula']
        self.createdAt = kwargs['createdAt']
        # TODO -> Is Object or Array
        self.defaultCheckInEndTime = kwargs['defaultCheckInEndTime']
        self.defaultCheckInTime = kwargs['defaultCheckInTime']
        self.defaultCheckOutTime = kwargs['defaultCheckOutTime']
        self.importedAt = kwargs['importedAt']
        self.integrations = [Integration(self.account_id, **i) for i in kwargs['integrations']]
        self.isListed = kwargs['isListed']
        self.lastActivityAt = kwargs['lastActivityAt']
        self.lastUpdatedAt = kwargs['lastUpdatedAt']
        # TODO -> Is Object or Array
        self.listingRooms = kwargs['listingRooms']
        # TODO -> Is Object or Array
        self.markups = kwargs['markups']
        self.netIncomeFormula = kwargs['netIncomeFormula']
        self.nickname = kwargs['nickname']
        self.occupancyStats = kwargs['occupancyStats']
        self.offeredServices = kwargs['offeredServices']
        self.otaRoomType = None
        if 'otaRoomType' in kwargs:
            self.otaRoomType = kwargs['otaRoomType']
        self.ownerRevenueFormula = kwargs['ownerRevenueFormula']
        # TODO -> Is Object or Array
        self.owners = kwargs['owners']
        # TODO -> Is Object or Array
        self.pendingTasks = kwargs['pendingTasks']
        self.picture = Picture(self.account_id, **kwargs['picture'])
        # TODO -> Is Object or Array
        self.pictures = kwargs['pictures']
        # TODO -> Is Object or Array
        self.pms = kwargs['pms']
        self.preBooking = kwargs['preBooking']
        # TODO -> Is Object or Array
        self.prices = kwargs['prices']
        # TODO -> Is Object or Array
        self.privateDescription = kwargs['privateDescription']
        self.propertyType = kwargs['propertyType']
        # TODO -> Is Object or Array
        self.publicDescription = kwargs['publicDescription']
        # TODO -> Is Object or Array
        self.receptionistsService = kwargs['receptionistsService']
        self.roomType = kwargs['roomType']
        # TODO -> Is Object or Array
        self.sales = kwargs['sales']
        # TODO -> Is Object or Array
        self.tags = kwargs['tags']
        # TODO -> Is Object or Array
        self.taxes = kwargs['taxes']
        # TODO -> Is Object or Array
        self.terms = kwargs['terms']
        self.timezone = kwargs['timezone']
        self.title = kwargs['title']
        self.type = kwargs['type']
        self.useAccountAdditionalFees = kwargs['useAccountAdditionalFees']
        self.useAccountMarkups = kwargs['useAccountMarkups']
        self.useAccountRevenueShare = kwargs['useAccountRevenueShare']
        self.useAccountTaxes = kwargs['useAccountTaxes']


    def to_any_object(self):
        return {
            'id': self.id,
            'accommodates': self.accommodates,
            'accountId': self.accountId,
            'accountTaxes': self.accountTaxes,
            'active': self.active,
            'address': self.address,
            'amenities': self.amenities,
            'amenitiesNotIncluded': self.amenitiesNotIncluded,
            'bathrooms': self.bathrooms,
            'bedrooms': self.bedrooms,
            'beds': self.beds,
            'calendarRules': self.calendarRules,
            'commissionFormula': self.commissionFormula,
            'createdAt': self.createdAt,
            'defaultCheckInEndTime': self.defaultCheckInEndTime,
            'defaultCheckInTime': self.defaultCheckInTime,
            'defaultCheckOutTime': self.defaultCheckOutTime,
            'importedAt': self.importedAt,
            'integrations': self.integrations,
            'isListed': self.isListed,
            'lastActivityAt': self.lastActivityAt,
            'lastUpdatedAt': self.lastUpdatedAt,
            'listingRooms': self.listingRooms,
            'markups': self.markups,
            'netIncomeFormula': self.netIncomeFormula,
            'nickname': self.nickname,
            'occupancyStats': self.occupancyStats,
            'offeredServices': self.offeredServices,
            'otaRoomType': self.otaRoomType,
            'ownerRevenueFormula': self.ownerRevenueFormula,
            'owners': self.owners,
            'pendingTasks': self.pendingTasks,
            'picture': self.picture,
            'pictures': self.pictures,
            'pms': self.pms,
            'preBooking': self.preBooking,
            'prices': self.prices,
            'privateDescription': self.privateDescription,
            'propertyType': self.propertyType,
            'publicDescription': self.publicDescription,
            'receptionistsService': self.receptionistsService,
            'roomType': self.roomType,
            'sales': self.sales,
            'tags': self.tags,
            'taxes': self.taxes,
            'terms': self.terms,
            'timezone': self.timezone,
            'title': self.title,
            'type': self.type,
            'useAccountAdditionalFees': self.useAccountAdditionalFees,
            'useAccountMarkups': self.useAccountMarkups,
            'useAccountRevenueShare': self.useAccountRevenueShare,
            'useAccountTaxes': self.useAccountTaxes,
        }


class Integration(GuestyAccountResource):

    def refresh_from(self, **kwargs):
        self.id = None
        self.airbnb2 = None
        self.homeaway2 = None
        self.externalUrl = None
        if 'airbnb2' in kwargs:
            self.airbnb2 = kwargs['airbnb2']
            if 'id' in kwargs['airbnb2']:
                self.id = kwargs['airbnb2']['id']
        if 'homeaway2' in kwargs:
            self.homeaway2 = kwargs['homeaway2']
            if 'id' in kwargs['homeaway2']:
                self.id = kwargs['homeaway2']['advertiserId']
        # TODO -> Object or Array
        self.bookingCom = kwargs['bookingCom']
        if 'externalUrl' in kwargs:
            self.externalUrl = kwargs['externalUrl']
        self.platform = kwargs['platform']

    def to_any_object(self):
        return {
            'id': self.id,
            'airbnb2': self.airbnb2,
            'homeaway2': self.homeaway2,
            'bookingCom': self.bookingCom,
            'externalUrl': self.externalUrl,
            'platform': self.platform,
        }


class Address(GuestyAccountResource):

    def refresh_from(self, **kwargs):
        self.apt = kwargs['apt']
        self.city = kwargs['city']
        self.country = kwargs['country']
        self.full = kwargs['full']
        self.lat = kwargs['lat']
        self.lng = kwargs['lng']
        self.state = kwargs['state']
        self.street = kwargs['street']
        self.zipcode = kwargs['zipcode']

    def to_any_object(self):
        return {
            'apt': self.apt,
            'city': self.city,
            'country': self.country,
            'full': self.full,
            'lat': self.lat,
            'lng': self.lng,
            'state': self.state,
            'street': self.street,
            'zipcode': self.zipcode,
        }


class Picture(GuestyAccountResource):

    def refresh_from(self, **kwargs):
        self.caption = kwargs['caption']
        self.large = kwargs['large']
        self.regular = kwargs['regular']
        self.thumbnail = kwargs['thumbnail']

    def to_any_object(self):
        return {
            'caption': self.caption,
            'large': self.large,
            'regular': self.regular,
            'thumbnail': self.thumbnail,
        }
