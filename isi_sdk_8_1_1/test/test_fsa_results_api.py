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
from isi_sdk_8_1_1.api.fsa_results_api import FsaResultsApi  # noqa: E501
from isi_sdk_8_1_1.rest import ApiException


class TestFsaResultsApi(unittest.TestCase):
    """FsaResultsApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_1_1.api.fsa_results_api.FsaResultsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_histogram_stat_by(self):
        """Test case for get_histogram_stat_by

        """
        pass

    def test_get_histogram_stat_by_breakout(self):
        """Test case for get_histogram_stat_by_breakout

        """
        pass

    def test_get_result_directories(self):
        """Test case for get_result_directories

        """
        pass

    def test_get_result_directory(self):
        """Test case for get_result_directory

        """
        pass

    def test_get_result_histogram(self):
        """Test case for get_result_histogram

        """
        pass

    def test_get_result_histogram_stat(self):
        """Test case for get_result_histogram_stat

        """
        pass

    def test_get_result_top_dir(self):
        """Test case for get_result_top_dir

        """
        pass

    def test_get_result_top_dirs(self):
        """Test case for get_result_top_dirs

        """
        pass

    def test_get_result_top_file(self):
        """Test case for get_result_top_file

        """
        pass

    def test_get_result_top_files(self):
        """Test case for get_result_top_files

        """
        pass


if __name__ == '__main__':
    unittest.main()
