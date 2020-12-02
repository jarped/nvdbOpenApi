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
from swagger_client.models.vegobjekt_type_egenskap_primitiv import VegobjektTypeEgenskapPrimitiv  # noqa: F401,E501

class VegobjektTypeEgenskapBinar(VegobjektTypeEgenskapPrimitiv):
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
        'mediatype': 'str'
    }
    if hasattr(VegobjektTypeEgenskapPrimitiv, "swagger_types"):
        swagger_types.update(VegobjektTypeEgenskapPrimitiv.swagger_types)

    attribute_map = {
        'mediatype': 'mediatype'
    }
    if hasattr(VegobjektTypeEgenskapPrimitiv, "attribute_map"):
        attribute_map.update(VegobjektTypeEgenskapPrimitiv.attribute_map)

    def __init__(self, mediatype=None, *args, **kwargs):  # noqa: E501
        """VegobjektTypeEgenskapBinar - a model defined in Swagger"""  # noqa: E501
        self._mediatype = None
        self.discriminator = None
        if mediatype is not None:
            self.mediatype = mediatype
        VegobjektTypeEgenskapPrimitiv.__init__(self, *args, **kwargs)

    @property
    def mediatype(self):
        """Gets the mediatype of this VegobjektTypeEgenskapBinar.  # noqa: E501


        :return: The mediatype of this VegobjektTypeEgenskapBinar.  # noqa: E501
        :rtype: str
        """
        return self._mediatype

    @mediatype.setter
    def mediatype(self, mediatype):
        """Sets the mediatype of this VegobjektTypeEgenskapBinar.


        :param mediatype: The mediatype of this VegobjektTypeEgenskapBinar.  # noqa: E501
        :type: str
        """

        self._mediatype = mediatype

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
        if issubclass(VegobjektTypeEgenskapBinar, dict):
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
        if not isinstance(other, VegobjektTypeEgenskapBinar):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
