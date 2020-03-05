from smartbnb import client
from smartbnb.resource import SmartBnBOAuthResource
from smartbnb.util import (
    cached_property,
    read_json,
)
from basedir import basedir

import time

class AccountOAuth(SmartBnBOAuthResource):

    def refresh_from(self, **kwargs):
        self.scope = kwargs['scope']
        self.expires_in = kwargs['expires_in']
        self.token_type = kwargs['token_type']

    # @cached_property
    def get_property(self, id):
        params = {
            'include': 'listings'
        }
        res = client.get(self.access_token, Property.get_url(id), params)
        res = res['data']
        return Property(**res)

    @cached_property
    def properties(self):
        new_properties = []
        params = {
            'include': 'listings'
        }
        res = client.get(self.access_token, Property.list_url(), params)

        # Pagination
        if 'total_pages' in res['_pagination']:
            num_pages = res['_pagination']['total_pages']
        if 'per_page' in res['_pagination']:
            per_page = res['_pagination']['per_page']

        # First Results
        res = res['data']
        new_properties.extend([Property(**i) for i in res])

        # More Results
        for page in range(2, num_pages + 1):
            params = {
                'include': 'listings'
            }
            params['page'] = page
            params['per_page'] = per_page
            res = client.get(self.access_token, Property.list_url(), params)
            res = res['data']
            new_properties.extend([Property(**i) for i in res])
        return new_properties

    # @cached_property
    def get_calendar(self, id, start_date, end_date):
        num_pages = 0
        per_page = 0
        new_calendar_days = []
        params = {
            'start_date': start_date,
            'end_date': end_date,
        }
        res = client.get(self.access_token, Calendar.get_url(id), params)
        res = res['data']
        return Calendar(**res)

    # @cached_property
    def get_reservations(self, id, start_date, end_date):
        num_pages = 0
        per_page = 0
        new_reservations = []
        params = {
            'listings[]': id,
            'start_date': start_date,
            'end_date': end_date
        }
        params = "&".join("%s=%s" % (k,v) for k,v in params.items())
        res = client.get(self.access_token, Reservation.list_url(), params)

        # Pagination
        if 'total_pages' in res['_pagination']:
            num_pages = res['_pagination']['total_pages']
        if 'per_page' in res['_pagination']:
            per_page = res['_pagination']['per_page']

        # Add First Page Results
        res = res['data']
        new_reservations.extend(Reservation(**i) for i in res)

        # More Results
        for page in range(2, num_pages + 1):
            params = {
                'listings[]': id,
                'start_date': start_date,
                'end_date': end_date
            }
            params['page'] = page
            params['per_page'] = per_page
            params = "&".join("%s=%s" % (k,v) for k,v in params.items())
            res = client.get(self.access_token, Reservation.list_url(), params)
            # Add Next Page Results
            res = res['data']
            new_reservations.extend(Reservation(**i) for i in res)
        return new_reservations

    def update_calendar(self,
                    propertyHash=None,
                    batch_array=None):

        result = Calendar.update(
            self.access_token,
            propertyHash,
            batch_array
        )

        return result

    def __unicode__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.id)

    def to_any_object(self):
        return {
            'access_token': self.access_token,
            'scope': self.scope,
            'expires_in': self.expires_in,
            'token_type': self.token_type,
        }

from smartbnb.resource.property import Property  # noqa - avoid circular import
from smartbnb.resource.listing import Listing  # noqa - avoid circular import
from smartbnb.resource.reservation import Reservation  # noqa - avoid circular import
from smartbnb.resource.calendar import Calendar  # noqa - avoid circular import
