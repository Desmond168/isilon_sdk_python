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


class DrivesDriveFirmwareNodeDrive(object):
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
        'baynum': 'int',
        'current_firmware': 'str',
        'desired_firmware': 'str',
        'devname': 'str',
        'lnum': 'int',
        'locnstr': 'str',
        'model': 'str'
    }

    attribute_map = {
        'baynum': 'baynum',
        'current_firmware': 'current_firmware',
        'desired_firmware': 'desired_firmware',
        'devname': 'devname',
        'lnum': 'lnum',
        'locnstr': 'locnstr',
        'model': 'model'
    }

    def __init__(self, baynum=None, current_firmware=None, desired_firmware=None, devname=None, lnum=None, locnstr=None, model=None):  # noqa: E501
        """DrivesDriveFirmwareNodeDrive - a model defined in Swagger"""  # noqa: E501

        self._baynum = None
        self._current_firmware = None
        self._desired_firmware = None
        self._devname = None
        self._lnum = None
        self._locnstr = None
        self._model = None
        self.discriminator = None

        if baynum is not None:
            self.baynum = baynum
        if current_firmware is not None:
            self.current_firmware = current_firmware
        if desired_firmware is not None:
            self.desired_firmware = desired_firmware
        if devname is not None:
            self.devname = devname
        if lnum is not None:
            self.lnum = lnum
        if locnstr is not None:
            self.locnstr = locnstr
        if model is not None:
            self.model = model

    @property
    def baynum(self):
        """Gets the baynum of this DrivesDriveFirmwareNodeDrive.  # noqa: E501

        Numerical representation of this drive's bay.  # noqa: E501

        :return: The baynum of this DrivesDriveFirmwareNodeDrive.  # noqa: E501
        :rtype: int
        """
        return self._baynum

    @baynum.setter
    def baynum(self, baynum):
        """Sets the baynum of this DrivesDriveFirmwareNodeDrive.

        Numerical representation of this drive's bay.  # noqa: E501

        :param baynum: The baynum of this DrivesDriveFirmwareNodeDrive.  # noqa: E501
        :type: int
        """
        if baynum is not None and baynum > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `baynum`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if baynum is not None and baynum < 0:  # noqa: E501
            raise ValueError("Invalid value for `baynum`, must be a value greater than or equal to `0`")  # noqa: E501

        self._baynum = baynum

    @property
    def current_firmware(self):
        """Gets the current_firmware of this DrivesDriveFirmwareNodeDrive.  # noqa: E501

        This drive's current firmware revision  # noqa: E501

        :return: The current_firmware of this DrivesDriveFirmwareNodeDrive.  # noqa: E501
        :rtype: str
        """
        return self._current_firmware

    @current_firmware.setter
    def current_firmware(self, current_firmware):
        """Sets the current_firmware of this DrivesDriveFirmwareNodeDrive.

        This drive's current firmware revision  # noqa: E501

        :param current_firmware: The current_firmware of this DrivesDriveFirmwareNodeDrive.  # noqa: E501
        :type: str
        """
        if current_firmware is not None and len(current_firmware) > 255:
            raise ValueError("Invalid value for `current_firmware`, length must be less than or equal to `255`")  # noqa: E501
        if current_firmware is not None and len(current_firmware) < 0:
            raise ValueError("Invalid value for `current_firmware`, length must be greater than or equal to `0`")  # noqa: E501

        self._current_firmware = current_firmware

    @property
    def desired_firmware(self):
        """Gets the desired_firmware of this DrivesDriveFirmwareNodeDrive.  # noqa: E501

        This drive's desired firmware revision.  # noqa: E501

        :return: The desired_firmware of this DrivesDriveFirmwareNodeDrive.  # noqa: E501
        :rtype: str
        """
        return self._desired_firmware

    @desired_firmware.setter
    def desired_firmware(self, desired_firmware):
        """Sets the desired_firmware of this DrivesDriveFirmwareNodeDrive.

        This drive's desired firmware revision.  # noqa: E501

        :param desired_firmware: The desired_firmware of this DrivesDriveFirmwareNodeDrive.  # noqa: E501
        :type: str
        """
        if desired_firmware is not None and len(desired_firmware) > 255:
            raise ValueError("Invalid value for `desired_firmware`, length must be less than or equal to `255`")  # noqa: E501
        if desired_firmware is not None and len(desired_firmware) < 0:
            raise ValueError("Invalid value for `desired_firmware`, length must be greater than or equal to `0`")  # noqa: E501

        self._desired_firmware = desired_firmware

    @property
    def devname(self):
        """Gets the devname of this DrivesDriveFirmwareNodeDrive.  # noqa: E501

        This drive's device name.  # noqa: E501

        :return: The devname of this DrivesDriveFirmwareNodeDrive.  # noqa: E501
        :rtype: str
        """
        return self._devname

    @devname.setter
    def devname(self, devname):
        """Sets the devname of this DrivesDriveFirmwareNodeDrive.

        This drive's device name.  # noqa: E501

        :param devname: The devname of this DrivesDriveFirmwareNodeDrive.  # noqa: E501
        :type: str
        """
        if devname is not None and len(devname) > 255:
            raise ValueError("Invalid value for `devname`, length must be less than or equal to `255`")  # noqa: E501
        if devname is not None and len(devname) < 0:
            raise ValueError("Invalid value for `devname`, length must be greater than or equal to `0`")  # noqa: E501

        self._devname = devname

    @property
    def lnum(self):
        """Gets the lnum of this DrivesDriveFirmwareNodeDrive.  # noqa: E501

        This drive's logical drive number in IFS.  # noqa: E501

        :return: The lnum of this DrivesDriveFirmwareNodeDrive.  # noqa: E501
        :rtype: int
        """
        return self._lnum

    @lnum.setter
    def lnum(self, lnum):
        """Sets the lnum of this DrivesDriveFirmwareNodeDrive.

        This drive's logical drive number in IFS.  # noqa: E501

        :param lnum: The lnum of this DrivesDriveFirmwareNodeDrive.  # noqa: E501
        :type: int
        """
        if lnum is not None and lnum > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `lnum`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if lnum is not None and lnum < 0:  # noqa: E501
            raise ValueError("Invalid value for `lnum`, must be a value greater than or equal to `0`")  # noqa: E501

        self._lnum = lnum

    @property
    def locnstr(self):
        """Gets the locnstr of this DrivesDriveFirmwareNodeDrive.  # noqa: E501

        String representation of this drive's physical location.  # noqa: E501

        :return: The locnstr of this DrivesDriveFirmwareNodeDrive.  # noqa: E501
        :rtype: str
        """
        return self._locnstr

    @locnstr.setter
    def locnstr(self, locnstr):
        """Sets the locnstr of this DrivesDriveFirmwareNodeDrive.

        String representation of this drive's physical location.  # noqa: E501

        :param locnstr: The locnstr of this DrivesDriveFirmwareNodeDrive.  # noqa: E501
        :type: str
        """
        if locnstr is not None and len(locnstr) > 255:
            raise ValueError("Invalid value for `locnstr`, length must be less than or equal to `255`")  # noqa: E501
        if locnstr is not None and len(locnstr) < 0:
            raise ValueError("Invalid value for `locnstr`, length must be greater than or equal to `0`")  # noqa: E501

        self._locnstr = locnstr

    @property
    def model(self):
        """Gets the model of this DrivesDriveFirmwareNodeDrive.  # noqa: E501

        This drive's manufacturer and model.  # noqa: E501

        :return: The model of this DrivesDriveFirmwareNodeDrive.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this DrivesDriveFirmwareNodeDrive.

        This drive's manufacturer and model.  # noqa: E501

        :param model: The model of this DrivesDriveFirmwareNodeDrive.  # noqa: E501
        :type: str
        """
        if model is not None and len(model) > 255:
            raise ValueError("Invalid value for `model`, length must be less than or equal to `255`")  # noqa: E501
        if model is not None and len(model) < 0:
            raise ValueError("Invalid value for `model`, length must be greater than or equal to `0`")  # noqa: E501

        self._model = model

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
        if not isinstance(other, DrivesDriveFirmwareNodeDrive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
