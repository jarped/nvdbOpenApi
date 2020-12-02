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

class PagineringMetadata(object):
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
        'antall': 'int',
        'returnert': 'int',
        'sidestrrelse': 'int',
        'neste': 'PagineringmetadataNeste'
    }

    attribute_map = {
        'antall': 'antall',
        'returnert': 'returnert',
        'sidestrrelse': 'sidestørrelse',
        'neste': 'neste'
    }

    def __init__(self, antall=None, returnert=None, sidestrrelse=None, neste=None):  # noqa: E501
        """PagineringMetadata - a model defined in Swagger"""  # noqa: E501
        self._antall = None
        self._returnert = None
        self._sidestrrelse = None
        self._neste = None
        self.discriminator = None
        if antall is not None:
            self.antall = antall
        if returnert is not None:
            self.returnert = returnert
        if sidestrrelse is not None:
            self.sidestrrelse = sidestrrelse
        if neste is not None:
            self.neste = neste

    @property
    def antall(self):
        """Gets the antall of this PagineringMetadata.  # noqa: E501

        Totalt antall treff  # noqa: E501

        :return: The antall of this PagineringMetadata.  # noqa: E501
        :rtype: int
        """
        return self._antall

    @antall.setter
    def antall(self, antall):
        """Sets the antall of this PagineringMetadata.

        Totalt antall treff  # noqa: E501

        :param antall: The antall of this PagineringMetadata.  # noqa: E501
        :type: int
        """

        self._antall = antall

    @property
    def returnert(self):
        """Gets the returnert of this PagineringMetadata.  # noqa: E501

        Antallet objekter som ble returnert i denne responsen.  # noqa: E501

        :return: The returnert of this PagineringMetadata.  # noqa: E501
        :rtype: int
        """
        return self._returnert

    @returnert.setter
    def returnert(self, returnert):
        """Sets the returnert of this PagineringMetadata.

        Antallet objekter som ble returnert i denne responsen.  # noqa: E501

        :param returnert: The returnert of this PagineringMetadata.  # noqa: E501
        :type: int
        """

        self._returnert = returnert

    @property
    def sidestrrelse(self):
        """Gets the sidestrrelse of this PagineringMetadata.  # noqa: E501

        Maks antall objekter som blir returnert per side  # noqa: E501

        :return: The sidestrrelse of this PagineringMetadata.  # noqa: E501
        :rtype: int
        """
        return self._sidestrrelse

    @sidestrrelse.setter
    def sidestrrelse(self, sidestrrelse):
        """Sets the sidestrrelse of this PagineringMetadata.

        Maks antall objekter som blir returnert per side  # noqa: E501

        :param sidestrrelse: The sidestrrelse of this PagineringMetadata.  # noqa: E501
        :type: int
        """

        self._sidestrrelse = sidestrrelse

    @property
    def neste(self):
        """Gets the neste of this PagineringMetadata.  # noqa: E501


        :return: The neste of this PagineringMetadata.  # noqa: E501
        :rtype: PagineringmetadataNeste
        """
        return self._neste

    @neste.setter
    def neste(self, neste):
        """Sets the neste of this PagineringMetadata.


        :param neste: The neste of this PagineringMetadata.  # noqa: E501
        :type: PagineringmetadataNeste
        """

        self._neste = neste

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
        if issubclass(PagineringMetadata, dict):
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
        if not isinstance(other, PagineringMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other