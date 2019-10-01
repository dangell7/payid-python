from __future__ import unicode_literals
from mmj import client
from mmj.util import read_json
from basedir import basedir


class PrintableResource(object):

    def __unicode__(self):
        return '<MMJ::{} {}>'.format(self.__class__.__name__, self.id)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __repr__(self):
        attrs = [
            '\'{}\': {}'.format(key, repr(getattr(self, key)))
            for key
            in self.__dict__
        ]

        return '\n{{\n\t{}\n}}'.format('\n\t'.join(attrs))


class MMJResource(PrintableResource):

    @classmethod
    def list_url(cls):
        # return client.build_url('dispensaries/')
        return client.build_url('menu_items/')

    @classmethod
    def retrieve_url(cls):
        return cls.list_url()

    @classmethod
    def get(cls):
        print('1')
        env = client.get_env()
        if env == 'Json':
            print('2')
            # path = basedir + '/server/utils/mmj/tmp/%s.json' % 'facility'
            # res = read_json(path)
            res = {}
        else:
            print('3')
            res = client.get(cls.retrieve_url())
        return cls(**res)

    def __init__(self, **kwargs):
        if 'id' in kwargs:
            self.id = kwargs['id']
        self.refresh_from(**kwargs)

    def refresh(self):
        res = client.get(self.instance_url)
        return self.refresh_from(**res)

    def refresh_from(self, **kwargs):
        raise NotImplementedError

    @property
    def instance_url(self):
        return self.__class__.retrieve_url(self.id)


class MMJFacilityResource(MMJResource):

    @classmethod
    def list_url(cls, facility_id):
        # return client.build_url('dispensaries/') + facility_id + '/'
        return client.build_url('menu_items/') + facility_id + '/'

    @classmethod
    def retrieve_url(cls, facility_id, instance_id):
        return cls.list_url(facility_id) + instance_id + '/'

    @classmethod
    def get(cls, facility_id, instance_id):
        res = client.get(cls.retrieve_url(facility_id, instance_id))
        return cls(**res)

    def __init__(self, facility_id, **kwargs):
        self.facility_id = facility_id
        super(MMJFacilityResource, self).__init__(**kwargs)

    @property
    def instance_url(self):
        return self.__class__.retrieve_url(self.facility_id, self.id)

    def __unicode__(self):
        return '<MMJ::{} {} at Facility {}>'.format(
            self.__class__.__name__,
            self.id,
            self.facility_id
        )
