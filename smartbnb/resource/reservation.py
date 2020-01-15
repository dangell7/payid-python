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

class Reservation(SmartBnBOAuthResource):

    @classmethod
    def list_url(cls):
        return super(Reservation, cls).list_url() + 'calendar/reservations'

    @classmethod
    def get_url(cls, id):
        return super(Reservation, cls).get_url() + 'calendar/reservations/' + id + '/'

    def refresh_from(self, **kwargs):
        print(kwargs)
        print(e)


    def to_any_object(self):
        return {
        }
