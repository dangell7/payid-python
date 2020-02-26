from unittest import TestCase

import smartbnb

class BaseTestConfig(TestCase):

    client_id = ''
    client_secret = ''
    version = 'v2'
    client = None

    def __main__():
        self.setUp()

    def setUp(self):
        print('Set Up Testing Auth')
        smartbnb.env = 'Prod'
        smartbnb.api_client_id = self.client_id
        smartbnb.api_client_secret = self.client_secret
        smartbnb.api_version = self.version
        self.smartbnb_auth()

    def smartbnb_auth(self):
        self.client = smartbnb.AccountOAuth()
        self.assertNotEqual(self.client, None)
        self.assertEqual(self.client.scope, 'read:calendar write:calendar')
        self.assertEqual(self.client.expires_in, 86400)
        self.assertEqual(self.client.token_type, 'Bearer')

    def tearDown(self):
        print('Tear Down')
