# ModuleResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_name** | **str** | Module name | [optional] 
**module_id** | **str** | Module identifier | [optional] 
**image_url** | **str** | Module image path | [optional] 
**module_type** | **str** | Module type | [optional] 
**module_tier** | **str** | Module tier | [optional] 
**module_socket_type** | **str** | Module slot socket type | [optional] 
**module_class** | **str** | Module class | [optional] 
**module_stat** | [**List[ModuleResponseInnerModuleStatInner]**](ModuleResponseInnerModuleStatInner.md) | Module attribute information | [optional] 

## Example

```python
from meta_client.models.module_response_inner import ModuleResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleResponseInner from a JSON string
module_response_inner_instance = ModuleResponseInner.from_json(json)
# print the JSON string representation of the object
print(ModuleResponseInner.to_json())

# convert the object into a dict
module_response_inner_dict = module_response_inner_instance.to_dict()
# create an instance of ModuleResponseInner from a dict
module_response_inner_from_dict = ModuleResponseInner.from_dict(module_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


