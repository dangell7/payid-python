from testing_config import BaseTestConfig
import pytest


@pytest.mark.skip(reason="Using Prod Cert")
class TestPayIDSDK(BaseTestConfig):

    '''
    Test sdk
    '''

    @pytest.mark.skip(reason="Using Prod Cert")
    def test_payid_get_user(self):
        user = self.client.get_property('alice')
        self.assertNotEqual(user.to_any_object(), {})
        self.assertEqual(user.payID, 'alice$127.0.0.1')
