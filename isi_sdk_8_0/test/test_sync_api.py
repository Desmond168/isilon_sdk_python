# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 3
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_0
from isi_sdk_8_0.api.sync_api import SyncApi  # noqa: E501
from isi_sdk_8_0.rest import ApiException


class TestSyncApi(unittest.TestCase):
    """SyncApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_0.api.sync_api.SyncApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_sync_job(self):
        """Test case for create_sync_job

        """
        pass

    def test_create_sync_policy(self):
        """Test case for create_sync_policy

        """
        pass

    def test_create_sync_reports_rotate_item(self):
        """Test case for create_sync_reports_rotate_item

        """
        pass

    def test_create_sync_rule(self):
        """Test case for create_sync_rule

        """
        pass

    def test_delete_sync_policies(self):
        """Test case for delete_sync_policies

        """
        pass

    def test_delete_sync_policy(self):
        """Test case for delete_sync_policy

        """
        pass

    def test_delete_sync_rule(self):
        """Test case for delete_sync_rule

        """
        pass

    def test_delete_sync_rules(self):
        """Test case for delete_sync_rules

        """
        pass

    def test_delete_target_policy(self):
        """Test case for delete_target_policy

        """
        pass

    def test_get_history_cpu(self):
        """Test case for get_history_cpu

        """
        pass

    def test_get_history_file(self):
        """Test case for get_history_file

        """
        pass

    def test_get_history_network(self):
        """Test case for get_history_network

        """
        pass

    def test_get_history_worker(self):
        """Test case for get_history_worker

        """
        pass

    def test_get_sync_job(self):
        """Test case for get_sync_job

        """
        pass

    def test_get_sync_license(self):
        """Test case for get_sync_license

        """
        pass

    def test_get_sync_policy(self):
        """Test case for get_sync_policy

        """
        pass

    def test_get_sync_report(self):
        """Test case for get_sync_report

        """
        pass

    def test_get_sync_reports(self):
        """Test case for get_sync_reports

        """
        pass

    def test_get_sync_rule(self):
        """Test case for get_sync_rule

        """
        pass

    def test_get_sync_settings(self):
        """Test case for get_sync_settings

        """
        pass

    def test_get_target_policies(self):
        """Test case for get_target_policies

        """
        pass

    def test_get_target_policy(self):
        """Test case for get_target_policy

        """
        pass

    def test_get_target_report(self):
        """Test case for get_target_report

        """
        pass

    def test_get_target_reports(self):
        """Test case for get_target_reports

        """
        pass

    def test_list_sync_jobs(self):
        """Test case for list_sync_jobs

        """
        pass

    def test_list_sync_policies(self):
        """Test case for list_sync_policies

        """
        pass

    def test_list_sync_reports_rotate(self):
        """Test case for list_sync_reports_rotate

        """
        pass

    def test_list_sync_rules(self):
        """Test case for list_sync_rules

        """
        pass

    def test_update_sync_job(self):
        """Test case for update_sync_job

        """
        pass

    def test_update_sync_policy(self):
        """Test case for update_sync_policy

        """
        pass

    def test_update_sync_rule(self):
        """Test case for update_sync_rule

        """
        pass

    def test_update_sync_settings(self):
        """Test case for update_sync_settings

        """
        pass


if __name__ == '__main__':
    unittest.main()
