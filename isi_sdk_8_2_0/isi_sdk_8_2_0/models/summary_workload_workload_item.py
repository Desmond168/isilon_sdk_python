# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 7
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SummaryWorkloadWorkloadItem(object):
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
        'bytes_in': 'float',
        'bytes_out': 'float',
        'cpu': 'float',
        'domain_id': 'str',
        'error': 'str',
        'group_id': 'float',
        'group_sid': 'str',
        'groupname': 'str',
        'job_type': 'str',
        'l2': 'float',
        'l3': 'float',
        'local_addr': 'str',
        'local_name': 'str',
        'node': 'float',
        'ops': 'float',
        'path': 'str',
        'protocol': 'str',
        'reads': 'float',
        'remote_addr': 'str',
        'remote_name': 'str',
        'share_name': 'str',
        'system_name': 'str',
        'time': 'int',
        'user_id': 'float',
        'user_sid': 'str',
        'username': 'str',
        'workload_id': 'int',
        'workload_type': 'str',
        'writes': 'float',
        'zone_id': 'float',
        'zone_name': 'str'
    }

    attribute_map = {
        'bytes_in': 'bytes_in',
        'bytes_out': 'bytes_out',
        'cpu': 'cpu',
        'domain_id': 'domain_id',
        'error': 'error',
        'group_id': 'group_id',
        'group_sid': 'group_sid',
        'groupname': 'groupname',
        'job_type': 'job_type',
        'l2': 'l2',
        'l3': 'l3',
        'local_addr': 'local_addr',
        'local_name': 'local_name',
        'node': 'node',
        'ops': 'ops',
        'path': 'path',
        'protocol': 'protocol',
        'reads': 'reads',
        'remote_addr': 'remote_addr',
        'remote_name': 'remote_name',
        'share_name': 'share_name',
        'system_name': 'system_name',
        'time': 'time',
        'user_id': 'user_id',
        'user_sid': 'user_sid',
        'username': 'username',
        'workload_id': 'workload_id',
        'workload_type': 'workload_type',
        'writes': 'writes',
        'zone_id': 'zone_id',
        'zone_name': 'zone_name'
    }

    def __init__(self, bytes_in=None, bytes_out=None, cpu=None, domain_id=None, error=None, group_id=None, group_sid=None, groupname=None, job_type=None, l2=None, l3=None, local_addr=None, local_name=None, node=None, ops=None, path=None, protocol=None, reads=None, remote_addr=None, remote_name=None, share_name=None, system_name=None, time=None, user_id=None, user_sid=None, username=None, workload_id=None, workload_type=None, writes=None, zone_id=None, zone_name=None):  # noqa: E501
        """SummaryWorkloadWorkloadItem - a model defined in Swagger"""  # noqa: E501

        self._bytes_in = None
        self._bytes_out = None
        self._cpu = None
        self._domain_id = None
        self._error = None
        self._group_id = None
        self._group_sid = None
        self._groupname = None
        self._job_type = None
        self._l2 = None
        self._l3 = None
        self._local_addr = None
        self._local_name = None
        self._node = None
        self._ops = None
        self._path = None
        self._protocol = None
        self._reads = None
        self._remote_addr = None
        self._remote_name = None
        self._share_name = None
        self._system_name = None
        self._time = None
        self._user_id = None
        self._user_sid = None
        self._username = None
        self._workload_id = None
        self._workload_type = None
        self._writes = None
        self._zone_id = None
        self._zone_name = None
        self.discriminator = None

        self.bytes_in = bytes_in
        self.bytes_out = bytes_out
        self.cpu = cpu
        if domain_id is not None:
            self.domain_id = domain_id
        if error is not None:
            self.error = error
        if group_id is not None:
            self.group_id = group_id
        if group_sid is not None:
            self.group_sid = group_sid
        if groupname is not None:
            self.groupname = groupname
        if job_type is not None:
            self.job_type = job_type
        self.l2 = l2
        self.l3 = l3
        if local_addr is not None:
            self.local_addr = local_addr
        if local_name is not None:
            self.local_name = local_name
        self.node = node
        self.ops = ops
        if path is not None:
            self.path = path
        if protocol is not None:
            self.protocol = protocol
        self.reads = reads
        if remote_addr is not None:
            self.remote_addr = remote_addr
        if remote_name is not None:
            self.remote_name = remote_name
        if share_name is not None:
            self.share_name = share_name
        if system_name is not None:
            self.system_name = system_name
        self.time = time
        if user_id is not None:
            self.user_id = user_id
        if user_sid is not None:
            self.user_sid = user_sid
        if username is not None:
            self.username = username
        if workload_id is not None:
            self.workload_id = workload_id
        if workload_type is not None:
            self.workload_type = workload_type
        self.writes = writes
        if zone_id is not None:
            self.zone_id = zone_id
        if zone_name is not None:
            self.zone_name = zone_name

    @property
    def bytes_in(self):
        """Gets the bytes_in of this SummaryWorkloadWorkloadItem.  # noqa: E501

        Count of bytes-in per second.  # noqa: E501

        :return: The bytes_in of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._bytes_in

    @bytes_in.setter
    def bytes_in(self, bytes_in):
        """Sets the bytes_in of this SummaryWorkloadWorkloadItem.

        Count of bytes-in per second.  # noqa: E501

        :param bytes_in: The bytes_in of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """
        if bytes_in is None:
            raise ValueError("Invalid value for `bytes_in`, must not be `None`")  # noqa: E501

        self._bytes_in = bytes_in

    @property
    def bytes_out(self):
        """Gets the bytes_out of this SummaryWorkloadWorkloadItem.  # noqa: E501

        Count of bytes-out per second.  # noqa: E501

        :return: The bytes_out of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._bytes_out

    @bytes_out.setter
    def bytes_out(self, bytes_out):
        """Sets the bytes_out of this SummaryWorkloadWorkloadItem.

        Count of bytes-out per second.  # noqa: E501

        :param bytes_out: The bytes_out of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """
        if bytes_out is None:
            raise ValueError("Invalid value for `bytes_out`, must not be `None`")  # noqa: E501

        self._bytes_out = bytes_out

    @property
    def cpu(self):
        """Gets the cpu of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The number (across all cores) of micro-seconds per second.  # noqa: E501

        :return: The cpu of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this SummaryWorkloadWorkloadItem.

        The number (across all cores) of micro-seconds per second.  # noqa: E501

        :param cpu: The cpu of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """
        if cpu is None:
            raise ValueError("Invalid value for `cpu`, must not be `None`")  # noqa: E501

        self._cpu = cpu

    @property
    def domain_id(self):
        """Gets the domain_id of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The IFS domain of the path which the operation was requested on.  # noqa: E501

        :return: The domain_id of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this SummaryWorkloadWorkloadItem.

        The IFS domain of the path which the operation was requested on.  # noqa: E501

        :param domain_id: The domain_id of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def error(self):
        """Gets the error of this SummaryWorkloadWorkloadItem.  # noqa: E501

        Report any errors during id resolution.  # noqa: E501

        :return: The error of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this SummaryWorkloadWorkloadItem.

        Report any errors during id resolution.  # noqa: E501

        :param error: The error of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def group_id(self):
        """Gets the group_id of this SummaryWorkloadWorkloadItem.  # noqa: E501

        Group ID of the group that initiated the operation.  # noqa: E501

        :return: The group_id of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this SummaryWorkloadWorkloadItem.

        Group ID of the group that initiated the operation.  # noqa: E501

        :param group_id: The group_id of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """

        self._group_id = group_id

    @property
    def group_sid(self):
        """Gets the group_sid of this SummaryWorkloadWorkloadItem.  # noqa: E501

        Group SID of the group that initiated the operation.  # noqa: E501

        :return: The group_sid of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._group_sid

    @group_sid.setter
    def group_sid(self, group_sid):
        """Sets the group_sid of this SummaryWorkloadWorkloadItem.

        Group SID of the group that initiated the operation.  # noqa: E501

        :param group_sid: The group_sid of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._group_sid = group_sid

    @property
    def groupname(self):
        """Gets the groupname of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The resolved text name of the group that initiated the operation.  # noqa: E501

        :return: The groupname of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._groupname

    @groupname.setter
    def groupname(self, groupname):
        """Sets the groupname of this SummaryWorkloadWorkloadItem.

        The resolved text name of the group that initiated the operation.  # noqa: E501

        :param groupname: The groupname of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._groupname = groupname

    @property
    def job_type(self):
        """Gets the job_type of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The canonical name for the job followed by phase in brackets, ie. 'AVscan[1]', etc...  # noqa: E501

        :return: The job_type of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this SummaryWorkloadWorkloadItem.

        The canonical name for the job followed by phase in brackets, ie. 'AVscan[1]', etc...  # noqa: E501

        :param job_type: The job_type of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._job_type = job_type

    @property
    def l2(self):
        """Gets the l2 of this SummaryWorkloadWorkloadItem.  # noqa: E501

        L2 cache hits per second.  # noqa: E501

        :return: The l2 of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._l2

    @l2.setter
    def l2(self, l2):
        """Sets the l2 of this SummaryWorkloadWorkloadItem.

        L2 cache hits per second.  # noqa: E501

        :param l2: The l2 of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """
        if l2 is None:
            raise ValueError("Invalid value for `l2`, must not be `None`")  # noqa: E501

        self._l2 = l2

    @property
    def l3(self):
        """Gets the l3 of this SummaryWorkloadWorkloadItem.  # noqa: E501

        L3 cache hits per second.  # noqa: E501

        :return: The l3 of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        """Sets the l3 of this SummaryWorkloadWorkloadItem.

        L3 cache hits per second.  # noqa: E501

        :param l3: The l3 of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """
        if l3 is None:
            raise ValueError("Invalid value for `l3`, must not be `None`")  # noqa: E501

        self._l3 = l3

    @property
    def local_addr(self):
        """Gets the local_addr of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The IP address of the host receiving the operation request.  # noqa: E501

        :return: The local_addr of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._local_addr

    @local_addr.setter
    def local_addr(self, local_addr):
        """Sets the local_addr of this SummaryWorkloadWorkloadItem.

        The IP address of the host receiving the operation request.  # noqa: E501

        :param local_addr: The local_addr of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._local_addr = local_addr

    @property
    def local_name(self):
        """Gets the local_name of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The resolved text name of the LocalAddr, if resolution can be performed.  # noqa: E501

        :return: The local_name of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._local_name

    @local_name.setter
    def local_name(self, local_name):
        """Sets the local_name of this SummaryWorkloadWorkloadItem.

        The resolved text name of the LocalAddr, if resolution can be performed.  # noqa: E501

        :param local_name: The local_name of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._local_name = local_name

    @property
    def node(self):
        """Gets the node of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The node on which the operation was performed or 0 for cluster scoped statistics.  # noqa: E501

        :return: The node of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this SummaryWorkloadWorkloadItem.

        The node on which the operation was performed or 0 for cluster scoped statistics.  # noqa: E501

        :param node: The node of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """
        if node is None:
            raise ValueError("Invalid value for `node`, must not be `None`")  # noqa: E501

        self._node = node

    @property
    def ops(self):
        """Gets the ops of this SummaryWorkloadWorkloadItem.  # noqa: E501

        Operations per second.  # noqa: E501

        :return: The ops of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._ops

    @ops.setter
    def ops(self, ops):
        """Sets the ops of this SummaryWorkloadWorkloadItem.

        Operations per second.  # noqa: E501

        :param ops: The ops of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """
        if ops is None:
            raise ValueError("Invalid value for `ops`, must not be `None`")  # noqa: E501

        self._ops = ops

    @property
    def path(self):
        """Gets the path of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The path which the operation was requestion on.  # noqa: E501

        :return: The path of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SummaryWorkloadWorkloadItem.

        The path which the operation was requestion on.  # noqa: E501

        :param path: The path of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def protocol(self):
        """Gets the protocol of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The protocol of the operation.  # noqa: E501

        :return: The protocol of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this SummaryWorkloadWorkloadItem.

        The protocol of the operation.  # noqa: E501

        :param protocol: The protocol of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def reads(self):
        """Gets the reads of this SummaryWorkloadWorkloadItem.  # noqa: E501

        Disk read operations per second.  # noqa: E501

        :return: The reads of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._reads

    @reads.setter
    def reads(self, reads):
        """Sets the reads of this SummaryWorkloadWorkloadItem.

        Disk read operations per second.  # noqa: E501

        :param reads: The reads of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """
        if reads is None:
            raise ValueError("Invalid value for `reads`, must not be `None`")  # noqa: E501

        self._reads = reads

    @property
    def remote_addr(self):
        """Gets the remote_addr of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The IP address of the host sending the operation request.  # noqa: E501

        :return: The remote_addr of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._remote_addr

    @remote_addr.setter
    def remote_addr(self, remote_addr):
        """Sets the remote_addr of this SummaryWorkloadWorkloadItem.

        The IP address of the host sending the operation request.  # noqa: E501

        :param remote_addr: The remote_addr of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._remote_addr = remote_addr

    @property
    def remote_name(self):
        """Gets the remote_name of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The resolved text name of the RemoteAddr, if resolution can be performed.  # noqa: E501

        :return: The remote_name of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._remote_name

    @remote_name.setter
    def remote_name(self, remote_name):
        """Sets the remote_name of this SummaryWorkloadWorkloadItem.

        The resolved text name of the RemoteAddr, if resolution can be performed.  # noqa: E501

        :param remote_name: The remote_name of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._remote_name = remote_name

    @property
    def share_name(self):
        """Gets the share_name of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The name of the SMB share through which the operation was requested.  # noqa: E501

        :return: The share_name of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._share_name

    @share_name.setter
    def share_name(self, share_name):
        """Sets the share_name of this SummaryWorkloadWorkloadItem.

        The name of the SMB share through which the operation was requested.  # noqa: E501

        :param share_name: The share_name of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._share_name = share_name

    @property
    def system_name(self):
        """Gets the system_name of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The process name, job ID, etc...  # noqa: E501

        :return: The system_name of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this SummaryWorkloadWorkloadItem.

        The process name, job ID, etc...  # noqa: E501

        :param system_name: The system_name of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._system_name = system_name

    @property
    def time(self):
        """Gets the time of this SummaryWorkloadWorkloadItem.  # noqa: E501

        Unix Epoch time in seconds that statistic was collected.  # noqa: E501

        :return: The time of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SummaryWorkloadWorkloadItem.

        Unix Epoch time in seconds that statistic was collected.  # noqa: E501

        :param time: The time of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def user_id(self):
        """Gets the user_id of this SummaryWorkloadWorkloadItem.  # noqa: E501

        User ID of the user who initiated the operation.  # noqa: E501

        :return: The user_id of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SummaryWorkloadWorkloadItem.

        User ID of the user who initiated the operation.  # noqa: E501

        :param user_id: The user_id of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """

        self._user_id = user_id

    @property
    def user_sid(self):
        """Gets the user_sid of this SummaryWorkloadWorkloadItem.  # noqa: E501

        User SID of the user who initiated the operation.  # noqa: E501

        :return: The user_sid of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._user_sid

    @user_sid.setter
    def user_sid(self, user_sid):
        """Sets the user_sid of this SummaryWorkloadWorkloadItem.

        User SID of the user who initiated the operation.  # noqa: E501

        :param user_sid: The user_sid of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._user_sid = user_sid

    @property
    def username(self):
        """Gets the username of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The resolved text name of the user who initiated the operation.  # noqa: E501

        :return: The username of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SummaryWorkloadWorkloadItem.

        The resolved text name of the user who initiated the operation.  # noqa: E501

        :param username: The username of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def workload_id(self):
        """Gets the workload_id of this SummaryWorkloadWorkloadItem.  # noqa: E501

        ID of the workload (Pinned workloads only).  # noqa: E501

        :return: The workload_id of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: int
        """
        return self._workload_id

    @workload_id.setter
    def workload_id(self, workload_id):
        """Sets the workload_id of this SummaryWorkloadWorkloadItem.

        ID of the workload (Pinned workloads only).  # noqa: E501

        :param workload_id: The workload_id of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: int
        """

        self._workload_id = workload_id

    @property
    def workload_type(self):
        """Gets the workload_type of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The type of workload output.  # noqa: E501

        :return: The workload_type of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        """Sets the workload_type of this SummaryWorkloadWorkloadItem.

        The type of workload output.  # noqa: E501

        :param workload_type: The workload_type of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._workload_type = workload_type

    @property
    def writes(self):
        """Gets the writes of this SummaryWorkloadWorkloadItem.  # noqa: E501

        Disk write operations per second.  # noqa: E501

        :return: The writes of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._writes

    @writes.setter
    def writes(self, writes):
        """Sets the writes of this SummaryWorkloadWorkloadItem.

        Disk write operations per second.  # noqa: E501

        :param writes: The writes of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """
        if writes is None:
            raise ValueError("Invalid value for `writes`, must not be `None`")  # noqa: E501

        self._writes = writes

    @property
    def zone_id(self):
        """Gets the zone_id of this SummaryWorkloadWorkloadItem.  # noqa: E501

        Zone ID  # noqa: E501

        :return: The zone_id of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this SummaryWorkloadWorkloadItem.

        Zone ID  # noqa: E501

        :param zone_id: The zone_id of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """

        self._zone_id = zone_id

    @property
    def zone_name(self):
        """Gets the zone_name of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The resolved text zone name  # noqa: E501

        :return: The zone_name of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this SummaryWorkloadWorkloadItem.

        The resolved text zone name  # noqa: E501

        :param zone_name: The zone_name of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._zone_name = zone_name

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
        if not isinstance(other, SummaryWorkloadWorkloadItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
