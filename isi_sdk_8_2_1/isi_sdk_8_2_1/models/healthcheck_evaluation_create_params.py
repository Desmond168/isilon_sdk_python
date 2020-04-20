# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 8
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk_8_2_1.models.empty import Empty  # noqa: F401,E501
from isi_sdk_8_2_1.models.healthcheck_evaluation_override import HealthcheckEvaluationOverride  # noqa: F401,E501


class HealthcheckEvaluationCreateParams(object):
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
        'checklist_id': 'str',
        'overrides': 'list[HealthcheckEvaluationOverride]',
        'parameters': 'Empty'
    }

    attribute_map = {
        'checklist_id': 'checklist_id',
        'overrides': 'overrides',
        'parameters': 'parameters'
    }

    def __init__(self, checklist_id=None, overrides=None, parameters=None):  # noqa: E501
        """HealthcheckEvaluationCreateParams - a model defined in Swagger"""  # noqa: E501

        self._checklist_id = None
        self._overrides = None
        self._parameters = None
        self.discriminator = None

        self.checklist_id = checklist_id
        if overrides is not None:
            self.overrides = overrides
        if parameters is not None:
            self.parameters = parameters

    @property
    def checklist_id(self):
        """Gets the checklist_id of this HealthcheckEvaluationCreateParams.  # noqa: E501

        Checklist to be run  # noqa: E501

        :return: The checklist_id of this HealthcheckEvaluationCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._checklist_id

    @checklist_id.setter
    def checklist_id(self, checklist_id):
        """Sets the checklist_id of this HealthcheckEvaluationCreateParams.

        Checklist to be run  # noqa: E501

        :param checklist_id: The checklist_id of this HealthcheckEvaluationCreateParams.  # noqa: E501
        :type: str
        """
        if checklist_id is None:
            raise ValueError("Invalid value for `checklist_id`, must not be `None`")  # noqa: E501

        self._checklist_id = checklist_id

    @property
    def overrides(self):
        """Gets the overrides of this HealthcheckEvaluationCreateParams.  # noqa: E501

        Optional overrides for thresholds etc.  # noqa: E501

        :return: The overrides of this HealthcheckEvaluationCreateParams.  # noqa: E501
        :rtype: list[HealthcheckEvaluationOverride]
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """Sets the overrides of this HealthcheckEvaluationCreateParams.

        Optional overrides for thresholds etc.  # noqa: E501

        :param overrides: The overrides of this HealthcheckEvaluationCreateParams.  # noqa: E501
        :type: list[HealthcheckEvaluationOverride]
        """

        self._overrides = overrides

    @property
    def parameters(self):
        """Gets the parameters of this HealthcheckEvaluationCreateParams.  # noqa: E501

        Parameters supplied for this evaluation  # noqa: E501

        :return: The parameters of this HealthcheckEvaluationCreateParams.  # noqa: E501
        :rtype: Empty
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this HealthcheckEvaluationCreateParams.

        Parameters supplied for this evaluation  # noqa: E501

        :param parameters: The parameters of this HealthcheckEvaluationCreateParams.  # noqa: E501
        :type: Empty
        """

        self._parameters = parameters

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
        if not isinstance(other, HealthcheckEvaluationCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
