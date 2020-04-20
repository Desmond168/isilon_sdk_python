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


class CloudJob(object):
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
        'all': 'bool',
        'state': 'str'
    }

    attribute_map = {
        'all': 'all',
        'state': 'state'
    }

    def __init__(self, all=None, state=None):  # noqa: E501
        """CloudJob - a model defined in Swagger"""  # noqa: E501

        self._all = None
        self._state = None
        self.discriminator = None

        if all is not None:
            self.all = all
        if state is not None:
            self.state = state

    @property
    def all(self):
        """Gets the all of this CloudJob.  # noqa: E501

        Whether to apply to the given operation type or to all jobs of the given operation type  # noqa: E501

        :return: The all of this CloudJob.  # noqa: E501
        :rtype: bool
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this CloudJob.

        Whether to apply to the given operation type or to all jobs of the given operation type  # noqa: E501

        :param all: The all of this CloudJob.  # noqa: E501
        :type: bool
        """

        self._all = all

    @property
    def state(self):
        """Gets the state of this CloudJob.  # noqa: E501

        The desired state of the job or operation  # noqa: E501

        :return: The state of this CloudJob.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CloudJob.

        The desired state of the job or operation  # noqa: E501

        :param state: The state of this CloudJob.  # noqa: E501
        :type: str
        """
        allowed_values = ["resume", "pause", "cancel"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if not isinstance(other, CloudJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
