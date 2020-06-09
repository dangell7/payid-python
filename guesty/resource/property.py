from __future__ import unicode_literals
from guesty import client, error
from guesty.resource import guestyOAuthResource
from guesty.resource.base import (
    AccountOAuth
)
from guesty.util import (
    get_included_object,
    has_included_objects,
    cached_property,
)
from guesty.resource.listing import Listing

import time
import json

class Property(guestyOAuthResource):

    @classmethod
    def list_url(cls):
        return super(Property, cls).list_url() + 'properties'

    @classmethod
    def get_url(cls, id):
        return super(Property, cls).list_url() + 'properties/' + id

    def refresh_from(self, **kwargs):
        print('Guesty Property: {} ID: {}'.format(kwargs['name'], kwargs['id']))
        # print('Guesty Property: {}'.format(kwargs))
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.listed = kwargs['listed']
        self.picture = kwargs['picture']
        self.address = Address(**kwargs['address'])
        if 'listings' in kwargs:
            self.listings = kwargs['listings']
            print('{} Listings for {}'.format(len(self.listings), self.name))

        if has_included_objects(kwargs):
            # print('Has Included Objects')
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
            'listed': self.listed,
            'picture': self.picture,
            'address': self.address.to_any_object(),
            'listings': self.listings,
        }

class Address(guestyOAuthResource):

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
