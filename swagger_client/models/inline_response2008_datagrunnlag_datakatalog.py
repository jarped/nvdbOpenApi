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

class InlineResponse2008DatagrunnlagDatakatalog(object):
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
        'dato': 'date',
        'id': 'int',
        'versjon': 'str'
    }

    attribute_map = {
        'dato': 'dato',
        'id': 'id',
        'versjon': 'versjon'
    }

    def __init__(self, dato=None, id=None, versjon=None):  # noqa: E501
        """InlineResponse2008DatagrunnlagDatakatalog - a model defined in Swagger"""  # noqa: E501
        self._dato = None
        self._id = None
        self._versjon = None
        self.discriminator = None
        if dato is not None:
            self.dato = dato
        if id is not None:
            self.id = id
        if versjon is not None:
            self.versjon = versjon

    @property
    def dato(self):
        """Gets the dato of this InlineResponse2008DatagrunnlagDatakatalog.  # noqa: E501


        :return: The dato of this InlineResponse2008DatagrunnlagDatakatalog.  # noqa: E501
        :rtype: date
        """
        return self._dato

    @dato.setter
    def dato(self, dato):
        """Sets the dato of this InlineResponse2008DatagrunnlagDatakatalog.


        :param dato: The dato of this InlineResponse2008DatagrunnlagDatakatalog.  # noqa: E501
        :type: date
        """

        self._dato = dato

    @property
    def id(self):
        """Gets the id of this InlineResponse2008DatagrunnlagDatakatalog.  # noqa: E501


        :return: The id of this InlineResponse2008DatagrunnlagDatakatalog.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2008DatagrunnlagDatakatalog.


        :param id: The id of this InlineResponse2008DatagrunnlagDatakatalog.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def versjon(self):
        """Gets the versjon of this InlineResponse2008DatagrunnlagDatakatalog.  # noqa: E501


        :return: The versjon of this InlineResponse2008DatagrunnlagDatakatalog.  # noqa: E501
        :rtype: str
        """
        return self._versjon

    @versjon.setter
    def versjon(self, versjon):
        """Sets the versjon of this InlineResponse2008DatagrunnlagDatakatalog.


        :param versjon: The versjon of this InlineResponse2008DatagrunnlagDatakatalog.  # noqa: E501
        :type: str
        """

        self._versjon = versjon

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
        if issubclass(InlineResponse2008DatagrunnlagDatakatalog, dict):
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
        if not isinstance(other, InlineResponse2008DatagrunnlagDatakatalog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
