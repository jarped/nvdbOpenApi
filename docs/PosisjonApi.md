# swagger_client.PosisjonApi

All URIs are relative to *https://nvdbapiles-v3.atlas.vegvesen.no*

Method | HTTP request | Description
------------- | ------------- | -------------
[**posisjon_get**](PosisjonApi.md#posisjon_get) | **GET** /posisjon | 
[**veg_batch_get**](PosisjonApi.md#veg_batch_get) | **GET** /veg/batch | 
[**veg_get**](PosisjonApi.md#veg_get) | **GET** /veg | 

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
api_instance = swagger_client.PosisjonApi()
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
    print("Exception when calling PosisjonApi->posisjon_get: %s\n" % e)
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
api_instance = swagger_client.PosisjonApi()
vegsystemreferanser = 'vegsystemreferanser_example' # str |  (optional)
veglenkesekvenser = 'veglenkesekvenser_example' # str |  (optional)
kommune = [56] # list[int] | Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. (optional)
srid = '6173' # str | Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) (optional) (default to 6173)

try:
    api_response = api_instance.veg_batch_get(vegsystemreferanser=vegsystemreferanser, veglenkesekvenser=veglenkesekvenser, kommune=kommune, srid=srid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PosisjonApi->veg_batch_get: %s\n" % e)
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
api_instance = swagger_client.PosisjonApi()
vegsystemreferanse = 'vegsystemreferanse_example' # str | Filtrer vegobjekter på [vegsystemreferanse](https://api.vegdata.no/v3/vegsystemreferanse.html) (optional)
veglenkesekvens = 'veglenkesekvens_example' # str | Filtrer vegobjekter på stedfesting på vegnettet. Format: `posisjon@veglenkesekvensid` (optional)
srid = '6173' # str | Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) (optional) (default to 6173)
kommune = [56] # list[int] | Filtrer på kommune. Kommaseparert liste. Se /omrader/kommuner for mulige verdier. (optional)

try:
    api_response = api_instance.veg_get(vegsystemreferanse=vegsystemreferanse, veglenkesekvens=veglenkesekvens, srid=srid, kommune=kommune)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PosisjonApi->veg_get: %s\n" % e)
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

