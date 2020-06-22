from unittest import TestCase

import guesty

class BaseTestConfig(TestCase):

    client_id = ''
    client_secret = ''
    version = 'v2'
    client = None

    def __main__():
        self.setUp()

    def setUp(self):
        print('Set Up Testing Auth')
        guesty.env = 'Prod'
        guesty.api_client_id = self.client_id
        guesty.api_client_secret = self.client_secret
        guesty.api_version = self.version
        self.guesty_auth()

    def guesty_auth(self):
        self.client = guesty.Account()
        self.assertNotEqual(self.client, None)
        self.assertEqual(self.client.scope, 'read:calendar write:calendar')
        self.assertEqual(self.client.expires_in, 86400)
        self.assertEqual(self.client.token_type, 'Bearer')

    def tearDown(self):
        print('Tear Down')
