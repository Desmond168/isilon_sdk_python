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
from isi_sdk_8_1_1.api.dedupe_api import DedupeApi  # noqa: E501
from isi_sdk_8_1_1.rest import ApiException


class TestDedupeApi(unittest.TestCase):
    """DedupeApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_1_1.api.dedupe_api.DedupeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_dedupe_dedupe_summary(self):
        """Test case for get_dedupe_dedupe_summary

        """
        pass

    def test_get_dedupe_report(self):
        """Test case for get_dedupe_report

        """
        pass

    def test_get_dedupe_reports(self):
        """Test case for get_dedupe_reports

        """
        pass

    def test_get_dedupe_settings(self):
        """Test case for get_dedupe_settings

        """
        pass

    def test_update_dedupe_settings(self):
        """Test case for update_dedupe_settings

        """
        pass


if __name__ == '__main__':
    unittest.main()
