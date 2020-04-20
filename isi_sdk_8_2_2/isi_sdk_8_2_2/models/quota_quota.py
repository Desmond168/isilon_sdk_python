# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 9
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk_8_2_2.models.quota_quota_thresholds import QuotaQuotaThresholds  # noqa: F401,E501


class QuotaQuota(object):
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
        'container': 'bool',
        'enforced': 'bool',
        'force': 'bool',
        'ignore_limit_checks': 'bool',
        'linked': 'bool',
        'thresholds': 'QuotaQuotaThresholds',
        'thresholds_include_overhead': 'bool',
        'thresholds_on': 'str'
    }

    attribute_map = {
        'container': 'container',
        'enforced': 'enforced',
        'force': 'force',
        'ignore_limit_checks': 'ignore_limit_checks',
        'linked': 'linked',
        'thresholds': 'thresholds',
        'thresholds_include_overhead': 'thresholds_include_overhead',
        'thresholds_on': 'thresholds_on'
    }

    def __init__(self, container=None, enforced=None, force=None, ignore_limit_checks=None, linked=None, thresholds=None, thresholds_include_overhead=None, thresholds_on='fslogicalsize'):  # noqa: E501
        """QuotaQuota - a model defined in Swagger"""  # noqa: E501

        self._container = None
        self._enforced = None
        self._force = None
        self._ignore_limit_checks = None
        self._linked = None
        self._thresholds = None
        self._thresholds_include_overhead = None
        self._thresholds_on = None
        self.discriminator = None

        if container is not None:
            self.container = container
        if enforced is not None:
            self.enforced = enforced
        if force is not None:
            self.force = force
        if ignore_limit_checks is not None:
            self.ignore_limit_checks = ignore_limit_checks
        if linked is not None:
            self.linked = linked
        if thresholds is not None:
            self.thresholds = thresholds
        if thresholds_include_overhead is not None:
            self.thresholds_include_overhead = thresholds_include_overhead
        if thresholds_on is not None:
            self.thresholds_on = thresholds_on

    @property
    def container(self):
        """Gets the container of this QuotaQuota.  # noqa: E501

        If true, SMB shares using the quota directory see the quota thresholds as share size.  # noqa: E501

        :return: The container of this QuotaQuota.  # noqa: E501
        :rtype: bool
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this QuotaQuota.

        If true, SMB shares using the quota directory see the quota thresholds as share size.  # noqa: E501

        :param container: The container of this QuotaQuota.  # noqa: E501
        :type: bool
        """

        self._container = container

    @property
    def enforced(self):
        """Gets the enforced of this QuotaQuota.  # noqa: E501

        True if the quota provides enforcement, otherwise an accounting quota.  # noqa: E501

        :return: The enforced of this QuotaQuota.  # noqa: E501
        :rtype: bool
        """
        return self._enforced

    @enforced.setter
    def enforced(self, enforced):
        """Sets the enforced of this QuotaQuota.

        True if the quota provides enforcement, otherwise an accounting quota.  # noqa: E501

        :param enforced: The enforced of this QuotaQuota.  # noqa: E501
        :type: bool
        """

        self._enforced = enforced

    @property
    def force(self):
        """Gets the force of this QuotaQuota.  # noqa: E501

        Force creation of quotas on the root of /ifs or percent based quotas.  # noqa: E501

        :return: The force of this QuotaQuota.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this QuotaQuota.

        Force creation of quotas on the root of /ifs or percent based quotas.  # noqa: E501

        :param force: The force of this QuotaQuota.  # noqa: E501
        :type: bool
        """

        self._force = force

    @property
    def ignore_limit_checks(self):
        """Gets the ignore_limit_checks of this QuotaQuota.  # noqa: E501

        If true, skip child quota's threshold comparison with parent quota path.  # noqa: E501

        :return: The ignore_limit_checks of this QuotaQuota.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_limit_checks

    @ignore_limit_checks.setter
    def ignore_limit_checks(self, ignore_limit_checks):
        """Sets the ignore_limit_checks of this QuotaQuota.

        If true, skip child quota's threshold comparison with parent quota path.  # noqa: E501

        :param ignore_limit_checks: The ignore_limit_checks of this QuotaQuota.  # noqa: E501
        :type: bool
        """

        self._ignore_limit_checks = ignore_limit_checks

    @property
    def linked(self):
        """Gets the linked of this QuotaQuota.  # noqa: E501

        If false and the quota is linked, attempt to unlink.  # noqa: E501

        :return: The linked of this QuotaQuota.  # noqa: E501
        :rtype: bool
        """
        return self._linked

    @linked.setter
    def linked(self, linked):
        """Sets the linked of this QuotaQuota.

        If false and the quota is linked, attempt to unlink.  # noqa: E501

        :param linked: The linked of this QuotaQuota.  # noqa: E501
        :type: bool
        """

        self._linked = linked

    @property
    def thresholds(self):
        """Gets the thresholds of this QuotaQuota.  # noqa: E501

          # noqa: E501

        :return: The thresholds of this QuotaQuota.  # noqa: E501
        :rtype: QuotaQuotaThresholds
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this QuotaQuota.

          # noqa: E501

        :param thresholds: The thresholds of this QuotaQuota.  # noqa: E501
        :type: QuotaQuotaThresholds
        """

        self._thresholds = thresholds

    @property
    def thresholds_include_overhead(self):
        """Gets the thresholds_include_overhead of this QuotaQuota.  # noqa: E501

        This option is deprecated. Use the option 'thresholds_on' to select the usage on which thresholds to apply.  # noqa: E501

        :return: The thresholds_include_overhead of this QuotaQuota.  # noqa: E501
        :rtype: bool
        """
        return self._thresholds_include_overhead

    @thresholds_include_overhead.setter
    def thresholds_include_overhead(self, thresholds_include_overhead):
        """Sets the thresholds_include_overhead of this QuotaQuota.

        This option is deprecated. Use the option 'thresholds_on' to select the usage on which thresholds to apply.  # noqa: E501

        :param thresholds_include_overhead: The thresholds_include_overhead of this QuotaQuota.  # noqa: E501
        :type: bool
        """

        self._thresholds_include_overhead = thresholds_include_overhead

    @property
    def thresholds_on(self):
        """Gets the thresholds_on of this QuotaQuota.  # noqa: E501

        Thresholds apply on quota accounting metric.  # noqa: E501

        :return: The thresholds_on of this QuotaQuota.  # noqa: E501
        :rtype: str
        """
        return self._thresholds_on

    @thresholds_on.setter
    def thresholds_on(self, thresholds_on):
        """Sets the thresholds_on of this QuotaQuota.

        Thresholds apply on quota accounting metric.  # noqa: E501

        :param thresholds_on: The thresholds_on of this QuotaQuota.  # noqa: E501
        :type: str
        """
        allowed_values = ["applogicalsize", "fslogicalsize", "physicalsize"]  # noqa: E501
        if thresholds_on not in allowed_values:
            raise ValueError(
                "Invalid value for `thresholds_on` ({0}), must be one of {1}"  # noqa: E501
                .format(thresholds_on, allowed_values)
            )

        self._thresholds_on = thresholds_on

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
        if not isinstance(other, QuotaQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
