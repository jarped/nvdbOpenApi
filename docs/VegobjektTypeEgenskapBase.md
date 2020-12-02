# VegobjektTypeEgenskapBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Angir egenskapstypens unike id. | [optional] 
**kategori** | **int** | Kategorien til denne egenskapstypen. Se endepunkt /vegobjekttyper/egenskapstypekategorier | [optional] 
**navn** | **str** | Angir egenskapstypens offisielle navn. | [optional] 
**kortnavn** | **str** | Et forkortet navn | [optional] 
**beskrivelse** | **str** | Tekstlig beskrivelse av egenskapstypen. | [optional] 
**egenskapstype** | [**Egenskapstype**](Egenskapstype.md) |  | [optional] 
**datatype** | [**Datatype**](Datatype.md) |  | [optional] 
**sosinvdbnavn** | **str** | Navn som brukes i dataleveranser | [optional] 
**sosinavn** | **str** | Navn på tilsvarende objekttype i SOSI-standarden | [optional] 
**sorteringsnummer** | **int** | Sorteringsnummer for egenskapstypen | [optional] 
**sensitivitet** | **int** | Angir om egenskapstypen har verdier av sensitiv art. Dersom verdi er 0 er egenskapen ikke sensitiv. | [optional] 
**viktighet** | **str** | Angir om det er krav til regisrering av egenskapstypen | [optional] 
**ledetekst** | **str** |  | [optional] 
**skrivebeskyttet** | **bool** |  | [optional] 
**komplementr_egenskapstype** | **int** |  | [optional] 
**grunnrissreferanse** | **str** |  | [optional] 
**nyaktighetskrav_grunnriss** | **float** |  | [optional] 
**hydereferanse** | **str** |  | [optional] 
**hydereferanse_tall** | **int** |  | [optional] 
**nyaktighetskrav_hyde** | **float** |  | [optional] 
**referansegeometri_tilstrekkelig** | **bool** |  | [optional] 
**sosi_referanse** | **str** |  | [optional] 
**avledet** | **bool** |  | [optional] 
**obligatorisk_verdi** | **bool** |  | [optional] 
**gruppesorteringsnummer** | **int** |  | [optional] 
**tilleggskrav** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

