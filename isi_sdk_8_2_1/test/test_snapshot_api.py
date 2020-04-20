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
from isi_sdk_8_2_1.api.snapshot_api import SnapshotApi  # noqa: E501
from isi_sdk_8_2_1.rest import ApiException


class TestSnapshotApi(unittest.TestCase):
    """SnapshotApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_2_1.api.snapshot_api.SnapshotApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_snapshot_alias(self):
        """Test case for create_snapshot_alias

        """
        pass

    def test_create_snapshot_schedule(self):
        """Test case for create_snapshot_schedule

        """
        pass

    def test_create_snapshot_snapshot(self):
        """Test case for create_snapshot_snapshot

        """
        pass

    def test_delete_snapshot_alias(self):
        """Test case for delete_snapshot_alias

        """
        pass

    def test_delete_snapshot_aliases(self):
        """Test case for delete_snapshot_aliases

        """
        pass

    def test_delete_snapshot_changelist(self):
        """Test case for delete_snapshot_changelist

        """
        pass

    def test_delete_snapshot_repstate(self):
        """Test case for delete_snapshot_repstate

        """
        pass

    def test_delete_snapshot_schedule(self):
        """Test case for delete_snapshot_schedule

        """
        pass

    def test_delete_snapshot_schedules(self):
        """Test case for delete_snapshot_schedules

        """
        pass

    def test_delete_snapshot_snapshot(self):
        """Test case for delete_snapshot_snapshot

        """
        pass

    def test_delete_snapshot_snapshots(self):
        """Test case for delete_snapshot_snapshots

        """
        pass

    def test_get_snapshot_alias(self):
        """Test case for get_snapshot_alias

        """
        pass

    def test_get_snapshot_changelist(self):
        """Test case for get_snapshot_changelist

        """
        pass

    def test_get_snapshot_changelists(self):
        """Test case for get_snapshot_changelists

        """
        pass

    def test_get_snapshot_license(self):
        """Test case for get_snapshot_license

        """
        pass

    def test_get_snapshot_pending(self):
        """Test case for get_snapshot_pending

        """
        pass

    def test_get_snapshot_repstate(self):
        """Test case for get_snapshot_repstate

        """
        pass

    def test_get_snapshot_repstates(self):
        """Test case for get_snapshot_repstates

        """
        pass

    def test_get_snapshot_schedule(self):
        """Test case for get_snapshot_schedule

        """
        pass

    def test_get_snapshot_settings(self):
        """Test case for get_snapshot_settings

        """
        pass

    def test_get_snapshot_snapshot(self):
        """Test case for get_snapshot_snapshot

        """
        pass

    def test_get_snapshot_snapshots_summary(self):
        """Test case for get_snapshot_snapshots_summary

        """
        pass

    def test_list_snapshot_aliases(self):
        """Test case for list_snapshot_aliases

        """
        pass

    def test_list_snapshot_schedules(self):
        """Test case for list_snapshot_schedules

        """
        pass

    def test_list_snapshot_snapshots(self):
        """Test case for list_snapshot_snapshots

        """
        pass

    def test_update_snapshot_alias(self):
        """Test case for update_snapshot_alias

        """
        pass

    def test_update_snapshot_schedule(self):
        """Test case for update_snapshot_schedule

        """
        pass

    def test_update_snapshot_settings(self):
        """Test case for update_snapshot_settings

        """
        pass

    def test_update_snapshot_snapshot(self):
        """Test case for update_snapshot_snapshot

        """
        pass


if __name__ == '__main__':
    unittest.main()
