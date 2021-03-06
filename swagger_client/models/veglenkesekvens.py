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

class Veglenkesekvens(object):
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
        'href': 'str',
        'lst_lengde': 'bool',
        'lengde': 'float',
        'porter': 'list[Port]',
        'veglenker': 'list[AnyOfveglenkesekvensVeglenkerItems]'
    }

    attribute_map = {
        'veglenkesekvensid': 'veglenkesekvensid',
        'href': 'href',
        'lst_lengde': 'låst_lengde',
        'lengde': 'lengde',
        'porter': 'porter',
        'veglenker': 'veglenker'
    }

    def __init__(self, veglenkesekvensid=None, href=None, lst_lengde=None, lengde=None, porter=None, veglenker=None):  # noqa: E501
        """Veglenkesekvens - a model defined in Swagger"""  # noqa: E501
        self._veglenkesekvensid = None
        self._href = None
        self._lst_lengde = None
        self._lengde = None
        self._porter = None
        self._veglenker = None
        self.discriminator = None
        if veglenkesekvensid is not None:
            self.veglenkesekvensid = veglenkesekvensid
        if href is not None:
            self.href = href
        if lst_lengde is not None:
            self.lst_lengde = lst_lengde
        if lengde is not None:
            self.lengde = lengde
        if porter is not None:
            self.porter = porter
        if veglenker is not None:
            self.veglenker = veglenker

    @property
    def veglenkesekvensid(self):
        """Gets the veglenkesekvensid of this Veglenkesekvens.  # noqa: E501


        :return: The veglenkesekvensid of this Veglenkesekvens.  # noqa: E501
        :rtype: int
        """
        return self._veglenkesekvensid

    @veglenkesekvensid.setter
    def veglenkesekvensid(self, veglenkesekvensid):
        """Sets the veglenkesekvensid of this Veglenkesekvens.


        :param veglenkesekvensid: The veglenkesekvensid of this Veglenkesekvens.  # noqa: E501
        :type: int
        """

        self._veglenkesekvensid = veglenkesekvensid

    @property
    def href(self):
        """Gets the href of this Veglenkesekvens.  # noqa: E501


        :return: The href of this Veglenkesekvens.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Veglenkesekvens.


        :param href: The href of this Veglenkesekvens.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def lst_lengde(self):
        """Gets the lst_lengde of this Veglenkesekvens.  # noqa: E501


        :return: The lst_lengde of this Veglenkesekvens.  # noqa: E501
        :rtype: bool
        """
        return self._lst_lengde

    @lst_lengde.setter
    def lst_lengde(self, lst_lengde):
        """Sets the lst_lengde of this Veglenkesekvens.


        :param lst_lengde: The lst_lengde of this Veglenkesekvens.  # noqa: E501
        :type: bool
        """

        self._lst_lengde = lst_lengde

    @property
    def lengde(self):
        """Gets the lengde of this Veglenkesekvens.  # noqa: E501


        :return: The lengde of this Veglenkesekvens.  # noqa: E501
        :rtype: float
        """
        return self._lengde

    @lengde.setter
    def lengde(self, lengde):
        """Sets the lengde of this Veglenkesekvens.


        :param lengde: The lengde of this Veglenkesekvens.  # noqa: E501
        :type: float
        """

        self._lengde = lengde

    @property
    def porter(self):
        """Gets the porter of this Veglenkesekvens.  # noqa: E501


        :return: The porter of this Veglenkesekvens.  # noqa: E501
        :rtype: list[Port]
        """
        return self._porter

    @porter.setter
    def porter(self, porter):
        """Sets the porter of this Veglenkesekvens.


        :param porter: The porter of this Veglenkesekvens.  # noqa: E501
        :type: list[Port]
        """

        self._porter = porter

    @property
    def veglenker(self):
        """Gets the veglenker of this Veglenkesekvens.  # noqa: E501


        :return: The veglenker of this Veglenkesekvens.  # noqa: E501
        :rtype: list[AnyOfveglenkesekvensVeglenkerItems]
        """
        return self._veglenker

    @veglenker.setter
    def veglenker(self, veglenker):
        """Sets the veglenker of this Veglenkesekvens.


        :param veglenker: The veglenker of this Veglenkesekvens.  # noqa: E501
        :type: list[AnyOfveglenkesekvensVeglenkerItems]
        """

        self._veglenker = veglenker

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
        if issubclass(Veglenkesekvens, dict):
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
        if not isinstance(other, Veglenkesekvens):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
