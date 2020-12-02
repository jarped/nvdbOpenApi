# Vegobjekttype

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**navn** | **str** |  | [optional] 
**beskrivelse** | **str** |  | [optional] 
**stedfesting** | [**Object**](Object.md) | TODO | [optional] 
**objektliste_dato** | **date** | Dato for når vegobjekttypen ble en del av objektlista. Om feltet ikke har noen verdi, er ikke vegobjekttypen en del av objektlista | [optional] 
**veiledning** | **str** | Supplerende informasjon til beskrivelsen, for eksempel en registreringsveiledning | [optional] 
**sosinvdbnavn** | **str** | Navn som brukes i dataleveranser | [optional] 
**sosinavn** | **str** | Navn som brukes i dataleveranser | [optional] 
**sorteringsnummer** | **int** | For bruk i sortering av objektlista | [optional] 
**kategorier** | [**list[VegobjekttypeKategorier]**](VegobjekttypeKategorier.md) | Hvilke kategorier denne vegobjekttypen hører til | [optional] 
**egenskaper** | [**list[VegobjekttypeEgenskap]**](VegobjekttypeEgenskap.md) |  | [optional] 
**relasjonstyper** | [**list[VegobjekttypeRelasjonstyper]**](VegobjekttypeRelasjonstyper.md) | TODO | [optional] 
**status** | **str** |  | [optional] 
**hovedkategori** | **str** |  | [optional] 
**dekningsgrad** | **bool** | Angir om eksisterende objekter skal bli automatisk splittet når de overlapper med nye objekter. true&#x3D;Skal splittes, false&#x3D;Skal ikke splittes | [optional] 
**tidsrom_relevant** | **bool** | Angir om vegobjektene normalt har en gyldighetsperiode på operativt vegnett | [optional] 
**konnekteringslenke_ok** | **bool** | Angir om vegobjekter av denne typen skal kunne stedfestes på konnekteringslenker | [optional] 
**abstrakt_type** | **bool** | Angir om vegobjekttype er abstrakt eller ikke. En abstrakt vegobjekttype skal ikke kunne ha forekomster i NVDB. | [optional] 
**m_ha_mor** | **bool** | Angir hvorvidt vegobjektene må være tilknyttet et morobjekt for å kunne eksistere. | [optional] 
**er_dataserie** | **bool** |  | [optional] 
**en_versjon** | **bool** | Angir om det er tillatt med kun én versjon av et vegobjekt. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

