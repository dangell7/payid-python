from __future__ import unicode_literals
from guesty.resource import GuestyAccountResource
import json


class Reservation(GuestyAccountResource):

    @classmethod
    def list_url(cls, account_id):
        return super(Reservation, cls).list_url(account_id) + 'reservations'

    @classmethod
    def get_url(cls, account_id, id):
        return super(Reservation, cls).get_url(account_id) + 'reservations/' + id + '/'

    def refresh_from(self, **kwargs):
        print('Guesty Reservations: {}'.format(json.dumps(kwargs, indent=4, sort_keys=True)))
        self._id = kwargs['_id']
        self.accountId = kwargs['accountId']
        self.checkIn = kwargs['checkIn']
        self.checkOut = kwargs['checkOut']
        self.confirmationCode = None
        if 'confirmationCode' in kwargs:
            self.confirmationCode = kwargs['confirmationCode']
        self.guest = ReservationGuest(self.account_id, **kwargs['guest'])
        self.guestId = kwargs['guestId']
        self.integration = ReservationIntegration(self.account_id, **kwargs['integration'])
        self.listing = ReservationListing(self.account_id, **kwargs['listing'])
        self.listingId = kwargs['listingId']

    def to_any_object(self):
        return {
            '_id': self._id,
            'accountId': self.accountId,
            'checkIn': self.checkIn,
            'checkOut': self.checkOut,
            'guest': self.guest.to_any_object(),
            'guestId': self.guestId,
            'integration': self.integration.to_any_object(),
            'listing': self.listing.to_any_object(),
            'listingId': self.listingId
        }


class ReservationGuest(GuestyAccountResource):

    def refresh_from(self, **kwargs):
        self._id = kwargs['_id']
        self.fullName = kwargs['fullName']

    def to_any_object(self):
        return {
            '_id': self._id,
            'fullName': self.fullName
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
        self.title = kwargs['title']

    def to_any_object(self):
        return {
            '_id': self._id,
            'title': self.title
        }
