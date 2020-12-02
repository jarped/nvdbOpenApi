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
from swagger_client.models.meter_referanse import MeterReferanse  # noqa: F401,E501

class AllOfvegsystemreferanseStrekning(MeterReferanse):
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
        'id': 'int',
        'version': 'int',
        'strekning': 'int',
        'delstrekning': 'int',
        'arm': 'bool',
        'adskilte_lp': 'str',
        'adskilte_lp_nummer': 'str',
        'trafikantgruppe': 'str',
        'retning': 'Retning'
    }
    if hasattr(MeterReferanse, "swagger_types"):
        swagger_types.update(MeterReferanse.swagger_types)

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'strekning': 'strekning',
        'delstrekning': 'delstrekning',
        'arm': 'arm',
        'adskilte_lp': 'adskilte_løp',
        'adskilte_lp_nummer': 'adskilte_løp_nummer',
        'trafikantgruppe': 'trafikantgruppe',
        'retning': 'retning'
    }
    if hasattr(MeterReferanse, "attribute_map"):
        attribute_map.update(MeterReferanse.attribute_map)

    def __init__(self, id=None, version=None, strekning=None, delstrekning=None, arm=None, adskilte_lp=None, adskilte_lp_nummer=None, trafikantgruppe=None, retning=None, *args, **kwargs):  # noqa: E501
        """AllOfvegsystemreferanseStrekning - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._version = None
        self._strekning = None
        self._delstrekning = None
        self._arm = None
        self._adskilte_lp = None
        self._adskilte_lp_nummer = None
        self._trafikantgruppe = None
        self._retning = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if strekning is not None:
            self.strekning = strekning
        if delstrekning is not None:
            self.delstrekning = delstrekning
        if arm is not None:
            self.arm = arm
        if adskilte_lp is not None:
            self.adskilte_lp = adskilte_lp
        if adskilte_lp_nummer is not None:
            self.adskilte_lp_nummer = adskilte_lp_nummer
        if trafikantgruppe is not None:
            self.trafikantgruppe = trafikantgruppe
        if retning is not None:
            self.retning = retning
        MeterReferanse.__init__(self, *args, **kwargs)

    @property
    def id(self):
        """Gets the id of this AllOfvegsystemreferanseStrekning.  # noqa: E501

        Fraværende for objekters vegsystemreferanse  # noqa: E501

        :return: The id of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AllOfvegsystemreferanseStrekning.

        Fraværende for objekters vegsystemreferanse  # noqa: E501

        :param id: The id of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def version(self):
        """Gets the version of this AllOfvegsystemreferanseStrekning.  # noqa: E501

        Fraværende for objekters vegsystemreferanse  # noqa: E501

        :return: The version of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AllOfvegsystemreferanseStrekning.

        Fraværende for objekters vegsystemreferanse  # noqa: E501

        :param version: The version of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def strekning(self):
        """Gets the strekning of this AllOfvegsystemreferanseStrekning.  # noqa: E501


        :return: The strekning of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :rtype: int
        """
        return self._strekning

    @strekning.setter
    def strekning(self, strekning):
        """Sets the strekning of this AllOfvegsystemreferanseStrekning.


        :param strekning: The strekning of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :type: int
        """

        self._strekning = strekning

    @property
    def delstrekning(self):
        """Gets the delstrekning of this AllOfvegsystemreferanseStrekning.  # noqa: E501


        :return: The delstrekning of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :rtype: int
        """
        return self._delstrekning

    @delstrekning.setter
    def delstrekning(self, delstrekning):
        """Sets the delstrekning of this AllOfvegsystemreferanseStrekning.


        :param delstrekning: The delstrekning of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :type: int
        """

        self._delstrekning = delstrekning

    @property
    def arm(self):
        """Gets the arm of this AllOfvegsystemreferanseStrekning.  # noqa: E501


        :return: The arm of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :rtype: bool
        """
        return self._arm

    @arm.setter
    def arm(self, arm):
        """Sets the arm of this AllOfvegsystemreferanseStrekning.


        :param arm: The arm of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :type: bool
        """

        self._arm = arm

    @property
    def adskilte_lp(self):
        """Gets the adskilte_lp of this AllOfvegsystemreferanseStrekning.  # noqa: E501


        :return: The adskilte_lp of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :rtype: str
        """
        return self._adskilte_lp

    @adskilte_lp.setter
    def adskilte_lp(self, adskilte_lp):
        """Sets the adskilte_lp of this AllOfvegsystemreferanseStrekning.


        :param adskilte_lp: The adskilte_lp of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :type: str
        """

        self._adskilte_lp = adskilte_lp

    @property
    def adskilte_lp_nummer(self):
        """Gets the adskilte_lp_nummer of this AllOfvegsystemreferanseStrekning.  # noqa: E501


        :return: The adskilte_lp_nummer of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :rtype: str
        """
        return self._adskilte_lp_nummer

    @adskilte_lp_nummer.setter
    def adskilte_lp_nummer(self, adskilte_lp_nummer):
        """Sets the adskilte_lp_nummer of this AllOfvegsystemreferanseStrekning.


        :param adskilte_lp_nummer: The adskilte_lp_nummer of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :type: str
        """

        self._adskilte_lp_nummer = adskilte_lp_nummer

    @property
    def trafikantgruppe(self):
        """Gets the trafikantgruppe of this AllOfvegsystemreferanseStrekning.  # noqa: E501


        :return: The trafikantgruppe of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :rtype: str
        """
        return self._trafikantgruppe

    @trafikantgruppe.setter
    def trafikantgruppe(self, trafikantgruppe):
        """Sets the trafikantgruppe of this AllOfvegsystemreferanseStrekning.


        :param trafikantgruppe: The trafikantgruppe of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :type: str
        """
        allowed_values = ["K", "G"]  # noqa: E501
        if trafikantgruppe not in allowed_values:
            raise ValueError(
                "Invalid value for `trafikantgruppe` ({0}), must be one of {1}"  # noqa: E501
                .format(trafikantgruppe, allowed_values)
            )

        self._trafikantgruppe = trafikantgruppe

    @property
    def retning(self):
        """Gets the retning of this AllOfvegsystemreferanseStrekning.  # noqa: E501


        :return: The retning of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :rtype: Retning
        """
        return self._retning

    @retning.setter
    def retning(self, retning):
        """Sets the retning of this AllOfvegsystemreferanseStrekning.


        :param retning: The retning of this AllOfvegsystemreferanseStrekning.  # noqa: E501
        :type: Retning
        """

        self._retning = retning

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
        if issubclass(AllOfvegsystemreferanseStrekning, dict):
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
        if not isinstance(other, AllOfvegsystemreferanseStrekning):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
