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

def get_arrays_from_array(batch_days_array):
    updated_calendar_arrays = []
    updated_calendar_days = []
    sbb_batch_max = 60
    for day in batch_days_array:
        updated_calendar_days.append(day)
        if len(updated_calendar_days) == sbb_batch_max:
            updated_calendar_arrays.append(updated_calendar_days)
            updated_calendar_days = []


    # Add non 60 batch (last)
    if len(updated_calendar_days) > 0:
        updated_calendar_arrays.append(updated_calendar_days)

    return [[{
          "date": "2020-02-22",
          "price": {
            "amount": 91,
          }
    }]]
    # return updated_calendar_arrays

class Calendar(SmartBnBOAuthResource):

    @classmethod
    def list_url(cls, id):
        return super(Calendar, cls).list_url() + 'calendar/' + id

    @classmethod
    def get_url(cls, id):
        return super(Calendar, cls).list_url() + 'calendar/' + id

    @classmethod
    def update(cls,
            access_token,
            propertyHash,
            batch_days_array):

        params = {
            'type': 'property'
        }

        arrays = get_arrays_from_array(batch_days_array)
        for array in arrays:
            res = client.put(access_token, cls.list_url(propertyHash), params, array)
            print(res)
        # return cls(propertyID, **res)

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
