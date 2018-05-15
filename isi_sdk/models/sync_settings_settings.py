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

from isi_sdk_8_1_1.models.sync_policy_source_network import SyncPolicySourceNetwork  # noqa: F401,E501


class SyncSettingsSettings(object):
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
        'burst_memory_constraint': 'int',
        'burst_socket_buffer_size': 'int',
        'force_interface': 'bool',
        'max_concurrent_jobs': 'int',
        'report_email': 'list[str]',
        'report_max_age': 'int',
        'report_max_count': 'int',
        'restrict_target_network': 'bool',
        'rpo_alerts': 'bool',
        'service': 'str',
        'source_network': 'SyncPolicySourceNetwork',
        'tw_chkpt_interval': 'int'
    }

    attribute_map = {
        'burst_memory_constraint': 'burst_memory_constraint',
        'burst_socket_buffer_size': 'burst_socket_buffer_size',
        'force_interface': 'force_interface',
        'max_concurrent_jobs': 'max_concurrent_jobs',
        'report_email': 'report_email',
        'report_max_age': 'report_max_age',
        'report_max_count': 'report_max_count',
        'restrict_target_network': 'restrict_target_network',
        'rpo_alerts': 'rpo_alerts',
        'service': 'service',
        'source_network': 'source_network',
        'tw_chkpt_interval': 'tw_chkpt_interval'
    }

    def __init__(self, burst_memory_constraint=None, burst_socket_buffer_size=None, force_interface=None, max_concurrent_jobs=None, report_email=None, report_max_age=None, report_max_count=None, restrict_target_network=None, rpo_alerts=None, service=None, source_network=None, tw_chkpt_interval=None):  # noqa: E501
        """SyncSettingsSettings - a model defined in Swagger"""  # noqa: E501

        self._burst_memory_constraint = None
        self._burst_socket_buffer_size = None
        self._force_interface = None
        self._max_concurrent_jobs = None
        self._report_email = None
        self._report_max_age = None
        self._report_max_count = None
        self._restrict_target_network = None
        self._rpo_alerts = None
        self._service = None
        self._source_network = None
        self._tw_chkpt_interval = None
        self.discriminator = None

        if burst_memory_constraint is not None:
            self.burst_memory_constraint = burst_memory_constraint
        if burst_socket_buffer_size is not None:
            self.burst_socket_buffer_size = burst_socket_buffer_size
        if force_interface is not None:
            self.force_interface = force_interface
        if max_concurrent_jobs is not None:
            self.max_concurrent_jobs = max_concurrent_jobs
        if report_email is not None:
            self.report_email = report_email
        if report_max_age is not None:
            self.report_max_age = report_max_age
        if report_max_count is not None:
            self.report_max_count = report_max_count
        if restrict_target_network is not None:
            self.restrict_target_network = restrict_target_network
        if rpo_alerts is not None:
            self.rpo_alerts = rpo_alerts
        if service is not None:
            self.service = service
        if source_network is not None:
            self.source_network = source_network
        if tw_chkpt_interval is not None:
            self.tw_chkpt_interval = tw_chkpt_interval

    @property
    def burst_memory_constraint(self):
        """Gets the burst_memory_constraint of this SyncSettingsSettings.  # noqa: E501

        The per-worker burst socket memory constraint, in bytes.  # noqa: E501

        :return: The burst_memory_constraint of this SyncSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._burst_memory_constraint

    @burst_memory_constraint.setter
    def burst_memory_constraint(self, burst_memory_constraint):
        """Sets the burst_memory_constraint of this SyncSettingsSettings.

        The per-worker burst socket memory constraint, in bytes.  # noqa: E501

        :param burst_memory_constraint: The burst_memory_constraint of this SyncSettingsSettings.  # noqa: E501
        :type: int
        """
        if burst_memory_constraint is not None and burst_memory_constraint > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `burst_memory_constraint`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if burst_memory_constraint is not None and burst_memory_constraint < 0:  # noqa: E501
            raise ValueError("Invalid value for `burst_memory_constraint`, must be a value greater than or equal to `0`")  # noqa: E501

        self._burst_memory_constraint = burst_memory_constraint

    @property
    def burst_socket_buffer_size(self):
        """Gets the burst_socket_buffer_size of this SyncSettingsSettings.  # noqa: E501

        The per-worker burst socket buffer coalesced data, in bytes.  # noqa: E501

        :return: The burst_socket_buffer_size of this SyncSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._burst_socket_buffer_size

    @burst_socket_buffer_size.setter
    def burst_socket_buffer_size(self, burst_socket_buffer_size):
        """Sets the burst_socket_buffer_size of this SyncSettingsSettings.

        The per-worker burst socket buffer coalesced data, in bytes.  # noqa: E501

        :param burst_socket_buffer_size: The burst_socket_buffer_size of this SyncSettingsSettings.  # noqa: E501
        :type: int
        """
        if burst_socket_buffer_size is not None and burst_socket_buffer_size > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `burst_socket_buffer_size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if burst_socket_buffer_size is not None and burst_socket_buffer_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `burst_socket_buffer_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._burst_socket_buffer_size = burst_socket_buffer_size

    @property
    def force_interface(self):
        """Gets the force_interface of this SyncSettingsSettings.  # noqa: E501

        NOTE: This field should not be changed without the help of Isilon support.  Default for the \"force_interface\" property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  Determines whether data is sent only through the subnet and pool specified in the \"source_network\" field. This option can be useful if there are multiple interfaces for the given source subnet.  # noqa: E501

        :return: The force_interface of this SyncSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._force_interface

    @force_interface.setter
    def force_interface(self, force_interface):
        """Sets the force_interface of this SyncSettingsSettings.

        NOTE: This field should not be changed without the help of Isilon support.  Default for the \"force_interface\" property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  Determines whether data is sent only through the subnet and pool specified in the \"source_network\" field. This option can be useful if there are multiple interfaces for the given source subnet.  # noqa: E501

        :param force_interface: The force_interface of this SyncSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._force_interface = force_interface

    @property
    def max_concurrent_jobs(self):
        """Gets the max_concurrent_jobs of this SyncSettingsSettings.  # noqa: E501

        The max concurrent jobs that SyncIQ can support. This number is based on the size of the current cluster and the current SyncIQ worker throttle rule.  # noqa: E501

        :return: The max_concurrent_jobs of this SyncSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_concurrent_jobs

    @max_concurrent_jobs.setter
    def max_concurrent_jobs(self, max_concurrent_jobs):
        """Sets the max_concurrent_jobs of this SyncSettingsSettings.

        The max concurrent jobs that SyncIQ can support. This number is based on the size of the current cluster and the current SyncIQ worker throttle rule.  # noqa: E501

        :param max_concurrent_jobs: The max_concurrent_jobs of this SyncSettingsSettings.  # noqa: E501
        :type: int
        """
        if max_concurrent_jobs is not None and max_concurrent_jobs > 1000:  # noqa: E501
            raise ValueError("Invalid value for `max_concurrent_jobs`, must be a value less than or equal to `1000`")  # noqa: E501
        if max_concurrent_jobs is not None and max_concurrent_jobs < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_concurrent_jobs`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_concurrent_jobs = max_concurrent_jobs

    @property
    def report_email(self):
        """Gets the report_email of this SyncSettingsSettings.  # noqa: E501

        Email sync reports to these addresses.  # noqa: E501

        :return: The report_email of this SyncSettingsSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._report_email

    @report_email.setter
    def report_email(self, report_email):
        """Sets the report_email of this SyncSettingsSettings.

        Email sync reports to these addresses.  # noqa: E501

        :param report_email: The report_email of this SyncSettingsSettings.  # noqa: E501
        :type: list[str]
        """

        self._report_email = report_email

    @property
    def report_max_age(self):
        """Gets the report_max_age of this SyncSettingsSettings.  # noqa: E501

        The default length of time (in seconds) a policy report will be stored.  # noqa: E501

        :return: The report_max_age of this SyncSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._report_max_age

    @report_max_age.setter
    def report_max_age(self, report_max_age):
        """Sets the report_max_age of this SyncSettingsSettings.

        The default length of time (in seconds) a policy report will be stored.  # noqa: E501

        :param report_max_age: The report_max_age of this SyncSettingsSettings.  # noqa: E501
        :type: int
        """
        if report_max_age is not None and report_max_age > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `report_max_age`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if report_max_age is not None and report_max_age < 0:  # noqa: E501
            raise ValueError("Invalid value for `report_max_age`, must be a value greater than or equal to `0`")  # noqa: E501

        self._report_max_age = report_max_age

    @property
    def report_max_count(self):
        """Gets the report_max_count of this SyncSettingsSettings.  # noqa: E501

        The default maximum number of reports to retain for a policy.  # noqa: E501

        :return: The report_max_count of this SyncSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._report_max_count

    @report_max_count.setter
    def report_max_count(self, report_max_count):
        """Sets the report_max_count of this SyncSettingsSettings.

        The default maximum number of reports to retain for a policy.  # noqa: E501

        :param report_max_count: The report_max_count of this SyncSettingsSettings.  # noqa: E501
        :type: int
        """
        if report_max_count is not None and report_max_count > 2000:  # noqa: E501
            raise ValueError("Invalid value for `report_max_count`, must be a value less than or equal to `2000`")  # noqa: E501
        if report_max_count is not None and report_max_count < 1:  # noqa: E501
            raise ValueError("Invalid value for `report_max_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._report_max_count = report_max_count

    @property
    def restrict_target_network(self):
        """Gets the restrict_target_network of this SyncSettingsSettings.  # noqa: E501

        Default for the \"restrict_target_network\" property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  If you specify true, and you specify a SmartConnect zone in the \"target_host\" field, replication policies will connect only to nodes in the specified SmartConnect zone.  If you specify false, replication policies are not restricted to specific nodes on the target cluster.  # noqa: E501

        :return: The restrict_target_network of this SyncSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._restrict_target_network

    @restrict_target_network.setter
    def restrict_target_network(self, restrict_target_network):
        """Sets the restrict_target_network of this SyncSettingsSettings.

        Default for the \"restrict_target_network\" property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  If you specify true, and you specify a SmartConnect zone in the \"target_host\" field, replication policies will connect only to nodes in the specified SmartConnect zone.  If you specify false, replication policies are not restricted to specific nodes on the target cluster.  # noqa: E501

        :param restrict_target_network: The restrict_target_network of this SyncSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._restrict_target_network = restrict_target_network

    @property
    def rpo_alerts(self):
        """Gets the rpo_alerts of this SyncSettingsSettings.  # noqa: E501

        If disabled, no RPO alerts will be generated.  # noqa: E501

        :return: The rpo_alerts of this SyncSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._rpo_alerts

    @rpo_alerts.setter
    def rpo_alerts(self, rpo_alerts):
        """Sets the rpo_alerts of this SyncSettingsSettings.

        If disabled, no RPO alerts will be generated.  # noqa: E501

        :param rpo_alerts: The rpo_alerts of this SyncSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._rpo_alerts = rpo_alerts

    @property
    def service(self):
        """Gets the service of this SyncSettingsSettings.  # noqa: E501

        Specifies if the SyncIQ service currently on, paused, or off.  If paused, all sync jobs will be paused.  If turned off, all jobs will be canceled.  # noqa: E501

        :return: The service of this SyncSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this SyncSettingsSettings.

        Specifies if the SyncIQ service currently on, paused, or off.  If paused, all sync jobs will be paused.  If turned off, all jobs will be canceled.  # noqa: E501

        :param service: The service of this SyncSettingsSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["on", "off", "paused"]  # noqa: E501
        if service not in allowed_values:
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"  # noqa: E501
                .format(service, allowed_values)
            )

        self._service = service

    @property
    def source_network(self):
        """Gets the source_network of this SyncSettingsSettings.  # noqa: E501

        Restricts replication policies on the local cluster to running on the specified subnet and pool.  # noqa: E501

        :return: The source_network of this SyncSettingsSettings.  # noqa: E501
        :rtype: SyncPolicySourceNetwork
        """
        return self._source_network

    @source_network.setter
    def source_network(self, source_network):
        """Sets the source_network of this SyncSettingsSettings.

        Restricts replication policies on the local cluster to running on the specified subnet and pool.  # noqa: E501

        :param source_network: The source_network of this SyncSettingsSettings.  # noqa: E501
        :type: SyncPolicySourceNetwork
        """

        self._source_network = source_network

    @property
    def tw_chkpt_interval(self):
        """Gets the tw_chkpt_interval of this SyncSettingsSettings.  # noqa: E501

        The interval (in seconds) in which treewalk syncs are forced to checkpoint.  # noqa: E501

        :return: The tw_chkpt_interval of this SyncSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._tw_chkpt_interval

    @tw_chkpt_interval.setter
    def tw_chkpt_interval(self, tw_chkpt_interval):
        """Sets the tw_chkpt_interval of this SyncSettingsSettings.

        The interval (in seconds) in which treewalk syncs are forced to checkpoint.  # noqa: E501

        :param tw_chkpt_interval: The tw_chkpt_interval of this SyncSettingsSettings.  # noqa: E501
        :type: int
        """
        if tw_chkpt_interval is not None and tw_chkpt_interval < 0:  # noqa: E501
            raise ValueError("Invalid value for `tw_chkpt_interval`, must be a value greater than or equal to `0`")  # noqa: E501

        self._tw_chkpt_interval = tw_chkpt_interval

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
        if not isinstance(other, SyncSettingsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
