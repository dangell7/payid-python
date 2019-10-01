from __future__ import unicode_literals
from mmj import client, env
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
        return client.build_url('facilities/v1')

    @classmethod
    def retrieve_url(cls, instance_id):
        return cls.list_url() + instance_id + '/'

    @classmethod
    def get(cls, instance_id):
        if env == 'Json':
            path = basedir + '/server/utils/mmj/tmp/%s.json' % 'facility'
            res = read_json(path)
        elif env == 'Firestore':
            mmj_ref = client.get_mmj_ref()
            res = mmj_ref.get()
            res = res.to_dict()
        else:
            res = client.get(cls.retrieve_url(instance_id))
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
        return client.build_url('facilities/v1') + facility_id + '/'

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
