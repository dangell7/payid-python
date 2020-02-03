from __future__ import unicode_literals
from smartbnb import client, error
from smartbnb.resource import SmartBnBOAuthResource
from smartbnb.resource.base import (
    AccountOAuth
)
from smartbnb.util import (
    cached_property,
    from_int_to_decimal,
)

import time
import json

class Calendar(SmartBnBOAuthResource):

    @classmethod
    def get_url(cls, id):
        return super(Calendar, cls).list_url() + 'calendar/' + id

    def refresh_from(self, **kwargs):
        self.listing_id = kwargs['listing_id']
        self.provider = kwargs['provider']
        self.start_date = kwargs['start_date']
        self.end_date = kwargs['end_date']
        days_collection = []
        for day in kwargs['days']:
            days_collection.append(Day(**day))
        self.days = days_collection

    def to_any_object(self):
        days_collection = []
        for day in self.days:
            days_collection.append(day.to_any_object())

        return {
            'listing_id': self.listing_id,
            'provider': self.provider,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'days': days_collection,
        }

class Day(SmartBnBOAuthResource):

    def refresh_from(self, **kwargs):
        self.date = kwargs['date']
        self.day = kwargs['day']
        self.status = DayStatus(**kwargs['status'])
        self.price = DayPrice(**kwargs['price'])
        self.reservation = {}


    def to_any_object(self):
        return {
            'listing_id': self.listing_id,
            'provider': self.provider,
            'date': self.date,
            'day': self.day,
            'status': self.status.to_any_object(),
            'price': self.price.to_any_object(),
            'reservation': self.reservation
        }

class DayStatus(SmartBnBOAuthResource):

    def refresh_from(self, **kwargs):
        self.reason = kwargs['reason']
        self.available = kwargs['available']


    def to_any_object(self):
        return {
            'reason': self.reason,
            'available': self.available
        }

class DayPrice(SmartBnBOAuthResource):

    def refresh_from(self, **kwargs):
        self.amount = from_int_to_decimal(kwargs['amount'])
        self.currency = kwargs['currency']


    def to_any_object(self):
        return {
            'amount': self.amount,
            'currency': self.currency
        }
