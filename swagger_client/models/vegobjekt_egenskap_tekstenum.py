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
from swagger_client.models.vegobjekt_egenskap_base import VegobjektEgenskapBase  # noqa: F401,E501

class VegobjektEgenskapTekstenum(VegobjektEgenskapBase):
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
        'verdi': 'str',
        'enum_id': 'int'
    }
    if hasattr(VegobjektEgenskapBase, "swagger_types"):
        swagger_types.update(VegobjektEgenskapBase.swagger_types)

    attribute_map = {
        'verdi': 'verdi',
        'enum_id': 'enum_id'
    }
    if hasattr(VegobjektEgenskapBase, "attribute_map"):
        attribute_map.update(VegobjektEgenskapBase.attribute_map)

    def __init__(self, verdi=None, enum_id=None, *args, **kwargs):  # noqa: E501
        """VegobjektEgenskapTekstenum - a model defined in Swagger"""  # noqa: E501
        self._verdi = None
        self._enum_id = None
        self.discriminator = None
        if verdi is not None:
            self.verdi = verdi
        if enum_id is not None:
            self.enum_id = enum_id
        VegobjektEgenskapBase.__init__(self, *args, **kwargs)

    @property
    def verdi(self):
        """Gets the verdi of this VegobjektEgenskapTekstenum.  # noqa: E501


        :return: The verdi of this VegobjektEgenskapTekstenum.  # noqa: E501
        :rtype: str
        """
        return self._verdi

    @verdi.setter
    def verdi(self, verdi):
        """Sets the verdi of this VegobjektEgenskapTekstenum.


        :param verdi: The verdi of this VegobjektEgenskapTekstenum.  # noqa: E501
        :type: str
        """

        self._verdi = verdi

    @property
    def enum_id(self):
        """Gets the enum_id of this VegobjektEgenskapTekstenum.  # noqa: E501


        :return: The enum_id of this VegobjektEgenskapTekstenum.  # noqa: E501
        :rtype: int
        """
        return self._enum_id

    @enum_id.setter
    def enum_id(self, enum_id):
        """Sets the enum_id of this VegobjektEgenskapTekstenum.


        :param enum_id: The enum_id of this VegobjektEgenskapTekstenum.  # noqa: E501
        :type: int
        """

        self._enum_id = enum_id

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
        if issubclass(VegobjektEgenskapTekstenum, dict):
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
        if not isinstance(other, VegobjektEgenskapTekstenum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
