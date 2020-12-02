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

class InlineResponse2008(object):
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
        'datagrunnlag': 'InlineResponse2008Datagrunnlag',
        'kjorende_oppgave': 'InlineResponse2008KjorendeOppgave'
    }

    attribute_map = {
        'datagrunnlag': 'datagrunnlag',
        'kjorende_oppgave': 'kjorende_oppgave'
    }

    def __init__(self, datagrunnlag=None, kjorende_oppgave=None):  # noqa: E501
        """InlineResponse2008 - a model defined in Swagger"""  # noqa: E501
        self._datagrunnlag = None
        self._kjorende_oppgave = None
        self.discriminator = None
        if datagrunnlag is not None:
            self.datagrunnlag = datagrunnlag
        if kjorende_oppgave is not None:
            self.kjorende_oppgave = kjorende_oppgave

    @property
    def datagrunnlag(self):
        """Gets the datagrunnlag of this InlineResponse2008.  # noqa: E501


        :return: The datagrunnlag of this InlineResponse2008.  # noqa: E501
        :rtype: InlineResponse2008Datagrunnlag
        """
        return self._datagrunnlag

    @datagrunnlag.setter
    def datagrunnlag(self, datagrunnlag):
        """Sets the datagrunnlag of this InlineResponse2008.


        :param datagrunnlag: The datagrunnlag of this InlineResponse2008.  # noqa: E501
        :type: InlineResponse2008Datagrunnlag
        """

        self._datagrunnlag = datagrunnlag

    @property
    def kjorende_oppgave(self):
        """Gets the kjorende_oppgave of this InlineResponse2008.  # noqa: E501


        :return: The kjorende_oppgave of this InlineResponse2008.  # noqa: E501
        :rtype: InlineResponse2008KjorendeOppgave
        """
        return self._kjorende_oppgave

    @kjorende_oppgave.setter
    def kjorende_oppgave(self, kjorende_oppgave):
        """Sets the kjorende_oppgave of this InlineResponse2008.


        :param kjorende_oppgave: The kjorende_oppgave of this InlineResponse2008.  # noqa: E501
        :type: InlineResponse2008KjorendeOppgave
        """

        self._kjorende_oppgave = kjorende_oppgave

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
        if issubclass(InlineResponse2008, dict):
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
        if not isinstance(other, InlineResponse2008):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
