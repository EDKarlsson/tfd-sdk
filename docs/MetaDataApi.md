# meta_client.MetaDataApi

All URIs are relative to *https://open.api.nexon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**static_tfd_meta_language_code_descendant_json_get**](MetaDataApi.md#static_tfd_meta_language_code_descendant_json_get) | **GET** /static/tfd/meta/{language_code}/descendant.json | Retrieve descendant metadata
[**static_tfd_meta_language_code_external_component_json_get**](MetaDataApi.md#static_tfd_meta_language_code_external_component_json_get) | **GET** /static/tfd/meta/{language_code}/external-component.json | Retrieve external component metadata
[**static_tfd_meta_language_code_module_json_get**](MetaDataApi.md#static_tfd_meta_language_code_module_json_get) | **GET** /static/tfd/meta/{language_code}/module.json | Retrieve module metadata
[**static_tfd_meta_language_code_reactor_json_get**](MetaDataApi.md#static_tfd_meta_language_code_reactor_json_get) | **GET** /static/tfd/meta/{language_code}/reactor.json | Retrieve Reactor metadata
[**static_tfd_meta_language_code_reward_json_get**](MetaDataApi.md#static_tfd_meta_language_code_reward_json_get) | **GET** /static/tfd/meta/{language_code}/reward.json | Retrieve Difficulty Level Rewards metadata
[**static_tfd_meta_language_code_stat_json_get**](MetaDataApi.md#static_tfd_meta_language_code_stat_json_get) | **GET** /static/tfd/meta/{language_code}/stat.json | Retrieve base stat metadata
[**static_tfd_meta_language_code_title_json_get**](MetaDataApi.md#static_tfd_meta_language_code_title_json_get) | **GET** /static/tfd/meta/{language_code}/title.json | Retrieve Title metadata
[**static_tfd_meta_language_code_void_battle_json_get**](MetaDataApi.md#static_tfd_meta_language_code_void_battle_json_get) | **GET** /static/tfd/meta/{language_code}/void-battle.json | Retrieve Void Intercept Battle metadata
[**static_tfd_meta_language_code_weapon_json_get**](MetaDataApi.md#static_tfd_meta_language_code_weapon_json_get) | **GET** /static/tfd/meta/{language_code}/weapon.json | Retrieve weapon metadata


# **static_tfd_meta_language_code_descendant_json_get**
> List[DescendantResponseInner] static_tfd_meta_language_code_descendant_json_get(language_code)

Retrieve descendant metadata

Retrieves descendant metadata.

### Example


```python
import meta_client
from meta_client.models.descendant_response_inner import DescendantResponseInner
from meta_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open.api.nexon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meta_client.Configuration(
    host = "https://open.api.nexon.com"
)


# Enter a context with an instance of the API client
with meta_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_client.MetaDataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve descendant metadata
        api_response = api_instance.static_tfd_meta_language_code_descendant_json_get(language_code)
        print("The response of MetaDataApi->static_tfd_meta_language_code_descendant_json_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaDataApi->static_tfd_meta_language_code_descendant_json_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[DescendantResponseInner]**](DescendantResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SUCCESS |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **static_tfd_meta_language_code_external_component_json_get**
> List[ExternalComponentResponseInner] static_tfd_meta_language_code_external_component_json_get(language_code)

Retrieve external component metadata

Retrieves external component metadata.</br> This API only provides path information. You can check it via a separate client.

### Example


```python
import meta_client
from meta_client.models.external_component_response_inner import ExternalComponentResponseInner
from meta_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open.api.nexon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meta_client.Configuration(
    host = "https://open.api.nexon.com"
)


# Enter a context with an instance of the API client
with meta_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_client.MetaDataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve external component metadata
        api_response = api_instance.static_tfd_meta_language_code_external_component_json_get(language_code)
        print("The response of MetaDataApi->static_tfd_meta_language_code_external_component_json_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaDataApi->static_tfd_meta_language_code_external_component_json_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[ExternalComponentResponseInner]**](ExternalComponentResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SUCCESS |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **static_tfd_meta_language_code_module_json_get**
> List[ModuleResponseInner] static_tfd_meta_language_code_module_json_get(language_code)

Retrieve module metadata

Retrieves module metadata.

### Example


```python
import meta_client
from meta_client.models.module_response_inner import ModuleResponseInner
from meta_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open.api.nexon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meta_client.Configuration(
    host = "https://open.api.nexon.com"
)


# Enter a context with an instance of the API client
with meta_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_client.MetaDataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve module metadata
        api_response = api_instance.static_tfd_meta_language_code_module_json_get(language_code)
        print("The response of MetaDataApi->static_tfd_meta_language_code_module_json_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaDataApi->static_tfd_meta_language_code_module_json_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[ModuleResponseInner]**](ModuleResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SUCCESS |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **static_tfd_meta_language_code_reactor_json_get**
> List[ReactorResponseInner] static_tfd_meta_language_code_reactor_json_get(language_code)

Retrieve Reactor metadata

Retrieves Reactor metadata.<br> This API only provides path information. You can check it via a separate client.

### Example


```python
import meta_client
from meta_client.models.reactor_response_inner import ReactorResponseInner
from meta_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open.api.nexon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meta_client.Configuration(
    host = "https://open.api.nexon.com"
)


# Enter a context with an instance of the API client
with meta_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_client.MetaDataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve Reactor metadata
        api_response = api_instance.static_tfd_meta_language_code_reactor_json_get(language_code)
        print("The response of MetaDataApi->static_tfd_meta_language_code_reactor_json_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaDataApi->static_tfd_meta_language_code_reactor_json_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[ReactorResponseInner]**](ReactorResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SUCCESS |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **static_tfd_meta_language_code_reward_json_get**
> List[RewardResponseInner] static_tfd_meta_language_code_reward_json_get(language_code)

Retrieve Difficulty Level Rewards metadata

Retrieves Difficulty Level Rewards metadata.

### Example


```python
import meta_client
from meta_client.models.reward_response_inner import RewardResponseInner
from meta_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open.api.nexon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meta_client.Configuration(
    host = "https://open.api.nexon.com"
)


# Enter a context with an instance of the API client
with meta_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_client.MetaDataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve Difficulty Level Rewards metadata
        api_response = api_instance.static_tfd_meta_language_code_reward_json_get(language_code)
        print("The response of MetaDataApi->static_tfd_meta_language_code_reward_json_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaDataApi->static_tfd_meta_language_code_reward_json_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[RewardResponseInner]**](RewardResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SUCCESS |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **static_tfd_meta_language_code_stat_json_get**
> List[StatResponseInner] static_tfd_meta_language_code_stat_json_get(language_code)

Retrieve base stat metadata

Retrieves base stat metadata.

### Example


```python
import meta_client
from meta_client.models.stat_response_inner import StatResponseInner
from meta_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open.api.nexon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meta_client.Configuration(
    host = "https://open.api.nexon.com"
)


# Enter a context with an instance of the API client
with meta_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_client.MetaDataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve base stat metadata
        api_response = api_instance.static_tfd_meta_language_code_stat_json_get(language_code)
        print("The response of MetaDataApi->static_tfd_meta_language_code_stat_json_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaDataApi->static_tfd_meta_language_code_stat_json_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[StatResponseInner]**](StatResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SUCCESS |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **static_tfd_meta_language_code_title_json_get**
> List[TitleResponseInner] static_tfd_meta_language_code_title_json_get(language_code)

Retrieve Title metadata

Retrieves Title metadata.

### Example


```python
import meta_client
from meta_client.models.title_response_inner import TitleResponseInner
from meta_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open.api.nexon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meta_client.Configuration(
    host = "https://open.api.nexon.com"
)


# Enter a context with an instance of the API client
with meta_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_client.MetaDataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve Title metadata
        api_response = api_instance.static_tfd_meta_language_code_title_json_get(language_code)
        print("The response of MetaDataApi->static_tfd_meta_language_code_title_json_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaDataApi->static_tfd_meta_language_code_title_json_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[TitleResponseInner]**](TitleResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SUCCESS |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **static_tfd_meta_language_code_void_battle_json_get**
> List[VoidBattleResponseInner] static_tfd_meta_language_code_void_battle_json_get(language_code)

Retrieve Void Intercept Battle metadata

Retrieves Void Intercept Battle metadata.

### Example


```python
import meta_client
from meta_client.models.void_battle_response_inner import VoidBattleResponseInner
from meta_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open.api.nexon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meta_client.Configuration(
    host = "https://open.api.nexon.com"
)


# Enter a context with an instance of the API client
with meta_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_client.MetaDataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve Void Intercept Battle metadata
        api_response = api_instance.static_tfd_meta_language_code_void_battle_json_get(language_code)
        print("The response of MetaDataApi->static_tfd_meta_language_code_void_battle_json_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaDataApi->static_tfd_meta_language_code_void_battle_json_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[VoidBattleResponseInner]**](VoidBattleResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SUCCESS |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **static_tfd_meta_language_code_weapon_json_get**
> List[WeaponResponseInner] static_tfd_meta_language_code_weapon_json_get(language_code)

Retrieve weapon metadata

Retrieves weapon metadata.<br> This API only provides path information. You can check it via a separate client.

### Example


```python
import meta_client
from meta_client.models.weapon_response_inner import WeaponResponseInner
from meta_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open.api.nexon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meta_client.Configuration(
    host = "https://open.api.nexon.com"
)


# Enter a context with an instance of the API client
with meta_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_client.MetaDataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve weapon metadata
        api_response = api_instance.static_tfd_meta_language_code_weapon_json_get(language_code)
        print("The response of MetaDataApi->static_tfd_meta_language_code_weapon_json_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaDataApi->static_tfd_meta_language_code_weapon_json_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[WeaponResponseInner]**](WeaponResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SUCCESS |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

