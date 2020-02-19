from __future__ import unicode_literals
from smartbnb import client, error
from smartbnb.resource import SmartBnBOAuthResource
from smartbnb.resource.base import (
    AccountOAuth
)

from smartbnb.util import (
    cached_property,
)

import time
import json

class Reservation(SmartBnBOAuthResource):

    @classmethod
    def list_url(cls):
        return super(Reservation, cls).list_url() + 'calendar/reservations'

    @classmethod
    def get_url(cls, id):
        return super(Reservation, cls).get_url() + 'calendar/reservations/' + id + '/'

    def refresh_from(self, **kwargs):
        print(kwargs)
        self.uuid = kwargs['uuid']
        self.guest_uuid = kwargs['guest_uuid']
        self.provider = kwargs['provider']
        self.listing_id = kwargs['listing_id']
        self.reservation_code = kwargs['reservation_code']
        self.status = kwargs['status']
        self.booked_at = kwargs['booked_at']
        self.instant_booked = kwargs['instant_booked']
        self.nights = kwargs['nights']
        self.occupancy = ReservationOccupancy(**kwargs['occupancy'])
        self.check_in = kwargs['check_in']
        self.check_out = kwargs['check_out']
        self.subtotal = ReservationPrice(**kwargs['subtotal'])


    def to_any_object(self):
        return {
            'UUID': self.uuid,
            'guestUUID': self.guest_uuid,
            'provider': self.provider,
            'listingID': self.listing_id,
            'reservationCode': self.reservation_code,
            'status': self.status,
            'bookedAt': self.booked_at,
            'instantBooked': self.instant_booked,
            'nights': self.nights,
            'occupancy': self.occupancy.to_any_object(),
            'checkIn': self.check_in,
            'checkOut': self.check_out,
            'subtotal': self.subtotal.to_any_object(),
        }

class ReservationOccupancy(SmartBnBOAuthResource):

    def refresh_from(self, **kwargs):
        self.adults = kwargs['adults']
        self.children = kwargs['children']
        self.pets = kwargs['pets']
        self.infants = kwargs['infants']


    def to_any_object(self):
        return {
            'adults': self.adults,
            'children': self.children,
            'pets': self.pets,
            'infants': self.infants
        }

class ReservationPrice(SmartBnBOAuthResource):

    def refresh_from(self, **kwargs):
        self.amount = kwargs['amount']
        self.currency = kwargs['currency']


    def to_any_object(self):
        return {
            'amount': self.amount,
            'currency': self.currency
        }
