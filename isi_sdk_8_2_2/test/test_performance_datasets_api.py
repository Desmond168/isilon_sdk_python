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
from isi_sdk_8_2_2.api.performance_datasets_api import PerformanceDatasetsApi  # noqa: E501
from isi_sdk_8_2_2.rest import ApiException


class TestPerformanceDatasetsApi(unittest.TestCase):
    """PerformanceDatasetsApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_2_2.api.performance_datasets_api.PerformanceDatasetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_dataset_filter(self):
        """Test case for create_dataset_filter

        """
        pass

    def test_create_dataset_workload(self):
        """Test case for create_dataset_workload

        """
        pass

    def test_delete_dataset_filter(self):
        """Test case for delete_dataset_filter

        """
        pass

    def test_delete_dataset_filters(self):
        """Test case for delete_dataset_filters

        """
        pass

    def test_delete_dataset_workload(self):
        """Test case for delete_dataset_workload

        """
        pass

    def test_delete_dataset_workloads(self):
        """Test case for delete_dataset_workloads

        """
        pass

    def test_get_dataset_filter(self):
        """Test case for get_dataset_filter

        """
        pass

    def test_get_dataset_workload(self):
        """Test case for get_dataset_workload

        """
        pass

    def test_list_dataset_filters(self):
        """Test case for list_dataset_filters

        """
        pass

    def test_list_dataset_workloads(self):
        """Test case for list_dataset_workloads

        """
        pass

    def test_update_dataset_filter(self):
        """Test case for update_dataset_filter

        """
        pass

    def test_update_dataset_workload(self):
        """Test case for update_dataset_workload

        """
        pass


if __name__ == '__main__':
    unittest.main()
