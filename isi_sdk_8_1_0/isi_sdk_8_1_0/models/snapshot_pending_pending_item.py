# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 5
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SnapshotPendingPendingItem(object):
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
        'id': 'str',
        'path': 'str',
        'schedule': 'str',
        'snapshot': 'str',
        'time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'path': 'path',
        'schedule': 'schedule',
        'snapshot': 'snapshot',
        'time': 'time'
    }

    def __init__(self, id=None, path=None, schedule=None, snapshot=None, time=None):  # noqa: E501
        """SnapshotPendingPendingItem - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._path = None
        self._schedule = None
        self._snapshot = None
        self._time = None
        self.discriminator = None

        self.id = id
        self.path = path
        self.schedule = schedule
        self.snapshot = snapshot
        self.time = time

    @property
    def id(self):
        """Gets the id of this SnapshotPendingPendingItem.  # noqa: E501

        The system supplied unique ID used for sorting and paging.  # noqa: E501

        :return: The id of this SnapshotPendingPendingItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SnapshotPendingPendingItem.

        The system supplied unique ID used for sorting and paging.  # noqa: E501

        :param id: The id of this SnapshotPendingPendingItem.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def path(self):
        """Gets the path of this SnapshotPendingPendingItem.  # noqa: E501

        The /ifs path that will snapshotted.  # noqa: E501

        :return: The path of this SnapshotPendingPendingItem.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SnapshotPendingPendingItem.

        The /ifs path that will snapshotted.  # noqa: E501

        :param path: The path of this SnapshotPendingPendingItem.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def schedule(self):
        """Gets the schedule of this SnapshotPendingPendingItem.  # noqa: E501

        The name of the schedule used to create this snapshot.  # noqa: E501

        :return: The schedule of this SnapshotPendingPendingItem.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this SnapshotPendingPendingItem.

        The name of the schedule used to create this snapshot.  # noqa: E501

        :param schedule: The schedule of this SnapshotPendingPendingItem.  # noqa: E501
        :type: str
        """
        if schedule is None:
            raise ValueError("Invalid value for `schedule`, must not be `None`")  # noqa: E501

        self._schedule = schedule

    @property
    def snapshot(self):
        """Gets the snapshot of this SnapshotPendingPendingItem.  # noqa: E501

        The system snapshot name formed from the schedule formate.  # noqa: E501

        :return: The snapshot of this SnapshotPendingPendingItem.  # noqa: E501
        :rtype: str
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        """Sets the snapshot of this SnapshotPendingPendingItem.

        The system snapshot name formed from the schedule formate.  # noqa: E501

        :param snapshot: The snapshot of this SnapshotPendingPendingItem.  # noqa: E501
        :type: str
        """
        if snapshot is None:
            raise ValueError("Invalid value for `snapshot`, must not be `None`")  # noqa: E501

        self._snapshot = snapshot

    @property
    def time(self):
        """Gets the time of this SnapshotPendingPendingItem.  # noqa: E501

        The Unix Epoch time the snapshot will be created.  # noqa: E501

        :return: The time of this SnapshotPendingPendingItem.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SnapshotPendingPendingItem.

        The Unix Epoch time the snapshot will be created.  # noqa: E501

        :param time: The time of this SnapshotPendingPendingItem.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

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
        if not isinstance(other, SnapshotPendingPendingItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
