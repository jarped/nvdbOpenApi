# swagger_client.DatakatalogApi

All URIs are relative to *https://nvdbapiles-v3.atlas.vegvesen.no*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_get**](DatakatalogApi.md#status_get) | **GET** /status | 
[**vegobjekttyper_datatyper_get**](DatakatalogApi.md#vegobjekttyper_datatyper_get) | **GET** /vegobjekttyper/datatyper | 
[**vegobjekttyper_egenskapstypekategorier_get**](DatakatalogApi.md#vegobjekttyper_egenskapstypekategorier_get) | **GET** /vegobjekttyper/egenskapstypekategorier | 
[**vegobjekttyper_enheter_get**](DatakatalogApi.md#vegobjekttyper_enheter_get) | **GET** /vegobjekttyper/enheter | 
[**vegobjekttyper_get**](DatakatalogApi.md#vegobjekttyper_get) | **GET** /vegobjekttyper | 
[**vegobjekttyper_kategorier_get**](DatakatalogApi.md#vegobjekttyper_kategorier_get) | **GET** /vegobjekttyper/kategorier | 
[**vegobjekttyper_vegobjekttypeid_get**](DatakatalogApi.md#vegobjekttyper_vegobjekttypeid_get) | **GET** /vegobjekttyper/{vegobjekttypeid} | 
[**vegobjekttyper_version_get**](DatakatalogApi.md#vegobjekttyper_version_get) | **GET** /vegobjekttyper/version | 

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
api_instance = swagger_client.DatakatalogApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)

try:
    api_response = api_instance.status_get(x_client, x_client_session=x_client_session)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatakatalogApi->status_get: %s\n" % e)
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

# **vegobjekttyper_datatyper_get**
> list[InlineResponse2002] vegobjekttyper_datatyper_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatakatalogApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
if_none_match = 'if_none_match_example' # str | Dersom header matcher gjeldende E-tag vil 304 returneres (optional)

try:
    api_response = api_instance.vegobjekttyper_datatyper_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatakatalogApi->vegobjekttyper_datatyper_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **if_none_match** | **str**| Dersom header matcher gjeldende E-tag vil 304 returneres | [optional] 

### Return type

[**list[InlineResponse2002]**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegobjekttyper_egenskapstypekategorier_get**
> list[InlineResponse2005] vegobjekttyper_egenskapstypekategorier_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatakatalogApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
if_none_match = 'if_none_match_example' # str | Dersom header matcher gjeldende E-tag vil 304 returneres (optional)

try:
    api_response = api_instance.vegobjekttyper_egenskapstypekategorier_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatakatalogApi->vegobjekttyper_egenskapstypekategorier_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **if_none_match** | **str**| Dersom header matcher gjeldende E-tag vil 304 returneres | [optional] 

### Return type

[**list[InlineResponse2005]**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegobjekttyper_enheter_get**
> list[InlineResponse2001] vegobjekttyper_enheter_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatakatalogApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
if_none_match = 'if_none_match_example' # str | Dersom header matcher gjeldende E-tag vil 304 returneres (optional)

try:
    api_response = api_instance.vegobjekttyper_enheter_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatakatalogApi->vegobjekttyper_enheter_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **if_none_match** | **str**| Dersom header matcher gjeldende E-tag vil 304 returneres | [optional] 

### Return type

[**list[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegobjekttyper_get**
> list[Vegobjekttype] vegobjekttyper_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match, inkluder=inkluder, kategori=kategori)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatakatalogApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
if_none_match = 'if_none_match_example' # str | Dersom header matcher gjeldende E-tag vil 304 returneres (optional)
inkluder = 'alle' # str | Angir hvilke informasjonsfelter som skal inkluderes i tillegg til vegobjekttypenes metadata. (optional) (default to alle)
kategori = 56 # int | Begrens vegobjekttyper etter kategori. (/vegobjekttyper/kategorier) (optional)

try:
    api_response = api_instance.vegobjekttyper_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match, inkluder=inkluder, kategori=kategori)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatakatalogApi->vegobjekttyper_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **if_none_match** | **str**| Dersom header matcher gjeldende E-tag vil 304 returneres | [optional] 
 **inkluder** | **str**| Angir hvilke informasjonsfelter som skal inkluderes i tillegg til vegobjekttypenes metadata. | [optional] [default to alle]
 **kategori** | **int**| Begrens vegobjekttyper etter kategori. (/vegobjekttyper/kategorier) | [optional] 

### Return type

[**list[Vegobjekttype]**](Vegobjekttype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegobjekttyper_kategorier_get**
> list[InlineResponse2003] vegobjekttyper_kategorier_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatakatalogApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
if_none_match = 'if_none_match_example' # str | Dersom header matcher gjeldende E-tag vil 304 returneres (optional)

try:
    api_response = api_instance.vegobjekttyper_kategorier_get(x_client, x_client_session=x_client_session, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatakatalogApi->vegobjekttyper_kategorier_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **if_none_match** | **str**| Dersom header matcher gjeldende E-tag vil 304 returneres | [optional] 

### Return type

[**list[InlineResponse2003]**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegobjekttyper_vegobjekttypeid_get**
> list[Vegobjekttype] vegobjekttyper_vegobjekttypeid_get(vegobjekttypeid, x_client, x_client_session=x_client_session, if_none_match=if_none_match, inkluder=inkluder, kategori=kategori)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatakatalogApi()
vegobjekttypeid = 56 # int | 
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)
if_none_match = 'if_none_match_example' # str | Dersom header matcher gjeldende E-tag vil 304 returneres (optional)
inkluder = 'alle' # str | Angir hvilke informasjonsfelter som skal inkluderes i tillegg til vegobjekttypenes metadata. (optional) (default to alle)
kategori = 56 # int | Begrens vegobjekttyper etter kategori. (/vegobjekttyper/kategorier) (optional)

try:
    api_response = api_instance.vegobjekttyper_vegobjekttypeid_get(vegobjekttypeid, x_client, x_client_session=x_client_session, if_none_match=if_none_match, inkluder=inkluder, kategori=kategori)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatakatalogApi->vegobjekttyper_vegobjekttypeid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vegobjekttypeid** | **int**|  | 
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 
 **if_none_match** | **str**| Dersom header matcher gjeldende E-tag vil 304 returneres | [optional] 
 **inkluder** | **str**| Angir hvilke informasjonsfelter som skal inkluderes i tillegg til vegobjekttypenes metadata. | [optional] [default to alle]
 **kategori** | **int**| Begrens vegobjekttyper etter kategori. (/vegobjekttyper/kategorier) | [optional] 

### Return type

[**list[Vegobjekttype]**](Vegobjekttype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vegobjekttyper_version_get**
> InlineResponse2004 vegobjekttyper_version_get(x_client, x_client_session=x_client_session)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatakatalogApi()
x_client = 'x_client_example' # str | Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes.
x_client_session = 'x_client_session_example' # str | Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) (optional)

try:
    api_response = api_instance.vegobjekttyper_version_get(x_client, x_client_session=x_client_session)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatakatalogApi->vegobjekttyper_version_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_client** | **str**| Noe som identifiserer klienten eller fagsystemet. Eksempler: «Vegkart», «NVDB Skrive-API». Må settes dersom User-Agent ikke er satt. X-Client foretrekkes. | 
 **x_client_session** | **str**| Settes for å identifisere en samling med requester, for eksempel en brukersesjon. (bruk i såfall en uuid eller noe lignende, ikke brukernavn eller epost) | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vegvesen.nvdb-v3-rev1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

