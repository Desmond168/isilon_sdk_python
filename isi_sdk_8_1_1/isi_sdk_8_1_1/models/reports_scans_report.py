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


class ReportsScansReport(object):
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
        'bytes_sent': 'int',
        'duration': 'int',
        'end': 'int',
        'files': 'int',
        'id': 'str',
        'infections': 'int',
        'job_id': 'int',
        'policy_id': 'str',
        'size': 'int',
        'start': 'int',
        'status': 'str'
    }

    attribute_map = {
        'bytes_sent': 'bytes_sent',
        'duration': 'duration',
        'end': 'end',
        'files': 'files',
        'id': 'id',
        'infections': 'infections',
        'job_id': 'job_id',
        'policy_id': 'policy_id',
        'size': 'size',
        'start': 'start',
        'status': 'status'
    }

    def __init__(self, bytes_sent=None, duration=None, end=None, files=None, id=None, infections=None, job_id=None, policy_id=None, size=None, start=None, status=None):  # noqa: E501
        """ReportsScansReport - a model defined in Swagger"""  # noqa: E501

        self._bytes_sent = None
        self._duration = None
        self._end = None
        self._files = None
        self._id = None
        self._infections = None
        self._job_id = None
        self._policy_id = None
        self._size = None
        self._start = None
        self._status = None
        self.discriminator = None

        if bytes_sent is not None:
            self.bytes_sent = bytes_sent
        if duration is not None:
            self.duration = duration
        if end is not None:
            self.end = end
        if files is not None:
            self.files = files
        if id is not None:
            self.id = id
        if infections is not None:
            self.infections = infections
        if job_id is not None:
            self.job_id = job_id
        if policy_id is not None:
            self.policy_id = policy_id
        if size is not None:
            self.size = size
        if start is not None:
            self.start = start
        if status is not None:
            self.status = status

    @property
    def bytes_sent(self):
        """Gets the bytes_sent of this ReportsScansReport.  # noqa: E501

        The number of bytes sent to the virus definition server to be scanned.  # noqa: E501

        :return: The bytes_sent of this ReportsScansReport.  # noqa: E501
        :rtype: int
        """
        return self._bytes_sent

    @bytes_sent.setter
    def bytes_sent(self, bytes_sent):
        """Sets the bytes_sent of this ReportsScansReport.

        The number of bytes sent to the virus definition server to be scanned.  # noqa: E501

        :param bytes_sent: The bytes_sent of this ReportsScansReport.  # noqa: E501
        :type: int
        """
        if bytes_sent is not None and bytes_sent > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `bytes_sent`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if bytes_sent is not None and bytes_sent < 0:  # noqa: E501
            raise ValueError("Invalid value for `bytes_sent`, must be a value greater than or equal to `0`")  # noqa: E501

        self._bytes_sent = bytes_sent

    @property
    def duration(self):
        """Gets the duration of this ReportsScansReport.  # noqa: E501

        The length of time the job ran for.  # noqa: E501

        :return: The duration of this ReportsScansReport.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ReportsScansReport.

        The length of time the job ran for.  # noqa: E501

        :param duration: The duration of this ReportsScansReport.  # noqa: E501
        :type: int
        """
        if duration is not None and duration > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if duration is not None and duration < 0:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `0`")  # noqa: E501

        self._duration = duration

    @property
    def end(self):
        """Gets the end of this ReportsScansReport.  # noqa: E501


        :return: The end of this ReportsScansReport.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this ReportsScansReport.


        :param end: The end of this ReportsScansReport.  # noqa: E501
        :type: int
        """
        if end is not None and end > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `end`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if end is not None and end < 0:  # noqa: E501
            raise ValueError("Invalid value for `end`, must be a value greater than or equal to `0`")  # noqa: E501

        self._end = end

    @property
    def files(self):
        """Gets the files of this ReportsScansReport.  # noqa: E501

        The number of files scanned.  # noqa: E501

        :return: The files of this ReportsScansReport.  # noqa: E501
        :rtype: int
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ReportsScansReport.

        The number of files scanned.  # noqa: E501

        :param files: The files of this ReportsScansReport.  # noqa: E501
        :type: int
        """
        if files is not None and files > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `files`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if files is not None and files < 0:  # noqa: E501
            raise ValueError("Invalid value for `files`, must be a value greater than or equal to `0`")  # noqa: E501

        self._files = files

    @property
    def id(self):
        """Gets the id of this ReportsScansReport.  # noqa: E501

        A unique identifier for the report.  # noqa: E501

        :return: The id of this ReportsScansReport.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReportsScansReport.

        A unique identifier for the report.  # noqa: E501

        :param id: The id of this ReportsScansReport.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def infections(self):
        """Gets the infections of this ReportsScansReport.  # noqa: E501

        The number of infections found.  # noqa: E501

        :return: The infections of this ReportsScansReport.  # noqa: E501
        :rtype: int
        """
        return self._infections

    @infections.setter
    def infections(self, infections):
        """Sets the infections of this ReportsScansReport.

        The number of infections found.  # noqa: E501

        :param infections: The infections of this ReportsScansReport.  # noqa: E501
        :type: int
        """
        if infections is not None and infections > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `infections`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if infections is not None and infections < 0:  # noqa: E501
            raise ValueError("Invalid value for `infections`, must be a value greater than or equal to `0`")  # noqa: E501

        self._infections = infections

    @property
    def job_id(self):
        """Gets the job_id of this ReportsScansReport.  # noqa: E501


        :return: The job_id of this ReportsScansReport.  # noqa: E501
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ReportsScansReport.


        :param job_id: The job_id of this ReportsScansReport.  # noqa: E501
        :type: int
        """
        if job_id is not None and job_id > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `job_id`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if job_id is not None and job_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `job_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._job_id = job_id

    @property
    def policy_id(self):
        """Gets the policy_id of this ReportsScansReport.  # noqa: E501

        The id of the policy that this scan job executed.  # noqa: E501

        :return: The policy_id of this ReportsScansReport.  # noqa: E501
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this ReportsScansReport.

        The id of the policy that this scan job executed.  # noqa: E501

        :param policy_id: The policy_id of this ReportsScansReport.  # noqa: E501
        :type: str
        """
        if policy_id is not None and len(policy_id) > 255:
            raise ValueError("Invalid value for `policy_id`, length must be less than or equal to `255`")  # noqa: E501
        if policy_id is not None and len(policy_id) < 0:
            raise ValueError("Invalid value for `policy_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._policy_id = policy_id

    @property
    def size(self):
        """Gets the size of this ReportsScansReport.  # noqa: E501

        The cumulative size of the files scanned.  # noqa: E501

        :return: The size of this ReportsScansReport.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ReportsScansReport.

        The cumulative size of the files scanned.  # noqa: E501

        :param size: The size of this ReportsScansReport.  # noqa: E501
        :type: int
        """
        if size is not None and size > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if size is not None and size < 0:  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._size = size

    @property
    def start(self):
        """Gets the start of this ReportsScansReport.  # noqa: E501


        :return: The start of this ReportsScansReport.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ReportsScansReport.


        :param start: The start of this ReportsScansReport.  # noqa: E501
        :type: int
        """
        if start is not None and start > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `start`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if start is not None and start < 0:  # noqa: E501
            raise ValueError("Invalid value for `start`, must be a value greater than or equal to `0`")  # noqa: E501

        self._start = start

    @property
    def status(self):
        """Gets the status of this ReportsScansReport.  # noqa: E501

        The state of the job.  # noqa: E501

        :return: The status of this ReportsScansReport.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ReportsScansReport.

        The state of the job.  # noqa: E501

        :param status: The status of this ReportsScansReport.  # noqa: E501
        :type: str
        """
        if status is not None and len(status) > 255:
            raise ValueError("Invalid value for `status`, length must be less than or equal to `255`")  # noqa: E501
        if status is not None and len(status) < 0:
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `0`")  # noqa: E501

        self._status = status

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
        if not isinstance(other, ReportsScansReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
