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
from isi_sdk_8_2_2.api.sync_service_api import SyncServiceApi  # noqa: E501
from isi_sdk_8_2_2.rest import ApiException


class TestSyncServiceApi(unittest.TestCase):
    """SyncServiceApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_2_2.api.sync_service_api.SyncServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_policies_policy_reset_item(self):
        """Test case for create_policies_policy_reset_item

        """
        pass


if __name__ == '__main__':
    unittest.main()
