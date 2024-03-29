# coding: utf-8

"""
    Imperva Client-Side Protection API

    This is an API for Imperva Client-Side Protection. Gain visibility into the JavaScript services making requests to your application along with their risk factors. Use these APIs to pull data and configure which services should have access to your application. For full feature documentation, see <a style=\"text-decoration:none\" href=\"https://docs.imperva.com/bundle/client-side-protection\">Client-Side Protection</a>  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Analytics(object):
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
        'tracking_id': 'str',
        'discovered_ms': 'int'
    }

    attribute_map = {
        'tracking_id': 'trackingId',
        'discovered_ms': 'discoveredMs'
    }

    def __init__(self, tracking_id=None, discovered_ms=None):  # noqa: E501
        """Analytics - a model defined in Swagger"""  # noqa: E501
        self._tracking_id = None
        self._discovered_ms = None
        self.discriminator = None
        if tracking_id is not None:
            self.tracking_id = tracking_id
        if discovered_ms is not None:
            self.discovered_ms = discovered_ms

    @property
    def tracking_id(self):
        """Gets the tracking_id of this Analytics.  # noqa: E501

        Google analytics tracking id  # noqa: E501

        :return: The tracking_id of this Analytics.  # noqa: E501
        :rtype: str
        """
        return self._tracking_id

    @tracking_id.setter
    def tracking_id(self, tracking_id):
        """Sets the tracking_id of this Analytics.

        Google analytics tracking id  # noqa: E501

        :param tracking_id: The tracking_id of this Analytics.  # noqa: E501
        :type: str
        """

        self._tracking_id = tracking_id

    @property
    def discovered_ms(self):
        """Gets the discovered_ms of this Analytics.  # noqa: E501

        Date the tracking id was discovered in milliseconds.  # noqa: E501

        :return: The discovered_ms of this Analytics.  # noqa: E501
        :rtype: int
        """
        return self._discovered_ms

    @discovered_ms.setter
    def discovered_ms(self, discovered_ms):
        """Sets the discovered_ms of this Analytics.

        Date the tracking id was discovered in milliseconds.  # noqa: E501

        :param discovered_ms: The discovered_ms of this Analytics.  # noqa: E501
        :type: int
        """

        self._discovered_ms = discovered_ms

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
        if issubclass(Analytics, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Analytics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other