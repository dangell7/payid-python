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

class Calendar(SmartBnBOAuthResource):

    @classmethod
    def get_url(cls, id):
        return super(Calendar, cls).list_url() + 'calendar/' + id

    def refresh_from(self, **kwargs):
        print(kwargs)
        print(e)

    def to_any_object(self):
        return {
        }
