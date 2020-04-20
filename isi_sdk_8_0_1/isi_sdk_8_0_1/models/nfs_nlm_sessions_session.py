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


class NfsNlmSessionsSession(object):
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
        'delegates': 'list[int]',
        'host_type': 'str',
        'hostname': 'str',
        'is_active': 'bool',
        'last_modified': 'int',
        'node_ip': 'str',
        'notify_attempts_remaining': 'int',
        'notify_error': 'str',
        'notify_last_attempt': 'int'
    }

    attribute_map = {
        'delegates': 'delegates',
        'host_type': 'host_type',
        'hostname': 'hostname',
        'is_active': 'is_active',
        'last_modified': 'last_modified',
        'node_ip': 'node_ip',
        'notify_attempts_remaining': 'notify_attempts_remaining',
        'notify_error': 'notify_error',
        'notify_last_attempt': 'notify_last_attempt'
    }

    def __init__(self, delegates=None, host_type=None, hostname=None, is_active=None, last_modified=None, node_ip=None, notify_attempts_remaining=None, notify_error=None, notify_last_attempt=None):  # noqa: E501
        """NfsNlmSessionsSession - a model defined in Swagger"""  # noqa: E501

        self._delegates = None
        self._host_type = None
        self._hostname = None
        self._is_active = None
        self._last_modified = None
        self._node_ip = None
        self._notify_attempts_remaining = None
        self._notify_error = None
        self._notify_last_attempt = None
        self.discriminator = None

        if delegates is not None:
            self.delegates = delegates
        if host_type is not None:
            self.host_type = host_type
        if hostname is not None:
            self.hostname = hostname
        if is_active is not None:
            self.is_active = is_active
        if last_modified is not None:
            self.last_modified = last_modified
        if node_ip is not None:
            self.node_ip = node_ip
        if notify_attempts_remaining is not None:
            self.notify_attempts_remaining = notify_attempts_remaining
        if notify_error is not None:
            self.notify_error = notify_error
        if notify_last_attempt is not None:
            self.notify_last_attempt = notify_last_attempt

    @property
    def delegates(self):
        """Gets the delegates of this NfsNlmSessionsSession.  # noqa: E501


        :return: The delegates of this NfsNlmSessionsSession.  # noqa: E501
        :rtype: list[int]
        """
        return self._delegates

    @delegates.setter
    def delegates(self, delegates):
        """Sets the delegates of this NfsNlmSessionsSession.


        :param delegates: The delegates of this NfsNlmSessionsSession.  # noqa: E501
        :type: list[int]
        """

        self._delegates = delegates

    @property
    def host_type(self):
        """Gets the host_type of this NfsNlmSessionsSession.  # noqa: E501

        The sort of host that this entry represents  # noqa: E501

        :return: The host_type of this NfsNlmSessionsSession.  # noqa: E501
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        """Sets the host_type of this NfsNlmSessionsSession.

        The sort of host that this entry represents  # noqa: E501

        :param host_type: The host_type of this NfsNlmSessionsSession.  # noqa: E501
        :type: str
        """
        allowed_values = ["client", "server", "reverse", "expired"]  # noqa: E501
        if host_type not in allowed_values:
            raise ValueError(
                "Invalid value for `host_type` ({0}), must be one of {1}"  # noqa: E501
                .format(host_type, allowed_values)
            )

        self._host_type = host_type

    @property
    def hostname(self):
        """Gets the hostname of this NfsNlmSessionsSession.  # noqa: E501

        The host being monitored  # noqa: E501

        :return: The hostname of this NfsNlmSessionsSession.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this NfsNlmSessionsSession.

        The host being monitored  # noqa: E501

        :param hostname: The hostname of this NfsNlmSessionsSession.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def is_active(self):
        """Gets the is_active of this NfsNlmSessionsSession.  # noqa: E501

        Whether or not the client is actively being monitored  # noqa: E501

        :return: The is_active of this NfsNlmSessionsSession.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this NfsNlmSessionsSession.

        Whether or not the client is actively being monitored  # noqa: E501

        :param is_active: The is_active of this NfsNlmSessionsSession.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def last_modified(self):
        """Gets the last_modified of this NfsNlmSessionsSession.  # noqa: E501

        Unix time in seconds that the client was last modified (monitored or unmonitored)  # noqa: E501

        :return: The last_modified of this NfsNlmSessionsSession.  # noqa: E501
        :rtype: int
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this NfsNlmSessionsSession.

        Unix time in seconds that the client was last modified (monitored or unmonitored)  # noqa: E501

        :param last_modified: The last_modified of this NfsNlmSessionsSession.  # noqa: E501
        :type: int
        """

        self._last_modified = last_modified

    @property
    def node_ip(self):
        """Gets the node_ip of this NfsNlmSessionsSession.  # noqa: E501

        An IP address for which NSM has client records  # noqa: E501

        :return: The node_ip of this NfsNlmSessionsSession.  # noqa: E501
        :rtype: str
        """
        return self._node_ip

    @node_ip.setter
    def node_ip(self, node_ip):
        """Sets the node_ip of this NfsNlmSessionsSession.

        An IP address for which NSM has client records  # noqa: E501

        :param node_ip: The node_ip of this NfsNlmSessionsSession.  # noqa: E501
        :type: str
        """

        self._node_ip = node_ip

    @property
    def notify_attempts_remaining(self):
        """Gets the notify_attempts_remaining of this NfsNlmSessionsSession.  # noqa: E501

        Number of times we will attempt to notify this client before giving up  # noqa: E501

        :return: The notify_attempts_remaining of this NfsNlmSessionsSession.  # noqa: E501
        :rtype: int
        """
        return self._notify_attempts_remaining

    @notify_attempts_remaining.setter
    def notify_attempts_remaining(self, notify_attempts_remaining):
        """Sets the notify_attempts_remaining of this NfsNlmSessionsSession.

        Number of times we will attempt to notify this client before giving up  # noqa: E501

        :param notify_attempts_remaining: The notify_attempts_remaining of this NfsNlmSessionsSession.  # noqa: E501
        :type: int
        """

        self._notify_attempts_remaining = notify_attempts_remaining

    @property
    def notify_error(self):
        """Gets the notify_error of this NfsNlmSessionsSession.  # noqa: E501

        Last error recieved attempting to notify this client  # noqa: E501

        :return: The notify_error of this NfsNlmSessionsSession.  # noqa: E501
        :rtype: str
        """
        return self._notify_error

    @notify_error.setter
    def notify_error(self, notify_error):
        """Sets the notify_error of this NfsNlmSessionsSession.

        Last error recieved attempting to notify this client  # noqa: E501

        :param notify_error: The notify_error of this NfsNlmSessionsSession.  # noqa: E501
        :type: str
        """

        self._notify_error = notify_error

    @property
    def notify_last_attempt(self):
        """Gets the notify_last_attempt of this NfsNlmSessionsSession.  # noqa: E501

        Unix time in seconds when we last attempted to notify this clients  # noqa: E501

        :return: The notify_last_attempt of this NfsNlmSessionsSession.  # noqa: E501
        :rtype: int
        """
        return self._notify_last_attempt

    @notify_last_attempt.setter
    def notify_last_attempt(self, notify_last_attempt):
        """Sets the notify_last_attempt of this NfsNlmSessionsSession.

        Unix time in seconds when we last attempted to notify this clients  # noqa: E501

        :param notify_last_attempt: The notify_last_attempt of this NfsNlmSessionsSession.  # noqa: E501
        :type: int
        """

        self._notify_last_attempt = notify_last_attempt

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
        if not isinstance(other, NfsNlmSessionsSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
