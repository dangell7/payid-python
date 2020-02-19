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

class Listing(SmartBnBOAuthResource):

    @classmethod
    def list_url(cls):
        return super(Listing, cls).list_url(None) + 'listings'

    @classmethod
    def get_url(cls, id):
        return super(Listing, cls).list_url() + 'listings/' + id + '/'

    def refresh_from(self, **kwargs):
        # print('Smart BnB Listing: {}'.format(kwargs))
        self.id = kwargs['id']
        self.provider = kwargs['provider']
        self.name = kwargs['name']
        self.picture = kwargs['picture']
        self.address = kwargs['address']
        self.available = kwargs['available']
        self.checkin = kwargs['checkin']
        self.checkout = kwargs['checkout']
        self.capacity = Capacity(**kwargs['capacity'])
        self.rating = kwargs['rating']


    def to_any_object(self):
        return {
            'id': self.id,
            'name': self.name,
            'picture': self.picture,
            'address': self.address,
            'checkin': self.checkin,
            'checkout': self.checkout,
            'capacity': self.capacity,
            'rating': self.rating,
        }

class Capacity(SmartBnBOAuthResource):

    def refresh_from(self, **kwargs):
        self.max = kwargs['max']
        self.bedrooms = kwargs['bedrooms']
        self.beds = kwargs['beds']
        self.bathrooms = kwargs['bathrooms']


    def to_any_object(self):
        return {
            'max': self.max,
            'bedrooms': self.bedrooms,
            'beds': self.beds,
            'bathrooms': self.bathrooms,
        }
