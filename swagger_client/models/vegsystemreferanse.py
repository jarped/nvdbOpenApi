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

class Vegsystemreferanse(object):
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
        'kortform': 'str',
        'vegsystem': 'VegsystemreferanseVegsystem',
        'strekning': 'AllOfvegsystemreferanseStrekning',
        'kryssystem': 'AllOfvegsystemreferanseKryssystem',
        'sidealegg': 'AllOfvegsystemreferanseSidealegg'
    }

    attribute_map = {
        'kortform': 'kortform',
        'vegsystem': 'vegsystem',
        'strekning': 'strekning',
        'kryssystem': 'kryssystem',
        'sidealegg': 'sidealegg'
    }

    def __init__(self, kortform=None, vegsystem=None, strekning=None, kryssystem=None, sidealegg=None):  # noqa: E501
        """Vegsystemreferanse - a model defined in Swagger"""  # noqa: E501
        self._kortform = None
        self._vegsystem = None
        self._strekning = None
        self._kryssystem = None
        self._sidealegg = None
        self.discriminator = None
        if kortform is not None:
            self.kortform = kortform
        if vegsystem is not None:
            self.vegsystem = vegsystem
        if strekning is not None:
            self.strekning = strekning
        if kryssystem is not None:
            self.kryssystem = kryssystem
        if sidealegg is not None:
            self.sidealegg = sidealegg

    @property
    def kortform(self):
        """Gets the kortform of this Vegsystemreferanse.  # noqa: E501


        :return: The kortform of this Vegsystemreferanse.  # noqa: E501
        :rtype: str
        """
        return self._kortform

    @kortform.setter
    def kortform(self, kortform):
        """Sets the kortform of this Vegsystemreferanse.


        :param kortform: The kortform of this Vegsystemreferanse.  # noqa: E501
        :type: str
        """

        self._kortform = kortform

    @property
    def vegsystem(self):
        """Gets the vegsystem of this Vegsystemreferanse.  # noqa: E501


        :return: The vegsystem of this Vegsystemreferanse.  # noqa: E501
        :rtype: VegsystemreferanseVegsystem
        """
        return self._vegsystem

    @vegsystem.setter
    def vegsystem(self, vegsystem):
        """Sets the vegsystem of this Vegsystemreferanse.


        :param vegsystem: The vegsystem of this Vegsystemreferanse.  # noqa: E501
        :type: VegsystemreferanseVegsystem
        """

        self._vegsystem = vegsystem

    @property
    def strekning(self):
        """Gets the strekning of this Vegsystemreferanse.  # noqa: E501

        Strekning (916)  # noqa: E501

        :return: The strekning of this Vegsystemreferanse.  # noqa: E501
        :rtype: AllOfvegsystemreferanseStrekning
        """
        return self._strekning

    @strekning.setter
    def strekning(self, strekning):
        """Sets the strekning of this Vegsystemreferanse.

        Strekning (916)  # noqa: E501

        :param strekning: The strekning of this Vegsystemreferanse.  # noqa: E501
        :type: AllOfvegsystemreferanseStrekning
        """

        self._strekning = strekning

    @property
    def kryssystem(self):
        """Gets the kryssystem of this Vegsystemreferanse.  # noqa: E501

        Kryssystem (917) og Kryssdel (918)  # noqa: E501

        :return: The kryssystem of this Vegsystemreferanse.  # noqa: E501
        :rtype: AllOfvegsystemreferanseKryssystem
        """
        return self._kryssystem

    @kryssystem.setter
    def kryssystem(self, kryssystem):
        """Sets the kryssystem of this Vegsystemreferanse.

        Kryssystem (917) og Kryssdel (918)  # noqa: E501

        :param kryssystem: The kryssystem of this Vegsystemreferanse.  # noqa: E501
        :type: AllOfvegsystemreferanseKryssystem
        """

        self._kryssystem = kryssystem

    @property
    def sidealegg(self):
        """Gets the sidealegg of this Vegsystemreferanse.  # noqa: E501

        Sideanlegg (919) og Sideanleggsdel (920)  # noqa: E501

        :return: The sidealegg of this Vegsystemreferanse.  # noqa: E501
        :rtype: AllOfvegsystemreferanseSidealegg
        """
        return self._sidealegg

    @sidealegg.setter
    def sidealegg(self, sidealegg):
        """Sets the sidealegg of this Vegsystemreferanse.

        Sideanlegg (919) og Sideanleggsdel (920)  # noqa: E501

        :param sidealegg: The sidealegg of this Vegsystemreferanse.  # noqa: E501
        :type: AllOfvegsystemreferanseSidealegg
        """

        self._sidealegg = sidealegg

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
        if issubclass(Vegsystemreferanse, dict):
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
        if not isinstance(other, Vegsystemreferanse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
