from __future__ import unicode_literals
from guesty.resource import GuestyAccountResource
import json


class Reservation(GuestyAccountResource):

    @classmethod
    def list_url(cls):
        return super(Reservation, cls).list_url(None) + 'reservations'

    @classmethod
    def get_url(cls, id):
        return super(Reservation, cls).list_url(None) + 'reservations/' + id + '/'

    def refresh_from(self, **kwargs):
        print('Guesty Reservation: {}'.format(json.dumps(kwargs, indent=4, sort_keys=True)))
        self._id = kwargs['_id']
        self.accountId = kwargs['accountId']
        self.nightsCount = kwargs['nightsCount']
        self.createdAt = kwargs['createdAt']
        self.checkIn = kwargs['checkIn']
        self.checkOut = kwargs['checkOut']
        self.confirmationCode = None
        if 'confirmationCode' in kwargs:
            self.confirmationCode = kwargs['confirmationCode']
        # self.guest = ReservationGuest(self.account_id, **kwargs['guest'])
        self.guestId = kwargs['guestId']
        self.integration = ReservationIntegration(self.account_id, **kwargs['integration'])
        # self.listing = ReservationListing(self.account_id, **kwargs['listing'])
        self.listingId = kwargs['listingId']
        self.status = kwargs['status']
        self.money = ReservationMoney(self.account_id, **kwargs['money'])
        # print('Guesty Reservation: {}'.format(json.dumps(self.to_any_object(), indent=4, sort_keys=True)))

    def to_any_object(self):
        return {
            '_id': self._id,
            'accountId': self.accountId,
            'createdAt': self.createdAt,
            'checkIn': self.checkIn,
            'checkOut': self.checkOut,
            # 'guest': self.guest.to_any_object(),
            'guestId': self.guestId,
            'integration': self.integration.to_any_object(),
            # 'listing': self.listing.to_any_object(),
            'listingId': self.listingId,
            'status': self.status,
            'money': self.money.to_any_object()
        }


class ReservationGuest(GuestyAccountResource):

    def refresh_from(self, **kwargs):
        self._id = kwargs['_id']
        # self.fullName = kwargs['fullName']

    def to_any_object(self):
        return {
            '_id': self._id,
            # 'fullName': self.fullName
        }


class ReservationIntegration(GuestyAccountResource):

    def refresh_from(self, **kwargs):
        self._id = kwargs['_id']
        # TODO Object/Array
        self.limitations = kwargs['limitations']
        self.platform = kwargs['platform']

    def to_any_object(self):
        return {
            '_id': self._id,
            'limitations': self.limitations,
            'platform': self.platform
        }


class ReservationListing(GuestyAccountResource):

    def refresh_from(self, **kwargs):
        self._id = kwargs['_id']
        # self.title = kwargs['title']

    def to_any_object(self):
        return {
            '_id': self._id,
            # 'title': self.title
        }


class ReservationMoney(GuestyAccountResource):

    def refresh_from(self, **kwargs):
        # print('Guesty Reservation Money: {}'.format(json.dumps(kwargs, indent=4, sort_keys=True)))
        # self.altered = kwargs['altered']
        # self.autoPaymentsPolicy = kwargs['autoPaymentsPolicy']
        # self.balanceDue = kwargs['balanceDue']
        # self.channelCommissionRules = kwargs['channelCommissionRules']
        # self.commission = kwargs['commission']
        # self.commissionFormula = kwargs['commissionFormula']
        # self.commissionIncTax = kwargs['commissionIncTax']
        # self.commissionTax = kwargs['commissionTax']
        # self.commissionTaxPercentage = kwargs['commissionTaxPercentage']
        self.currency = kwargs['currency']
        self.fareAccommodation = kwargs['fareAccommodation']
        # self.fareAccommodationAdjusted = kwargs['fareAccommodationAdjusted']
        self.fareCleaning = kwargs['fareCleaning']
        # self.hostOriginalPayout = kwargs['hostOriginalPayout']
        # self.hostPayout = kwargs['hostPayout']
        # self.hostPayoutUsd = kwargs['hostPayoutUsd']
        # self.hostServiceFee = kwargs['hostServiceFee']
        # self.hostServiceFeeIncTax = kwargs['hostServiceFeeIncTax']
        # self.hostServiceFeeTax = kwargs['hostServiceFeeTax']
        # self.invoiceItems = kwargs['invoiceItems']
        # self.isFullyPaid = kwargs['isFullyPaid']
        # self.netIncome = kwargs['netIncome']
        # self.netIncomeFormula = kwargs['netIncomeFormula']
        # self.ownerRevenue = kwargs['ownerRevenue']
        # self.ownerRevenueFormula = kwargs['ownerRevenueFormula']
        # self.payments = kwargs['payments']
        # self.paymentsDue = kwargs['paymentsDue']
        # self.subTotalPrice = kwargs['subTotalPrice']
        # self.totalRefunded = kwargs['totalRefunded']
        # self.useAccountRevenueShare = kwargs['useAccountRevenueShare']

    def to_any_object(self):
        return {
            # 'altered': self.altered,
            # 'autoPaymentsPolicy': self.autoPaymentsPolicy,
            # 'balanceDue': self.balanceDue,
            # 'channelCommissionRules': self.channelCommissionRules,
            # 'commissionIncTax': self.commissionIncTax,
            # 'commissionTax': self.commissionTax,
            # 'commissionTaxPercentage': self.commissionTaxPercentage,
            'currency': self.currency,
            'fareAccommodation': self.fareAccommodation,
            # 'fareAccommodationAdjusted': self.fareAccommodationAdjusted,
            'fareCleaning': self.fareCleaning,
            # 'hostOriginalPayout': self.hostOriginalPayout,
            # 'hostPayout': self.hostPayout,
            # 'hostPayoutUsd': self.hostPayoutUsd,
            # 'hostServiceFee': self.hostServiceFee,
            # 'hostServiceFeeIncTax': self.hostServiceFeeIncTax,
            # 'hostServiceFeeTax': self.hostServiceFeeTax,
            # 'invoiceItems': self.invoiceItems,
            # 'isFullyPaid': self.isFullyPaid,
            # 'netIncome': self.netIncome,
            # 'netIncomeFormula': self.netIncomeFormula,
            # 'ownerRevenue': self.ownerRevenue,
            # 'ownerRevenueFormula': self.ownerRevenueFormula,
            # 'payments': self.payments,
            # 'paymentsDue': self.paymentsDue,
            # 'subTotalPrice': self.subTotalPrice,
            # 'totalRefunded': self.totalRefunded,
            # 'useAccountRevenueShare': self.useAccountRevenueShare,
        }
