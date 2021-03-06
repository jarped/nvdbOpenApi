# swagger_client.OmrderApi

All URIs are relative to *https://nvdbapiles-v3.atlas.vegvesen.no*

Method | HTTP request | Description
------------- | ------------- | -------------
[**omrader_fylker_get**](OmrderApi.md#omrader_fylker_get) | **GET** /omrader/fylker | 
[**omrader_get**](OmrderApi.md#omrader_get) | **GET** /omrader | 
[**omrader_kommuner_get**](OmrderApi.md#omrader_kommuner_get) | **GET** /omrader/kommuner | 
[**omrader_kontraktomrader_get**](OmrderApi.md#omrader_kontraktomrader_get) | **GET** /omrader/kontraktomrader | 
[**omrader_riksvegruter_get**](OmrderApi.md#omrader_riksvegruter_get) | **GET** /omrader/riksvegruter | 

# **omrader_fylker_get**
> list[Fylke] omrader_fylker_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match, srid=srid, inkluder=inkluder)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OmrderApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
if_none_match = 'if_none_match_example' # str | Dersom header matcher gjeldende E-tag vil 304 returneres (optional)
srid = '6173' # str | Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) (optional) (default to 6173)
inkluder = ['inkluder_example'] # list[str] | kommaseparert liste over hvilke informasjonselementer som skal returneres i tillegg til vegobjektenes id. (optional)

try:
    api_response = api_instance.omrader_fylker_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match, srid=srid, inkluder=inkluder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OmrderApi->omrader_fylker_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **if_none_match** | **str**| Dersom header matcher gjeldende E-tag vil 304 returneres | [optional] 
 **srid** | **str**| Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) | [optional] [default to 6173]
 **inkluder** | [**list[str]**](str.md)| kommaseparert liste over hvilke informasjonselementer som skal returneres i tillegg til vegobjektenes id. | [optional] 

### Return type

[**list[Fylke]**](Fylke.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **omrader_get**
> list[InlineResponse2007] omrader_get(x_client, x_client_session=x_client_session)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OmrderApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)

try:
    api_response = api_instance.omrader_get(x_client, x_client_session=x_client_session)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OmrderApi->omrader_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 

### Return type

[**list[InlineResponse2007]**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **omrader_kommuner_get**
> list[Kommune] omrader_kommuner_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match, srid=srid, inkluder=inkluder)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OmrderApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
if_none_match = 'if_none_match_example' # str | Dersom header matcher gjeldende E-tag vil 304 returneres (optional)
srid = '6173' # str | Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) (optional) (default to 6173)
inkluder = ['inkluder_example'] # list[str] | kommaseparert liste over hvilke informasjonselementer som skal returneres i tillegg til vegobjektenes id. (optional)

try:
    api_response = api_instance.omrader_kommuner_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match, srid=srid, inkluder=inkluder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OmrderApi->omrader_kommuner_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **if_none_match** | **str**| Dersom header matcher gjeldende E-tag vil 304 returneres | [optional] 
 **srid** | **str**| Angir hvilket geografisk referansesystem geometrien skal returneres i.   Mer informasjon: [EPSG:6173](https://epsg.io/6173) [EPSG:6173 i NVDB](https://github.com/nvdb-vegdata/utviklerkonferanse-2018/blob/master/doc/epsg6173.md) [EPSG:4326](http://epsg.io/4326) | [optional] [default to 6173]
 **inkluder** | [**list[str]**](str.md)| kommaseparert liste over hvilke informasjonselementer som skal returneres i tillegg til vegobjektenes id. | [optional] 

### Return type

[**list[Kommune]**](Kommune.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **omrader_kontraktomrader_get**
> list[Kontraktsomrade] omrader_kontraktomrader_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match, inkluder=inkluder)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OmrderApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
if_none_match = 'if_none_match_example' # str | Dersom header matcher gjeldende E-tag vil 304 returneres (optional)
inkluder = ['inkluder_example'] # list[str] | kommaseparert liste over hvilke informasjonselementer som skal returneres i tillegg til vegobjektenes id. (optional)

try:
    api_response = api_instance.omrader_kontraktomrader_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match, inkluder=inkluder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OmrderApi->omrader_kontraktomrader_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **if_none_match** | **str**| Dersom header matcher gjeldende E-tag vil 304 returneres | [optional] 
 **inkluder** | [**list[str]**](str.md)| kommaseparert liste over hvilke informasjonselementer som skal returneres i tillegg til vegobjektenes id. | [optional] 

### Return type

[**list[Kontraktsomrade]**](Kontraktsomrade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **omrader_riksvegruter_get**
> list[Riksvegrute] omrader_riksvegruter_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match, inkluder=inkluder)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OmrderApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
if_none_match = 'if_none_match_example' # str | Dersom header matcher gjeldende E-tag vil 304 returneres (optional)
inkluder = ['inkluder_example'] # list[str] | kommaseparert liste over hvilke informasjonselementer som skal returneres i tillegg til vegobjektenes id. (optional)

try:
    api_response = api_instance.omrader_riksvegruter_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match, inkluder=inkluder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OmrderApi->omrader_riksvegruter_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **if_none_match** | **str**| Dersom header matcher gjeldende E-tag vil 304 returneres | [optional] 
 **inkluder** | [**list[str]**](str.md)| kommaseparert liste over hvilke informasjonselementer som skal returneres i tillegg til vegobjektenes id. | [optional] 

### Return type

[**list[Riksvegrute]**](Riksvegrute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

