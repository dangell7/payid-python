
from protocols.payid.resource import (
    PayIDPublicResource,
    PayIDPrivateResource,
)


class Public(PayIDPublicResource):

    def refresh_from(self, **kwargs):
        print(kwargs)
        self.payId = kwargs['payId']
        self.addresses = kwargs['addresses']

    def __unicode__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.payID)


class Private(PayIDPrivateResource):

    def refresh_from(self, **kwargs):
        print(kwargs)
        self.payId = kwargs['payId']
        # self.memo = kwargs['memo']
        self.addresses = kwargs['addresses']

    def __unicode__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.payID)
