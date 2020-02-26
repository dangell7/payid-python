from __future__ import unicode_literals
from smartbnb import client, error
from smartbnb.resource import SmartBnBOAuthResource
from smartbnb.resource.base import (
    AccountOAuth
)
from smartbnb.util import (
    get_included_object,
    has_included_objects,
    cached_property,
)
from smartbnb.resource.listing import Listing

import time
import json

class Property(SmartBnBOAuthResource):

    @classmethod
    def list_url(cls):
        return super(Property, cls).list_url() + 'properties'

    @classmethod
    def get_url(cls, id):
        return super(Property, cls).list_url() + 'properties/' + id

    def refresh_from(self, **kwargs):
        print('Smart BnB Property: {}'.format(kwargs))
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.picture = kwargs['picture']
        self.address = Address(**kwargs['address'])
        if 'listings' in kwargs:
            self.listings = kwargs['listings']
        if has_included_objects(kwargs):
            print('Has Included Objects')
            # Listing Objects
            rel, listings = get_included_object(kwargs)
            self.listings = [
                Listing(**listing)
                for listing
                in listings
            ]


    def to_any_object(self):
        return {
            'id': self.id,
            'name': self.name,
            'picture': self.picture,
            'address': self.address.to_any_object(),
            'listings': self.listings,
        }

class Address(SmartBnBOAuthResource):

    def refresh_from(self, **kwargs):
        self.number = kwargs['number']
        self.city = kwargs['city']
        self.street = kwargs['street']
        self.state = kwargs['state']
        self.country = kwargs['country']
        self.postcode = kwargs['postcode']
        self.coordinates = kwargs['coordinates']
        self.display = kwargs['display']


    def to_any_object(self):
        return {
            'number': self.number,
            'street': self.street,
            'state': self.state,
            'country': self.country,
            'postcode': self.postcode,
            'coordinates': self.coordinates,
            'display': self.display,
        }
