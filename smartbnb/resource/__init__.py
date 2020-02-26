from __future__ import unicode_literals
from smartbnb import client
from smartbnb.util import read_json
from basedir import basedir


class PrintableResource(object):

    def __unicode__(self):
        return '<SmartBnB::{} {}>'.format(self.__class__.__name__, self.id)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __repr__(self):
        attrs = [
            '\'{}\': {}'.format(key, repr(getattr(self, key)))
            for key
            in self.__dict__
        ]

        return '\n{{\n\t{}\n}}'.format('\n\t'.join(attrs))


class SmartBnBResource(PrintableResource):

    @classmethod
    def list_url(cls, id=None):
        if id:
            return client.build_url(id)
        return client.build_url(None)

    def __init__(self, **kwargs):
        if 'access_token' in kwargs:
            self.access_token = kwargs['access_token']
        self.refresh_from(**kwargs)

    def refresh(self, **kwargs):
        if 'access_token' in kwargs:
            self.access_token = kwargs['access_token']
        self.refresh_from(**kwargs)

    def refresh_from(self, **kwargs):
        raise NotImplementedError

    @property
    def instance_url(self):
        return self.__class__.retrieve_url(self.id)

class SmartBnBOAuthResource(SmartBnBResource):

    @classmethod
    def list_url(cls, id=None):
        if id:
            return client.build_url(id)
        return client.build_url(None)

    def __init__(self, **kwargs):
        if not kwargs:
            kwargs = client.get_bearer_token()

        if 'access_token' in kwargs:
            # if kwargs['expires_at'] > time.time():
            #     print('Expirated of Access Token... Refreshing...')
            #     kwargs = client.get_bearer_token()
            self.access_token = kwargs['access_token']
        super(SmartBnBOAuthResource, self).__init__(**kwargs)

    def __unicode__(self):
        return '<SmartBnB::{} {} at OAuth {}>'.format(
            self.__class__.__name__,
            self.access_token,
        )
