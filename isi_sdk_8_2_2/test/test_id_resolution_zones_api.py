# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 9
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_2_2
from isi_sdk_8_2_2.api.id_resolution_zones_api import IdResolutionZonesApi  # noqa: E501
from isi_sdk_8_2_2.rest import ApiException


class TestIdResolutionZonesApi(unittest.TestCase):
    """IdResolutionZonesApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_2_2.api.id_resolution_zones_api.IdResolutionZonesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_zone_group(self):
        """Test case for get_zone_group

        """
        pass

    def test_get_zone_groups(self):
        """Test case for get_zone_groups

        """
        pass

    def test_get_zone_user(self):
        """Test case for get_zone_user

        """
        pass

    def test_get_zone_users(self):
        """Test case for get_zone_users

        """
        pass


if __name__ == '__main__':
    unittest.main()
