from mmj import client
from mmj.resource import MMJResource, MMJFacilityResource
from mmj.util import (
    cached_property,
    read_json,
)
from basedir import basedir

import json
import time

class Facility(MMJResource):

    @classmethod
    def all(cls):
        env = client.get_env()
        print(env)
        if env == 'Json':
            path = basedir + '/server/utils/mmj/tmp/%s.json' % 'facilities'
            res = read_json(path)
        else:
            res = client.get(Facility.list_url())
        facilitys = res
        return [Facility(**l) for l in facilities]

    def refresh_from(self, **kwargs):
        self.HireDate = kwargs['HireDate']
        self.IsOwner = kwargs['IsOwner']
        self.IsManager = kwargs['IsManager']
        self.Occupations = kwargs['Occupations']
        self.Name = kwargs['Name']
        self.Alias = kwargs['Alias']
        self.DisplayName = kwargs['DisplayName']
        self.CredentialedDate = kwargs['CredentialedDate']
        self.SupportActivationDate = kwargs['SupportActivationDate']
        self.SupportExpirationDate = kwargs['SupportExpirationDate']
        self.SupportLastPaidDate = kwargs[ 'SupportLastPaidDate']
        self.FacilityType = kwargs['FacilityType']
        self.LicenseNumber = kwargs['License']['Number']
        self.LicenseStartDate = kwargs['License']['StartDate']
        self.LicenseEndDate = kwargs['License']['EndDate']
        self.LicenseType = kwargs['License']['LicenseType']


    # @cached_property
    def get_item(self, id):
        env = client.get_env()
        if env == 'Json':
            path = basedir + '/server/utils/mmj/tmp/%s.json' % 'menu_item'
            res = read_json(path)
        else:
            res = client.get(Item.get_url(self.LicenseNumber, id))
        return Item(self, **res)

    @cached_property
    def items(self):
        env = client.get_env()
        if env == 'Json':
            path = basedir + '/server/utils/mmj/tmp/%s.json' % 'menu_items'
            res = read_json(path)
        else:
            res = client.get(Item.list_url(self.LicenseNumber))

        res = res['menu_items']
        return [Item(self.LicenseNumber, **i) for i in res]

    def __unicode__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.LicenseNumber)

from mmj.resource.item import Item  # noqa - avoid circular import
