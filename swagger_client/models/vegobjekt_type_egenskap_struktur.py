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
from swagger_client.models.vegobjekt_type_egenskap_base import VegobjektTypeEgenskapBase  # noqa: F401,E501

class VegobjektTypeEgenskapStruktur(VegobjektTypeEgenskapBase):
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
        'egenskaper': 'list[Egenskapstype]'
    }
    if hasattr(VegobjektTypeEgenskapBase, "swagger_types"):
        swagger_types.update(VegobjektTypeEgenskapBase.swagger_types)

    attribute_map = {
        'egenskaper': 'egenskaper'
    }
    if hasattr(VegobjektTypeEgenskapBase, "attribute_map"):
        attribute_map.update(VegobjektTypeEgenskapBase.attribute_map)

    def __init__(self, egenskaper=None, *args, **kwargs):  # noqa: E501
        """VegobjektTypeEgenskapStruktur - a model defined in Swagger"""  # noqa: E501
        self._egenskaper = None
        self.discriminator = None
        if egenskaper is not None:
            self.egenskaper = egenskaper
        VegobjektTypeEgenskapBase.__init__(self, *args, **kwargs)

    @property
    def egenskaper(self):
        """Gets the egenskaper of this VegobjektTypeEgenskapStruktur.  # noqa: E501

        Egenskapstyper som kan inngå i strukturen  # noqa: E501

        :return: The egenskaper of this VegobjektTypeEgenskapStruktur.  # noqa: E501
        :rtype: list[Egenskapstype]
        """
        return self._egenskaper

    @egenskaper.setter
    def egenskaper(self, egenskaper):
        """Sets the egenskaper of this VegobjektTypeEgenskapStruktur.

        Egenskapstyper som kan inngå i strukturen  # noqa: E501

        :param egenskaper: The egenskaper of this VegobjektTypeEgenskapStruktur.  # noqa: E501
        :type: list[Egenskapstype]
        """

        self._egenskaper = egenskaper

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
        if issubclass(VegobjektTypeEgenskapStruktur, dict):
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
        if not isinstance(other, VegobjektTypeEgenskapStruktur):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
