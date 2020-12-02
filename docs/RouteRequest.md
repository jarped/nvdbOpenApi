# RouteRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | Startposisjon som et punkt eller posisjon@veglenkesekvens. | [optional] 
**slutt** | **str** | Sluttposisjon som et punkt eller posisjon@veglenkesekvens. | [optional] 
**geometri** | **str** | Finn sammenhengende vegnett som passer med denne geometrien. Benytter punkt-til-punkt-beregning mellom alle punkter i geometrien. | [optional] 
**maks_avstand** | **int** | Maks avstand i meter til veglenker | [optional] [default to 10]
**omkrets** | **int** | Konvolutt lagt rund start- og slutt-punkt for å beregne rute | [optional] [default to 100]
**konnekteringslenker** | **bool** | Inkludere konnekteringslenker | [optional] [default to False]
**detaljerte_lenker** | **bool** | Inkludere detaljerte lenker | [optional] [default to False]
**kortform** | **bool** | Returner minimal respons | [optional] [default to False]
**vegsystemreferanse** | **str** | Begrens søk innenfor vegreferanse | [optional] 
**trafikantgruppe** | **str** | Begrens søk innenfor trafikantgruppe. Overstyrer behold_trafikantgruppe | [optional] 
**behold_trafikantgruppe** | **bool** | Behold trafikantgruppe gjennom ruten. Trafikantgruppe velges fra første og siste punkt i ruten, om de er ulike velges K (kjørende) | [optional] [default to False]
**typeveg** | **str** | Begrens søk innenfor typeveg | [optional] 
**tidspunkt** | **date** | Søk i vegnett åpent på dette tidspunktet | [optional] 
**tidspunkt_start** | **date** | Begrens vegnettgyldighet til denne startdatoen. Må brukes sammen med &#x60;tidspunkt_slutt&#x60;. | [optional] 
**tidspunkt_slutt** | **date** | Begrens vegnettgyldighet til denne sluttdatoen. Må brukes sammen med &#x60;tidspunkt_start&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

