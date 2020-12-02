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

class PosisjonsresultatVeglenkesekvens(object):
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
        'veglenkesekvensid': 'int',
        'relativ_posisjon': 'float',
        'kortform': 'str'
    }

    attribute_map = {
        'veglenkesekvensid': 'veglenkesekvensid',
        'relativ_posisjon': 'relativPosisjon',
        'kortform': 'kortform'
    }

    def __init__(self, veglenkesekvensid=None, relativ_posisjon=None, kortform=None):  # noqa: E501
        """PosisjonsresultatVeglenkesekvens - a model defined in Swagger"""  # noqa: E501
        self._veglenkesekvensid = None
        self._relativ_posisjon = None
        self._kortform = None
        self.discriminator = None
        if veglenkesekvensid is not None:
            self.veglenkesekvensid = veglenkesekvensid
        if relativ_posisjon is not None:
            self.relativ_posisjon = relativ_posisjon
        if kortform is not None:
            self.kortform = kortform

    @property
    def veglenkesekvensid(self):
        """Gets the veglenkesekvensid of this PosisjonsresultatVeglenkesekvens.  # noqa: E501


        :return: The veglenkesekvensid of this PosisjonsresultatVeglenkesekvens.  # noqa: E501
        :rtype: int
        """
        return self._veglenkesekvensid

    @veglenkesekvensid.setter
    def veglenkesekvensid(self, veglenkesekvensid):
        """Sets the veglenkesekvensid of this PosisjonsresultatVeglenkesekvens.


        :param veglenkesekvensid: The veglenkesekvensid of this PosisjonsresultatVeglenkesekvens.  # noqa: E501
        :type: int
        """

        self._veglenkesekvensid = veglenkesekvensid

    @property
    def relativ_posisjon(self):
        """Gets the relativ_posisjon of this PosisjonsresultatVeglenkesekvens.  # noqa: E501


        :return: The relativ_posisjon of this PosisjonsresultatVeglenkesekvens.  # noqa: E501
        :rtype: float
        """
        return self._relativ_posisjon

    @relativ_posisjon.setter
    def relativ_posisjon(self, relativ_posisjon):
        """Sets the relativ_posisjon of this PosisjonsresultatVeglenkesekvens.


        :param relativ_posisjon: The relativ_posisjon of this PosisjonsresultatVeglenkesekvens.  # noqa: E501
        :type: float
        """

        self._relativ_posisjon = relativ_posisjon

    @property
    def kortform(self):
        """Gets the kortform of this PosisjonsresultatVeglenkesekvens.  # noqa: E501


        :return: The kortform of this PosisjonsresultatVeglenkesekvens.  # noqa: E501
        :rtype: str
        """
        return self._kortform

    @kortform.setter
    def kortform(self, kortform):
        """Sets the kortform of this PosisjonsresultatVeglenkesekvens.


        :param kortform: The kortform of this PosisjonsresultatVeglenkesekvens.  # noqa: E501
        :type: str
        """

        self._kortform = kortform

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
        if issubclass(PosisjonsresultatVeglenkesekvens, dict):
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
        if not isinstance(other, PosisjonsresultatVeglenkesekvens):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
