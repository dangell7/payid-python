from guesty import client
from guesty.resource import GuestyResource
from guesty.util import (
    cached_property,
)
import json
import math


class Account(GuestyResource):

    @classmethod
    def all(cls):
        res = client.get(Account.list_url())
        return [Account(**a) for a in res]

    def refresh_from(self, **kwargs):
        self.id = kwargs['_id']
        self.name = kwargs['name']
        self.timezone = kwargs['timezone']

    # @cached_listing
    def get_listing(self, id):
        res = client.get(Listing.get_url(id))
        res = res['data']
        return Listing(self.id, **res)

    @cached_property
    def listings(self):
        try:
            new_listings = []
            params = {
                'limit': 25,
            }
            res = client.get(Listing.list_url(), params)

            # Pagination
            total_count = 0
            if 'count' in res:
                total_count = res['count']
            if 'limit' in res:
                limit = res['limit']
            num_pages = math.ceil(total_count / limit)

            # First Results
            res = res['results']
            new_listings.extend([Listing(self.id, **l) for l in res])
            # More Results
            for page in range(1, num_pages):
                params = {}
                params['skip'] = page * limit
                params['limit'] = limit
                res = client.get(Listing.list_url(), params)
                res = res['results']
                new_listings.extend([Listing(self.id, **i) for i in res])
            return new_listings
        except Exception as e:
            print(e)

    # @cached_property
    def get_calendar(self, id, start_date, end_date):
        params = {
            'from': start_date,
            'to': end_date,
        }
        res = client.get(Calendar.get_url(id), params)
        kwargs = {}
        kwargs['days'] = res
        return Calendar(self.id, **kwargs)

    # @cached_property
    def get_reservations(self, id, start_date, end_date):
        # num_pages = 0
        # per_page = 0
        new_reservations = []
        filters = []
        filters.append({
            'field': 'listingId',
            'operator': '$eq',
            'value': id,
            'context': None
        })
        if start_date:
            filters.append({
                'field': 'checkIn',
                'operator': '$gt',
                'value': start_date,
                'context': None
            })
        # if end_date:
        #     filters.append({
        #         'field': 'status',
        #         'operator': '$eq',
        #         'value': 'confirmed',
        #         'context': None
        #     })
        params = {
            'filters': json.dumps(filters),
            'fields': 'nightsCount checkIn checkOut createdAt money status confirmationCode',
        }
        res = client.get(Reservation.list_url(), params)

        # Pagination
        total_count = 0
        if 'count' in res:
            total_count = res['count']
        if 'limit' in res:
            limit = res['limit']
        num_pages = math.ceil(total_count / limit)

        # Add First Page Results
        res = res['results']
        new_reservations.extend(Reservation(self.id, **r) for r in res)

        # More Results
        for page in range(1, num_pages):
            params['skip'] = page * limit
            params['limit'] = limit
            res = client.get(Reservation.list_url(), params)
            res = res['results']
            new_reservations.extend([Reservation(self.id, **r) for r in res])
        return new_reservations

    def update_calendar(self, listingHash=None, batch_array=None):
        result = Calendar.update(
            listingHash,
            batch_array
        )
        return result

    def __unicode__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.id)

from guesty.resource.listing import Listing  # noqa - avoid circular import
from guesty.resource.reservation import Reservation  # noqa - avoid circular import
from guesty.resource.calendar import Calendar  # noqa - avoid circular import
