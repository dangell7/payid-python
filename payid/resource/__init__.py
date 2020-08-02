from __future__ import unicode_literals
from protocols.payid import client
from protocols.payid.util import read_json
from basedir import basedir


class PrintableResource(object):

    def __unicode__(self):
        return '<PayID::{} {}>'.format(self.__class__.__name__, self.id)

    def __str__(self):
        return str(self.encode('utf-8'))

    def __repr__(self):
        attrs = [
            '\'{}\': {}'.format(key, repr(getattr(self, key)))
            for key
            in self.__dict__
        ]

        return '\n{{\n\t{}\n}}'.format('\n\t'.join(attrs))


class PayIDPublicResource(PrintableResource):

    @classmethod
    def list_url(cls):
        return client.build_url(None)

    @classmethod
    def retrieve_url(cls, payID):
        return cls.list_url() + payID

    @classmethod
    def get(cls, payID, protocol):
        res = client.get(cls.retrieve_url(payID), protocol)
        return cls(**res)

    def __init__(self, **kwargs):
        self.refresh_from(**kwargs)

    def refresh(self):
        print(self.instance_url)
        res = client.get(self.instance_url)
        return self.refresh_from(**res)

    def refresh_from(self, **kwargs):
        raise NotImplementedError

    @property
    def instance_url(self):
        return self.__class__.retrieve_url(self.payID)


class PayIDPrivateResource(PayIDPublicResource):

    @classmethod
    def list_url(cls):
        return client.build_private_url('users/')

    @classmethod
    def retrieve_url(cls, payID):
        return cls.list_url() + payID + '/'

    @classmethod
    def get(cls, payID):
        res = client.private_get(cls.retrieve_url(payID))
        return cls(**res)

    @classmethod
    def post(cls, data):
        res = client.private_post(cls.list_url(), data)
        return cls(**res)

    @classmethod
    def put(cls, payID, data):
        res = client.private_put(cls.retrieve_url(payID), data)
        return cls(**res)

    @classmethod
    def patch(cls, payID, data):
        res = client.private_patch(cls.retrieve_url(payID), data)
        return cls(**res)

    @classmethod
    def delete(cls, payID):
        res = client.private_delete(cls.retrieve_url(payID))
        return cls(**res)

    def __init__(self, **kwargs):
        super(PayIDPrivateResource, self).__init__(**kwargs)

    @property
    def instance_url(self):
        return self.__class__.retrieve_url(self.payID)

    def __unicode__(self):
        return '<PayID::{} {} at User {}>'.format(
            self.__class__.__name__,
            self.payID
        )
