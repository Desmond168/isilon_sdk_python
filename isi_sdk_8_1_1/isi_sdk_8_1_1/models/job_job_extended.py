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


class JobJobExtended(object):
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
        'control_state': 'str',
        'create_time': 'int',
        'current_phase': 'int',
        'description': 'str',
        'end_time': 'int',
        'id': 'int',
        'impact': 'str',
        'participants': 'list[int]',
        'paths': 'list[str]',
        'policy': 'str',
        'priority': 'int',
        'progress': 'str',
        'retries_remaining': 'int',
        'running_time': 'int',
        'start_time': 'int',
        'state': 'str',
        'total_phases': 'int',
        'type': 'str',
        'waiting_on': 'int',
        'waiting_reason': 'str'
    }

    attribute_map = {
        'control_state': 'control_state',
        'create_time': 'create_time',
        'current_phase': 'current_phase',
        'description': 'description',
        'end_time': 'end_time',
        'id': 'id',
        'impact': 'impact',
        'participants': 'participants',
        'paths': 'paths',
        'policy': 'policy',
        'priority': 'priority',
        'progress': 'progress',
        'retries_remaining': 'retries_remaining',
        'running_time': 'running_time',
        'start_time': 'start_time',
        'state': 'state',
        'total_phases': 'total_phases',
        'type': 'type',
        'waiting_on': 'waiting_on',
        'waiting_reason': 'waiting_reason'
    }

    def __init__(self, control_state=None, create_time=None, current_phase=None, description=None, end_time=None, id=None, impact=None, participants=None, paths=None, policy=None, priority=None, progress=None, retries_remaining=None, running_time=None, start_time=None, state=None, total_phases=None, type=None, waiting_on=None, waiting_reason=None):  # noqa: E501
        """JobJobExtended - a model defined in Swagger"""  # noqa: E501

        self._control_state = None
        self._create_time = None
        self._current_phase = None
        self._description = None
        self._end_time = None
        self._id = None
        self._impact = None
        self._participants = None
        self._paths = None
        self._policy = None
        self._priority = None
        self._progress = None
        self._retries_remaining = None
        self._running_time = None
        self._start_time = None
        self._state = None
        self._total_phases = None
        self._type = None
        self._waiting_on = None
        self._waiting_reason = None
        self.discriminator = None

        if control_state is not None:
            self.control_state = control_state
        self.create_time = create_time
        if current_phase is not None:
            self.current_phase = current_phase
        if description is not None:
            self.description = description
        if end_time is not None:
            self.end_time = end_time
        self.id = id
        self.impact = impact
        if participants is not None:
            self.participants = participants
        if paths is not None:
            self.paths = paths
        self.policy = policy
        self.priority = priority
        if progress is not None:
            self.progress = progress
        self.retries_remaining = retries_remaining
        if running_time is not None:
            self.running_time = running_time
        if start_time is not None:
            self.start_time = start_time
        self.state = state
        self.total_phases = total_phases
        self.type = type
        if waiting_on is not None:
            self.waiting_on = waiting_on
        if waiting_reason is not None:
            self.waiting_reason = waiting_reason

    @property
    def control_state(self):
        """Gets the control_state of this JobJobExtended.  # noqa: E501

        State to which the job is transitioning; if control_state is identical to state, the job's state is stable.  # noqa: E501

        :return: The control_state of this JobJobExtended.  # noqa: E501
        :rtype: str
        """
        return self._control_state

    @control_state.setter
    def control_state(self, control_state):
        """Sets the control_state of this JobJobExtended.

        State to which the job is transitioning; if control_state is identical to state, the job's state is stable.  # noqa: E501

        :param control_state: The control_state of this JobJobExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["running", "paused_user", "paused_system", "paused_policy", "paused_priority", "cancelled_user", "cancelled_system", "failed", "succeeded", "unknown"]  # noqa: E501
        if control_state not in allowed_values:
            raise ValueError(
                "Invalid value for `control_state` ({0}), must be one of {1}"  # noqa: E501
                .format(control_state, allowed_values)
            )

        self._control_state = control_state

    @property
    def create_time(self):
        """Gets the create_time of this JobJobExtended.  # noqa: E501

        The time the job was queued, in seconds since the epoch.  # noqa: E501

        :return: The create_time of this JobJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this JobJobExtended.

        The time the job was queued, in seconds since the epoch.  # noqa: E501

        :param create_time: The create_time of this JobJobExtended.  # noqa: E501
        :type: int
        """
        if create_time is None:
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def current_phase(self):
        """Gets the current_phase of this JobJobExtended.  # noqa: E501

        The current phase of the job.  # noqa: E501

        :return: The current_phase of this JobJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._current_phase

    @current_phase.setter
    def current_phase(self, current_phase):
        """Sets the current_phase of this JobJobExtended.

        The current phase of the job.  # noqa: E501

        :param current_phase: The current_phase of this JobJobExtended.  # noqa: E501
        :type: int
        """

        self._current_phase = current_phase

    @property
    def description(self):
        """Gets the description of this JobJobExtended.  # noqa: E501

        A text representation of the job.  # noqa: E501

        :return: The description of this JobJobExtended.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JobJobExtended.

        A text representation of the job.  # noqa: E501

        :param description: The description of this JobJobExtended.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end_time(self):
        """Gets the end_time of this JobJobExtended.  # noqa: E501

        The time the job ended, in seconds since the Epoch.  # noqa: E501

        :return: The end_time of this JobJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this JobJobExtended.

        The time the job ended, in seconds since the Epoch.  # noqa: E501

        :param end_time: The end_time of this JobJobExtended.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def id(self):
        """Gets the id of this JobJobExtended.  # noqa: E501

        The ID of the job.  # noqa: E501

        :return: The id of this JobJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobJobExtended.

        The ID of the job.  # noqa: E501

        :param id: The id of this JobJobExtended.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and id < 1:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def impact(self):
        """Gets the impact of this JobJobExtended.  # noqa: E501

        The current impact of the job.  # noqa: E501

        :return: The impact of this JobJobExtended.  # noqa: E501
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        """Sets the impact of this JobJobExtended.

        The current impact of the job.  # noqa: E501

        :param impact: The impact of this JobJobExtended.  # noqa: E501
        :type: str
        """
        if impact is None:
            raise ValueError("Invalid value for `impact`, must not be `None`")  # noqa: E501
        allowed_values = ["Low", "Medium", "High", "Paused"]  # noqa: E501
        if impact not in allowed_values:
            raise ValueError(
                "Invalid value for `impact` ({0}), must be one of {1}"  # noqa: E501
                .format(impact, allowed_values)
            )

        self._impact = impact

    @property
    def participants(self):
        """Gets the participants of this JobJobExtended.  # noqa: E501

        The set of devids working on the job.  # noqa: E501

        :return: The participants of this JobJobExtended.  # noqa: E501
        :rtype: list[int]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """Sets the participants of this JobJobExtended.

        The set of devids working on the job.  # noqa: E501

        :param participants: The participants of this JobJobExtended.  # noqa: E501
        :type: list[int]
        """

        self._participants = participants

    @property
    def paths(self):
        """Gets the paths of this JobJobExtended.  # noqa: E501

        Paths for which the job was queued.  # noqa: E501

        :return: The paths of this JobJobExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this JobJobExtended.

        Paths for which the job was queued.  # noqa: E501

        :param paths: The paths of this JobJobExtended.  # noqa: E501
        :type: list[str]
        """

        self._paths = paths

    @property
    def policy(self):
        """Gets the policy of this JobJobExtended.  # noqa: E501

        Current impact policy of the job.  # noqa: E501

        :return: The policy of this JobJobExtended.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this JobJobExtended.

        Current impact policy of the job.  # noqa: E501

        :param policy: The policy of this JobJobExtended.  # noqa: E501
        :type: str
        """
        if policy is None:
            raise ValueError("Invalid value for `policy`, must not be `None`")  # noqa: E501

        self._policy = policy

    @property
    def priority(self):
        """Gets the priority of this JobJobExtended.  # noqa: E501

        Current priority of the job; lower numbers preempt higher numbers.  # noqa: E501

        :return: The priority of this JobJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this JobJobExtended.

        Current priority of the job; lower numbers preempt higher numbers.  # noqa: E501

        :param priority: The priority of this JobJobExtended.  # noqa: E501
        :type: int
        """
        if priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501
        if priority is not None and priority > 10:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value less than or equal to `10`")  # noqa: E501
        if priority is not None and priority < 1:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `1`")  # noqa: E501

        self._priority = priority

    @property
    def progress(self):
        """Gets the progress of this JobJobExtended.  # noqa: E501

        A text representation of the job's progress.  # noqa: E501

        :return: The progress of this JobJobExtended.  # noqa: E501
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this JobJobExtended.

        A text representation of the job's progress.  # noqa: E501

        :param progress: The progress of this JobJobExtended.  # noqa: E501
        :type: str
        """

        self._progress = progress

    @property
    def retries_remaining(self):
        """Gets the retries_remaining of this JobJobExtended.  # noqa: E501

        The number of retries remaining if the job fails.  # noqa: E501

        :return: The retries_remaining of this JobJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._retries_remaining

    @retries_remaining.setter
    def retries_remaining(self, retries_remaining):
        """Sets the retries_remaining of this JobJobExtended.

        The number of retries remaining if the job fails.  # noqa: E501

        :param retries_remaining: The retries_remaining of this JobJobExtended.  # noqa: E501
        :type: int
        """
        if retries_remaining is None:
            raise ValueError("Invalid value for `retries_remaining`, must not be `None`")  # noqa: E501

        self._retries_remaining = retries_remaining

    @property
    def running_time(self):
        """Gets the running_time of this JobJobExtended.  # noqa: E501

        The number of seconds the job has executed.  # noqa: E501

        :return: The running_time of this JobJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._running_time

    @running_time.setter
    def running_time(self, running_time):
        """Sets the running_time of this JobJobExtended.

        The number of seconds the job has executed.  # noqa: E501

        :param running_time: The running_time of this JobJobExtended.  # noqa: E501
        :type: int
        """

        self._running_time = running_time

    @property
    def start_time(self):
        """Gets the start_time of this JobJobExtended.  # noqa: E501

        The time the job started, in seconds since the Epoch.  # noqa: E501

        :return: The start_time of this JobJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this JobJobExtended.

        The time the job started, in seconds since the Epoch.  # noqa: E501

        :param start_time: The start_time of this JobJobExtended.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def state(self):
        """Gets the state of this JobJobExtended.  # noqa: E501

        Current state of the job.  # noqa: E501

        :return: The state of this JobJobExtended.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this JobJobExtended.

        Current state of the job.  # noqa: E501

        :param state: The state of this JobJobExtended.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["running", "paused_user", "paused_system", "paused_policy", "paused_priority", "cancelled_user", "cancelled_system", "failed", "succeeded", "unknown"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def total_phases(self):
        """Gets the total_phases of this JobJobExtended.  # noqa: E501

        The total number of phases of the job type.  # noqa: E501

        :return: The total_phases of this JobJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._total_phases

    @total_phases.setter
    def total_phases(self, total_phases):
        """Sets the total_phases of this JobJobExtended.

        The total number of phases of the job type.  # noqa: E501

        :param total_phases: The total_phases of this JobJobExtended.  # noqa: E501
        :type: int
        """
        if total_phases is None:
            raise ValueError("Invalid value for `total_phases`, must not be `None`")  # noqa: E501

        self._total_phases = total_phases

    @property
    def type(self):
        """Gets the type of this JobJobExtended.  # noqa: E501

        The job type.  # noqa: E501

        :return: The type of this JobJobExtended.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JobJobExtended.

        The job type.  # noqa: E501

        :param type: The type of this JobJobExtended.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def waiting_on(self):
        """Gets the waiting_on of this JobJobExtended.  # noqa: E501

        The ID of a job for which this job is waiting.  # noqa: E501

        :return: The waiting_on of this JobJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._waiting_on

    @waiting_on.setter
    def waiting_on(self, waiting_on):
        """Sets the waiting_on of this JobJobExtended.

        The ID of a job for which this job is waiting.  # noqa: E501

        :param waiting_on: The waiting_on of this JobJobExtended.  # noqa: E501
        :type: int
        """

        self._waiting_on = waiting_on

    @property
    def waiting_reason(self):
        """Gets the waiting_reason of this JobJobExtended.  # noqa: E501

        The reason the job is waiting.  # noqa: E501

        :return: The waiting_reason of this JobJobExtended.  # noqa: E501
        :rtype: str
        """
        return self._waiting_reason

    @waiting_reason.setter
    def waiting_reason(self, waiting_reason):
        """Sets the waiting_reason of this JobJobExtended.

        The reason the job is waiting.  # noqa: E501

        :param waiting_reason: The waiting_reason of this JobJobExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["blocked_by_priority"]  # noqa: E501
        if waiting_reason not in allowed_values:
            raise ValueError(
                "Invalid value for `waiting_reason` ({0}), must be one of {1}"  # noqa: E501
                .format(waiting_reason, allowed_values)
            )

        self._waiting_reason = waiting_reason

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
        if not isinstance(other, JobJobExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
