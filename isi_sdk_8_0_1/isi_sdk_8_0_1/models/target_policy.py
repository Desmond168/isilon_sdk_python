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


class TargetPolicy(object):
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
        'failover_failback_state': 'str',
        'id': 'str',
        'last_job_state': 'str',
        'last_source_coordinator_ip': 'str',
        'last_update_from_source': 'int',
        'legacy_policy': 'bool',
        'name': 'str',
        'source_cluster_guid': 'str',
        'source_host': 'str',
        'target_path': 'str'
    }

    attribute_map = {
        'failover_failback_state': 'failover_failback_state',
        'id': 'id',
        'last_job_state': 'last_job_state',
        'last_source_coordinator_ip': 'last_source_coordinator_ip',
        'last_update_from_source': 'last_update_from_source',
        'legacy_policy': 'legacy_policy',
        'name': 'name',
        'source_cluster_guid': 'source_cluster_guid',
        'source_host': 'source_host',
        'target_path': 'target_path'
    }

    def __init__(self, failover_failback_state=None, id=None, last_job_state=None, last_source_coordinator_ip=None, last_update_from_source=None, legacy_policy=None, name=None, source_cluster_guid=None, source_host=None, target_path=None):  # noqa: E501
        """TargetPolicy - a model defined in Swagger"""  # noqa: E501

        self._failover_failback_state = None
        self._id = None
        self._last_job_state = None
        self._last_source_coordinator_ip = None
        self._last_update_from_source = None
        self._legacy_policy = None
        self._name = None
        self._source_cluster_guid = None
        self._source_host = None
        self._target_path = None
        self.discriminator = None

        self.failover_failback_state = failover_failback_state
        self.id = id
        self.last_job_state = last_job_state
        self.last_source_coordinator_ip = last_source_coordinator_ip
        if last_update_from_source is not None:
            self.last_update_from_source = last_update_from_source
        self.legacy_policy = legacy_policy
        self.name = name
        self.source_cluster_guid = source_cluster_guid
        self.source_host = source_host
        self.target_path = target_path

    @property
    def failover_failback_state(self):
        """Gets the failover_failback_state of this TargetPolicy.  # noqa: E501

        The condition of this policy with respect to sync failover/failback.  # noqa: E501

        :return: The failover_failback_state of this TargetPolicy.  # noqa: E501
        :rtype: str
        """
        return self._failover_failback_state

    @failover_failback_state.setter
    def failover_failback_state(self, failover_failback_state):
        """Sets the failover_failback_state of this TargetPolicy.

        The condition of this policy with respect to sync failover/failback.  # noqa: E501

        :param failover_failback_state: The failover_failback_state of this TargetPolicy.  # noqa: E501
        :type: str
        """
        if failover_failback_state is None:
            raise ValueError("Invalid value for `failover_failback_state`, must not be `None`")  # noqa: E501
        allowed_values = ["writes_disabled", "enabling_writes", "writes_enabled", "disabling_writes", "creating_resync_policy", "resync_policy_created"]  # noqa: E501
        if failover_failback_state not in allowed_values:
            raise ValueError(
                "Invalid value for `failover_failback_state` ({0}), must be one of {1}"  # noqa: E501
                .format(failover_failback_state, allowed_values)
            )

        self._failover_failback_state = failover_failback_state

    @property
    def id(self):
        """Gets the id of this TargetPolicy.  # noqa: E501

        The system ID given to this sync policy.  # noqa: E501

        :return: The id of this TargetPolicy.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TargetPolicy.

        The system ID given to this sync policy.  # noqa: E501

        :param id: The id of this TargetPolicy.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def last_job_state(self):
        """Gets the last_job_state of this TargetPolicy.  # noqa: E501

        The state of the last job run for this policy.  # noqa: E501

        :return: The last_job_state of this TargetPolicy.  # noqa: E501
        :rtype: str
        """
        return self._last_job_state

    @last_job_state.setter
    def last_job_state(self, last_job_state):
        """Sets the last_job_state of this TargetPolicy.

        The state of the last job run for this policy.  # noqa: E501

        :param last_job_state: The last_job_state of this TargetPolicy.  # noqa: E501
        :type: str
        """
        if last_job_state is None:
            raise ValueError("Invalid value for `last_job_state`, must not be `None`")  # noqa: E501
        allowed_values = ["scheduled", "running", "paused", "finished", "failed", "canceled", "needs_attention", "skipped", "pending", "unknown"]  # noqa: E501
        if last_job_state not in allowed_values:
            raise ValueError(
                "Invalid value for `last_job_state` ({0}), must be one of {1}"  # noqa: E501
                .format(last_job_state, allowed_values)
            )

        self._last_job_state = last_job_state

    @property
    def last_source_coordinator_ip(self):
        """Gets the last_source_coordinator_ip of this TargetPolicy.  # noqa: E501

        The IP address from which a SyncIQ coordinator daemon most recently connected to this cluster to update it about the progress of a job for this policy.  # noqa: E501

        :return: The last_source_coordinator_ip of this TargetPolicy.  # noqa: E501
        :rtype: str
        """
        return self._last_source_coordinator_ip

    @last_source_coordinator_ip.setter
    def last_source_coordinator_ip(self, last_source_coordinator_ip):
        """Sets the last_source_coordinator_ip of this TargetPolicy.

        The IP address from which a SyncIQ coordinator daemon most recently connected to this cluster to update it about the progress of a job for this policy.  # noqa: E501

        :param last_source_coordinator_ip: The last_source_coordinator_ip of this TargetPolicy.  # noqa: E501
        :type: str
        """
        if last_source_coordinator_ip is None:
            raise ValueError("Invalid value for `last_source_coordinator_ip`, must not be `None`")  # noqa: E501

        self._last_source_coordinator_ip = last_source_coordinator_ip

    @property
    def last_update_from_source(self):
        """Gets the last_update_from_source of this TargetPolicy.  # noqa: E501

        The last time this cluster was updated with sync information from the source cluster for this policy, in unix epoch seconds.  Null if no such update has occurred yet.  # noqa: E501

        :return: The last_update_from_source of this TargetPolicy.  # noqa: E501
        :rtype: int
        """
        return self._last_update_from_source

    @last_update_from_source.setter
    def last_update_from_source(self, last_update_from_source):
        """Sets the last_update_from_source of this TargetPolicy.

        The last time this cluster was updated with sync information from the source cluster for this policy, in unix epoch seconds.  Null if no such update has occurred yet.  # noqa: E501

        :param last_update_from_source: The last_update_from_source of this TargetPolicy.  # noqa: E501
        :type: int
        """

        self._last_update_from_source = last_update_from_source

    @property
    def legacy_policy(self):
        """Gets the legacy_policy of this TargetPolicy.  # noqa: E501

        Was this policy defined by a OneFS version earlier than 6.0? (Pre-6.0 policies did not have the target policy concept and canceling from the target side will not be available.)  # noqa: E501

        :return: The legacy_policy of this TargetPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._legacy_policy

    @legacy_policy.setter
    def legacy_policy(self, legacy_policy):
        """Sets the legacy_policy of this TargetPolicy.

        Was this policy defined by a OneFS version earlier than 6.0? (Pre-6.0 policies did not have the target policy concept and canceling from the target side will not be available.)  # noqa: E501

        :param legacy_policy: The legacy_policy of this TargetPolicy.  # noqa: E501
        :type: bool
        """
        if legacy_policy is None:
            raise ValueError("Invalid value for `legacy_policy`, must not be `None`")  # noqa: E501

        self._legacy_policy = legacy_policy

    @property
    def name(self):
        """Gets the name of this TargetPolicy.  # noqa: E501

        User-assigned name of this sync policy.  # noqa: E501

        :return: The name of this TargetPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TargetPolicy.

        User-assigned name of this sync policy.  # noqa: E501

        :param name: The name of this TargetPolicy.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def source_cluster_guid(self):
        """Gets the source_cluster_guid of this TargetPolicy.  # noqa: E501

        Unique identifier for the source cluster.  # noqa: E501

        :return: The source_cluster_guid of this TargetPolicy.  # noqa: E501
        :rtype: str
        """
        return self._source_cluster_guid

    @source_cluster_guid.setter
    def source_cluster_guid(self, source_cluster_guid):
        """Sets the source_cluster_guid of this TargetPolicy.

        Unique identifier for the source cluster.  # noqa: E501

        :param source_cluster_guid: The source_cluster_guid of this TargetPolicy.  # noqa: E501
        :type: str
        """
        if source_cluster_guid is None:
            raise ValueError("Invalid value for `source_cluster_guid`, must not be `None`")  # noqa: E501

        self._source_cluster_guid = source_cluster_guid

    @property
    def source_host(self):
        """Gets the source_host of this TargetPolicy.  # noqa: E501

        Hostname or IP address of sync source cluster.  # noqa: E501

        :return: The source_host of this TargetPolicy.  # noqa: E501
        :rtype: str
        """
        return self._source_host

    @source_host.setter
    def source_host(self, source_host):
        """Sets the source_host of this TargetPolicy.

        Hostname or IP address of sync source cluster.  # noqa: E501

        :param source_host: The source_host of this TargetPolicy.  # noqa: E501
        :type: str
        """
        if source_host is None:
            raise ValueError("Invalid value for `source_host`, must not be `None`")  # noqa: E501

        self._source_host = source_host

    @property
    def target_path(self):
        """Gets the target_path of this TargetPolicy.  # noqa: E501

        Absolute filesystem path on the target cluster for the sync destination.  # noqa: E501

        :return: The target_path of this TargetPolicy.  # noqa: E501
        :rtype: str
        """
        return self._target_path

    @target_path.setter
    def target_path(self, target_path):
        """Sets the target_path of this TargetPolicy.

        Absolute filesystem path on the target cluster for the sync destination.  # noqa: E501

        :param target_path: The target_path of this TargetPolicy.  # noqa: E501
        :type: str
        """
        if target_path is None:
            raise ValueError("Invalid value for `target_path`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, TargetPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
