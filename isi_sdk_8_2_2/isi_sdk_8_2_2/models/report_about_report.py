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


class ReportAboutReport(object):
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
        'generated': 'str',
        'id': 'str',
        'time': 'int',
        'type': 'str'
    }

    attribute_map = {
        'generated': 'generated',
        'id': 'id',
        'time': 'time',
        'type': 'type'
    }

    def __init__(self, generated=None, id=None, time=None, type=None):  # noqa: E501
        """ReportAboutReport - a model defined in Swagger"""  # noqa: E501

        self._generated = None
        self._id = None
        self._time = None
        self._type = None
        self.discriminator = None

        self.generated = generated
        self.id = id
        self.time = time
        self.type = type

    @property
    def generated(self):
        """Gets the generated of this ReportAboutReport.  # noqa: E501

        Whether report was manually requested (live) or scheduled.  # noqa: E501

        :return: The generated of this ReportAboutReport.  # noqa: E501
        :rtype: str
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this ReportAboutReport.

        Whether report was manually requested (live) or scheduled.  # noqa: E501

        :param generated: The generated of this ReportAboutReport.  # noqa: E501
        :type: str
        """
        if generated is None:
            raise ValueError("Invalid value for `generated`, must not be `None`")  # noqa: E501
        allowed_values = ["manual", "scheduled"]  # noqa: E501
        if generated not in allowed_values:
            raise ValueError(
                "Invalid value for `generated` ({0}), must be one of {1}"  # noqa: E501
                .format(generated, allowed_values)
            )

        self._generated = generated

    @property
    def id(self):
        """Gets the id of this ReportAboutReport.  # noqa: E501

        The system ID given to the report.  # noqa: E501

        :return: The id of this ReportAboutReport.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReportAboutReport.

        The system ID given to the report.  # noqa: E501

        :param id: The id of this ReportAboutReport.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def time(self):
        """Gets the time of this ReportAboutReport.  # noqa: E501

        Unix epoch time the report was taken.  # noqa: E501

        :return: The time of this ReportAboutReport.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ReportAboutReport.

        Unix epoch time the report was taken.  # noqa: E501

        :param time: The time of this ReportAboutReport.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def type(self):
        """Gets the type of this ReportAboutReport.  # noqa: E501

        Whether this is a summary or detail report.  # noqa: E501

        :return: The type of this ReportAboutReport.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ReportAboutReport.

        Whether this is a summary or detail report.  # noqa: E501

        :param type: The type of this ReportAboutReport.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["summary", "detail"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, ReportAboutReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
