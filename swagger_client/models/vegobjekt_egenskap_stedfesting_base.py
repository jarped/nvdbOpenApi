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

class VegobjektEgenskapStedfestingBase(object):
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
        'retning': 'Retning',
        'sideposisjon': 'Sideposisjon',
        'kjrefelt': 'Kjorefelt'
    }

    attribute_map = {
        'veglenkesekvensid': 'veglenkesekvensid',
        'retning': 'retning',
        'sideposisjon': 'sideposisjon',
        'kjrefelt': 'kjørefelt'
    }

    def __init__(self, veglenkesekvensid=None, retning=None, sideposisjon=None, kjrefelt=None):  # noqa: E501
        """VegobjektEgenskapStedfestingBase - a model defined in Swagger"""  # noqa: E501
        self._veglenkesekvensid = None
        self._retning = None
        self._sideposisjon = None
        self._kjrefelt = None
        self.discriminator = None
        if veglenkesekvensid is not None:
            self.veglenkesekvensid = veglenkesekvensid
        if retning is not None:
            self.retning = retning
        if sideposisjon is not None:
            self.sideposisjon = sideposisjon
        if kjrefelt is not None:
            self.kjrefelt = kjrefelt

    @property
    def veglenkesekvensid(self):
        """Gets the veglenkesekvensid of this VegobjektEgenskapStedfestingBase.  # noqa: E501

        Id for veglenkesekvens  # noqa: E501

        :return: The veglenkesekvensid of this VegobjektEgenskapStedfestingBase.  # noqa: E501
        :rtype: int
        """
        return self._veglenkesekvensid

    @veglenkesekvensid.setter
    def veglenkesekvensid(self, veglenkesekvensid):
        """Sets the veglenkesekvensid of this VegobjektEgenskapStedfestingBase.

        Id for veglenkesekvens  # noqa: E501

        :param veglenkesekvensid: The veglenkesekvensid of this VegobjektEgenskapStedfestingBase.  # noqa: E501
        :type: int
        """

        self._veglenkesekvensid = veglenkesekvensid

    @property
    def retning(self):
        """Gets the retning of this VegobjektEgenskapStedfestingBase.  # noqa: E501


        :return: The retning of this VegobjektEgenskapStedfestingBase.  # noqa: E501
        :rtype: Retning
        """
        return self._retning

    @retning.setter
    def retning(self, retning):
        """Sets the retning of this VegobjektEgenskapStedfestingBase.


        :param retning: The retning of this VegobjektEgenskapStedfestingBase.  # noqa: E501
        :type: Retning
        """

        self._retning = retning

    @property
    def sideposisjon(self):
        """Gets the sideposisjon of this VegobjektEgenskapStedfestingBase.  # noqa: E501


        :return: The sideposisjon of this VegobjektEgenskapStedfestingBase.  # noqa: E501
        :rtype: Sideposisjon
        """
        return self._sideposisjon

    @sideposisjon.setter
    def sideposisjon(self, sideposisjon):
        """Sets the sideposisjon of this VegobjektEgenskapStedfestingBase.


        :param sideposisjon: The sideposisjon of this VegobjektEgenskapStedfestingBase.  # noqa: E501
        :type: Sideposisjon
        """

        self._sideposisjon = sideposisjon

    @property
    def kjrefelt(self):
        """Gets the kjrefelt of this VegobjektEgenskapStedfestingBase.  # noqa: E501


        :return: The kjrefelt of this VegobjektEgenskapStedfestingBase.  # noqa: E501
        :rtype: Kjorefelt
        """
        return self._kjrefelt

    @kjrefelt.setter
    def kjrefelt(self, kjrefelt):
        """Sets the kjrefelt of this VegobjektEgenskapStedfestingBase.


        :param kjrefelt: The kjrefelt of this VegobjektEgenskapStedfestingBase.  # noqa: E501
        :type: Kjorefelt
        """

        self._kjrefelt = kjrefelt

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
        if issubclass(VegobjektEgenskapStedfestingBase, dict):
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
        if not isinstance(other, VegobjektEgenskapStedfestingBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
