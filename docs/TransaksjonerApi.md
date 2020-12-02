# swagger_client.TransaksjonerApi

All URIs are relative to *https://nvdbapiles-v3.atlas.vegvesen.no*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_get**](TransaksjonerApi.md#status_get) | **GET** /status | 
[**transaksjoner_get**](TransaksjonerApi.md#transaksjoner_get) | **GET** /transaksjoner | 

# **status_get**
> InlineResponse2008 status_get(x_client, x_client_session=x_client_session)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransaksjonerApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)

try:
    api_response = api_instance.status_get(x_client, x_client_session=x_client_session)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransaksjonerApi->status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaksjoner_get**
> TransaksjonListeRespons transaksjoner_get(x_client, x_client_session=x_client_session, ider=ider, fra=fra, til=til)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransaksjonerApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
ider = [56] # list[int] | Filtrer på objekter med id. Kommaseparert (optional)
fra = 'fra_example' # str | Inkluder transaksjoner fra og med dette tidspunktet (optional)
til = 'til_example' # str | Inkluder transaksjoner til og med dette tidspunktet (optional)

try:
    api_response = api_instance.transaksjoner_get(x_client, x_client_session=x_client_session, ider=ider, fra=fra, til=til)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransaksjonerApi->transaksjoner_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **ider** | [**list[int]**](int.md)| Filtrer på objekter med id. Kommaseparert | [optional] 
 **fra** | **str**| Inkluder transaksjoner fra og med dette tidspunktet | [optional] 
 **til** | **str**| Inkluder transaksjoner til og med dette tidspunktet | [optional] 

### Return type

[**TransaksjonListeRespons**](TransaksjonListeRespons.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

