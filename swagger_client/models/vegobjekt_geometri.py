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

class VegobjektGeometri(object):
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
        'wkt': 'str',
        'srid': 'int',
        'egengeometri': 'bool',
        'forenklet': 'Object'
    }

    attribute_map = {
        'wkt': 'wkt',
        'srid': 'srid',
        'egengeometri': 'egengeometri',
        'forenklet': 'forenklet'
    }

    def __init__(self, wkt=None, srid=None, egengeometri=None, forenklet=None):  # noqa: E501
        """VegobjektGeometri - a model defined in Swagger"""  # noqa: E501
        self._wkt = None
        self._srid = None
        self._egengeometri = None
        self._forenklet = None
        self.discriminator = None
        if wkt is not None:
            self.wkt = wkt
        if srid is not None:
            self.srid = srid
        if egengeometri is not None:
            self.egengeometri = egengeometri
        if forenklet is not None:
            self.forenklet = forenklet

    @property
    def wkt(self):
        """Gets the wkt of this VegobjektGeometri.  # noqa: E501


        :return: The wkt of this VegobjektGeometri.  # noqa: E501
        :rtype: str
        """
        return self._wkt

    @wkt.setter
    def wkt(self, wkt):
        """Sets the wkt of this VegobjektGeometri.


        :param wkt: The wkt of this VegobjektGeometri.  # noqa: E501
        :type: str
        """

        self._wkt = wkt

    @property
    def srid(self):
        """Gets the srid of this VegobjektGeometri.  # noqa: E501

        Hvilket geografiske referansesystem koordinatene er i  # noqa: E501

        :return: The srid of this VegobjektGeometri.  # noqa: E501
        :rtype: int
        """
        return self._srid

    @srid.setter
    def srid(self, srid):
        """Sets the srid of this VegobjektGeometri.

        Hvilket geografiske referansesystem koordinatene er i  # noqa: E501

        :param srid: The srid of this VegobjektGeometri.  # noqa: E501
        :type: int
        """
        allowed_values = [6173, 4326]  # noqa: E501
        if srid not in allowed_values:
            raise ValueError(
                "Invalid value for `srid` ({0}), must be one of {1}"  # noqa: E501
                .format(srid, allowed_values)
            )

        self._srid = srid

    @property
    def egengeometri(self):
        """Gets the egengeometri of this VegobjektGeometri.  # noqa: E501

        Angir om geometrien er vegobjektets egengeometri, eller om geometrien er utledet fra vegnettes geometri  # noqa: E501

        :return: The egengeometri of this VegobjektGeometri.  # noqa: E501
        :rtype: bool
        """
        return self._egengeometri

    @egengeometri.setter
    def egengeometri(self, egengeometri):
        """Sets the egengeometri of this VegobjektGeometri.

        Angir om geometrien er vegobjektets egengeometri, eller om geometrien er utledet fra vegnettes geometri  # noqa: E501

        :param egengeometri: The egengeometri of this VegobjektGeometri.  # noqa: E501
        :type: bool
        """

        self._egengeometri = egengeometri

    @property
    def forenklet(self):
        """Gets the forenklet of this VegobjektGeometri.  # noqa: E501

        tilstede dersom `geometritoleranse` er spesifisert.  # noqa: E501

        :return: The forenklet of this VegobjektGeometri.  # noqa: E501
        :rtype: Object
        """
        return self._forenklet

    @forenklet.setter
    def forenklet(self, forenklet):
        """Sets the forenklet of this VegobjektGeometri.

        tilstede dersom `geometritoleranse` er spesifisert.  # noqa: E501

        :param forenklet: The forenklet of this VegobjektGeometri.  # noqa: E501
        :type: Object
        """

        self._forenklet = forenklet

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
        if issubclass(VegobjektGeometri, dict):
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
        if not isinstance(other, VegobjektGeometri):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other