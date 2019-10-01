from __future__ import unicode_literals
from mmj import client, error
from mmj.resource import MMJFacilityResource
from mmj.resource.base import (
    Facility
)
from mmj.util import (
    cached_property,
)

import time

class Item(MMJFacilityResource):

    @classmethod
    def list_url(cls, facility_id):
        return super(Item, cls).list_url(facility_id) + 'menu_items/'

    @classmethod
    def get_url(cls, facility_id, id):
        return super(Item, cls).list_url(facility_id) + 'menu_items/' + id + '/'

    def refresh_from(self, **kwargs):
        self.amount = kwargs['amount']
        self.body_html = kwargs['body_html']
        self.category = kwargs['category']
        self.cbd = kwargs['cbd']
        self.cbda = kwargs['cbda']
        self.cbn = kwargs['cbn']
        self.created_at = kwargs['created_at']
        self.genetics = kwargs['genetics']
        self.id = kwargs['id']
        self.indica = kwargs['indica']
        self.measurement = kwargs['measurement']
        self.name = kwargs['name']
        self.on_hold = kwargs['on_hold']
        self.picture = kwargs['picture']
        self.price = kwargs['price']
        self.sativa = kwargs['sativa']
        self.thc_percent = kwargs['thc_percent']
        self.thca_percent = kwargs['thca_percent']
        self.updated_at = kwargs['updated_at']

    def to_any_object(self):
        return {
            "amount": self.amount,
            "body_html": self.body_html,
            "category": self.category,
            "cbd": self.cbd,
            "cbda": self.cbda,
            "cbn": self.cbn,
            "created_at": self.created_at,
            "genetics": self.genetics,
            "id": self.id,
            "indica": self.indica,
            "measurement": self.measurement,
            "name": self.name,
            "on_hold": self.on_hold,
            "picture": self.picture,
            "price": self.price,
            "sativa": self.sativa,
            "thc_percent": self.thc_percent,
            "thca_percent": self.thca_percent,
            "updated_at": self.updated_at,
        }
