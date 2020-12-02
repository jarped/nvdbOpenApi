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

class VegobjektEgenskapBase(object):
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
        'id': 'int',
        'navn': 'str',
        'egenskapstype': 'Egenskapstype',
        'datatype': 'Datatype'
    }

    attribute_map = {
        'id': 'id',
        'navn': 'navn',
        'egenskapstype': 'egenskapstype',
        'datatype': 'datatype'
    }

    def __init__(self, id=None, navn=None, egenskapstype=None, datatype=None):  # noqa: E501
        """VegobjektEgenskapBase - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._navn = None
        self._egenskapstype = None
        self._datatype = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if navn is not None:
            self.navn = navn
        if egenskapstype is not None:
            self.egenskapstype = egenskapstype
        if datatype is not None:
            self.datatype = datatype

    @property
    def id(self):
        """Gets the id of this VegobjektEgenskapBase.  # noqa: E501

        id for egenskapen  # noqa: E501

        :return: The id of this VegobjektEgenskapBase.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VegobjektEgenskapBase.

        id for egenskapen  # noqa: E501

        :param id: The id of this VegobjektEgenskapBase.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def navn(self):
        """Gets the navn of this VegobjektEgenskapBase.  # noqa: E501

        Navnet på egenskapstypen i datakatalogen  # noqa: E501

        :return: The navn of this VegobjektEgenskapBase.  # noqa: E501
        :rtype: str
        """
        return self._navn

    @navn.setter
    def navn(self, navn):
        """Sets the navn of this VegobjektEgenskapBase.

        Navnet på egenskapstypen i datakatalogen  # noqa: E501

        :param navn: The navn of this VegobjektEgenskapBase.  # noqa: E501
        :type: str
        """

        self._navn = navn

    @property
    def egenskapstype(self):
        """Gets the egenskapstype of this VegobjektEgenskapBase.  # noqa: E501


        :return: The egenskapstype of this VegobjektEgenskapBase.  # noqa: E501
        :rtype: Egenskapstype
        """
        return self._egenskapstype

    @egenskapstype.setter
    def egenskapstype(self, egenskapstype):
        """Sets the egenskapstype of this VegobjektEgenskapBase.


        :param egenskapstype: The egenskapstype of this VegobjektEgenskapBase.  # noqa: E501
        :type: Egenskapstype
        """

        self._egenskapstype = egenskapstype

    @property
    def datatype(self):
        """Gets the datatype of this VegobjektEgenskapBase.  # noqa: E501


        :return: The datatype of this VegobjektEgenskapBase.  # noqa: E501
        :rtype: Datatype
        """
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        """Sets the datatype of this VegobjektEgenskapBase.


        :param datatype: The datatype of this VegobjektEgenskapBase.  # noqa: E501
        :type: Datatype
        """

        self._datatype = datatype

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
        if issubclass(VegobjektEgenskapBase, dict):
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
        if not isinstance(other, VegobjektEgenskapBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
