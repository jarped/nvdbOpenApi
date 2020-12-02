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

class VegobjekttypeRelasjonListe(object):
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
        'innhold': 'VegobjekttypeRelasjonEnkel'
    }

    attribute_map = {
        'innhold': 'innhold'
    }

    def __init__(self, innhold=None):  # noqa: E501
        """VegobjekttypeRelasjonListe - a model defined in Swagger"""  # noqa: E501
        self._innhold = None
        self.discriminator = None
        if innhold is not None:
            self.innhold = innhold

    @property
    def innhold(self):
        """Gets the innhold of this VegobjekttypeRelasjonListe.  # noqa: E501


        :return: The innhold of this VegobjekttypeRelasjonListe.  # noqa: E501
        :rtype: VegobjekttypeRelasjonEnkel
        """
        return self._innhold

    @innhold.setter
    def innhold(self, innhold):
        """Sets the innhold of this VegobjekttypeRelasjonListe.


        :param innhold: The innhold of this VegobjekttypeRelasjonListe.  # noqa: E501
        :type: VegobjekttypeRelasjonEnkel
        """

        self._innhold = innhold

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
        if issubclass(VegobjekttypeRelasjonListe, dict):
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
        if not isinstance(other, VegobjekttypeRelasjonListe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
