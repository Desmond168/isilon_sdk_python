# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 6
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_1_1
from isi_sdk_8_1_1.api.protocols_hdfs_api import ProtocolsHdfsApi  # noqa: E501
from isi_sdk_8_1_1.rest import ApiException


class TestProtocolsHdfsApi(unittest.TestCase):
    """ProtocolsHdfsApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_1_1.api.protocols_hdfs_api.ProtocolsHdfsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_proxyusers_name_member(self):
        """Test case for create_proxyusers_name_member

        """
        pass

    def test_delete_proxyusers_name_member(self):
        """Test case for delete_proxyusers_name_member

        """
        pass

    def test_list_proxyusers_name_members(self):
        """Test case for list_proxyusers_name_members

        """
        pass

    def test_update_proxyusers_name_member(self):
        """Test case for update_proxyusers_name_member

        """
        pass


if __name__ == '__main__':
    unittest.main()
