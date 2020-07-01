from __future__ import unicode_literals
from guesty import client
from guesty.resource import GuestyAccountResource
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
    return updated_calendar_arrays


def format_array(listingHash, batch_days_array):
    new_array = []
    for day in batch_days_array:
        day['listingId'] = listingHash
        new_array.append(day)
    return new_array


class Calendar(GuestyAccountResource):

    @classmethod
    def list_url(cls):
        return super(Calendar, cls).list_url(None) + 'listings/calendars'

    @classmethod
    def get_url(cls, id):
        print('GET CAL')
        return super(Calendar, cls).list_url(None) + 'listings/' + id + '/calendar'

    @classmethod
    def update(cls, listingHash, batch_days_array):

        batch_days_array = format_array(listingHash, batch_days_array)
        res = client.put(cls.list_url(None), batch_days_array)
        return res

    def refresh_from(self, **kwargs):
        days_collection = []
        for day in kwargs['days']:
            days_collection.append(Day(self.account_id, **day))
        self.days = days_collection

    def to_any_object(self):
        days_collection = []
        for day in self.days:
            days_collection.append(day.to_any_object())

        return {
            'days': days_collection,
        }


class Day(GuestyAccountResource):

    def refresh_from(self, **kwargs):
        # print('Guesty Day: {}'.format(json.dumps(kwargs, indent=4, sort_keys=True)))
        self.v = None
        self.id = None
        self.accountId = None
        if '__v' in kwargs:
            self.v = kwargs['__v']
        if '_id' in kwargs:
            self.id = kwargs['_id']
        if 'accountId' in kwargs:
            self.accountId = kwargs['accountId']

        self.blocks = DayBlocks(self.account_id, **kwargs['blocks'])
        self.currency = kwargs['currency']
        self.date = kwargs['date']
        self.listing = DayListing(self.account_id, **kwargs['listing'])
        self.listingId = kwargs['listingId']
        self.price = kwargs['price']
        self.status = kwargs['status']
        # print('Guesty Day: {}'.format(json.dumps(self.to_any_object(), indent=4, sort_keys=True)))


    def to_any_object(self):
        return {
            'v': self.v,
            'id': self.id,
            'accountId': self.accountId,
            'blocks': self.blocks.to_any_object(),
            'currency': self.currency,
            'date': self.date,
            'listing': self.listing.to_any_object(),
            'listingId': self.listingId,
            'price': self.price,
            'status': self.status,
        }


class DayBlocks(GuestyAccountResource):

    def refresh_from(self, **kwargs):
        self.a = kwargs['a']
        self.abl = kwargs['abl']
        self.b = kwargs['b']
        self.bd = kwargs['bd']
        self.bw = kwargs['bw']
        self.m = kwargs['m']
        self.o = kwargs['o']
        self.r = kwargs['r']
        self.sr = kwargs['sr']

    def to_any_object(self):
        return {
            'a': self.a,
            'abl': self.abl,
            'b': self.b,
            'bd': self.bd,
            'bw': self.bw,
            'm': self.m,
            'o': self.o,
            'r': self.r,
            'sr': self.sr,
        }


class DayListing(GuestyAccountResource):

    def refresh_from(self, **kwargs):
        self.id = kwargs['_id']
        self.prices = kwargs['prices']


    def to_any_object(self):
        return {
            'id': self.id,
            'prices': self.prices
        }
