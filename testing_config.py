from unittest import TestCase

import payid

class BaseTestConfig(TestCase):

    client_id = ''
    client_secret = ''
    version = 'v2'
    client = None

    def __main__():
        self.setUp()

    def setUp(self):
        print('Set Up Testing Auth')
        payid.env = 'Prod'
        payid.api_client_id = self.client_id
        payid.api_client_secret = self.client_secret
        payid.api_version = self.version
        self.payid_auth()

    def payid_auth(self):
        self.client = payid.Account()
        self.assertNotEqual(self.client, None)
        self.assertEqual(self.client.scope, 'read:calendar write:calendar')
        self.assertEqual(self.client.expires_in, 86400)
        self.assertEqual(self.client.token_type, 'Bearer')

    def tearDown(self):
        print('Tear Down')
