# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 4
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NetworkDnscacheExtended(object):
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
        'cache_entry_limit': 'int',
        'cluster_timeout': 'int',
        'dns_timeout': 'int',
        'eager_refresh': 'int',
        'testping_delta': 'int',
        'ttl_max_noerror': 'int',
        'ttl_max_nxdomain': 'int',
        'ttl_max_other': 'int',
        'ttl_max_servfail': 'int',
        'ttl_min_noerror': 'int',
        'ttl_min_nxdomain': 'int',
        'ttl_min_other': 'int',
        'ttl_min_servfail': 'int'
    }

    attribute_map = {
        'cache_entry_limit': 'cache_entry_limit',
        'cluster_timeout': 'cluster_timeout',
        'dns_timeout': 'dns_timeout',
        'eager_refresh': 'eager_refresh',
        'testping_delta': 'testping_delta',
        'ttl_max_noerror': 'ttl_max_noerror',
        'ttl_max_nxdomain': 'ttl_max_nxdomain',
        'ttl_max_other': 'ttl_max_other',
        'ttl_max_servfail': 'ttl_max_servfail',
        'ttl_min_noerror': 'ttl_min_noerror',
        'ttl_min_nxdomain': 'ttl_min_nxdomain',
        'ttl_min_other': 'ttl_min_other',
        'ttl_min_servfail': 'ttl_min_servfail'
    }

    def __init__(self, cache_entry_limit=None, cluster_timeout=None, dns_timeout=None, eager_refresh=None, testping_delta=None, ttl_max_noerror=None, ttl_max_nxdomain=None, ttl_max_other=None, ttl_max_servfail=None, ttl_min_noerror=None, ttl_min_nxdomain=None, ttl_min_other=None, ttl_min_servfail=None):  # noqa: E501
        """NetworkDnscacheExtended - a model defined in Swagger"""  # noqa: E501

        self._cache_entry_limit = None
        self._cluster_timeout = None
        self._dns_timeout = None
        self._eager_refresh = None
        self._testping_delta = None
        self._ttl_max_noerror = None
        self._ttl_max_nxdomain = None
        self._ttl_max_other = None
        self._ttl_max_servfail = None
        self._ttl_min_noerror = None
        self._ttl_min_nxdomain = None
        self._ttl_min_other = None
        self._ttl_min_servfail = None
        self.discriminator = None

        if cache_entry_limit is not None:
            self.cache_entry_limit = cache_entry_limit
        if cluster_timeout is not None:
            self.cluster_timeout = cluster_timeout
        if dns_timeout is not None:
            self.dns_timeout = dns_timeout
        if eager_refresh is not None:
            self.eager_refresh = eager_refresh
        if testping_delta is not None:
            self.testping_delta = testping_delta
        if ttl_max_noerror is not None:
            self.ttl_max_noerror = ttl_max_noerror
        if ttl_max_nxdomain is not None:
            self.ttl_max_nxdomain = ttl_max_nxdomain
        if ttl_max_other is not None:
            self.ttl_max_other = ttl_max_other
        if ttl_max_servfail is not None:
            self.ttl_max_servfail = ttl_max_servfail
        if ttl_min_noerror is not None:
            self.ttl_min_noerror = ttl_min_noerror
        if ttl_min_nxdomain is not None:
            self.ttl_min_nxdomain = ttl_min_nxdomain
        if ttl_min_other is not None:
            self.ttl_min_other = ttl_min_other
        if ttl_min_servfail is not None:
            self.ttl_min_servfail = ttl_min_servfail

    @property
    def cache_entry_limit(self):
        """Gets the cache_entry_limit of this NetworkDnscacheExtended.  # noqa: E501

        DNS cache entry limit  # noqa: E501

        :return: The cache_entry_limit of this NetworkDnscacheExtended.  # noqa: E501
        :rtype: int
        """
        return self._cache_entry_limit

    @cache_entry_limit.setter
    def cache_entry_limit(self, cache_entry_limit):
        """Sets the cache_entry_limit of this NetworkDnscacheExtended.

        DNS cache entry limit  # noqa: E501

        :param cache_entry_limit: The cache_entry_limit of this NetworkDnscacheExtended.  # noqa: E501
        :type: int
        """
        if cache_entry_limit is not None and cache_entry_limit > 1048576:  # noqa: E501
            raise ValueError("Invalid value for `cache_entry_limit`, must be a value less than or equal to `1048576`")  # noqa: E501
        if cache_entry_limit is not None and cache_entry_limit < 1024:  # noqa: E501
            raise ValueError("Invalid value for `cache_entry_limit`, must be a value greater than or equal to `1024`")  # noqa: E501

        self._cache_entry_limit = cache_entry_limit

    @property
    def cluster_timeout(self):
        """Gets the cluster_timeout of this NetworkDnscacheExtended.  # noqa: E501

        Timeout value for calls made to other nodes in the cluster  # noqa: E501

        :return: The cluster_timeout of this NetworkDnscacheExtended.  # noqa: E501
        :rtype: int
        """
        return self._cluster_timeout

    @cluster_timeout.setter
    def cluster_timeout(self, cluster_timeout):
        """Sets the cluster_timeout of this NetworkDnscacheExtended.

        Timeout value for calls made to other nodes in the cluster  # noqa: E501

        :param cluster_timeout: The cluster_timeout of this NetworkDnscacheExtended.  # noqa: E501
        :type: int
        """
        if cluster_timeout is not None and cluster_timeout > 30:  # noqa: E501
            raise ValueError("Invalid value for `cluster_timeout`, must be a value less than or equal to `30`")  # noqa: E501
        if cluster_timeout is not None and cluster_timeout < 1:  # noqa: E501
            raise ValueError("Invalid value for `cluster_timeout`, must be a value greater than or equal to `1`")  # noqa: E501

        self._cluster_timeout = cluster_timeout

    @property
    def dns_timeout(self):
        """Gets the dns_timeout of this NetworkDnscacheExtended.  # noqa: E501

        Timeout value for calls made to the dns resolvers  # noqa: E501

        :return: The dns_timeout of this NetworkDnscacheExtended.  # noqa: E501
        :rtype: int
        """
        return self._dns_timeout

    @dns_timeout.setter
    def dns_timeout(self, dns_timeout):
        """Sets the dns_timeout of this NetworkDnscacheExtended.

        Timeout value for calls made to the dns resolvers  # noqa: E501

        :param dns_timeout: The dns_timeout of this NetworkDnscacheExtended.  # noqa: E501
        :type: int
        """
        if dns_timeout is not None and dns_timeout > 30:  # noqa: E501
            raise ValueError("Invalid value for `dns_timeout`, must be a value less than or equal to `30`")  # noqa: E501
        if dns_timeout is not None and dns_timeout < 1:  # noqa: E501
            raise ValueError("Invalid value for `dns_timeout`, must be a value greater than or equal to `1`")  # noqa: E501

        self._dns_timeout = dns_timeout

    @property
    def eager_refresh(self):
        """Gets the eager_refresh of this NetworkDnscacheExtended.  # noqa: E501

        Lead time to refresh cache entries nearing expiration  # noqa: E501

        :return: The eager_refresh of this NetworkDnscacheExtended.  # noqa: E501
        :rtype: int
        """
        return self._eager_refresh

    @eager_refresh.setter
    def eager_refresh(self, eager_refresh):
        """Sets the eager_refresh of this NetworkDnscacheExtended.

        Lead time to refresh cache entries nearing expiration  # noqa: E501

        :param eager_refresh: The eager_refresh of this NetworkDnscacheExtended.  # noqa: E501
        :type: int
        """
        if eager_refresh is not None and eager_refresh > 60:  # noqa: E501
            raise ValueError("Invalid value for `eager_refresh`, must be a value less than or equal to `60`")  # noqa: E501
        if eager_refresh is not None and eager_refresh < 0:  # noqa: E501
            raise ValueError("Invalid value for `eager_refresh`, must be a value greater than or equal to `0`")  # noqa: E501

        self._eager_refresh = eager_refresh

    @property
    def testping_delta(self):
        """Gets the testping_delta of this NetworkDnscacheExtended.  # noqa: E501

        Deltas for checking cbind cluster health  # noqa: E501

        :return: The testping_delta of this NetworkDnscacheExtended.  # noqa: E501
        :rtype: int
        """
        return self._testping_delta

    @testping_delta.setter
    def testping_delta(self, testping_delta):
        """Sets the testping_delta of this NetworkDnscacheExtended.

        Deltas for checking cbind cluster health  # noqa: E501

        :param testping_delta: The testping_delta of this NetworkDnscacheExtended.  # noqa: E501
        :type: int
        """
        if testping_delta is not None and testping_delta > 60:  # noqa: E501
            raise ValueError("Invalid value for `testping_delta`, must be a value less than or equal to `60`")  # noqa: E501
        if testping_delta is not None and testping_delta < 0:  # noqa: E501
            raise ValueError("Invalid value for `testping_delta`, must be a value greater than or equal to `0`")  # noqa: E501

        self._testping_delta = testping_delta

    @property
    def ttl_max_noerror(self):
        """Gets the ttl_max_noerror of this NetworkDnscacheExtended.  # noqa: E501

        Upper bound on ttl for cache hits  # noqa: E501

        :return: The ttl_max_noerror of this NetworkDnscacheExtended.  # noqa: E501
        :rtype: int
        """
        return self._ttl_max_noerror

    @ttl_max_noerror.setter
    def ttl_max_noerror(self, ttl_max_noerror):
        """Sets the ttl_max_noerror of this NetworkDnscacheExtended.

        Upper bound on ttl for cache hits  # noqa: E501

        :param ttl_max_noerror: The ttl_max_noerror of this NetworkDnscacheExtended.  # noqa: E501
        :type: int
        """
        if ttl_max_noerror is not None and ttl_max_noerror > 3600:  # noqa: E501
            raise ValueError("Invalid value for `ttl_max_noerror`, must be a value less than or equal to `3600`")  # noqa: E501
        if ttl_max_noerror is not None and ttl_max_noerror < 0:  # noqa: E501
            raise ValueError("Invalid value for `ttl_max_noerror`, must be a value greater than or equal to `0`")  # noqa: E501

        self._ttl_max_noerror = ttl_max_noerror

    @property
    def ttl_max_nxdomain(self):
        """Gets the ttl_max_nxdomain of this NetworkDnscacheExtended.  # noqa: E501

        Upper bound on ttl for nxdomain  # noqa: E501

        :return: The ttl_max_nxdomain of this NetworkDnscacheExtended.  # noqa: E501
        :rtype: int
        """
        return self._ttl_max_nxdomain

    @ttl_max_nxdomain.setter
    def ttl_max_nxdomain(self, ttl_max_nxdomain):
        """Sets the ttl_max_nxdomain of this NetworkDnscacheExtended.

        Upper bound on ttl for nxdomain  # noqa: E501

        :param ttl_max_nxdomain: The ttl_max_nxdomain of this NetworkDnscacheExtended.  # noqa: E501
        :type: int
        """
        if ttl_max_nxdomain is not None and ttl_max_nxdomain > 3600:  # noqa: E501
            raise ValueError("Invalid value for `ttl_max_nxdomain`, must be a value less than or equal to `3600`")  # noqa: E501
        if ttl_max_nxdomain is not None and ttl_max_nxdomain < 0:  # noqa: E501
            raise ValueError("Invalid value for `ttl_max_nxdomain`, must be a value greater than or equal to `0`")  # noqa: E501

        self._ttl_max_nxdomain = ttl_max_nxdomain

    @property
    def ttl_max_other(self):
        """Gets the ttl_max_other of this NetworkDnscacheExtended.  # noqa: E501

        Upper bound on ttl for non-nxdomain failures  # noqa: E501

        :return: The ttl_max_other of this NetworkDnscacheExtended.  # noqa: E501
        :rtype: int
        """
        return self._ttl_max_other

    @ttl_max_other.setter
    def ttl_max_other(self, ttl_max_other):
        """Sets the ttl_max_other of this NetworkDnscacheExtended.

        Upper bound on ttl for non-nxdomain failures  # noqa: E501

        :param ttl_max_other: The ttl_max_other of this NetworkDnscacheExtended.  # noqa: E501
        :type: int
        """
        if ttl_max_other is not None and ttl_max_other > 3600:  # noqa: E501
            raise ValueError("Invalid value for `ttl_max_other`, must be a value less than or equal to `3600`")  # noqa: E501
        if ttl_max_other is not None and ttl_max_other < 0:  # noqa: E501
            raise ValueError("Invalid value for `ttl_max_other`, must be a value greater than or equal to `0`")  # noqa: E501

        self._ttl_max_other = ttl_max_other

    @property
    def ttl_max_servfail(self):
        """Gets the ttl_max_servfail of this NetworkDnscacheExtended.  # noqa: E501

        Upper bound on ttl for server failures  # noqa: E501

        :return: The ttl_max_servfail of this NetworkDnscacheExtended.  # noqa: E501
        :rtype: int
        """
        return self._ttl_max_servfail

    @ttl_max_servfail.setter
    def ttl_max_servfail(self, ttl_max_servfail):
        """Sets the ttl_max_servfail of this NetworkDnscacheExtended.

        Upper bound on ttl for server failures  # noqa: E501

        :param ttl_max_servfail: The ttl_max_servfail of this NetworkDnscacheExtended.  # noqa: E501
        :type: int
        """
        if ttl_max_servfail is not None and ttl_max_servfail > 3600:  # noqa: E501
            raise ValueError("Invalid value for `ttl_max_servfail`, must be a value less than or equal to `3600`")  # noqa: E501
        if ttl_max_servfail is not None and ttl_max_servfail < 0:  # noqa: E501
            raise ValueError("Invalid value for `ttl_max_servfail`, must be a value greater than or equal to `0`")  # noqa: E501

        self._ttl_max_servfail = ttl_max_servfail

    @property
    def ttl_min_noerror(self):
        """Gets the ttl_min_noerror of this NetworkDnscacheExtended.  # noqa: E501

        Lower bound on ttl for cache hits  # noqa: E501

        :return: The ttl_min_noerror of this NetworkDnscacheExtended.  # noqa: E501
        :rtype: int
        """
        return self._ttl_min_noerror

    @ttl_min_noerror.setter
    def ttl_min_noerror(self, ttl_min_noerror):
        """Sets the ttl_min_noerror of this NetworkDnscacheExtended.

        Lower bound on ttl for cache hits  # noqa: E501

        :param ttl_min_noerror: The ttl_min_noerror of this NetworkDnscacheExtended.  # noqa: E501
        :type: int
        """
        if ttl_min_noerror is not None and ttl_min_noerror > 3600:  # noqa: E501
            raise ValueError("Invalid value for `ttl_min_noerror`, must be a value less than or equal to `3600`")  # noqa: E501
        if ttl_min_noerror is not None and ttl_min_noerror < 0:  # noqa: E501
            raise ValueError("Invalid value for `ttl_min_noerror`, must be a value greater than or equal to `0`")  # noqa: E501

        self._ttl_min_noerror = ttl_min_noerror

    @property
    def ttl_min_nxdomain(self):
        """Gets the ttl_min_nxdomain of this NetworkDnscacheExtended.  # noqa: E501

        Lower bound on ttl for nxdomain  # noqa: E501

        :return: The ttl_min_nxdomain of this NetworkDnscacheExtended.  # noqa: E501
        :rtype: int
        """
        return self._ttl_min_nxdomain

    @ttl_min_nxdomain.setter
    def ttl_min_nxdomain(self, ttl_min_nxdomain):
        """Sets the ttl_min_nxdomain of this NetworkDnscacheExtended.

        Lower bound on ttl for nxdomain  # noqa: E501

        :param ttl_min_nxdomain: The ttl_min_nxdomain of this NetworkDnscacheExtended.  # noqa: E501
        :type: int
        """
        if ttl_min_nxdomain is not None and ttl_min_nxdomain > 3600:  # noqa: E501
            raise ValueError("Invalid value for `ttl_min_nxdomain`, must be a value less than or equal to `3600`")  # noqa: E501
        if ttl_min_nxdomain is not None and ttl_min_nxdomain < 0:  # noqa: E501
            raise ValueError("Invalid value for `ttl_min_nxdomain`, must be a value greater than or equal to `0`")  # noqa: E501

        self._ttl_min_nxdomain = ttl_min_nxdomain

    @property
    def ttl_min_other(self):
        """Gets the ttl_min_other of this NetworkDnscacheExtended.  # noqa: E501

        Lower bound on ttl for non-nxdomain failures  # noqa: E501

        :return: The ttl_min_other of this NetworkDnscacheExtended.  # noqa: E501
        :rtype: int
        """
        return self._ttl_min_other

    @ttl_min_other.setter
    def ttl_min_other(self, ttl_min_other):
        """Sets the ttl_min_other of this NetworkDnscacheExtended.

        Lower bound on ttl for non-nxdomain failures  # noqa: E501

        :param ttl_min_other: The ttl_min_other of this NetworkDnscacheExtended.  # noqa: E501
        :type: int
        """
        if ttl_min_other is not None and ttl_min_other > 3600:  # noqa: E501
            raise ValueError("Invalid value for `ttl_min_other`, must be a value less than or equal to `3600`")  # noqa: E501
        if ttl_min_other is not None and ttl_min_other < 0:  # noqa: E501
            raise ValueError("Invalid value for `ttl_min_other`, must be a value greater than or equal to `0`")  # noqa: E501

        self._ttl_min_other = ttl_min_other

    @property
    def ttl_min_servfail(self):
        """Gets the ttl_min_servfail of this NetworkDnscacheExtended.  # noqa: E501

        Lower bound on ttl for server failures  # noqa: E501

        :return: The ttl_min_servfail of this NetworkDnscacheExtended.  # noqa: E501
        :rtype: int
        """
        return self._ttl_min_servfail

    @ttl_min_servfail.setter
    def ttl_min_servfail(self, ttl_min_servfail):
        """Sets the ttl_min_servfail of this NetworkDnscacheExtended.

        Lower bound on ttl for server failures  # noqa: E501

        :param ttl_min_servfail: The ttl_min_servfail of this NetworkDnscacheExtended.  # noqa: E501
        :type: int
        """
        if ttl_min_servfail is not None and ttl_min_servfail > 3600:  # noqa: E501
            raise ValueError("Invalid value for `ttl_min_servfail`, must be a value less than or equal to `3600`")  # noqa: E501
        if ttl_min_servfail is not None and ttl_min_servfail < 0:  # noqa: E501
            raise ValueError("Invalid value for `ttl_min_servfail`, must be a value greater than or equal to `0`")  # noqa: E501

        self._ttl_min_servfail = ttl_min_servfail

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
        if not isinstance(other, NetworkDnscacheExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
