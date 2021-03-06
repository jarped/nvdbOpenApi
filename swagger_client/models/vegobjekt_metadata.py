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

class VegobjektMetadata(object):
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
        'type': 'VegobjektmetadataType',
        'versjon': 'int',
        'startdato': 'date',
        'sluttdato': 'date'
    }

    attribute_map = {
        'type': 'type',
        'versjon': 'versjon',
        'startdato': 'startdato',
        'sluttdato': 'sluttdato'
    }

    def __init__(self, type=None, versjon=None, startdato=None, sluttdato=None):  # noqa: E501
        """VegobjektMetadata - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._versjon = None
        self._startdato = None
        self._sluttdato = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if versjon is not None:
            self.versjon = versjon
        if startdato is not None:
            self.startdato = startdato
        if sluttdato is not None:
            self.sluttdato = sluttdato

    @property
    def type(self):
        """Gets the type of this VegobjektMetadata.  # noqa: E501


        :return: The type of this VegobjektMetadata.  # noqa: E501
        :rtype: VegobjektmetadataType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VegobjektMetadata.


        :param type: The type of this VegobjektMetadata.  # noqa: E501
        :type: VegobjektmetadataType
        """

        self._type = type

    @property
    def versjon(self):
        """Gets the versjon of this VegobjektMetadata.  # noqa: E501

        Versjonsnummer for dette objektet  # noqa: E501

        :return: The versjon of this VegobjektMetadata.  # noqa: E501
        :rtype: int
        """
        return self._versjon

    @versjon.setter
    def versjon(self, versjon):
        """Sets the versjon of this VegobjektMetadata.

        Versjonsnummer for dette objektet  # noqa: E501

        :param versjon: The versjon of this VegobjektMetadata.  # noqa: E501
        :type: int
        """

        self._versjon = versjon

    @property
    def startdato(self):
        """Gets the startdato of this VegobjektMetadata.  # noqa: E501

        Når dette objektet ble gjeldende  # noqa: E501

        :return: The startdato of this VegobjektMetadata.  # noqa: E501
        :rtype: date
        """
        return self._startdato

    @startdato.setter
    def startdato(self, startdato):
        """Sets the startdato of this VegobjektMetadata.

        Når dette objektet ble gjeldende  # noqa: E501

        :param startdato: The startdato of this VegobjektMetadata.  # noqa: E501
        :type: date
        """

        self._startdato = startdato

    @property
    def sluttdato(self):
        """Gets the sluttdato of this VegobjektMetadata.  # noqa: E501

        Når dette objektet ikke lengre er gjeldende  # noqa: E501

        :return: The sluttdato of this VegobjektMetadata.  # noqa: E501
        :rtype: date
        """
        return self._sluttdato

    @sluttdato.setter
    def sluttdato(self, sluttdato):
        """Sets the sluttdato of this VegobjektMetadata.

        Når dette objektet ikke lengre er gjeldende  # noqa: E501

        :param sluttdato: The sluttdato of this VegobjektMetadata.  # noqa: E501
        :type: date
        """

        self._sluttdato = sluttdato

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
        if issubclass(VegobjektMetadata, dict):
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
        if not isinstance(other, VegobjektMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
