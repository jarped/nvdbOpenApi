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

class GeometriKvalitet(object):
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
        'mlemetode': 'str',
        'nyaktighet': 'int',
        'synbarhet': 'str',
        'mlemetode_hyde': 'str',
        'nyaktighet_hyde': 'int',
        'toleranse': 'int'
    }

    attribute_map = {
        'mlemetode': 'målemetode',
        'nyaktighet': 'nøyaktighet',
        'synbarhet': 'synbarhet',
        'mlemetode_hyde': 'målemetodeHøyde',
        'nyaktighet_hyde': 'nøyaktighetHøyde',
        'toleranse': 'toleranse'
    }

    def __init__(self, mlemetode=None, nyaktighet=None, synbarhet=None, mlemetode_hyde=None, nyaktighet_hyde=None, toleranse=None):  # noqa: E501
        """GeometriKvalitet - a model defined in Swagger"""  # noqa: E501
        self._mlemetode = None
        self._nyaktighet = None
        self._synbarhet = None
        self._mlemetode_hyde = None
        self._nyaktighet_hyde = None
        self._toleranse = None
        self.discriminator = None
        if mlemetode is not None:
            self.mlemetode = mlemetode
        if nyaktighet is not None:
            self.nyaktighet = nyaktighet
        if synbarhet is not None:
            self.synbarhet = synbarhet
        if mlemetode_hyde is not None:
            self.mlemetode_hyde = mlemetode_hyde
        if nyaktighet_hyde is not None:
            self.nyaktighet_hyde = nyaktighet_hyde
        if toleranse is not None:
            self.toleranse = toleranse

    @property
    def mlemetode(self):
        """Gets the mlemetode of this GeometriKvalitet.  # noqa: E501

        Se vegobjekttype 793 NVDB Dokumentasjon, egenskap 9543 Målemetode eller Kodeliste i kapitel 1.6.2.8.2.  # noqa: E501

        :return: The mlemetode of this GeometriKvalitet.  # noqa: E501
        :rtype: str
        """
        return self._mlemetode

    @mlemetode.setter
    def mlemetode(self, mlemetode):
        """Sets the mlemetode of this GeometriKvalitet.

        Se vegobjekttype 793 NVDB Dokumentasjon, egenskap 9543 Målemetode eller Kodeliste i kapitel 1.6.2.8.2.  # noqa: E501

        :param mlemetode: The mlemetode of this GeometriKvalitet.  # noqa: E501
        :type: str
        """
        allowed_values = ["Terrengmålt", "Fastsatt ved dom eller kongelig resolusjon", "Flere, som ikke listes ut her."]  # noqa: E501
        if mlemetode not in allowed_values:
            raise ValueError(
                "Invalid value for `mlemetode` ({0}), must be one of {1}"  # noqa: E501
                .format(mlemetode, allowed_values)
            )

        self._mlemetode = mlemetode

    @property
    def nyaktighet(self):
        """Gets the nyaktighet of this GeometriKvalitet.  # noqa: E501

        Punktstandardavviket i grunnriss for punkter samt tverravvik for linjer, i cm. Se underegenskap 9551 Nøyaktighet.  # noqa: E501

        :return: The nyaktighet of this GeometriKvalitet.  # noqa: E501
        :rtype: int
        """
        return self._nyaktighet

    @nyaktighet.setter
    def nyaktighet(self, nyaktighet):
        """Sets the nyaktighet of this GeometriKvalitet.

        Punktstandardavviket i grunnriss for punkter samt tverravvik for linjer, i cm. Se underegenskap 9551 Nøyaktighet.  # noqa: E501

        :param nyaktighet: The nyaktighet of this GeometriKvalitet.  # noqa: E501
        :type: int
        """

        self._nyaktighet = nyaktighet

    @property
    def synbarhet(self):
        """Gets the synbarhet of this GeometriKvalitet.  # noqa: E501

        Hvor godt den kartlagte detalj var synbar ved kartleggingen. Kodeliste i kapitel 1.6.2.8.4. Se underegenskap 9545 Synbarhet  # noqa: E501

        :return: The synbarhet of this GeometriKvalitet.  # noqa: E501
        :rtype: str
        """
        return self._synbarhet

    @synbarhet.setter
    def synbarhet(self, synbarhet):
        """Sets the synbarhet of this GeometriKvalitet.

        Hvor godt den kartlagte detalj var synbar ved kartleggingen. Kodeliste i kapitel 1.6.2.8.4. Se underegenskap 9545 Synbarhet  # noqa: E501

        :param synbarhet: The synbarhet of this GeometriKvalitet.  # noqa: E501
        :type: str
        """
        allowed_values = ["Ikke registrert", "Fullt ut synlig/gjenfinnbar i terrenget", "Dårlig gjenfinnbar i terreng", "Middels synlig i flybilde/modell", "Dårlig/ikke synlig i flybilde/modell"]  # noqa: E501
        if synbarhet not in allowed_values:
            raise ValueError(
                "Invalid value for `synbarhet` ({0}), must be one of {1}"  # noqa: E501
                .format(synbarhet, allowed_values)
            )

        self._synbarhet = synbarhet

    @property
    def mlemetode_hyde(self):
        """Gets the mlemetode_hyde of this GeometriKvalitet.  # noqa: E501

        Metode for å måle objekttypens høydeverdi. Kodeliste i kapitel 1.6.2.8.3. Se underegenskap 9544 H-målemetode.  # noqa: E501

        :return: The mlemetode_hyde of this GeometriKvalitet.  # noqa: E501
        :rtype: str
        """
        return self._mlemetode_hyde

    @mlemetode_hyde.setter
    def mlemetode_hyde(self, mlemetode_hyde):
        """Sets the mlemetode_hyde of this GeometriKvalitet.

        Metode for å måle objekttypens høydeverdi. Kodeliste i kapitel 1.6.2.8.3. Se underegenskap 9544 H-målemetode.  # noqa: E501

        :param mlemetode_hyde: The mlemetode_hyde of this GeometriKvalitet.  # noqa: E501
        :type: str
        """
        allowed_values = ["Spesielle metoder", "Ikke registrert", "Flere, ikke listet ut her."]  # noqa: E501
        if mlemetode_hyde not in allowed_values:
            raise ValueError(
                "Invalid value for `mlemetode_hyde` ({0}), must be one of {1}"  # noqa: E501
                .format(mlemetode_hyde, allowed_values)
            )

        self._mlemetode_hyde = mlemetode_hyde

    @property
    def nyaktighet_hyde(self):
        """Gets the nyaktighet_hyde of this GeometriKvalitet.  # noqa: E501

        Nøyaktighet for høyden i cm. Se underegenskap 9552 H-nøyaktighet  # noqa: E501

        :return: The nyaktighet_hyde of this GeometriKvalitet.  # noqa: E501
        :rtype: int
        """
        return self._nyaktighet_hyde

    @nyaktighet_hyde.setter
    def nyaktighet_hyde(self, nyaktighet_hyde):
        """Sets the nyaktighet_hyde of this GeometriKvalitet.

        Nøyaktighet for høyden i cm. Se underegenskap 9552 H-nøyaktighet  # noqa: E501

        :param nyaktighet_hyde: The nyaktighet_hyde of this GeometriKvalitet.  # noqa: E501
        :type: int
        """

        self._nyaktighet_hyde = nyaktighet_hyde

    @property
    def toleranse(self):
        """Gets the toleranse of this GeometriKvalitet.  # noqa: E501

        Absolutt toleranse for geometriske avvik. Se underegenskap 9783 Toleranse  # noqa: E501

        :return: The toleranse of this GeometriKvalitet.  # noqa: E501
        :rtype: int
        """
        return self._toleranse

    @toleranse.setter
    def toleranse(self, toleranse):
        """Sets the toleranse of this GeometriKvalitet.

        Absolutt toleranse for geometriske avvik. Se underegenskap 9783 Toleranse  # noqa: E501

        :param toleranse: The toleranse of this GeometriKvalitet.  # noqa: E501
        :type: int
        """

        self._toleranse = toleranse

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
        if issubclass(GeometriKvalitet, dict):
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
        if not isinstance(other, GeometriKvalitet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
