from testing_config import BaseTestConfig
import pytest

import smartbnb

# @pytest.mark.skip(reason="Using Prod Cert")
class TestSmartBNBProperty(BaseTestConfig):

    '''
    Test Property Objects
    '''

    def test_smartbnb_get_property(self):
        property = self.client.get_property('327154')
        self.assertNotEqual(property.to_any_object(), {})
        self.assertEqual(property.id, '327154')
        print(e)

    @pytest.mark.skip(reason="Using Prod Cert")
    def test_smartbnb_properties(self):
        properties = self.client.properties
        self.assertNotEqual(len(properties), 0)
        # print(e)
