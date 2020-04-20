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
from isi_sdk_8_1_1.api.statistics_api import StatisticsApi  # noqa: E501
from isi_sdk_8_1_1.rest import ApiException


class TestStatisticsApi(unittest.TestCase):
    """StatisticsApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_1_1.api.statistics_api.StatisticsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_statistics_current(self):
        """Test case for get_statistics_current

        """
        pass

    def test_get_statistics_history(self):
        """Test case for get_statistics_history

        """
        pass

    def test_get_statistics_key(self):
        """Test case for get_statistics_key

        """
        pass

    def test_get_statistics_keys(self):
        """Test case for get_statistics_keys

        """
        pass

    def test_get_statistics_operations(self):
        """Test case for get_statistics_operations

        """
        pass

    def test_get_statistics_protocols(self):
        """Test case for get_statistics_protocols

        """
        pass

    def test_get_summary_client(self):
        """Test case for get_summary_client

        """
        pass

    def test_get_summary_drive(self):
        """Test case for get_summary_drive

        """
        pass

    def test_get_summary_heat(self):
        """Test case for get_summary_heat

        """
        pass

    def test_get_summary_protocol(self):
        """Test case for get_summary_protocol

        """
        pass

    def test_get_summary_protocol_stats(self):
        """Test case for get_summary_protocol_stats

        """
        pass

    def test_get_summary_system(self):
        """Test case for get_summary_system

        """
        pass

    def test_get_summary_workload(self):
        """Test case for get_summary_workload

        """
        pass


if __name__ == '__main__':
    unittest.main()
