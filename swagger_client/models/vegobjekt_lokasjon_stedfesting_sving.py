# coding: utf-8

"""
    NVDB API LES V3

    API for å lese vegobjekter, vegnett og transaksjoner fra NVDB  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: nvdb@vegvesen.no
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class VegobjektLokasjonStedfestingSving(object):
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
        'type': 'str',
        'nodeid': 'int',
        'startpunkt': 'VegobjektLokasjonStedfestingPunkt',
        'sluttpunkt': 'VegobjektLokasjonStedfestingPunkt'
    }

    attribute_map = {
        'type': 'type',
        'nodeid': 'nodeid',
        'startpunkt': 'startpunkt',
        'sluttpunkt': 'sluttpunkt'
    }

    def __init__(self, type=None, nodeid=None, startpunkt=None, sluttpunkt=None):  # noqa: E501
        """VegobjektLokasjonStedfestingSving - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._nodeid = None
        self._startpunkt = None
        self._sluttpunkt = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if nodeid is not None:
            self.nodeid = nodeid
        if startpunkt is not None:
            self.startpunkt = startpunkt
        if sluttpunkt is not None:
            self.sluttpunkt = sluttpunkt

    @property
    def type(self):
        """Gets the type of this VegobjektLokasjonStedfestingSving.  # noqa: E501


        :return: The type of this VegobjektLokasjonStedfestingSving.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VegobjektLokasjonStedfestingSving.


        :param type: The type of this VegobjektLokasjonStedfestingSving.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def nodeid(self):
        """Gets the nodeid of this VegobjektLokasjonStedfestingSving.  # noqa: E501


        :return: The nodeid of this VegobjektLokasjonStedfestingSving.  # noqa: E501
        :rtype: int
        """
        return self._nodeid

    @nodeid.setter
    def nodeid(self, nodeid):
        """Sets the nodeid of this VegobjektLokasjonStedfestingSving.


        :param nodeid: The nodeid of this VegobjektLokasjonStedfestingSving.  # noqa: E501
        :type: int
        """

        self._nodeid = nodeid

    @property
    def startpunkt(self):
        """Gets the startpunkt of this VegobjektLokasjonStedfestingSving.  # noqa: E501


        :return: The startpunkt of this VegobjektLokasjonStedfestingSving.  # noqa: E501
        :rtype: VegobjektLokasjonStedfestingPunkt
        """
        return self._startpunkt

    @startpunkt.setter
    def startpunkt(self, startpunkt):
        """Sets the startpunkt of this VegobjektLokasjonStedfestingSving.


        :param startpunkt: The startpunkt of this VegobjektLokasjonStedfestingSving.  # noqa: E501
        :type: VegobjektLokasjonStedfestingPunkt
        """

        self._startpunkt = startpunkt

    @property
    def sluttpunkt(self):
        """Gets the sluttpunkt of this VegobjektLokasjonStedfestingSving.  # noqa: E501


        :return: The sluttpunkt of this VegobjektLokasjonStedfestingSving.  # noqa: E501
        :rtype: VegobjektLokasjonStedfestingPunkt
        """
        return self._sluttpunkt

    @sluttpunkt.setter
    def sluttpunkt(self, sluttpunkt):
        """Sets the sluttpunkt of this VegobjektLokasjonStedfestingSving.


        :param sluttpunkt: The sluttpunkt of this VegobjektLokasjonStedfestingSving.  # noqa: E501
        :type: VegobjektLokasjonStedfestingPunkt
        """

        self._sluttpunkt = sluttpunkt

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
        if issubclass(VegobjektLokasjonStedfestingSving, dict):
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
        if not isinstance(other, VegobjektLokasjonStedfestingSving):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other