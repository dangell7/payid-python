from __future__ import unicode_literals
from airbnb import client
from airbnb.util import read_json
from basedir import basedir


class PrintableResource(object):

    def __unicode__(self):
        return '<AirBnB::{} {}>'.format(self.__class__.__name__, self.id)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __repr__(self):
        attrs = [
            '\'{}\': {}'.format(key, repr(getattr(self, key)))
            for key
            in self.__dict__
        ]

        return '\n{{\n\t{}\n}}'.format('\n\t'.join(attrs))


class AirBnBResource(PrintableResource):

    @classmethod
    def list_url(cls):
        return client.build_url('users/')

    @classmethod
    def retrieve_url(cls, instance_id):
        return cls.list_url() + instance_id + '/'

    @classmethod
    def get(cls, instance_id):
        params = {
            'token': 'public',
            'client_id': 'd306zoyjsyarp7ifhu67rjxn52tv0t20',
        }
        res = client.get(cls.retrieve_url(instance_id), params)
        return cls(**res)

    def __init__(self, **kwargs):
        if 'id' in kwargs['user']:
            self.id = kwargs['user']['id']
        self.refresh_from(**kwargs)

    def refresh(self):
        res = client.get(self.instance_url)
        return self.refresh_from(**res)

    def refresh_from(self, **kwargs):
        raise NotImplementedError

    @property
    def instance_url(self):
        return self.__class__.retrieve_url(self.id)


class AirBnBAccountResource(AirBnBResource):

    @classmethod
    def list_url(cls, account_id):
        # print('Account Resource "ListID1": {}'.format(account_id))
        return client.build_url('')

    @classmethod
    def retrieve_url(cls, account_id, instance_id):
        # print('Account Resource "RetID1": {} "RetID2": {}'.format(account_id, instance_id))
        return cls.list_url(account_id) + instance_id + '/'

    @classmethod
    def get(cls, account_id, instance_id):
        # print('Account Resource "GetID1": {} "GetID2": {}'.format(account_id, instance_id))
        res = client.get(cls.retrieve_url(account_id, instance_id))
        return cls(**res)

    def __init__(self, account_id, **kwargs):
        self.account_id = account_id
        super(AirBnBAccountResource, self).__init__(**kwargs)

    @property
    def instance_url(self):
        return self.__class__.retrieve_url(self.account_id, self.id)

    def __unicode__(self):
        return '<AirBnB::{} {} at Account {}>'.format(
            self.__class__.__name__,
            self.id,
            self.account_id
        )
