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

class VegobjektListeRespons(object):
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
        'objekter': 'list[Vegobjekt]',
        'metadata': 'PagineringMetadata'
    }

    attribute_map = {
        'objekter': 'objekter',
        'metadata': 'metadata'
    }

    def __init__(self, objekter=None, metadata=None):  # noqa: E501
        """VegobjektListeRespons - a model defined in Swagger"""  # noqa: E501
        self._objekter = None
        self._metadata = None
        self.discriminator = None
        if objekter is not None:
            self.objekter = objekter
        if metadata is not None:
            self.metadata = metadata

    @property
    def objekter(self):
        """Gets the objekter of this VegobjektListeRespons.  # noqa: E501


        :return: The objekter of this VegobjektListeRespons.  # noqa: E501
        :rtype: list[Vegobjekt]
        """
        return self._objekter

    @objekter.setter
    def objekter(self, objekter):
        """Sets the objekter of this VegobjektListeRespons.


        :param objekter: The objekter of this VegobjektListeRespons.  # noqa: E501
        :type: list[Vegobjekt]
        """

        self._objekter = objekter

    @property
    def metadata(self):
        """Gets the metadata of this VegobjektListeRespons.  # noqa: E501


        :return: The metadata of this VegobjektListeRespons.  # noqa: E501
        :rtype: PagineringMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this VegobjektListeRespons.


        :param metadata: The metadata of this VegobjektListeRespons.  # noqa: E501
        :type: PagineringMetadata
        """

        self._metadata = metadata

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
        if issubclass(VegobjektListeRespons, dict):
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
        if not isinstance(other, VegobjektListeRespons):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other