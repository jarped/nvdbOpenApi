# swagger_client.VegnettApi

All URIs are relative to *https://nvdbapiles-v3.atlas.vegvesen.no*

Method | HTTP request | Description
------------- | ------------- | -------------
[**beta_vegnett_rute_get**](VegnettApi.md#beta_vegnett_rute_get) | **GET** /beta/vegnett/rute | 
[**beta_vegnett_rute_post**](VegnettApi.md#beta_vegnett_rute_post) | **POST** /beta/vegnett/rute | 
[**posisjon_get**](VegnettApi.md#posisjon_get) | **GET** /posisjon | 
[**veg_batch_get**](VegnettApi.md#veg_batch_get) | **GET** /veg/batch | 
[**veg_get**](VegnettApi.md#veg_get) | **GET** /veg | 
[**vegnett_get**](VegnettApi.md#vegnett_get) | **GET** /vegnett | 
[**vegnett_noder_get**](VegnettApi.md#vegnett_noder_get) | **GET** /vegnett/noder | 
[**vegnett_noder_nodeid_get**](VegnettApi.md#vegnett_noder_nodeid_get) | **GET** /vegnett/noder/{nodeid} | 
[**vegnett_veglenkesekvenser_get**](VegnettApi.md#vegnett_veglenkesekvenser_get) | **GET** /vegnett/veglenkesekvenser | 
[**vegnett_veglenkesekvenser_segmentert_get**](VegnettApi.md#vegnett_veglenkesekvenser_segmentert_get) | **GET** /vegnett/veglenkesekvenser/segmentert | 
[**vegnett_veglenkesekvenser_segmentert_veglenkesekvensid_get**](VegnettApi.md#vegnett_veglenkesekvenser_segmentert_veglenkesekvensid_get) | **GET** /vegnett/veglenkesekvenser/segmentert/{veglenkesekvensid} | 
[**vegnett_veglenkesekvenser_veglenkesekvensid_get**](VegnettApi.md#vegnett_veglenkesekvenser_veglenkesekvensid_get) | **GET** /vegnett/veglenkesekvenser/{veglenkesekvensid} | 

# **beta_vegnett_rute_get**
> RuteRespons beta_vegnett_rute_get(x_client, x_client_session=x_client_session, start=start, slutt=slutt, geometri=geometri, maks_avstand=maks_avstand, omkrets=omkrets, konnekteringslenker=konnekteringslenker, detaljerte_lenker=detaljerte_lenker, kortform=kortform, vegsystemreferanse=vegsystemreferanse, trafikantgruppe=trafikantgruppe, behold_trafikantgruppe=behold_trafikantgruppe, typeveg=typeveg, tidspunkt=tidspunkt, tidspunkt_start=tidspunkt_start, tidspunkt_slutt=tidspunkt_slutt, srid=srid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegnettApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
start = 'start_example' # str | Startposisjon som et punkt eller posisjon@veglenkesekvens. (optional)
slutt = 'slutt_example' # str | Sluttposisjon som et punkt eller posisjon@veglenkesekvens (optional)
geometri = 'geometri_example' # str | Finn sammenhengende vegnett som passer med denne geometrien (optional)
maks_avstand = 10 # int | Maks avstand i meter til veglenker (optional) (default to 10)
omkrets = 100 # int | Konvolutt lagt rund start- og slutt-punkt for å beregne rute (optional) (default to 100)
konnekteringslenker = true # bool | Inkludere konnekteringslenker (optional) (default to true)
detaljerte_lenker = false # bool | Inkludere detaljerte lenker (optional) (default to false)
kortform = false # bool | Returner minimal respons (optional) (default to false)
vegsystemreferanse = ['vegsystemreferanse_example'] # list[str] | Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. (optional)
trafikantgruppe = 'trafikantgruppe_example' # str | Filtrer vegobjekter på trafikantgruppe (optional)
behold_trafikantgruppe = false # bool | Behold trafikantgruppe gjennom ruten. Trafikantgruppe velges fra første og siste punkt i ruten, om de er ulike velges K (kjørende). Overstyres av parameteren trafikantgruppe. (optional) (default to false)
typeveg = ['typeveg_example'] # list[str] | Filtrer vegobjekter på type veg på vegnettet objektet er stedfestet på. Kommaseparert liste. (optional)
tidspunkt = '2013-10-20' # date | Begrense spørring til det gitte tidspunktet (optional)
tidspunkt_start = '2013-10-20' # date | Begrens vegnettgyldighet til denne startdatoen. Må brukes sammen med `tidspunkt_slutt`. (optional)
tidspunkt_slutt = '2013-10-20' # date | Begrens vegnettgyldighet til denne sluttdatoen. Må brukes sammen med `tidspunkt_start`. (optional)
srid = '6173' # str | Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) (optional) (default to 6173)

try:
    api_response = api_instance.beta_vegnett_rute_get(x_client, x_client_session=x_client_session, start=start, slutt=slutt, geometri=geometri, maks_avstand=maks_avstand, omkrets=omkrets, konnekteringslenker=konnekteringslenker, detaljerte_lenker=detaljerte_lenker, kortform=kortform, vegsystemreferanse=vegsystemreferanse, trafikantgruppe=trafikantgruppe, behold_trafikantgruppe=behold_trafikantgruppe, typeveg=typeveg, tidspunkt=tidspunkt, tidspunkt_start=tidspunkt_start, tidspunkt_slutt=tidspunkt_slutt, srid=srid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegnettApi->beta_vegnett_rute_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **start** | **str**| Startposisjon som et punkt eller posisjon@veglenkesekvens. | [optional] 
 **slutt** | **str**| Sluttposisjon som et punkt eller posisjon@veglenkesekvens | [optional] 
 **geometri** | **str**| Finn sammenhengende vegnett som passer med denne geometrien | [optional] 
 **maks_avstand** | **int**| Maks avstand i meter til veglenker | [optional] [default to 10]
 **omkrets** | **int**| Konvolutt lagt rund start- og slutt-punkt for å beregne rute | [optional] [default to 100]
 **konnekteringslenker** | **bool**| Inkludere konnekteringslenker | [optional] [default to true]
 **detaljerte_lenker** | **bool**| Inkludere detaljerte lenker | [optional] [default to false]
 **kortform** | **bool**| Returner minimal respons | [optional] [default to false]
 **vegsystemreferanse** | [**list[str]**](str.md)| Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. | [optional] 
 **trafikantgruppe** | **str**| Filtrer vegobjekter på trafikantgruppe | [optional] 
 **behold_trafikantgruppe** | **bool**| Behold trafikantgruppe gjennom ruten. Trafikantgruppe velges fra første og siste punkt i ruten, om de er ulike velges K (kjørende). Overstyres av parameteren trafikantgruppe. | [optional] [default to false]
 **typeveg** | [**list[str]**](str.md)| Filtrer vegobjekter på type veg på vegnettet objektet er stedfestet på. Kommaseparert liste. | [optional] 
 **tidspunkt** | **date**| Begrense spørring til det gitte tidspunktet | [optional] 
 **tidspunkt_start** | **date**| Begrens vegnettgyldighet til denne startdatoen. Må brukes sammen med &#x60;tidspunkt_slutt&#x60;. | [optional] 
 **tidspunkt_slutt** | **date**| Begrens vegnettgyldighet til denne sluttdatoen. Må brukes sammen med &#x60;tidspunkt_start&#x60;. | [optional] 
 **srid** | **str**| Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) | [optional] [default to 6173]

### Return type

[**RuteRespons**](RuteRespons.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **beta_vegnett_rute_post**
> RuteRespons beta_vegnett_rute_post(body, x_client, x_client_session=x_client_session)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegnettApi()
body = swagger_client.RouteRequest() # RouteRequest | Ruteforespørsel definert som JSON.
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)

try:
    api_response = api_instance.beta_vegnett_rute_post(body, x_client, x_client_session=x_client_session)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegnettApi->beta_vegnett_rute_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RouteRequest**](RouteRequest.md)| Ruteforespørsel definert som JSON. | 
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 

### Return type

[**RuteRespons**](RuteRespons.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **posisjon_get**
> list[Posisjonsresultat] posisjon_get(x_client, x_client_session=x_client_session, nord=nord, ost=ost, lat=lat, lon=lon, maks_avstand=maks_avstand, maks_antall=maks_antall, konnekteringslenker=konnekteringslenker, detaljerte_lenker=detaljerte_lenker, vegsystemreferanse=vegsystemreferanse, srid=srid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegnettApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
nord = 1.2 # float | Nordlig koordinat (optional)
ost = 1.2 # float | Østlig koordinat (optional)
lat = 1.2 # float | Breddegrad (optional)
lon = 1.2 # float | Lengdegrad (optional)
maks_avstand = 30 # int | Angir søkeavstand i meter (optional) (default to 30)
maks_antall = 1 # int | Angir hvor mange resultater som maksimum skal returneres (optional) (default to 1)
konnekteringslenker = false # bool | Angir om det skal returneres treff på konnekteringslenker (optional) (default to false)
detaljerte_lenker = false # bool | Angir om det skal returneres treff på detaljerte vegnettsnivå (optional) (default to false)
vegsystemreferanse = ['vegsystemreferanse_example'] # list[str] | Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. (optional)
srid = '6173' # str | Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) (optional) (default to 6173)

try:
    api_response = api_instance.posisjon_get(x_client, x_client_session=x_client_session, nord=nord, ost=ost, lat=lat, lon=lon, maks_avstand=maks_avstand, maks_antall=maks_antall, konnekteringslenker=konnekteringslenker, detaljerte_lenker=detaljerte_lenker, vegsystemreferanse=vegsystemreferanse, srid=srid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegnettApi->posisjon_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **nord** | **float**| Nordlig koordinat | [optional] 
 **ost** | **float**| Østlig koordinat | [optional] 
 **lat** | **float**| Breddegrad | [optional] 
 **lon** | **float**| Lengdegrad | [optional] 
 **maks_avstand** | **int**| Angir søkeavstand i meter | [optional] [default to 30]
 **maks_antall** | **int**| Angir hvor mange resultater som maksimum skal returneres | [optional] [default to 1]
 **konnekteringslenker** | **bool**| Angir om det skal returneres treff på konnekteringslenker | [optional] [default to false]
 **detaljerte_lenker** | **bool**| Angir om det skal returneres treff på detaljerte vegnettsnivå | [optional] [default to false]
 **vegsystemreferanse** | [**list[str]**](str.md)| Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. | [optional] 
 **srid** | **str**| Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) | [optional] [default to 6173]

### Return type

[**list[Posisjonsresultat]**](Posisjonsresultat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **veg_batch_get**
> dict(str, Posisjonsresultat) veg_batch_get(vegsystemreferanser=vegsystemreferanser, veglenkesekvenser=veglenkesekvenser, kommune=kommune, srid=srid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegnettApi()
vegsystemreferanser = 'vegsystemreferanser_example' # str |  (optional)
veglenkesekvenser = 'veglenkesekvenser_example' # str |  (optional)
kommune = [56] # list[int] | Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. (optional)
srid = '6173' # str | Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) (optional) (default to 6173)

try:
    api_response = api_instance.veg_batch_get(vegsystemreferanser=vegsystemreferanser, veglenkesekvenser=veglenkesekvenser, kommune=kommune, srid=srid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegnettApi->veg_batch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vegsystemreferanser** | **str**|  | [optional] 
 **veglenkesekvenser** | **str**|  | [optional] 
 **kommune** | [**list[int]**](int.md)| Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. | [optional] 
 **srid** | **str**| Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) | [optional] [default to 6173]

### Return type

[**dict(str, Posisjonsresultat)**](Posisjonsresultat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **veg_get**
> Posisjonsresultat veg_get(vegsystemreferanse=vegsystemreferanse, veglenkesekvens=veglenkesekvens, srid=srid, kommune=kommune)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegnettApi()
vegsystemreferanse = 'vegsystemreferanse_example' # str | Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) (optional)
veglenkesekvens = 'veglenkesekvens_example' # str | Filtrer vegobjekter på stedfesting på vegnettet. Format: `posisjon@veglenkesekvensid` (optional)
srid = '6173' # str | Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) (optional) (default to 6173)
kommune = [56] # list[int] | Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. (optional)

try:
    api_response = api_instance.veg_get(vegsystemreferanse=vegsystemreferanse, veglenkesekvens=veglenkesekvens, srid=srid, kommune=kommune)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegnettApi->veg_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vegsystemreferanse** | **str**| Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) | [optional] 
 **veglenkesekvens** | **str**| Filtrer vegobjekter på stedfesting på vegnettet. Format: &#x60;posisjon@veglenkesekvensid&#x60; | [optional] 
 **srid** | **str**| Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) | [optional] [default to 6173]
 **kommune** | [**list[int]**](int.md)| Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. | [optional] 

### Return type

[**Posisjonsresultat**](Posisjonsresultat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegnett_get**
> list[InlineResponse2006] vegnett_get(x_client, x_client_session=x_client_session)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegnettApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)

try:
    api_response = api_instance.vegnett_get(x_client, x_client_session=x_client_session)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegnettApi->vegnett_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 

### Return type

[**list[InlineResponse2006]**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegnett_noder_get**
> VegnoderListeRespons vegnett_noder_get(x_client, x_client_session=x_client_session, ider=ider, topologiniv=topologiniv, superid=superid, fylke=fylke, kommune=kommune, kontraktsomrade=kontraktsomrade, riksvegrute=riksvegrute, vegsystemreferanse=vegsystemreferanse, kartutnitt=kartutnitt, polygon=polygon, tidspunkt=tidspunkt)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegnettApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
ider = [56] # list[int] | Filtrer på objekter med id. Kommaseparert (optional)
topologiniv = 'topologiniv_example' # str | Hent kun elementer på det gitte topologinivået. - Dersom en veglenke har nivå vegtrasé er ofte feltet for topologinivå ikke tilstede. Man vil da få alle veglenker som ikke har verdi kjørefelt eller kjørebane. (optional)
superid = 789 # int | Hent alle noder med tilkobling til veglenker som har veglenke med oppgitt id som \"forelder\" i overordnet topologinivå. (optional)
fylke = [56] # list[int] | Filtrer på fylke. Kommaseparert liste. Se /omrader/fylker for mulige verdier. (optional)
kommune = [56] # list[int] | Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. (optional)
kontraktsomrade = ['kontraktsomrade_example'] # list[str] | Filtrer på kontraktsomrade. Kommaseparert liste. Se /omrader/kontraktsomrader for mulige verdier. (optional)
riksvegrute = ['riksvegrute_example'] # list[str] | Filtrer på riksvegrute. Kommaseparert liste. Se /omrader/riksvegruter for mulige verdier. (optional)
vegsystemreferanse = ['vegsystemreferanse_example'] # list[str] | Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. (optional)
kartutnitt = 'kartutnitt_example' # str | Filtrer vegobjekter med kartutnitt i det gjeldende geografiske referansesystemet (`srid`-paramteret) (optional)
polygon = 'polygon_example' # str | Filtrer vegobjekter med polygon i det gjeldende geografiske referansesystemet (`srid`-paramteret) (optional)
tidspunkt = '2013-10-20' # date | Begrense spørring til det gitte tidspunktet (optional)

try:
    api_response = api_instance.vegnett_noder_get(x_client, x_client_session=x_client_session, ider=ider, topologiniv=topologiniv, superid=superid, fylke=fylke, kommune=kommune, kontraktsomrade=kontraktsomrade, riksvegrute=riksvegrute, vegsystemreferanse=vegsystemreferanse, kartutnitt=kartutnitt, polygon=polygon, tidspunkt=tidspunkt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegnettApi->vegnett_noder_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **ider** | [**list[int]**](int.md)| Filtrer på objekter med id. Kommaseparert | [optional] 
 **topologiniv** | **str**| Hent kun elementer på det gitte topologinivået. - Dersom en veglenke har nivå vegtrasé er ofte feltet for topologinivå ikke tilstede. Man vil da få alle veglenker som ikke har verdi kjørefelt eller kjørebane. | [optional] 
 **superid** | **int**| Hent alle noder med tilkobling til veglenker som har veglenke med oppgitt id som \&quot;forelder\&quot; i overordnet topologinivå. | [optional] 
 **fylke** | [**list[int]**](int.md)| Filtrer på fylke. Kommaseparert liste. Se /omrader/fylker for mulige verdier. | [optional] 
 **kommune** | [**list[int]**](int.md)| Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. | [optional] 
 **kontraktsomrade** | [**list[str]**](str.md)| Filtrer på kontraktsomrade. Kommaseparert liste. Se /omrader/kontraktsomrader for mulige verdier. | [optional] 
 **riksvegrute** | [**list[str]**](str.md)| Filtrer på riksvegrute. Kommaseparert liste. Se /omrader/riksvegruter for mulige verdier. | [optional] 
 **vegsystemreferanse** | [**list[str]**](str.md)| Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. | [optional] 
 **kartutnitt** | **str**| Filtrer vegobjekter med kartutnitt i det gjeldende geografiske referansesystemet (&#x60;srid&#x60;-paramteret) | [optional] 
 **polygon** | **str**| Filtrer vegobjekter med polygon i det gjeldende geografiske referansesystemet (&#x60;srid&#x60;-paramteret) | [optional] 
 **tidspunkt** | **date**| Begrense spørring til det gitte tidspunktet | [optional] 

### Return type

[**VegnoderListeRespons**](VegnoderListeRespons.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegnett_noder_nodeid_get**
> Vegnode vegnett_noder_nodeid_get(x_client, nodeid, x_client_session=x_client_session, srid=srid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegnettApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
nodeid = 789 # int | 
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
srid = '6173' # str | Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) (optional) (default to 6173)

try:
    api_response = api_instance.vegnett_noder_nodeid_get(x_client, nodeid, x_client_session=x_client_session, srid=srid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegnettApi->vegnett_noder_nodeid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **nodeid** | **int**|  | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **srid** | **str**| Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) | [optional] [default to 6173]

### Return type

[**Vegnode**](Vegnode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegnett_veglenkesekvenser_get**
> VeglenkesekvensListeRespons vegnett_veglenkesekvenser_get(x_client, x_client_session=x_client_session, ider=ider, fylke=fylke, kommune=kommune, kontraktsomrade=kontraktsomrade, riksvegrute=riksvegrute, vegsystemreferanse=vegsystemreferanse, kartutnitt=kartutnitt, polygon=polygon, topologiniv=topologiniv, superid=superid, antall=antall, start=start)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegnettApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
ider = [56] # list[int] | Filtrer på objekter med id. Kommaseparert (optional)
fylke = [56] # list[int] | Filtrer på fylke. Kommaseparert liste. Se /omrader/fylker for mulige verdier. (optional)
kommune = [56] # list[int] | Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. (optional)
kontraktsomrade = ['kontraktsomrade_example'] # list[str] | Filtrer på kontraktsomrade. Kommaseparert liste. Se /omrader/kontraktsomrader for mulige verdier. (optional)
riksvegrute = ['riksvegrute_example'] # list[str] | Filtrer på riksvegrute. Kommaseparert liste. Se /omrader/riksvegruter for mulige verdier. (optional)
vegsystemreferanse = ['vegsystemreferanse_example'] # list[str] | Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. (optional)
kartutnitt = 'kartutnitt_example' # str | Filtrer vegobjekter med kartutnitt i det gjeldende geografiske referansesystemet (`srid`-paramteret) (optional)
polygon = 'polygon_example' # str | Filtrer vegobjekter med polygon i det gjeldende geografiske referansesystemet (`srid`-paramteret) (optional)
topologiniv = 'topologiniv_example' # str | Hent kun elementer på det gitte topologinivået. - Dersom en veglenke har nivå vegtrasé er ofte feltet for topologinivå ikke tilstede. Man vil da få alle veglenker som ikke har verdi kjørefelt eller kjørebane. (optional)
superid = 789 # int | Hent detaljerte veglenkesekvenser stedfestet på veglenkesekvens med denne id (optional)
antall = 56 # int | Angir hvor mange objekter som skal returneres. Øvre grense er avhengig av størrelse på respons, og vil kunne variere fra endepunkt til endepunkt. Dersom det angis en verdi for antall som overskrider maksimum, vil maksimumsverdi benyttes. Se også `sidestørrelse` i responsens `metadata`-objekt. (optional)
start = 'start_example' # str | Angir markør for neste side objekter som skal returneres. Denne får man i metadata-feltet i responsen. (optional)

try:
    api_response = api_instance.vegnett_veglenkesekvenser_get(x_client, x_client_session=x_client_session, ider=ider, fylke=fylke, kommune=kommune, kontraktsomrade=kontraktsomrade, riksvegrute=riksvegrute, vegsystemreferanse=vegsystemreferanse, kartutnitt=kartutnitt, polygon=polygon, topologiniv=topologiniv, superid=superid, antall=antall, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegnettApi->vegnett_veglenkesekvenser_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **ider** | [**list[int]**](int.md)| Filtrer på objekter med id. Kommaseparert | [optional] 
 **fylke** | [**list[int]**](int.md)| Filtrer på fylke. Kommaseparert liste. Se /omrader/fylker for mulige verdier. | [optional] 
 **kommune** | [**list[int]**](int.md)| Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. | [optional] 
 **kontraktsomrade** | [**list[str]**](str.md)| Filtrer på kontraktsomrade. Kommaseparert liste. Se /omrader/kontraktsomrader for mulige verdier. | [optional] 
 **riksvegrute** | [**list[str]**](str.md)| Filtrer på riksvegrute. Kommaseparert liste. Se /omrader/riksvegruter for mulige verdier. | [optional] 
 **vegsystemreferanse** | [**list[str]**](str.md)| Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. | [optional] 
 **kartutnitt** | **str**| Filtrer vegobjekter med kartutnitt i det gjeldende geografiske referansesystemet (&#x60;srid&#x60;-paramteret) | [optional] 
 **polygon** | **str**| Filtrer vegobjekter med polygon i det gjeldende geografiske referansesystemet (&#x60;srid&#x60;-paramteret) | [optional] 
 **topologiniv** | **str**| Hent kun elementer på det gitte topologinivået. - Dersom en veglenke har nivå vegtrasé er ofte feltet for topologinivå ikke tilstede. Man vil da få alle veglenker som ikke har verdi kjørefelt eller kjørebane. | [optional] 
 **superid** | **int**| Hent detaljerte veglenkesekvenser stedfestet på veglenkesekvens med denne id | [optional] 
 **antall** | **int**| Angir hvor mange objekter som skal returneres. Øvre grense er avhengig av størrelse på respons, og vil kunne variere fra endepunkt til endepunkt. Dersom det angis en verdi for antall som overskrider maksimum, vil maksimumsverdi benyttes. Se også &#x60;sidestørrelse&#x60; i responsens &#x60;metadata&#x60;-objekt. | [optional] 
 **start** | **str**| Angir markør for neste side objekter som skal returneres. Denne får man i metadata-feltet i responsen. | [optional] 

### Return type

[**VeglenkesekvensListeRespons**](VeglenkesekvensListeRespons.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegnett_veglenkesekvenser_segmentert_get**
> VeglenkesegmentListeRespons vegnett_veglenkesekvenser_segmentert_get(x_client, x_client_session=x_client_session, vegsystemreferanse=vegsystemreferanse, fylke=fylke, kommune=kommune, kontraktsomrade=kontraktsomrade, riksvegrute=riksvegrute, kartutnitt=kartutnitt, polygon=polygon, tidspunkt=tidspunkt, historisk=historisk, arm=arm, kryssystem=kryssystem, sideanlegg=sideanlegg, detaljniva=detaljniva, typeveg=typeveg, adskiltelop=adskiltelop, veglenketype=veglenketype, trafikantgruppe=trafikantgruppe, geometritoleranse=geometritoleranse)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegnettApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
vegsystemreferanse = ['vegsystemreferanse_example'] # list[str] | Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. (optional)
fylke = [56] # list[int] | Filtrer på fylke. Kommaseparert liste. Se /omrader/fylker for mulige verdier. (optional)
kommune = [56] # list[int] | Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. (optional)
kontraktsomrade = ['kontraktsomrade_example'] # list[str] | Filtrer på kontraktsomrade. Kommaseparert liste. Se /omrader/kontraktsomrader for mulige verdier. (optional)
riksvegrute = ['riksvegrute_example'] # list[str] | Filtrer på riksvegrute. Kommaseparert liste. Se /omrader/riksvegruter for mulige verdier. (optional)
kartutnitt = 'kartutnitt_example' # str | Filtrer vegobjekter med kartutnitt i det gjeldende geografiske referansesystemet (`srid`-paramteret) (optional)
polygon = 'polygon_example' # str | Filtrer vegobjekter med polygon i det gjeldende geografiske referansesystemet (`srid`-paramteret) (optional)
tidspunkt = '2013-10-20' # date | Begrense spørring til det gitte tidspunktet (optional)
historisk = false # bool | Ved `true` returneres også segmenter med sluttdato (optional) (default to false)
arm = true # bool | Filtrer vegobjekter på om de er stedfestet på Strekning med verdi satt for «arm» (optional)
kryssystem = true # bool | Filtrer vegobjekter på om de er stedfestet samme hvor det er et Kryssystem (optional)
sideanlegg = true # bool | Filtrer vegobjekter på om de er stedfestet samme hvor det er et Sideanlegg (optional)
detaljniva = 'detaljniva_example' # str | Filtrer vegobjekter på detaljnivå på vegnettet objektet er stedfestet på (kortnavn fra datakatalogen). (optional)
typeveg = ['typeveg_example'] # list[str] | Filtrer vegobjekter på type veg på vegnettet objektet er stedfestet på. Kommaseparert liste. (optional)
adskiltelop = 'adskiltelop_example' # str | Filtrer vegobjekter på om de er stedfestet hvor det er Strekning med verdi satt for «adskilte løp» (optional)
veglenketype = ['veglenketype_example'] # list[str] | Filtrer vegobjekter på veglenketype på vegnettet objektet er stedfestet. Kommaseparert liste. (optional)
trafikantgruppe = 'trafikantgruppe_example' # str | Filtrer vegobjekter på trafikantgruppe (optional)
geometritoleranse = 56 # int | Angir om det skal returneres en forenklet geometri. Dersom parameteren utelates, returneres full geometri for vegobjektene. Nummeret angir distansetoleranse for generering av forenklet geometri. (optional)

try:
    api_response = api_instance.vegnett_veglenkesekvenser_segmentert_get(x_client, x_client_session=x_client_session, vegsystemreferanse=vegsystemreferanse, fylke=fylke, kommune=kommune, kontraktsomrade=kontraktsomrade, riksvegrute=riksvegrute, kartutnitt=kartutnitt, polygon=polygon, tidspunkt=tidspunkt, historisk=historisk, arm=arm, kryssystem=kryssystem, sideanlegg=sideanlegg, detaljniva=detaljniva, typeveg=typeveg, adskiltelop=adskiltelop, veglenketype=veglenketype, trafikantgruppe=trafikantgruppe, geometritoleranse=geometritoleranse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegnettApi->vegnett_veglenkesekvenser_segmentert_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **vegsystemreferanse** | [**list[str]**](str.md)| Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) Kommaseparert liste. | [optional] 
 **fylke** | [**list[int]**](int.md)| Filtrer på fylke. Kommaseparert liste. Se /omrader/fylker for mulige verdier. | [optional] 
 **kommune** | [**list[int]**](int.md)| Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. | [optional] 
 **kontraktsomrade** | [**list[str]**](str.md)| Filtrer på kontraktsomrade. Kommaseparert liste. Se /omrader/kontraktsomrader for mulige verdier. | [optional] 
 **riksvegrute** | [**list[str]**](str.md)| Filtrer på riksvegrute. Kommaseparert liste. Se /omrader/riksvegruter for mulige verdier. | [optional] 
 **kartutnitt** | **str**| Filtrer vegobjekter med kartutnitt i det gjeldende geografiske referansesystemet (&#x60;srid&#x60;-paramteret) | [optional] 
 **polygon** | **str**| Filtrer vegobjekter med polygon i det gjeldende geografiske referansesystemet (&#x60;srid&#x60;-paramteret) | [optional] 
 **tidspunkt** | **date**| Begrense spørring til det gitte tidspunktet | [optional] 
 **historisk** | **bool**| Ved &#x60;true&#x60; returneres også segmenter med sluttdato | [optional] [default to false]
 **arm** | **bool**| Filtrer vegobjekter på om de er stedfestet på Strekning med verdi satt for «arm» | [optional] 
 **kryssystem** | **bool**| Filtrer vegobjekter på om de er stedfestet samme hvor det er et Kryssystem | [optional] 
 **sideanlegg** | **bool**| Filtrer vegobjekter på om de er stedfestet samme hvor det er et Sideanlegg | [optional] 
 **detaljniva** | **str**| Filtrer vegobjekter på detaljnivå på vegnettet objektet er stedfestet på (kortnavn fra datakatalogen). | [optional] 
 **typeveg** | [**list[str]**](str.md)| Filtrer vegobjekter på type veg på vegnettet objektet er stedfestet på. Kommaseparert liste. | [optional] 
 **adskiltelop** | **str**| Filtrer vegobjekter på om de er stedfestet hvor det er Strekning med verdi satt for «adskilte løp» | [optional] 
 **veglenketype** | [**list[str]**](str.md)| Filtrer vegobjekter på veglenketype på vegnettet objektet er stedfestet. Kommaseparert liste. | [optional] 
 **trafikantgruppe** | **str**| Filtrer vegobjekter på trafikantgruppe | [optional] 
 **geometritoleranse** | **int**| Angir om det skal returneres en forenklet geometri. Dersom parameteren utelates, returneres full geometri for vegobjektene. Nummeret angir distansetoleranse for generering av forenklet geometri. | [optional] 

### Return type

[**VeglenkesegmentListeRespons**](VeglenkesegmentListeRespons.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegnett_veglenkesekvenser_segmentert_veglenkesekvensid_get**
> list[Veglenkesegment] vegnett_veglenkesekvenser_segmentert_veglenkesekvensid_get(x_client, veglenkesekvensid, x_client_session=x_client_session, historisk=historisk, srid=srid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegnettApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
veglenkesekvensid = 789 # int | 
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
historisk = false # bool | Ved `true` returneres også segmenter med sluttdato (optional) (default to false)
srid = '6173' # str | Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) (optional) (default to 6173)

try:
    api_response = api_instance.vegnett_veglenkesekvenser_segmentert_veglenkesekvensid_get(x_client, veglenkesekvensid, x_client_session=x_client_session, historisk=historisk, srid=srid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegnettApi->vegnett_veglenkesekvenser_segmentert_veglenkesekvensid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **veglenkesekvensid** | **int**|  | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **historisk** | **bool**| Ved &#x60;true&#x60; returneres også segmenter med sluttdato | [optional] [default to false]
 **srid** | **str**| Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) | [optional] [default to 6173]

### Return type

[**list[Veglenkesegment]**](Veglenkesegment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegnett_veglenkesekvenser_veglenkesekvensid_get**
> Veglenkesekvens vegnett_veglenkesekvenser_veglenkesekvensid_get(x_client, veglenkesekvensid, x_client_session=x_client_session, srid=srid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VegnettApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
veglenkesekvensid = 789 # int | 
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
srid = '6173' # str | Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) (optional) (default to 6173)

try:
    api_response = api_instance.vegnett_veglenkesekvenser_veglenkesekvensid_get(x_client, veglenkesekvensid, x_client_session=x_client_session, srid=srid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VegnettApi->vegnett_veglenkesekvenser_veglenkesekvensid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **veglenkesekvensid** | **int**|  | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **srid** | **str**| Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) | [optional] [default to 6173]

### Return type

[**Veglenkesekvens**](Veglenkesekvens.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

