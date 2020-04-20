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


class FilepoolPolicyAction(object):
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
        'action_param': 'str',
        'action_type': 'str'
    }

    attribute_map = {
        'action_param': 'action_param',
        'action_type': 'action_type'
    }

    def __init__(self, action_param=None, action_type=None):  # noqa: E501
        """FilepoolPolicyAction - a model defined in Swagger"""  # noqa: E501

        self._action_param = None
        self._action_type = None
        self.discriminator = None

        if action_param is not None:
            self.action_param = action_param
        self.action_type = action_type

    @property
    def action_param(self):
        """Gets the action_param of this FilepoolPolicyAction.  # noqa: E501

        Varies according to action_type  # noqa: E501

        :return: The action_param of this FilepoolPolicyAction.  # noqa: E501
        :rtype: str
        """
        return self._action_param

    @action_param.setter
    def action_param(self, action_param):
        """Sets the action_param of this FilepoolPolicyAction.

        Varies according to action_type  # noqa: E501

        :param action_param: The action_param of this FilepoolPolicyAction.  # noqa: E501
        :type: str
        """

        self._action_param = action_param

    @property
    def action_type(self):
        """Gets the action_type of this FilepoolPolicyAction.  # noqa: E501


        :return: The action_type of this FilepoolPolicyAction.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this FilepoolPolicyAction.


        :param action_type: The action_type of this FilepoolPolicyAction.  # noqa: E501
        :type: str
        """
        if action_type is None:
            raise ValueError("Invalid value for `action_type`, must not be `None`")  # noqa: E501
        allowed_values = ["set_requested_protection", "set_data_access_pattern", "enable_coalescer", "apply_data_storage_policy", "apply_snapshot_storage_policy", "set_cloudpool_policy", "enable_packing"]  # noqa: E501
        if action_type not in allowed_values:
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"  # noqa: E501
                .format(action_type, allowed_values)
            )

        self._action_type = action_type

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
        if not isinstance(other, FilepoolPolicyAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
