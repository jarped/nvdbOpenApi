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

class VegobjekttypeKategorier(object):
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
        'primrkategori': 'bool',
        'nummer': 'int',
        'id': 'int',
        'navn': 'str'
    }

    attribute_map = {
        'primrkategori': 'primærkategori',
        'nummer': 'nummer',
        'id': 'id',
        'navn': 'navn'
    }

    def __init__(self, primrkategori=None, nummer=None, id=None, navn=None):  # noqa: E501
        """VegobjekttypeKategorier - a model defined in Swagger"""  # noqa: E501
        self._primrkategori = None
        self._nummer = None
        self._id = None
        self._navn = None
        self.discriminator = None
        if primrkategori is not None:
            self.primrkategori = primrkategori
        if nummer is not None:
            self.nummer = nummer
        if id is not None:
            self.id = id
        if navn is not None:
            self.navn = navn

    @property
    def primrkategori(self):
        """Gets the primrkategori of this VegobjekttypeKategorier.  # noqa: E501


        :return: The primrkategori of this VegobjekttypeKategorier.  # noqa: E501
        :rtype: bool
        """
        return self._primrkategori

    @primrkategori.setter
    def primrkategori(self, primrkategori):
        """Sets the primrkategori of this VegobjekttypeKategorier.


        :param primrkategori: The primrkategori of this VegobjekttypeKategorier.  # noqa: E501
        :type: bool
        """

        self._primrkategori = primrkategori

    @property
    def nummer(self):
        """Gets the nummer of this VegobjekttypeKategorier.  # noqa: E501


        :return: The nummer of this VegobjekttypeKategorier.  # noqa: E501
        :rtype: int
        """
        return self._nummer

    @nummer.setter
    def nummer(self, nummer):
        """Sets the nummer of this VegobjekttypeKategorier.


        :param nummer: The nummer of this VegobjekttypeKategorier.  # noqa: E501
        :type: int
        """

        self._nummer = nummer

    @property
    def id(self):
        """Gets the id of this VegobjekttypeKategorier.  # noqa: E501


        :return: The id of this VegobjekttypeKategorier.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VegobjekttypeKategorier.


        :param id: The id of this VegobjekttypeKategorier.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def navn(self):
        """Gets the navn of this VegobjekttypeKategorier.  # noqa: E501


        :return: The navn of this VegobjekttypeKategorier.  # noqa: E501
        :rtype: str
        """
        return self._navn

    @navn.setter
    def navn(self, navn):
        """Sets the navn of this VegobjekttypeKategorier.


        :param navn: The navn of this VegobjekttypeKategorier.  # noqa: E501
        :type: str
        """

        self._navn = navn

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
        if issubclass(VegobjekttypeKategorier, dict):
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
        if not isinstance(other, VegobjekttypeKategorier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
