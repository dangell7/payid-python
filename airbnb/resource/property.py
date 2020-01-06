from __future__ import unicode_literals
from airbnb import client, error
from airbnb.resource import AirBnBAccountResource
from airbnb.resource.base import (
    Account
)
from airbnb.util import (
    cached_property,
)

import time
import json

class Property(AirBnBAccountResource):

    @classmethod
    def list_url(cls, account_id):
        return super(Property, cls).list_url(account_id) + 'listings'

    @classmethod
    def get_url(cls, account_id, id):
        return super(Property, cls).list_url(account_id) + 'listings/' + id + '/'

    def refresh_from(self, **kwargs):
        print(kwargs['name'])
        self.id = kwargs['id']
        self.bedrooms = kwargs['bedrooms']
        self.beds = kwargs['beds']
        self.cancellation_policy = kwargs['cancellation_policy']
        self.city = kwargs['city']
        self.country_code = kwargs['country_code']
        self.name = kwargs['name']
        self.medium_url = kwargs['medium_url']
        self.person_capacity = kwargs['person_capacity']
        self.price = kwargs['price']
        self.property_type = kwargs['property_type']
        self.reviews_count = kwargs['reviews_count']
        self.star_rating = kwargs['star_rating']
        self.room_type_category = kwargs['room_type_category']
        self.state = kwargs['state']
        # Handle None User First Name
        self.user_first = None
        if 'first_name' in kwargs['user']:
            self.user_first = kwargs['user']['first_name']

        # Handle None User Last Name
        self.user_last = None
        if 'last_name' in kwargs['user']:
            self.user_last = kwargs['user']['last_name']
        self.user_id = kwargs['user']['id']
        self.user_avatar = kwargs['user']['thumbnail_url']
        self.zipcode = kwargs['zipcode']

    def to_any_object(self):
        return {
            'id': self.id,
            'bedrooms': self.bedrooms,
            'beds': self.beds,
            'cancellation_policy': self.cancellation_policy,
            'city': self.city,
            'country_code': self.country_code,
            'name': self.name,
            'medium_url': self.medium_url,
            'person_capacity': self.person_capacity,
            'price': self.price,
            'property_type': self.property_type,
            'star_rating': self.star_rating,
            'room_type_category': self.room_type_category,
            'state': self.state,
            'user_first': self.user_first,
            'user_last': self.user_last,
            'user_id': self.user_id,
            'user_avatar': self.user_avatar,
            'zipcode': self.zipcode,
        }
