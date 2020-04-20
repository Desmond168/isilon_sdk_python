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


class JobStatisticsJobNodeWorker(object):
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
        'stw': 'float',
        'task': 'str',
        'task_result': 'str',
        'worker': 'int'
    }

    attribute_map = {
        'stw': 'stw',
        'task': 'task',
        'task_result': 'task_result',
        'worker': 'worker'
    }

    def __init__(self, stw=None, task=None, task_result=None, worker=None):  # noqa: E501
        """JobStatisticsJobNodeWorker - a model defined in Swagger"""  # noqa: E501

        self._stw = None
        self._task = None
        self._task_result = None
        self._worker = None
        self.discriminator = None

        if stw is not None:
            self.stw = stw
        if task is not None:
            self.task = task
        if task_result is not None:
            self.task_result = task_result
        self.worker = worker

    @property
    def stw(self):
        """Gets the stw of this JobStatisticsJobNodeWorker.  # noqa: E501

        The sleep-to-work ratio of this worker; how much time it spends sleeping compared to working.  # noqa: E501

        :return: The stw of this JobStatisticsJobNodeWorker.  # noqa: E501
        :rtype: float
        """
        return self._stw

    @stw.setter
    def stw(self, stw):
        """Sets the stw of this JobStatisticsJobNodeWorker.

        The sleep-to-work ratio of this worker; how much time it spends sleeping compared to working.  # noqa: E501

        :param stw: The stw of this JobStatisticsJobNodeWorker.  # noqa: E501
        :type: float
        """

        self._stw = stw

    @property
    def task(self):
        """Gets the task of this JobStatisticsJobNodeWorker.  # noqa: E501

        A representation of the task the worker is currently processing; not intended to be read by humans.  # noqa: E501

        :return: The task of this JobStatisticsJobNodeWorker.  # noqa: E501
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this JobStatisticsJobNodeWorker.

        A representation of the task the worker is currently processing; not intended to be read by humans.  # noqa: E501

        :param task: The task of this JobStatisticsJobNodeWorker.  # noqa: E501
        :type: str
        """

        self._task = task

    @property
    def task_result(self):
        """Gets the task_result of this JobStatisticsJobNodeWorker.  # noqa: E501

        A representation of the most recent task result produced by the worker; not intended to be read by humans.  # noqa: E501

        :return: The task_result of this JobStatisticsJobNodeWorker.  # noqa: E501
        :rtype: str
        """
        return self._task_result

    @task_result.setter
    def task_result(self, task_result):
        """Sets the task_result of this JobStatisticsJobNodeWorker.

        A representation of the most recent task result produced by the worker; not intended to be read by humans.  # noqa: E501

        :param task_result: The task_result of this JobStatisticsJobNodeWorker.  # noqa: E501
        :type: str
        """

        self._task_result = task_result

    @property
    def worker(self):
        """Gets the worker of this JobStatisticsJobNodeWorker.  # noqa: E501

        The worker ID.  # noqa: E501

        :return: The worker of this JobStatisticsJobNodeWorker.  # noqa: E501
        :rtype: int
        """
        return self._worker

    @worker.setter
    def worker(self, worker):
        """Sets the worker of this JobStatisticsJobNodeWorker.

        The worker ID.  # noqa: E501

        :param worker: The worker of this JobStatisticsJobNodeWorker.  # noqa: E501
        :type: int
        """
        if worker is None:
            raise ValueError("Invalid value for `worker`, must not be `None`")  # noqa: E501

        self._worker = worker

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
        if not isinstance(other, JobStatisticsJobNodeWorker):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
