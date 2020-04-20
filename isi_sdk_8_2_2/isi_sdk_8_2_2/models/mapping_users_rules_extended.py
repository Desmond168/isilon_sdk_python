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

from isi_sdk_8_2_2.models.mapping_users_rules_parameters import MappingUsersRulesParameters  # noqa: F401,E501
from isi_sdk_8_2_2.models.mapping_users_rules_rule_extended import MappingUsersRulesRuleExtended  # noqa: F401,E501


class MappingUsersRulesExtended(object):
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
        'parameters': 'MappingUsersRulesParameters',
        'rules': 'list[MappingUsersRulesRuleExtended]'
    }

    attribute_map = {
        'parameters': 'parameters',
        'rules': 'rules'
    }

    def __init__(self, parameters=None, rules=None):  # noqa: E501
        """MappingUsersRulesExtended - a model defined in Swagger"""  # noqa: E501

        self._parameters = None
        self._rules = None
        self.discriminator = None

        if parameters is not None:
            self.parameters = parameters
        if rules is not None:
            self.rules = rules

    @property
    def parameters(self):
        """Gets the parameters of this MappingUsersRulesExtended.  # noqa: E501

        Specifies the default UNIX user information that can be applied if the final credentials do not have valid UID and GID information.  # noqa: E501

        :return: The parameters of this MappingUsersRulesExtended.  # noqa: E501
        :rtype: MappingUsersRulesParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this MappingUsersRulesExtended.

        Specifies the default UNIX user information that can be applied if the final credentials do not have valid UID and GID information.  # noqa: E501

        :param parameters: The parameters of this MappingUsersRulesExtended.  # noqa: E501
        :type: MappingUsersRulesParameters
        """

        self._parameters = parameters

    @property
    def rules(self):
        """Gets the rules of this MappingUsersRulesExtended.  # noqa: E501

        Specifies the list of user mapping rules.  # noqa: E501

        :return: The rules of this MappingUsersRulesExtended.  # noqa: E501
        :rtype: list[MappingUsersRulesRuleExtended]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this MappingUsersRulesExtended.

        Specifies the list of user mapping rules.  # noqa: E501

        :param rules: The rules of this MappingUsersRulesExtended.  # noqa: E501
        :type: list[MappingUsersRulesRuleExtended]
        """

        self._rules = rules

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
        if not isinstance(other, MappingUsersRulesExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
