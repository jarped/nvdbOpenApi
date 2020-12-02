# swagger_client.VegobjekterApi

All URIs are relative to *https://nvdbapiles-v3.atlas.vegvesen.no*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vegobjekt_get**](VegobjekterApi.md#vegobjekt_get) | **GET** /vegobjekt | 
[**vegobjekter_get**](VegobjekterApi.md#vegobjekter_get) | **GET** /vegobjekter | 
[**vegobjekter_statistikk_get**](VegobjekterApi.md#vegobjekter_statistikk_get) | **GET** /vegobjekter/statistikk | 
[**vegobjekter_vegobjekttypeid_get**](VegobjekterApi.md#vegobjekter_vegobjekttypeid_get) | **GET** /vegobjekter/{vegobjekttypeid} | 
[**vegobjekter_vegobjekttypeid_statistikk_get**](VegobjekterApi.md#vegobjekter_vegobjekttypeid_statistikk_get) | **GET** /vegobjekter/{vegobjekttypeid}/statistikk | 
[**vegobjekter_vegobjekttypeid_vegobjektid_get**](VegobjekterApi.md#vegobjekter_vegobjekttypeid_vegobjektid_get) | **GET** /vegobjekter/{vegobjekttypeid}/{vegobjektid} | 
[**vegobjekter_vegobjekttypeid_vegobjektid_versjon_egenskaper_egenskapid_binaerobjektid_binaer_get**](VegobjekterApi.md#vegobjekter_vegobjekttypeid_vegobjektid_versjon_egenskaper_egenskapid_binaerobjektid_binaer_get) | **GET** /vegobjekter/{vegobjekttypeid}/{vegobjektid}/{versjon}/egenskaper/{egenskapid}/{binaerobjektid}/binaer | 
[**vegobjekter_vegobjekttypeid_vegobjektid_versjon_get**](VegobjekterApi.md#vegobjekter_vegobjekttypeid_vegobjektid_versjon_get) | **GET** /vegobjekter/{vegobjekttypeid}/{vegobjektid}/{versjon} | 
[**vegobjekter_vegobjekttypeid_vegobjektid_versjoner_get**](VegobjekterApi.md#vegobjekter_vegobjekttypeid_vegobjektid_versjoner_get) | **GET** /vegobjekter/{vegobjekttypeid}/{vegobjektid}/versjoner | 

# **vegobjekt_get**
> vegobjekt_get(x_client, x_client_session=x_client_session, id=id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegobjekterApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
id = 56 # int | Id for objektet (optional)

try:
    api_instance.vegobjekt_get(x_client, x_client_session=x_client_session, id=id)
except ApiException as e:
    print("Exception when calling VegobjekterApi->vegobjekt_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **id** | **int**| Id for objektet | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegobjekter_get**
> list[VegobjekttypeStatistikk] vegobjekter_get(x_client, x_client_session=x_client_session, statistikk=statistikk, fylke=fylke, kommune=kommune, kontraktsomrade=kontraktsomrade, riksvegrute=riksvegrute, vegsystemreferanse=vegsystemreferanse, veglenkesekvens=veglenkesekvens, kartutnitt=kartutnitt, polygon=polygon, tidspunkt=tidspunkt, overlapp=overlapp)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegobjekterApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
statistikk = true # bool | Om statistikk skal inkluderes. (optional) (default to true)
fylke = [56] # list[int] | Filtrer på fylke. Kommaseparert liste. Se /omrader/fylker for mulige verdier. (optional)
kommune = [56] # list[int] | Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. (optional)
kontraktsomrade = ['kontraktsomrade_example'] # list[str] | Filtrer på kontraktsomrade. Kommaseparert liste. Se /omrader/kontraktsomrader for mulige verdier. (optional)
riksvegrute = ['riksvegrute_example'] # list[str] | Filtrer på riksvegrute. Kommaseparert liste. Se /omrader/riksvegruter for mulige verdier. (optional)
vegsystemreferanse = ['vegsystemreferanse_example'] # list[str] | Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. (optional)
veglenkesekvens = ['veglenkesekvens_example'] # list[str] | Filtrer vegobjekter på stedfesting på vegnettet. Format: `[fra[-til]]@veglenkesekvensid` Kommaseparert liste. (optional)
kartutnitt = 'kartutnitt_example' # str | Filtrer vegobjekter med kartutnitt i det gjeldende geografiske referansesystemet (`srid`-paramteret) (optional)
polygon = 'polygon_example' # str | Filtrer vegobjekter med polygon i det gjeldende geografiske referansesystemet (`srid`-paramteret) (optional)
tidspunkt = '2013-10-20' # date | Begrense spørring til det gitte tidspunktet (optional)
overlapp = 'overlapp_example' # str | Filtrer på objekter som er stedfestet på samme sted i vegnettet. Format: `?overlapp=<objekttypeid>[(egenskap(attributtid)=\"verdi\" eller enumid)] [Eksempler](https://api.vegdata.no/parameter/avansertefilter.html#filtrering-på-objekter-som-er-stedfestet-på-samme-sted-overlapp) (optional)

try:
    api_response = api_instance.vegobjekter_get(x_client, x_client_session=x_client_session, statistikk=statistikk, fylke=fylke, kommune=kommune, kontraktsomrade=kontraktsomrade, riksvegrute=riksvegrute, vegsystemreferanse=vegsystemreferanse, veglenkesekvens=veglenkesekvens, kartutnitt=kartutnitt, polygon=polygon, tidspunkt=tidspunkt, overlapp=overlapp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegobjekterApi->vegobjekter_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **statistikk** | **bool**| Om statistikk skal inkluderes. | [optional] [default to true]
 **fylke** | [**list[int]**](int.md)| Filtrer på fylke. Kommaseparert liste. Se /omrader/fylker for mulige verdier. | [optional] 
 **kommune** | [**list[int]**](int.md)| Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. | [optional] 
 **kontraktsomrade** | [**list[str]**](str.md)| Filtrer på kontraktsomrade. Kommaseparert liste. Se /omrader/kontraktsomrader for mulige verdier. | [optional] 
 **riksvegrute** | [**list[str]**](str.md)| Filtrer på riksvegrute. Kommaseparert liste. Se /omrader/riksvegruter for mulige verdier. | [optional] 
 **vegsystemreferanse** | [**list[str]**](str.md)| Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. | [optional] 
 **veglenkesekvens** | [**list[str]**](str.md)| Filtrer vegobjekter på stedfesting på vegnettet. Format: &#x60;[fra[-til]]@veglenkesekvensid&#x60; Kommaseparert liste. | [optional] 
 **kartutnitt** | **str**| Filtrer vegobjekter med kartutnitt i det gjeldende geografiske referansesystemet (&#x60;srid&#x60;-paramteret) | [optional] 
 **polygon** | **str**| Filtrer vegobjekter med polygon i det gjeldende geografiske referansesystemet (&#x60;srid&#x60;-paramteret) | [optional] 
 **tidspunkt** | **date**| Begrense spørring til det gitte tidspunktet | [optional] 
 **overlapp** | **str**| Filtrer på objekter som er stedfestet på samme sted i vegnettet. Format: &#x60;?overlapp&#x3D;&lt;objekttypeid&gt;[(egenskap(attributtid)&#x3D;\&quot;verdi\&quot; eller enumid)] [Eksempler](https://api.vegdata.no/parameter/avansertefilter.html#filtrering-på-objekter-som-er-stedfestet-på-samme-sted-overlapp) | [optional] 

### Return type

[**list[VegobjekttypeStatistikk]**](VegobjekttypeStatistikk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegobjekter_statistikk_get**
> list[VegobjekttypeStatistikk] vegobjekter_statistikk_get(x_client, x_client_session=x_client_session, fylke=fylke, kommune=kommune, kontraktsomrade=kontraktsomrade, riksvegrute=riksvegrute, vegsystemreferanse=vegsystemreferanse, veglenkesekvens=veglenkesekvens, kartutnitt=kartutnitt, polygon=polygon, tidspunkt=tidspunkt, overlapp=overlapp)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegobjekterApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
fylke = [56] # list[int] | Filtrer på fylke. Kommaseparert liste. Se /omrader/fylker for mulige verdier. (optional)
kommune = [56] # list[int] | Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. (optional)
kontraktsomrade = ['kontraktsomrade_example'] # list[str] | Filtrer på kontraktsomrade. Kommaseparert liste. Se /omrader/kontraktsomrader for mulige verdier. (optional)
riksvegrute = ['riksvegrute_example'] # list[str] | Filtrer på riksvegrute. Kommaseparert liste. Se /omrader/riksvegruter for mulige verdier. (optional)
vegsystemreferanse = ['vegsystemreferanse_example'] # list[str] | Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. (optional)
veglenkesekvens = ['veglenkesekvens_example'] # list[str] | Filtrer vegobjekter på stedfesting på vegnettet. Format: `[fra[-til]]@veglenkesekvensid` Kommaseparert liste. (optional)
kartutnitt = 'kartutnitt_example' # str | Filtrer vegobjekter med kartutnitt i det gjeldende geografiske referansesystemet (`srid`-paramteret) (optional)
polygon = 'polygon_example' # str | Filtrer vegobjekter med polygon i det gjeldende geografiske referansesystemet (`srid`-paramteret) (optional)
tidspunkt = '2013-10-20' # date | Begrense spørring til det gitte tidspunktet (optional)
overlapp = 'overlapp_example' # str | Filtrer på objekter som er stedfestet på samme sted i vegnettet. Format: `?overlapp=<objekttypeid>[(egenskap(attributtid)=\"verdi\" eller enumid)] [Eksempler](https://api.vegdata.no/parameter/avansertefilter.html#filtrering-på-objekter-som-er-stedfestet-på-samme-sted-overlapp) (optional)

try:
    api_response = api_instance.vegobjekter_statistikk_get(x_client, x_client_session=x_client_session, fylke=fylke, kommune=kommune, kontraktsomrade=kontraktsomrade, riksvegrute=riksvegrute, vegsystemreferanse=vegsystemreferanse, veglenkesekvens=veglenkesekvens, kartutnitt=kartutnitt, polygon=polygon, tidspunkt=tidspunkt, overlapp=overlapp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegobjekterApi->vegobjekter_statistikk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **fylke** | [**list[int]**](int.md)| Filtrer på fylke. Kommaseparert liste. Se /omrader/fylker for mulige verdier. | [optional] 
 **kommune** | [**list[int]**](int.md)| Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. | [optional] 
 **kontraktsomrade** | [**list[str]**](str.md)| Filtrer på kontraktsomrade. Kommaseparert liste. Se /omrader/kontraktsomrader for mulige verdier. | [optional] 
 **riksvegrute** | [**list[str]**](str.md)| Filtrer på riksvegrute. Kommaseparert liste. Se /omrader/riksvegruter for mulige verdier. | [optional] 
 **vegsystemreferanse** | [**list[str]**](str.md)| Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. | [optional] 
 **veglenkesekvens** | [**list[str]**](str.md)| Filtrer vegobjekter på stedfesting på vegnettet. Format: &#x60;[fra[-til]]@veglenkesekvensid&#x60; Kommaseparert liste. | [optional] 
 **kartutnitt** | **str**| Filtrer vegobjekter med kartutnitt i det gjeldende geografiske referansesystemet (&#x60;srid&#x60;-paramteret) | [optional] 
 **polygon** | **str**| Filtrer vegobjekter med polygon i det gjeldende geografiske referansesystemet (&#x60;srid&#x60;-paramteret) | [optional] 
 **tidspunkt** | **date**| Begrense spørring til det gitte tidspunktet | [optional] 
 **overlapp** | **str**| Filtrer på objekter som er stedfestet på samme sted i vegnettet. Format: &#x60;?overlapp&#x3D;&lt;objekttypeid&gt;[(egenskap(attributtid)&#x3D;\&quot;verdi\&quot; eller enumid)] [Eksempler](https://api.vegdata.no/parameter/avansertefilter.html#filtrering-på-objekter-som-er-stedfestet-på-samme-sted-overlapp) | [optional] 

### Return type

[**list[VegobjekttypeStatistikk]**](VegobjekttypeStatistikk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegobjekter_vegobjekttypeid_get**
> VegobjektListeRespons vegobjekter_vegobjekttypeid_get(x_client, vegobjekttypeid, x_client_session=x_client_session, inkluder=inkluder, srid=srid, geometritoleranse=geometritoleranse, inkludergeometri=inkludergeometri, inkluder_egenskaper=inkluder_egenskaper, segmentering=segmentering, fylke=fylke, kommune=kommune, kontraktsomrade=kontraktsomrade, riksvegrute=riksvegrute, vegsystemreferanse=vegsystemreferanse, veglenkesekvens=veglenkesekvens, kartutnitt=kartutnitt, polygon=polygon, tidspunkt=tidspunkt, overlapp=overlapp, arm=arm, veglenketype=veglenketype, adskiltelop=adskiltelop, typeveg=typeveg, detaljniva=detaljniva, kryssystem=kryssystem, sideanlegg=sideanlegg, trafikantgruppe=trafikantgruppe, antall=antall, start=start, egenskap=egenskap, dybde=dybde, ider=ider, alle_versjoner=alle_versjoner, endret_etter=endret_etter)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegobjekterApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
vegobjekttypeid = 56 # int | Id for vegobjekttype som skal hentes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
inkluder = ['inkluder_example'] # list[str] | kommaseparert liste over hvilke informasjonselementer som skal returneres i tillegg til vegobjektenes id. (optional)
srid = '6173' # str | Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) (optional) (default to 6173)
geometritoleranse = 56 # int | Angir om det skal returneres en forenklet geometri. Dersom parameteren utelates, returneres full geometri for vegobjektene. Nummeret angir distansetoleranse for generering av forenklet geometri. (optional)
inkludergeometri = 'inkludergeometri_example' # str | Et vegobjekt har opptil to geometrier, egengeometri og stedfestet geometri. Egengeoemtrien er plassert under `vegobjekt.egenskaper` om den finnes, stedfestet geometri er plassert under `vegobjekt.lokasjon`. I tillegg til de nevnte feltene på vegobjekt-responsen returneres også `vegobjekt.geometri` (dersom man har inkluder=geometri eller alle), slik at man alltid finner geometrien for vegobjektet ett sted. Dette feltet er egengeometri dersom objektet har det, hvis ikke har feltet stedfestet geometri Ved hvilken av disse som er tilfelle finner man ut ved å se på `vegobjekt.geometri.egengeometri` (optional)
inkluder_egenskaper = 'inkluder_egenskaper_example' # str | Gir mulighet til å filtrere hvilke egenskaper som skal returneres med `inkluder=egenskaper`. `basis` er alle egenskaper som ikke er assosiasjoner, stedfesting, geometri, eller lister av disse. (optional)
segmentering = true # bool | Angir om strekningsobjekter skal segmenteres etter søkeområdet (fylke, kommune, vegsystemreferanse, kontraksområde, riksvegrute, veglenkesekvens). (optional) (default to true)
fylke = [56] # list[int] | Filtrer på fylke. Kommaseparert liste. Se /omrader/fylker for mulige verdier. (optional)
kommune = [56] # list[int] | Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. (optional)
kontraktsomrade = ['kontraktsomrade_example'] # list[str] | Filtrer på kontraktsomrade. Kommaseparert liste. Se /omrader/kontraktsomrader for mulige verdier. (optional)
riksvegrute = ['riksvegrute_example'] # list[str] | Filtrer på riksvegrute. Kommaseparert liste. Se /omrader/riksvegruter for mulige verdier. (optional)
vegsystemreferanse = ['vegsystemreferanse_example'] # list[str] | Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. (optional)
veglenkesekvens = ['veglenkesekvens_example'] # list[str] | Filtrer vegobjekter på stedfesting på vegnettet. Format: `[fra[-til]]@veglenkesekvensid` Kommaseparert liste. (optional)
kartutnitt = 'kartutnitt_example' # str | Filtrer vegobjekter med kartutnitt i det gjeldende geografiske referansesystemet (`srid`-paramteret) (optional)
polygon = 'polygon_example' # str | Filtrer vegobjekter med polygon i det gjeldende geografiske referansesystemet (`srid`-paramteret) (optional)
tidspunkt = '2013-10-20' # date | Begrense spørring til det gitte tidspunktet (optional)
overlapp = 'overlapp_example' # str | Filtrer på objekter som er stedfestet på samme sted i vegnettet. Format: `?overlapp=<objekttypeid>[(egenskap(attributtid)=\"verdi\" eller enumid)] [Eksempler](https://api.vegdata.no/parameter/avansertefilter.html#filtrering-på-objekter-som-er-stedfestet-på-samme-sted-overlapp) (optional)
arm = true # bool | Filtrer vegobjekter på om de er stedfestet på Strekning med verdi satt for «arm» (optional)
veglenketype = ['veglenketype_example'] # list[str] | Filtrer vegobjekter på veglenketype på vegnettet objektet er stedfestet. Kommaseparert liste. (optional)
adskiltelop = 'adskiltelop_example' # str | Filtrer vegobjekter på om de er stedfestet hvor det er Strekning med verdi satt for «adskilte løp» (optional)
typeveg = ['typeveg_example'] # list[str] | Filtrer vegobjekter på type veg på vegnettet objektet er stedfestet på. Kommaseparert liste. (optional)
detaljniva = 'detaljniva_example' # str | Filtrer vegobjekter på detaljnivå på vegnettet objektet er stedfestet på (kortnavn fra datakatalogen). (optional)
kryssystem = true # bool | Filtrer vegobjekter på om de er stedfestet samme hvor det er et Kryssystem (optional)
sideanlegg = true # bool | Filtrer vegobjekter på om de er stedfestet samme hvor det er et Sideanlegg (optional)
trafikantgruppe = 'trafikantgruppe_example' # str | Filtrer vegobjekter på trafikantgruppe (optional)
antall = 56 # int | Angir hvor mange objekter som skal returneres. Øvre grense er avhengig av størrelse på respons, og vil kunne variere fra endepunkt til endepunkt. Dersom det angis en verdi for antall som overskrider maksimum, vil maksimumsverdi benyttes. Se også `sidestørrelse` i responsens `metadata`-objekt. (optional)
start = 'start_example' # str | Angir markør for neste side objekter som skal returneres. Denne får man i metadata-feltet i responsen. (optional)
egenskap = 'egenskap_example' # str | Filtrer vegobjekter på egenskapene de har Egenskapsfilter består av egenskapstypeid, operator og verdi, `?egenskap=\"<egenskapstype><operator><verdi>\"`           Det er støtte for følgende operatorer: * `=` - lik * `!=` - ulik * `<` - større enn * `>` - mindre enn, * `>=` - større enn, eller lik * `<=` - mindre enn, eller lik  Større enn- og mindre enn-operatorene er kun relevant for egenskapstyper av type tall eller dato. Verdien skal være i henhold til egenskapstypens datatype, og er som oftest en tekst eller et tall. Tekst og tidspunkt må markeres med enkle anførselstegn. For egenskapstyper med forhåndsdefinerte verdier, er det for øyeblikket kun mulig å bruke verdiens id. Bruk null som verdi for å finne objekter som har, eller ikke har, verdi på bestemte egenskapstyper. Syntaksen for spørrespråket støtter bruk av paranteser og AND/OR-sammenhenger. Wildcard * kan benyttes for tekst og datoer. Merk! Egenskapstyper med datatype struktur er ikke søkbare. Du vil få 0 treff for ÅDT-fordeling (606069).  *Filtrering på relasjoner*: Filtrering på egenskaper i relaterte objekter gjøres også i egenskapsfilteret. Objekter er relatert ved at de har relasjoner til andre objekter. Foreløpig støtter API-et kun filtrering på datter-objekter. Relaterte objekter filtreres ved bruk av funksjonen relasjon. Denne funksjonen tar en objekttype ID som første parameter, og et nytt egenskapsfilter som andre parameter. Eksempel: `?egenskap=\"relasjon(67, egenskap(1317)>2000\"` (Tunneler (581) som har Tunnelløp (67) med Lengde (1317) over 2 km) (optional)
dybde = '1' # str | Hvor mange nivå datterobjekter som skal inkluderes (optional) (default to 1)
ider = [56] # list[int] | Hent objekter med de oppgitte idene. Kommaseparert. (optional)
alle_versjoner = true # bool | Returner alle versjoner som matcher de oppgitte parametrene. Dersom ikke fraværende eller `false` vil kun objekter uten tildato returneres. (optional)
endret_etter = '2013-10-20T19:20:30+01:00' # datetime | hent alle objekter som er endret etter det gitte tidspunkt. (optional)

try:
    api_response = api_instance.vegobjekter_vegobjekttypeid_get(x_client, vegobjekttypeid, x_client_session=x_client_session, inkluder=inkluder, srid=srid, geometritoleranse=geometritoleranse, inkludergeometri=inkludergeometri, inkluder_egenskaper=inkluder_egenskaper, segmentering=segmentering, fylke=fylke, kommune=kommune, kontraktsomrade=kontraktsomrade, riksvegrute=riksvegrute, vegsystemreferanse=vegsystemreferanse, veglenkesekvens=veglenkesekvens, kartutnitt=kartutnitt, polygon=polygon, tidspunkt=tidspunkt, overlapp=overlapp, arm=arm, veglenketype=veglenketype, adskiltelop=adskiltelop, typeveg=typeveg, detaljniva=detaljniva, kryssystem=kryssystem, sideanlegg=sideanlegg, trafikantgruppe=trafikantgruppe, antall=antall, start=start, egenskap=egenskap, dybde=dybde, ider=ider, alle_versjoner=alle_versjoner, endret_etter=endret_etter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegobjekterApi->vegobjekter_vegobjekttypeid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **vegobjekttypeid** | **int**| Id for vegobjekttype som skal hentes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **inkluder** | [**list[str]**](str.md)| kommaseparert liste over hvilke informasjonselementer som skal returneres i tillegg til vegobjektenes id. | [optional] 
 **srid** | **str**| Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) | [optional] [default to 6173]
 **geometritoleranse** | **int**| Angir om det skal returneres en forenklet geometri. Dersom parameteren utelates, returneres full geometri for vegobjektene. Nummeret angir distansetoleranse for generering av forenklet geometri. | [optional] 
 **inkludergeometri** | **str**| Et vegobjekt har opptil to geometrier, egengeometri og stedfestet geometri. Egengeoemtrien er plassert under &#x60;vegobjekt.egenskaper&#x60; om den finnes, stedfestet geometri er plassert under &#x60;vegobjekt.lokasjon&#x60;. I tillegg til de nevnte feltene på vegobjekt-responsen returneres også &#x60;vegobjekt.geometri&#x60; (dersom man har inkluder&#x3D;geometri eller alle), slik at man alltid finner geometrien for vegobjektet ett sted. Dette feltet er egengeometri dersom objektet har det, hvis ikke har feltet stedfestet geometri Ved hvilken av disse som er tilfelle finner man ut ved å se på &#x60;vegobjekt.geometri.egengeometri&#x60; | [optional] 
 **inkluder_egenskaper** | **str**| Gir mulighet til å filtrere hvilke egenskaper som skal returneres med &#x60;inkluder&#x3D;egenskaper&#x60;. &#x60;basis&#x60; er alle egenskaper som ikke er assosiasjoner, stedfesting, geometri, eller lister av disse. | [optional] 
 **segmentering** | **bool**| Angir om strekningsobjekter skal segmenteres etter søkeområdet (fylke, kommune, vegsystemreferanse, kontraksområde, riksvegrute, veglenkesekvens). | [optional] [default to true]
 **fylke** | [**list[int]**](int.md)| Filtrer på fylke. Kommaseparert liste. Se /omrader/fylker for mulige verdier. | [optional] 
 **kommune** | [**list[int]**](int.md)| Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. | [optional] 
 **kontraktsomrade** | [**list[str]**](str.md)| Filtrer på kontraktsomrade. Kommaseparert liste. Se /omrader/kontraktsomrader for mulige verdier. | [optional] 
 **riksvegrute** | [**list[str]**](str.md)| Filtrer på riksvegrute. Kommaseparert liste. Se /omrader/riksvegruter for mulige verdier. | [optional] 
 **vegsystemreferanse** | [**list[str]**](str.md)| Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. | [optional] 
 **veglenkesekvens** | [**list[str]**](str.md)| Filtrer vegobjekter på stedfesting på vegnettet. Format: &#x60;[fra[-til]]@veglenkesekvensid&#x60; Kommaseparert liste. | [optional] 
 **kartutnitt** | **str**| Filtrer vegobjekter med kartutnitt i det gjeldende geografiske referansesystemet (&#x60;srid&#x60;-paramteret) | [optional] 
 **polygon** | **str**| Filtrer vegobjekter med polygon i det gjeldende geografiske referansesystemet (&#x60;srid&#x60;-paramteret) | [optional] 
 **tidspunkt** | **date**| Begrense spørring til det gitte tidspunktet | [optional] 
 **overlapp** | **str**| Filtrer på objekter som er stedfestet på samme sted i vegnettet. Format: &#x60;?overlapp&#x3D;&lt;objekttypeid&gt;[(egenskap(attributtid)&#x3D;\&quot;verdi\&quot; eller enumid)] [Eksempler](https://api.vegdata.no/parameter/avansertefilter.html#filtrering-på-objekter-som-er-stedfestet-på-samme-sted-overlapp) | [optional] 
 **arm** | **bool**| Filtrer vegobjekter på om de er stedfestet på Strekning med verdi satt for «arm» | [optional] 
 **veglenketype** | [**list[str]**](str.md)| Filtrer vegobjekter på veglenketype på vegnettet objektet er stedfestet. Kommaseparert liste. | [optional] 
 **adskiltelop** | **str**| Filtrer vegobjekter på om de er stedfestet hvor det er Strekning med verdi satt for «adskilte løp» | [optional] 
 **typeveg** | [**list[str]**](str.md)| Filtrer vegobjekter på type veg på vegnettet objektet er stedfestet på. Kommaseparert liste. | [optional] 
 **detaljniva** | **str**| Filtrer vegobjekter på detaljnivå på vegnettet objektet er stedfestet på (kortnavn fra datakatalogen). | [optional] 
 **kryssystem** | **bool**| Filtrer vegobjekter på om de er stedfestet samme hvor det er et Kryssystem | [optional] 
 **sideanlegg** | **bool**| Filtrer vegobjekter på om de er stedfestet samme hvor det er et Sideanlegg | [optional] 
 **trafikantgruppe** | **str**| Filtrer vegobjekter på trafikantgruppe | [optional] 
 **antall** | **int**| Angir hvor mange objekter som skal returneres. Øvre grense er avhengig av størrelse på respons, og vil kunne variere fra endepunkt til endepunkt. Dersom det angis en verdi for antall som overskrider maksimum, vil maksimumsverdi benyttes. Se også &#x60;sidestørrelse&#x60; i responsens &#x60;metadata&#x60;-objekt. | [optional] 
 **start** | **str**| Angir markør for neste side objekter som skal returneres. Denne får man i metadata-feltet i responsen. | [optional] 
 **egenskap** | **str**| Filtrer vegobjekter på egenskapene de har Egenskapsfilter består av egenskapstypeid, operator og verdi, &#x60;?egenskap&#x3D;\&quot;&lt;egenskapstype&gt;&lt;operator&gt;&lt;verdi&gt;\&quot;&#x60;           Det er støtte for følgende operatorer: * &#x60;&#x3D;&#x60; - lik * &#x60;!&#x3D;&#x60; - ulik * &#x60;&lt;&#x60; - større enn * &#x60;&gt;&#x60; - mindre enn, * &#x60;&gt;&#x3D;&#x60; - større enn, eller lik * &#x60;&lt;&#x3D;&#x60; - mindre enn, eller lik  Større enn- og mindre enn-operatorene er kun relevant for egenskapstyper av type tall eller dato. Verdien skal være i henhold til egenskapstypens datatype, og er som oftest en tekst eller et tall. Tekst og tidspunkt må markeres med enkle anførselstegn. For egenskapstyper med forhåndsdefinerte verdier, er det for øyeblikket kun mulig å bruke verdiens id. Bruk null som verdi for å finne objekter som har, eller ikke har, verdi på bestemte egenskapstyper. Syntaksen for spørrespråket støtter bruk av paranteser og AND/OR-sammenhenger. Wildcard * kan benyttes for tekst og datoer. Merk! Egenskapstyper med datatype struktur er ikke søkbare. Du vil få 0 treff for ÅDT-fordeling (606069).  *Filtrering på relasjoner*: Filtrering på egenskaper i relaterte objekter gjøres også i egenskapsfilteret. Objekter er relatert ved at de har relasjoner til andre objekter. Foreløpig støtter API-et kun filtrering på datter-objekter. Relaterte objekter filtreres ved bruk av funksjonen relasjon. Denne funksjonen tar en objekttype ID som første parameter, og et nytt egenskapsfilter som andre parameter. Eksempel: &#x60;?egenskap&#x3D;\&quot;relasjon(67, egenskap(1317)&gt;2000\&quot;&#x60; (Tunneler (581) som har Tunnelløp (67) med Lengde (1317) over 2 km) | [optional] 
 **dybde** | **str**| Hvor mange nivå datterobjekter som skal inkluderes | [optional] [default to 1]
 **ider** | [**list[int]**](int.md)| Hent objekter med de oppgitte idene. Kommaseparert. | [optional] 
 **alle_versjoner** | **bool**| Returner alle versjoner som matcher de oppgitte parametrene. Dersom ikke fraværende eller &#x60;false&#x60; vil kun objekter uten tildato returneres. | [optional] 
 **endret_etter** | **datetime**| hent alle objekter som er endret etter det gitte tidspunkt. | [optional] 

### Return type

[**VegobjektListeRespons**](VegobjektListeRespons.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegobjekter_vegobjekttypeid_statistikk_get**
> Statistikk vegobjekter_vegobjekttypeid_statistikk_get(x_client, vegobjekttypeid, x_client_session=x_client_session, srid=srid, segmentering=segmentering, fylke=fylke, kommune=kommune, kontraktsomrade=kontraktsomrade, riksvegrute=riksvegrute, vegsystemreferanse=vegsystemreferanse, veglenkesekvens=veglenkesekvens, kartutnitt=kartutnitt, polygon=polygon, tidspunkt=tidspunkt, overlapp=overlapp, arm=arm, veglenketype=veglenketype, adskiltelop=adskiltelop, typeveg=typeveg, detaljniva=detaljniva, kryssystem=kryssystem, sideanlegg=sideanlegg, trafikantgruppe=trafikantgruppe, egenskap=egenskap, alle_versjoner=alle_versjoner, endret_etter=endret_etter)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegobjekterApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
vegobjekttypeid = 56 # int | Id for vegobjekttype som skal hentes statistikk for.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
srid = '6173' # str | Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) (optional) (default to 6173)
segmentering = true # bool | Angir om strekningsobjekter skal segmenteres etter søkeområdet (fylke, kommune, vegsystemreferanse, kontraksområde, riksvegrute, veglenkesekvens). (optional) (default to true)
fylke = [56] # list[int] | Filtrer på fylke. Kommaseparert liste. Se /omrader/fylker for mulige verdier. (optional)
kommune = [56] # list[int] | Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. (optional)
kontraktsomrade = ['kontraktsomrade_example'] # list[str] | Filtrer på kontraktsomrade. Kommaseparert liste. Se /omrader/kontraktsomrader for mulige verdier. (optional)
riksvegrute = ['riksvegrute_example'] # list[str] | Filtrer på riksvegrute. Kommaseparert liste. Se /omrader/riksvegruter for mulige verdier. (optional)
vegsystemreferanse = ['vegsystemreferanse_example'] # list[str] | Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. (optional)
veglenkesekvens = ['veglenkesekvens_example'] # list[str] | Filtrer vegobjekter på stedfesting på vegnettet. Format: `[fra[-til]]@veglenkesekvensid` Kommaseparert liste. (optional)
kartutnitt = 'kartutnitt_example' # str | Filtrer vegobjekter med kartutnitt i det gjeldende geografiske referansesystemet (`srid`-paramteret) (optional)
polygon = 'polygon_example' # str | Filtrer vegobjekter med polygon i det gjeldende geografiske referansesystemet (`srid`-paramteret) (optional)
tidspunkt = '2013-10-20' # date | Begrense spørring til det gitte tidspunktet (optional)
overlapp = 'overlapp_example' # str | Filtrer på objekter som er stedfestet på samme sted i vegnettet. Format: `?overlapp=<objekttypeid>[(egenskap(attributtid)=\"verdi\" eller enumid)] [Eksempler](https://api.vegdata.no/parameter/avansertefilter.html#filtrering-på-objekter-som-er-stedfestet-på-samme-sted-overlapp) (optional)
arm = true # bool | Filtrer vegobjekter på om de er stedfestet på Strekning med verdi satt for «arm» (optional)
veglenketype = ['veglenketype_example'] # list[str] | Filtrer vegobjekter på veglenketype på vegnettet objektet er stedfestet. Kommaseparert liste. (optional)
adskiltelop = 'adskiltelop_example' # str | Filtrer vegobjekter på om de er stedfestet hvor det er Strekning med verdi satt for «adskilte løp» (optional)
typeveg = ['typeveg_example'] # list[str] | Filtrer vegobjekter på type veg på vegnettet objektet er stedfestet på. Kommaseparert liste. (optional)
detaljniva = 'detaljniva_example' # str | Filtrer vegobjekter på detaljnivå på vegnettet objektet er stedfestet på (kortnavn fra datakatalogen). (optional)
kryssystem = true # bool | Filtrer vegobjekter på om de er stedfestet samme hvor det er et Kryssystem (optional)
sideanlegg = true # bool | Filtrer vegobjekter på om de er stedfestet samme hvor det er et Sideanlegg (optional)
trafikantgruppe = 'trafikantgruppe_example' # str | Filtrer vegobjekter på trafikantgruppe (optional)
egenskap = 'egenskap_example' # str | Filtrer vegobjekter på egenskapene de har Egenskapsfilter består av egenskapstypeid, operator og verdi, `?egenskap=\"<egenskapstype><operator><verdi>\"`           Det er støtte for følgende operatorer: * `=` - lik * `!=` - ulik * `<` - større enn * `>` - mindre enn, * `>=` - større enn, eller lik * `<=` - mindre enn, eller lik  Større enn- og mindre enn-operatorene er kun relevant for egenskapstyper av type tall eller dato. Verdien skal være i henhold til egenskapstypens datatype, og er som oftest en tekst eller et tall. Tekst og tidspunkt må markeres med enkle anførselstegn. For egenskapstyper med forhåndsdefinerte verdier, er det for øyeblikket kun mulig å bruke verdiens id. Bruk null som verdi for å finne objekter som har, eller ikke har, verdi på bestemte egenskapstyper. Syntaksen for spørrespråket støtter bruk av paranteser og AND/OR-sammenhenger. Wildcard * kan benyttes for tekst og datoer. Merk! Egenskapstyper med datatype struktur er ikke søkbare. Du vil få 0 treff for ÅDT-fordeling (606069).  *Filtrering på relasjoner*: Filtrering på egenskaper i relaterte objekter gjøres også i egenskapsfilteret. Objekter er relatert ved at de har relasjoner til andre objekter. Foreløpig støtter API-et kun filtrering på datter-objekter. Relaterte objekter filtreres ved bruk av funksjonen relasjon. Denne funksjonen tar en objekttype ID som første parameter, og et nytt egenskapsfilter som andre parameter. Eksempel: `?egenskap=\"relasjon(67, egenskap(1317)>2000\"` (Tunneler (581) som har Tunnelløp (67) med Lengde (1317) over 2 km) (optional)
alle_versjoner = true # bool | Returner alle versjoner som matcher de oppgitte parametrene. Dersom ikke fraværende eller `false` vil kun objekter uten tildato returneres. (optional)
endret_etter = '2013-10-20T19:20:30+01:00' # datetime | hent alle objekter som er endret etter det gitte tidspunkt. (optional)

try:
    api_response = api_instance.vegobjekter_vegobjekttypeid_statistikk_get(x_client, vegobjekttypeid, x_client_session=x_client_session, srid=srid, segmentering=segmentering, fylke=fylke, kommune=kommune, kontraktsomrade=kontraktsomrade, riksvegrute=riksvegrute, vegsystemreferanse=vegsystemreferanse, veglenkesekvens=veglenkesekvens, kartutnitt=kartutnitt, polygon=polygon, tidspunkt=tidspunkt, overlapp=overlapp, arm=arm, veglenketype=veglenketype, adskiltelop=adskiltelop, typeveg=typeveg, detaljniva=detaljniva, kryssystem=kryssystem, sideanlegg=sideanlegg, trafikantgruppe=trafikantgruppe, egenskap=egenskap, alle_versjoner=alle_versjoner, endret_etter=endret_etter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegobjekterApi->vegobjekter_vegobjekttypeid_statistikk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **vegobjekttypeid** | **int**| Id for vegobjekttype som skal hentes statistikk for. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **srid** | **str**| Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) | [optional] [default to 6173]
 **segmentering** | **bool**| Angir om strekningsobjekter skal segmenteres etter søkeområdet (fylke, kommune, vegsystemreferanse, kontraksområde, riksvegrute, veglenkesekvens). | [optional] [default to true]
 **fylke** | [**list[int]**](int.md)| Filtrer på fylke. Kommaseparert liste. Se /omrader/fylker for mulige verdier. | [optional] 
 **kommune** | [**list[int]**](int.md)| Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. | [optional] 
 **kontraktsomrade** | [**list[str]**](str.md)| Filtrer på kontraktsomrade. Kommaseparert liste. Se /omrader/kontraktsomrader for mulige verdier. | [optional] 
 **riksvegrute** | [**list[str]**](str.md)| Filtrer på riksvegrute. Kommaseparert liste. Se /omrader/riksvegruter for mulige verdier. | [optional] 
 **vegsystemreferanse** | [**list[str]**](str.md)| Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. | [optional] 
 **veglenkesekvens** | [**list[str]**](str.md)| Filtrer vegobjekter på stedfesting på vegnettet. Format: &#x60;[fra[-til]]@veglenkesekvensid&#x60; Kommaseparert liste. | [optional] 
 **kartutnitt** | **str**| Filtrer vegobjekter med kartutnitt i det gjeldende geografiske referansesystemet (&#x60;srid&#x60;-paramteret) | [optional] 
 **polygon** | **str**| Filtrer vegobjekter med polygon i det gjeldende geografiske referansesystemet (&#x60;srid&#x60;-paramteret) | [optional] 
 **tidspunkt** | **date**| Begrense spørring til det gitte tidspunktet | [optional] 
 **overlapp** | **str**| Filtrer på objekter som er stedfestet på samme sted i vegnettet. Format: &#x60;?overlapp&#x3D;&lt;objekttypeid&gt;[(egenskap(attributtid)&#x3D;\&quot;verdi\&quot; eller enumid)] [Eksempler](https://api.vegdata.no/parameter/avansertefilter.html#filtrering-på-objekter-som-er-stedfestet-på-samme-sted-overlapp) | [optional] 
 **arm** | **bool**| Filtrer vegobjekter på om de er stedfestet på Strekning med verdi satt for «arm» | [optional] 
 **veglenketype** | [**list[str]**](str.md)| Filtrer vegobjekter på veglenketype på vegnettet objektet er stedfestet. Kommaseparert liste. | [optional] 
 **adskiltelop** | **str**| Filtrer vegobjekter på om de er stedfestet hvor det er Strekning med verdi satt for «adskilte løp» | [optional] 
 **typeveg** | [**list[str]**](str.md)| Filtrer vegobjekter på type veg på vegnettet objektet er stedfestet på. Kommaseparert liste. | [optional] 
 **detaljniva** | **str**| Filtrer vegobjekter på detaljnivå på vegnettet objektet er stedfestet på (kortnavn fra datakatalogen). | [optional] 
 **kryssystem** | **bool**| Filtrer vegobjekter på om de er stedfestet samme hvor det er et Kryssystem | [optional] 
 **sideanlegg** | **bool**| Filtrer vegobjekter på om de er stedfestet samme hvor det er et Sideanlegg | [optional] 
 **trafikantgruppe** | **str**| Filtrer vegobjekter på trafikantgruppe | [optional] 
 **egenskap** | **str**| Filtrer vegobjekter på egenskapene de har Egenskapsfilter består av egenskapstypeid, operator og verdi, &#x60;?egenskap&#x3D;\&quot;&lt;egenskapstype&gt;&lt;operator&gt;&lt;verdi&gt;\&quot;&#x60;           Det er støtte for følgende operatorer: * &#x60;&#x3D;&#x60; - lik * &#x60;!&#x3D;&#x60; - ulik * &#x60;&lt;&#x60; - større enn * &#x60;&gt;&#x60; - mindre enn, * &#x60;&gt;&#x3D;&#x60; - større enn, eller lik * &#x60;&lt;&#x3D;&#x60; - mindre enn, eller lik  Større enn- og mindre enn-operatorene er kun relevant for egenskapstyper av type tall eller dato. Verdien skal være i henhold til egenskapstypens datatype, og er som oftest en tekst eller et tall. Tekst og tidspunkt må markeres med enkle anførselstegn. For egenskapstyper med forhåndsdefinerte verdier, er det for øyeblikket kun mulig å bruke verdiens id. Bruk null som verdi for å finne objekter som har, eller ikke har, verdi på bestemte egenskapstyper. Syntaksen for spørrespråket støtter bruk av paranteser og AND/OR-sammenhenger. Wildcard * kan benyttes for tekst og datoer. Merk! Egenskapstyper med datatype struktur er ikke søkbare. Du vil få 0 treff for ÅDT-fordeling (606069).  *Filtrering på relasjoner*: Filtrering på egenskaper i relaterte objekter gjøres også i egenskapsfilteret. Objekter er relatert ved at de har relasjoner til andre objekter. Foreløpig støtter API-et kun filtrering på datter-objekter. Relaterte objekter filtreres ved bruk av funksjonen relasjon. Denne funksjonen tar en objekttype ID som første parameter, og et nytt egenskapsfilter som andre parameter. Eksempel: &#x60;?egenskap&#x3D;\&quot;relasjon(67, egenskap(1317)&gt;2000\&quot;&#x60; (Tunneler (581) som har Tunnelløp (67) med Lengde (1317) over 2 km) | [optional] 
 **alle_versjoner** | **bool**| Returner alle versjoner som matcher de oppgitte parametrene. Dersom ikke fraværende eller &#x60;false&#x60; vil kun objekter uten tildato returneres. | [optional] 
 **endret_etter** | **datetime**| hent alle objekter som er endret etter det gitte tidspunkt. | [optional] 

### Return type

[**Statistikk**](Statistikk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegobjekter_vegobjekttypeid_vegobjektid_get**
> vegobjekter_vegobjekttypeid_vegobjektid_get(x_client, vegobjekttypeid, vegobjektid, x_client_session=x_client_session, srid=srid, inkluder=inkluder, inkludergeometri=inkludergeometri, inkluder_egenskaper=inkluder_egenskaper, geometritoleranse=geometritoleranse, dybde=dybde)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegobjekterApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
vegobjekttypeid = 56 # int | Id for objektets vegobjekttype
vegobjektid = 789 # int | Id for objektet
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
srid = '6173' # str | Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) (optional) (default to 6173)
inkluder = ['inkluder_example'] # list[str] | kommaseparert liste over hvilke informasjonselementer som skal returneres i tillegg til vegobjektenes id. (optional)
inkludergeometri = 'inkludergeometri_example' # str | Et vegobjekt har opptil to geometrier, egengeometri og stedfestet geometri. Egengeoemtrien er plassert under `vegobjekt.egenskaper` om den finnes, stedfestet geometri er plassert under `vegobjekt.lokasjon`. I tillegg til de nevnte feltene på vegobjekt-responsen returneres også `vegobjekt.geometri` (dersom man har inkluder=geometri eller alle), slik at man alltid finner geometrien for vegobjektet ett sted. Dette feltet er egengeometri dersom objektet har det, hvis ikke har feltet stedfestet geometri Ved hvilken av disse som er tilfelle finner man ut ved å se på `vegobjekt.geometri.egengeometri` (optional)
inkluder_egenskaper = 'inkluder_egenskaper_example' # str | Gir mulighet til å filtrere hvilke egenskaper som skal returneres med `inkluder=egenskaper`. `basis` er alle egenskaper som ikke er assosiasjoner, stedfesting, geometri, eller lister av disse. (optional)
geometritoleranse = 56 # int | Angir om det skal returneres en forenklet geometri. Dersom parameteren utelates, returneres full geometri for vegobjektene. Nummeret angir distansetoleranse for generering av forenklet geometri. (optional)
dybde = '1' # str | Hvor mange nivå datterobjekter som skal inkluderes (optional) (default to 1)

try:
    api_instance.vegobjekter_vegobjekttypeid_vegobjektid_get(x_client, vegobjekttypeid, vegobjektid, x_client_session=x_client_session, srid=srid, inkluder=inkluder, inkludergeometri=inkludergeometri, inkluder_egenskaper=inkluder_egenskaper, geometritoleranse=geometritoleranse, dybde=dybde)
except ApiException as e:
    print("Exception when calling VegobjekterApi->vegobjekter_vegobjekttypeid_vegobjektid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **vegobjekttypeid** | **int**| Id for objektets vegobjekttype | 
 **vegobjektid** | **int**| Id for objektet | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **srid** | **str**| Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) | [optional] [default to 6173]
 **inkluder** | [**list[str]**](str.md)| kommaseparert liste over hvilke informasjonselementer som skal returneres i tillegg til vegobjektenes id. | [optional] 
 **inkludergeometri** | **str**| Et vegobjekt har opptil to geometrier, egengeometri og stedfestet geometri. Egengeoemtrien er plassert under &#x60;vegobjekt.egenskaper&#x60; om den finnes, stedfestet geometri er plassert under &#x60;vegobjekt.lokasjon&#x60;. I tillegg til de nevnte feltene på vegobjekt-responsen returneres også &#x60;vegobjekt.geometri&#x60; (dersom man har inkluder&#x3D;geometri eller alle), slik at man alltid finner geometrien for vegobjektet ett sted. Dette feltet er egengeometri dersom objektet har det, hvis ikke har feltet stedfestet geometri Ved hvilken av disse som er tilfelle finner man ut ved å se på &#x60;vegobjekt.geometri.egengeometri&#x60; | [optional] 
 **inkluder_egenskaper** | **str**| Gir mulighet til å filtrere hvilke egenskaper som skal returneres med &#x60;inkluder&#x3D;egenskaper&#x60;. &#x60;basis&#x60; er alle egenskaper som ikke er assosiasjoner, stedfesting, geometri, eller lister av disse. | [optional] 
 **geometritoleranse** | **int**| Angir om det skal returneres en forenklet geometri. Dersom parameteren utelates, returneres full geometri for vegobjektene. Nummeret angir distansetoleranse for generering av forenklet geometri. | [optional] 
 **dybde** | **str**| Hvor mange nivå datterobjekter som skal inkluderes | [optional] [default to 1]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegobjekter_vegobjekttypeid_vegobjektid_versjon_egenskaper_egenskapid_binaerobjektid_binaer_get**
> str vegobjekter_vegobjekttypeid_vegobjektid_versjon_egenskaper_egenskapid_binaerobjektid_binaer_get(vegobjekttypeid, vegobjektid, versjon, egenskapid, binaerobjektid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegobjekterApi()
vegobjekttypeid = 56 # int | Id for objektets vegobjekttype
vegobjektid = 789 # int | Id for objektet
versjon = 56 # int | versjon av objektet
egenskapid = 56 # int | Id for binæregenskapen som refererer til blob
binaerobjektid = 56 # int | blob_id fra binæregenskap

try:
    api_response = api_instance.vegobjekter_vegobjekttypeid_vegobjektid_versjon_egenskaper_egenskapid_binaerobjektid_binaer_get(vegobjekttypeid, vegobjektid, versjon, egenskapid, binaerobjektid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegobjekterApi->vegobjekter_vegobjekttypeid_vegobjektid_versjon_egenskaper_egenskapid_binaerobjektid_binaer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vegobjekttypeid** | **int**| Id for objektets vegobjekttype | 
 **vegobjektid** | **int**| Id for objektet | 
 **versjon** | **int**| versjon av objektet | 
 **egenskapid** | **int**| Id for binæregenskapen som refererer til blob | 
 **binaerobjektid** | **int**| blob_id fra binæregenskap | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegobjekter_vegobjekttypeid_vegobjektid_versjon_get**
> Vegobjekt vegobjekter_vegobjekttypeid_vegobjektid_versjon_get(x_client, vegobjekttypeid, vegobjektid, versjon, x_client_session=x_client_session, srid=srid, inkluder=inkluder, inkludergeometri=inkludergeometri, inkluder_egenskaper=inkluder_egenskaper, geometritoleranse=geometritoleranse, dybde=dybde)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegobjekterApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
vegobjekttypeid = 56 # int | Id for objektets vegobjekttype
vegobjektid = 789 # int | Id for objektet
versjon = 56 # int | versjon av objektet
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
srid = '6173' # str | Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) (optional) (default to 6173)
inkluder = ['inkluder_example'] # list[str] | kommaseparert liste over hvilke informasjonselementer som skal returneres i tillegg til vegobjektenes id. (optional)
inkludergeometri = 'inkludergeometri_example' # str | Et vegobjekt har opptil to geometrier, egengeometri og stedfestet geometri. Egengeoemtrien er plassert under `vegobjekt.egenskaper` om den finnes, stedfestet geometri er plassert under `vegobjekt.lokasjon`. I tillegg til de nevnte feltene på vegobjekt-responsen returneres også `vegobjekt.geometri` (dersom man har inkluder=geometri eller alle), slik at man alltid finner geometrien for vegobjektet ett sted. Dette feltet er egengeometri dersom objektet har det, hvis ikke har feltet stedfestet geometri Ved hvilken av disse som er tilfelle finner man ut ved å se på `vegobjekt.geometri.egengeometri` (optional)
inkluder_egenskaper = 'inkluder_egenskaper_example' # str | Gir mulighet til å filtrere hvilke egenskaper som skal returneres med `inkluder=egenskaper`. `basis` er alle egenskaper som ikke er assosiasjoner, stedfesting, geometri, eller lister av disse. (optional)
geometritoleranse = 56 # int | Angir om det skal returneres en forenklet geometri. Dersom parameteren utelates, returneres full geometri for vegobjektene. Nummeret angir distansetoleranse for generering av forenklet geometri. (optional)
dybde = '1' # str | Hvor mange nivå datterobjekter som skal inkluderes (optional) (default to 1)

try:
    api_response = api_instance.vegobjekter_vegobjekttypeid_vegobjektid_versjon_get(x_client, vegobjekttypeid, vegobjektid, versjon, x_client_session=x_client_session, srid=srid, inkluder=inkluder, inkludergeometri=inkludergeometri, inkluder_egenskaper=inkluder_egenskaper, geometritoleranse=geometritoleranse, dybde=dybde)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegobjekterApi->vegobjekter_vegobjekttypeid_vegobjektid_versjon_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **vegobjekttypeid** | **int**| Id for objektets vegobjekttype | 
 **vegobjektid** | **int**| Id for objektet | 
 **versjon** | **int**| versjon av objektet | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **srid** | **str**| Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) | [optional] [default to 6173]
 **inkluder** | [**list[str]**](str.md)| kommaseparert liste over hvilke informasjonselementer som skal returneres i tillegg til vegobjektenes id. | [optional] 
 **inkludergeometri** | **str**| Et vegobjekt har opptil to geometrier, egengeometri og stedfestet geometri. Egengeoemtrien er plassert under &#x60;vegobjekt.egenskaper&#x60; om den finnes, stedfestet geometri er plassert under &#x60;vegobjekt.lokasjon&#x60;. I tillegg til de nevnte feltene på vegobjekt-responsen returneres også &#x60;vegobjekt.geometri&#x60; (dersom man har inkluder&#x3D;geometri eller alle), slik at man alltid finner geometrien for vegobjektet ett sted. Dette feltet er egengeometri dersom objektet har det, hvis ikke har feltet stedfestet geometri Ved hvilken av disse som er tilfelle finner man ut ved å se på &#x60;vegobjekt.geometri.egengeometri&#x60; | [optional] 
 **inkluder_egenskaper** | **str**| Gir mulighet til å filtrere hvilke egenskaper som skal returneres med &#x60;inkluder&#x3D;egenskaper&#x60;. &#x60;basis&#x60; er alle egenskaper som ikke er assosiasjoner, stedfesting, geometri, eller lister av disse. | [optional] 
 **geometritoleranse** | **int**| Angir om det skal returneres en forenklet geometri. Dersom parameteren utelates, returneres full geometri for vegobjektene. Nummeret angir distansetoleranse for generering av forenklet geometri. | [optional] 
 **dybde** | **str**| Hvor mange nivå datterobjekter som skal inkluderes | [optional] [default to 1]

### Return type

[**Vegobjekt**](Vegobjekt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegobjekter_vegobjekttypeid_vegobjektid_versjoner_get**
> list[Vegobjekt] vegobjekter_vegobjekttypeid_vegobjektid_versjoner_get(x_client, vegobjekttypeid, vegobjektid, x_client_session=x_client_session, srid=srid, inkluder=inkluder, inkludergeometri=inkludergeometri, inkluder_egenskaper=inkluder_egenskaper, geometritoleranse=geometritoleranse, dybde=dybde)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegobjekterApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
vegobjekttypeid = 56 # int | Id for objektets vegobjekttype
vegobjektid = 789 # int | Id for objektet
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
srid = '6173' # str | Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) (optional) (default to 6173)
inkluder = ['inkluder_example'] # list[str] | kommaseparert liste over hvilke informasjonselementer som skal returneres i tillegg til vegobjektenes id. (optional)
inkludergeometri = 'inkludergeometri_example' # str | Et vegobjekt har opptil to geometrier, egengeometri og stedfestet geometri. Egengeoemtrien er plassert under `vegobjekt.egenskaper` om den finnes, stedfestet geometri er plassert under `vegobjekt.lokasjon`. I tillegg til de nevnte feltene på vegobjekt-responsen returneres også `vegobjekt.geometri` (dersom man har inkluder=geometri eller alle), slik at man alltid finner geometrien for vegobjektet ett sted. Dette feltet er egengeometri dersom objektet har det, hvis ikke har feltet stedfestet geometri Ved hvilken av disse som er tilfelle finner man ut ved å se på `vegobjekt.geometri.egengeometri` (optional)
inkluder_egenskaper = 'inkluder_egenskaper_example' # str | Gir mulighet til å filtrere hvilke egenskaper som skal returneres med `inkluder=egenskaper`. `basis` er alle egenskaper som ikke er assosiasjoner, stedfesting, geometri, eller lister av disse. (optional)
geometritoleranse = 56 # int | Angir om det skal returneres en forenklet geometri. Dersom parameteren utelates, returneres full geometri for vegobjektene. Nummeret angir distansetoleranse for generering av forenklet geometri. (optional)
dybde = '1' # str | Hvor mange nivå datterobjekter som skal inkluderes (optional) (default to 1)

try:
    api_response = api_instance.vegobjekter_vegobjekttypeid_vegobjektid_versjoner_get(x_client, vegobjekttypeid, vegobjektid, x_client_session=x_client_session, srid=srid, inkluder=inkluder, inkludergeometri=inkludergeometri, inkluder_egenskaper=inkluder_egenskaper, geometritoleranse=geometritoleranse, dybde=dybde)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegobjekterApi->vegobjekter_vegobjekttypeid_vegobjektid_versjoner_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **vegobjekttypeid** | **int**| Id for objektets vegobjekttype | 
 **vegobjektid** | **int**| Id for objektet | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **srid** | **str**| Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) | [optional] [default to 6173]
 **inkluder** | [**list[str]**](str.md)| kommaseparert liste over hvilke informasjonselementer som skal returneres i tillegg til vegobjektenes id. | [optional] 
 **inkludergeometri** | **str**| Et vegobjekt har opptil to geometrier, egengeometri og stedfestet geometri. Egengeoemtrien er plassert under &#x60;vegobjekt.egenskaper&#x60; om den finnes, stedfestet geometri er plassert under &#x60;vegobjekt.lokasjon&#x60;. I tillegg til de nevnte feltene på vegobjekt-responsen returneres også &#x60;vegobjekt.geometri&#x60; (dersom man har inkluder&#x3D;geometri eller alle), slik at man alltid finner geometrien for vegobjektet ett sted. Dette feltet er egengeometri dersom objektet har det, hvis ikke har feltet stedfestet geometri Ved hvilken av disse som er tilfelle finner man ut ved å se på &#x60;vegobjekt.geometri.egengeometri&#x60; | [optional] 
 **inkluder_egenskaper** | **str**| Gir mulighet til å filtrere hvilke egenskaper som skal returneres med &#x60;inkluder&#x3D;egenskaper&#x60;. &#x60;basis&#x60; er alle egenskaper som ikke er assosiasjoner, stedfesting, geometri, eller lister av disse. | [optional] 
 **geometritoleranse** | **int**| Angir om det skal returneres en forenklet geometri. Dersom parameteren utelates, returneres full geometri for vegobjektene. Nummeret angir distansetoleranse for generering av forenklet geometri. | [optional] 
 **dybde** | **str**| Hvor mange nivå datterobjekter som skal inkluderes | [optional] [default to 1]

### Return type

[**list[Vegobjekt]**](Vegobjekt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

