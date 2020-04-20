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

from isi_sdk_8_2_1.models.dataset_filter import DatasetFilter  # noqa: F401,E501
from isi_sdk_8_2_1.models.dataset_filter_metric_values import DatasetFilterMetricValues  # noqa: F401,E501


class DatasetFilterExtended(object):
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
        'name': 'str',
        'creation_time': 'int',
        'dataset_id': 'int',
        'error': 'str',
        'id': 'int',
        'metric_values': 'DatasetFilterMetricValues'
    }

    attribute_map = {
        'name': 'name',
        'creation_time': 'creation_time',
        'dataset_id': 'dataset_id',
        'error': 'error',
        'id': 'id',
        'metric_values': 'metric_values'
    }

    def __init__(self, name=None, creation_time=None, dataset_id=None, error=None, id=None, metric_values=None):  # noqa: E501
        """DatasetFilterExtended - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._creation_time = None
        self._dataset_id = None
        self._error = None
        self._id = None
        self._metric_values = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if creation_time is not None:
            self.creation_time = creation_time
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if error is not None:
            self.error = error
        self.id = id
        if metric_values is not None:
            self.metric_values = metric_values

    @property
    def name(self):
        """Gets the name of this DatasetFilterExtended.  # noqa: E501

        The name of the filter. User specified.  # noqa: E501

        :return: The name of this DatasetFilterExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatasetFilterExtended.

        The name of the filter. User specified.  # noqa: E501

        :param name: The name of this DatasetFilterExtended.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 80:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `80`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def creation_time(self):
        """Gets the creation_time of this DatasetFilterExtended.  # noqa: E501

        Timestamp of when the filter was applied.  # noqa: E501

        :return: The creation_time of this DatasetFilterExtended.  # noqa: E501
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this DatasetFilterExtended.

        Timestamp of when the filter was applied.  # noqa: E501

        :param creation_time: The creation_time of this DatasetFilterExtended.  # noqa: E501
        :type: int
        """
        if creation_time is not None and creation_time > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `creation_time`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if creation_time is not None and creation_time < 0:  # noqa: E501
            raise ValueError("Invalid value for `creation_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._creation_time = creation_time

    @property
    def dataset_id(self):
        """Gets the dataset_id of this DatasetFilterExtended.  # noqa: E501

        Unique identifier of the associated dataset.  # noqa: E501

        :return: The dataset_id of this DatasetFilterExtended.  # noqa: E501
        :rtype: int
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this DatasetFilterExtended.

        Unique identifier of the associated dataset.  # noqa: E501

        :param dataset_id: The dataset_id of this DatasetFilterExtended.  # noqa: E501
        :type: int
        """
        if dataset_id is not None and dataset_id > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `dataset_id`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if dataset_id is not None and dataset_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `dataset_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._dataset_id = dataset_id

    @property
    def error(self):
        """Gets the error of this DatasetFilterExtended.  # noqa: E501

        If this field is present, then there was an error fetching the filter configuration.  # noqa: E501

        :return: The error of this DatasetFilterExtended.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this DatasetFilterExtended.

        If this field is present, then there was an error fetching the filter configuration.  # noqa: E501

        :param error: The error of this DatasetFilterExtended.  # noqa: E501
        :type: str
        """
        if error is not None and len(error) > 255:
            raise ValueError("Invalid value for `error`, length must be less than or equal to `255`")  # noqa: E501
        if error is not None and len(error) < 1:
            raise ValueError("Invalid value for `error`, length must be greater than or equal to `1`")  # noqa: E501

        self._error = error

    @property
    def id(self):
        """Gets the id of this DatasetFilterExtended.  # noqa: E501

        The filter ID. Unique and automatically assigned.  # noqa: E501

        :return: The id of this DatasetFilterExtended.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatasetFilterExtended.

        The filter ID. Unique and automatically assigned.  # noqa: E501

        :param id: The id of this DatasetFilterExtended.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and id > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def metric_values(self):
        """Gets the metric_values of this DatasetFilterExtended.  # noqa: E501

        Performance metric values that can be used to pin workloads and apply filters, and performance metric values that are used to display information about the system performance dataset.  # noqa: E501

        :return: The metric_values of this DatasetFilterExtended.  # noqa: E501
        :rtype: DatasetFilterMetricValues
        """
        return self._metric_values

    @metric_values.setter
    def metric_values(self, metric_values):
        """Sets the metric_values of this DatasetFilterExtended.

        Performance metric values that can be used to pin workloads and apply filters, and performance metric values that are used to display information about the system performance dataset.  # noqa: E501

        :param metric_values: The metric_values of this DatasetFilterExtended.  # noqa: E501
        :type: DatasetFilterMetricValues
        """

        self._metric_values = metric_values

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
        if not isinstance(other, DatasetFilterExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
