from airbnb import client
from airbnb.resource import AirBnBResource, AirBnBAccountResource
from airbnb.util import (
    cached_property,
    read_json,
)
from basedir import basedir

import json
import time

class Account(AirBnBResource):

    @classmethod
    def all(cls):
        res = client.get(Account.list_url())
        facilitys = res
        return [Account(**l) for l in facilities]

    def refresh_from(self, **kwargs):
        user = kwargs["user"]
        self.about = user['about']
        self.email = user['email']
        self.listings_count = user['listings_count']
        self.total_listings_count = user['total_listings_count']
        self.picture_url = user['picture_url']


    # @cached_property
    def get_property(self, id):
        res = client.get(Property.get_url(self.id, id))
        return Property(self, **res)

    @cached_property
    def properties(self):
        params = {
            'key': 'd306zoyjsyarp7ifhu67rjxn52tv0t20',
            'currency': 'USD',
            'user_id': self.id,
            'format': 'v1_legacy_long',
            'offset': 0,
            'limit': 100
        }
        res = client.get(Property.list_url(self.id), params)
        res = res['listings']
        return [Property(self.id, **i) for i in res]

    def __unicode__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.id)

from airbnb.resource.property import Property  # noqa - avoid circular import
