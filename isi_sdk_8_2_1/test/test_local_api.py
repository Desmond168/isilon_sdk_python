# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 8
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_2_1
from isi_sdk_8_2_1.api.local_api import LocalApi  # noqa: E501
from isi_sdk_8_2_1.rest import ApiException


class TestLocalApi(unittest.TestCase):
    """LocalApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_2_1.api.local_api.LocalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_cluster_time(self):
        """Test case for get_cluster_time

        """
        pass

    def test_get_upgrade_cluster_firmware_status(self):
        """Test case for get_upgrade_cluster_firmware_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
