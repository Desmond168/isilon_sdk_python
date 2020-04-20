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
from isi_sdk_8_2_2.api.auth_groups_api import AuthGroupsApi  # noqa: E501
from isi_sdk_8_2_2.rest import ApiException


class TestAuthGroupsApi(unittest.TestCase):
    """AuthGroupsApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_2_2.api.auth_groups_api.AuthGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_group_member(self):
        """Test case for create_group_member

        """
        pass

    def test_delete_group_member(self):
        """Test case for delete_group_member

        """
        pass

    def test_list_group_members(self):
        """Test case for list_group_members

        """
        pass


if __name__ == '__main__':
    unittest.main()
