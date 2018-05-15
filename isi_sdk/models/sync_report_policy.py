# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 6
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk_8_1_1.models.sync_job_policy_file_matching_pattern import SyncJobPolicyFileMatchingPattern  # noqa: F401,E501


class SyncReportPolicy(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'action': 'str',
        'file_matching_pattern': 'SyncJobPolicyFileMatchingPattern',
        'name': 'str',
        'source_exclude_directories': 'list[str]',
        'source_include_directories': 'list[str]',
        'source_root_path': 'str',
        'target_host': 'str',
        'target_path': 'str'
    }

    attribute_map = {
        'action': 'action',
        'file_matching_pattern': 'file_matching_pattern',
        'name': 'name',
        'source_exclude_directories': 'source_exclude_directories',
        'source_include_directories': 'source_include_directories',
        'source_root_path': 'source_root_path',
        'target_host': 'target_host',
        'target_path': 'target_path'
    }

    def __init__(self, action=None, file_matching_pattern=None, name=None, source_exclude_directories=None, source_include_directories=None, source_root_path=None, target_host=None, target_path=None):  # noqa: E501
        """SyncReportPolicy - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._file_matching_pattern = None
        self._name = None
        self._source_exclude_directories = None
        self._source_include_directories = None
        self._source_root_path = None
        self._target_host = None
        self._target_path = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if file_matching_pattern is not None:
            self.file_matching_pattern = file_matching_pattern
        if name is not None:
            self.name = name
        if source_exclude_directories is not None:
            self.source_exclude_directories = source_exclude_directories
        if source_include_directories is not None:
            self.source_include_directories = source_include_directories
        if source_root_path is not None:
            self.source_root_path = source_root_path
        if target_host is not None:
            self.target_host = target_host
        if target_path is not None:
            self.target_path = target_path

    @property
    def action(self):
        """Gets the action of this SyncReportPolicy.  # noqa: E501

        If 'copy', source files will be copied to the target cluster.  If 'sync', the target directory will be made an image of the source directory:  Files and directories that have been deleted on the source, have been moved within the target directory, or no longer match the selection criteria will be deleted from the target directory.  # noqa: E501

        :return: The action of this SyncReportPolicy.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this SyncReportPolicy.

        If 'copy', source files will be copied to the target cluster.  If 'sync', the target directory will be made an image of the source directory:  Files and directories that have been deleted on the source, have been moved within the target directory, or no longer match the selection criteria will be deleted from the target directory.  # noqa: E501

        :param action: The action of this SyncReportPolicy.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def file_matching_pattern(self):
        """Gets the file_matching_pattern of this SyncReportPolicy.  # noqa: E501

        A file matching pattern, organized as an OR'ed set of AND'ed file criteria, for example ((a AND b) OR (x AND y)) used to define a set of files with specific properties.  Policies of type 'sync' cannot use 'path' or time criteria in their matching patterns, but policies of type 'copy' can use all listed criteria.  # noqa: E501

        :return: The file_matching_pattern of this SyncReportPolicy.  # noqa: E501
        :rtype: SyncJobPolicyFileMatchingPattern
        """
        return self._file_matching_pattern

    @file_matching_pattern.setter
    def file_matching_pattern(self, file_matching_pattern):
        """Sets the file_matching_pattern of this SyncReportPolicy.

        A file matching pattern, organized as an OR'ed set of AND'ed file criteria, for example ((a AND b) OR (x AND y)) used to define a set of files with specific properties.  Policies of type 'sync' cannot use 'path' or time criteria in their matching patterns, but policies of type 'copy' can use all listed criteria.  # noqa: E501

        :param file_matching_pattern: The file_matching_pattern of this SyncReportPolicy.  # noqa: E501
        :type: SyncJobPolicyFileMatchingPattern
        """

        self._file_matching_pattern = file_matching_pattern

    @property
    def name(self):
        """Gets the name of this SyncReportPolicy.  # noqa: E501

        User-assigned name of this sync policy.  # noqa: E501

        :return: The name of this SyncReportPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SyncReportPolicy.

        User-assigned name of this sync policy.  # noqa: E501

        :param name: The name of this SyncReportPolicy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def source_exclude_directories(self):
        """Gets the source_exclude_directories of this SyncReportPolicy.  # noqa: E501

        Directories that will be excluded from the sync.  Modifying this field will result in a full synchronization of all data.  # noqa: E501

        :return: The source_exclude_directories of this SyncReportPolicy.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_exclude_directories

    @source_exclude_directories.setter
    def source_exclude_directories(self, source_exclude_directories):
        """Sets the source_exclude_directories of this SyncReportPolicy.

        Directories that will be excluded from the sync.  Modifying this field will result in a full synchronization of all data.  # noqa: E501

        :param source_exclude_directories: The source_exclude_directories of this SyncReportPolicy.  # noqa: E501
        :type: list[str]
        """

        self._source_exclude_directories = source_exclude_directories

    @property
    def source_include_directories(self):
        """Gets the source_include_directories of this SyncReportPolicy.  # noqa: E501

        Directories that will be included in the sync.  Modifying this field will result in a full synchronization of all data.  # noqa: E501

        :return: The source_include_directories of this SyncReportPolicy.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_include_directories

    @source_include_directories.setter
    def source_include_directories(self, source_include_directories):
        """Sets the source_include_directories of this SyncReportPolicy.

        Directories that will be included in the sync.  Modifying this field will result in a full synchronization of all data.  # noqa: E501

        :param source_include_directories: The source_include_directories of this SyncReportPolicy.  # noqa: E501
        :type: list[str]
        """

        self._source_include_directories = source_include_directories

    @property
    def source_root_path(self):
        """Gets the source_root_path of this SyncReportPolicy.  # noqa: E501

        The root directory on the source cluster the files will be synced from.  Modifying this field will result in a full synchronization of all data.  # noqa: E501

        :return: The source_root_path of this SyncReportPolicy.  # noqa: E501
        :rtype: str
        """
        return self._source_root_path

    @source_root_path.setter
    def source_root_path(self, source_root_path):
        """Sets the source_root_path of this SyncReportPolicy.

        The root directory on the source cluster the files will be synced from.  Modifying this field will result in a full synchronization of all data.  # noqa: E501

        :param source_root_path: The source_root_path of this SyncReportPolicy.  # noqa: E501
        :type: str
        """

        self._source_root_path = source_root_path

    @property
    def target_host(self):
        """Gets the target_host of this SyncReportPolicy.  # noqa: E501

        Hostname or IP address of sync target cluster.  Modifying the target cluster host can result in the policy being unrunnable if the new target does not match the current target association.  # noqa: E501

        :return: The target_host of this SyncReportPolicy.  # noqa: E501
        :rtype: str
        """
        return self._target_host

    @target_host.setter
    def target_host(self, target_host):
        """Sets the target_host of this SyncReportPolicy.

        Hostname or IP address of sync target cluster.  Modifying the target cluster host can result in the policy being unrunnable if the new target does not match the current target association.  # noqa: E501

        :param target_host: The target_host of this SyncReportPolicy.  # noqa: E501
        :type: str
        """

        self._target_host = target_host

    @property
    def target_path(self):
        """Gets the target_path of this SyncReportPolicy.  # noqa: E501

        Absolute filesystem path on the target cluster for the sync destination.  # noqa: E501

        :return: The target_path of this SyncReportPolicy.  # noqa: E501
        :rtype: str
        """
        return self._target_path

    @target_path.setter
    def target_path(self, target_path):
        """Sets the target_path of this SyncReportPolicy.

        Absolute filesystem path on the target cluster for the sync destination.  # noqa: E501

        :param target_path: The target_path of this SyncReportPolicy.  # noqa: E501
        :type: str
        """

        self._target_path = target_path

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SyncReportPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
