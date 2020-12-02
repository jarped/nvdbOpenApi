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

class VegobjektTypeEgenskapGeometri(VegobjektTypeEgenskapBase):
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
        'dimensjoner': 'int',
        'geometritype': 'str',
        'innenfor_mor': 'bool'
    }
    if hasattr(VegobjektTypeEgenskapBase, "swagger_types"):
        swagger_types.update(VegobjektTypeEgenskapBase.swagger_types)

    attribute_map = {
        'dimensjoner': 'dimensjoner',
        'geometritype': 'geometritype',
        'innenfor_mor': 'innenfor_mor'
    }
    if hasattr(VegobjektTypeEgenskapBase, "attribute_map"):
        attribute_map.update(VegobjektTypeEgenskapBase.attribute_map)

    def __init__(self, dimensjoner=None, geometritype=None, innenfor_mor=None, *args, **kwargs):  # noqa: E501
        """VegobjektTypeEgenskapGeometri - a model defined in Swagger"""  # noqa: E501
        self._dimensjoner = None
        self._geometritype = None
        self._innenfor_mor = None
        self.discriminator = None
        if dimensjoner is not None:
            self.dimensjoner = dimensjoner
        if geometritype is not None:
            self.geometritype = geometritype
        if innenfor_mor is not None:
            self.innenfor_mor = innenfor_mor
        VegobjektTypeEgenskapBase.__init__(self, *args, **kwargs)

    @property
    def dimensjoner(self):
        """Gets the dimensjoner of this VegobjektTypeEgenskapGeometri.  # noqa: E501


        :return: The dimensjoner of this VegobjektTypeEgenskapGeometri.  # noqa: E501
        :rtype: int
        """
        return self._dimensjoner

    @dimensjoner.setter
    def dimensjoner(self, dimensjoner):
        """Sets the dimensjoner of this VegobjektTypeEgenskapGeometri.


        :param dimensjoner: The dimensjoner of this VegobjektTypeEgenskapGeometri.  # noqa: E501
        :type: int
        """

        self._dimensjoner = dimensjoner

    @property
    def geometritype(self):
        """Gets the geometritype of this VegobjektTypeEgenskapGeometri.  # noqa: E501


        :return: The geometritype of this VegobjektTypeEgenskapGeometri.  # noqa: E501
        :rtype: str
        """
        return self._geometritype

    @geometritype.setter
    def geometritype(self, geometritype):
        """Sets the geometritype of this VegobjektTypeEgenskapGeometri.


        :param geometritype: The geometritype of this VegobjektTypeEgenskapGeometri.  # noqa: E501
        :type: str
        """
        allowed_values = ["PUNKT", "POLYGON", "LINJE", "FLERELINJE", "FLEREPUNKT", "FLEREPOLYGON", "KOMPLEKS"]  # noqa: E501
        if geometritype not in allowed_values:
            raise ValueError(
                "Invalid value for `geometritype` ({0}), must be one of {1}"  # noqa: E501
                .format(geometritype, allowed_values)
            )

        self._geometritype = geometritype

    @property
    def innenfor_mor(self):
        """Gets the innenfor_mor of this VegobjektTypeEgenskapGeometri.  # noqa: E501


        :return: The innenfor_mor of this VegobjektTypeEgenskapGeometri.  # noqa: E501
        :rtype: bool
        """
        return self._innenfor_mor

    @innenfor_mor.setter
    def innenfor_mor(self, innenfor_mor):
        """Sets the innenfor_mor of this VegobjektTypeEgenskapGeometri.


        :param innenfor_mor: The innenfor_mor of this VegobjektTypeEgenskapGeometri.  # noqa: E501
        :type: bool
        """

        self._innenfor_mor = innenfor_mor

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
        if issubclass(VegobjektTypeEgenskapGeometri, dict):
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
        if not isinstance(other, VegobjektTypeEgenskapGeometri):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other