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

class VegobjekttypeRelasjonstyper(object):
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
        'foreldre': 'list[VegobjekttypeRelasjon]',
        'barn': 'list[VegobjekttypeRelasjon]'
    }

    attribute_map = {
        'foreldre': 'foreldre',
        'barn': 'barn'
    }

    def __init__(self, foreldre=None, barn=None):  # noqa: E501
        """VegobjekttypeRelasjonstyper - a model defined in Swagger"""  # noqa: E501
        self._foreldre = None
        self._barn = None
        self.discriminator = None
        if foreldre is not None:
            self.foreldre = foreldre
        if barn is not None:
            self.barn = barn

    @property
    def foreldre(self):
        """Gets the foreldre of this VegobjekttypeRelasjonstyper.  # noqa: E501


        :return: The foreldre of this VegobjekttypeRelasjonstyper.  # noqa: E501
        :rtype: list[VegobjekttypeRelasjon]
        """
        return self._foreldre

    @foreldre.setter
    def foreldre(self, foreldre):
        """Sets the foreldre of this VegobjekttypeRelasjonstyper.


        :param foreldre: The foreldre of this VegobjekttypeRelasjonstyper.  # noqa: E501
        :type: list[VegobjekttypeRelasjon]
        """

        self._foreldre = foreldre

    @property
    def barn(self):
        """Gets the barn of this VegobjekttypeRelasjonstyper.  # noqa: E501


        :return: The barn of this VegobjekttypeRelasjonstyper.  # noqa: E501
        :rtype: list[VegobjekttypeRelasjon]
        """
        return self._barn

    @barn.setter
    def barn(self, barn):
        """Sets the barn of this VegobjekttypeRelasjonstyper.


        :param barn: The barn of this VegobjekttypeRelasjonstyper.  # noqa: E501
        :type: list[VegobjekttypeRelasjon]
        """

        self._barn = barn

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
        if issubclass(VegobjekttypeRelasjonstyper, dict):
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
        if not isinstance(other, VegobjekttypeRelasjonstyper):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other