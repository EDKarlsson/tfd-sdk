# WeaponResponseInnerBaseStatInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stat_id** | **str** | Weapon base spec identifier (Refer to /meta/stat API) | [optional] 
**stat_value** | **float** | Weapon base spec value | [optional] 

## Example

```python
from meta_client.models.weapon_response_inner_base_stat_inner import WeaponResponseInnerBaseStatInner

# TODO update the JSON string below
json = "{}"
# create an instance of WeaponResponseInnerBaseStatInner from a JSON string
weapon_response_inner_base_stat_inner_instance = WeaponResponseInnerBaseStatInner.from_json(json)
# print the JSON string representation of the object
print(WeaponResponseInnerBaseStatInner.to_json())

# convert the object into a dict
weapon_response_inner_base_stat_inner_dict = weapon_response_inner_base_stat_inner_instance.to_dict()
# create an instance of WeaponResponseInnerBaseStatInner from a dict
weapon_response_inner_base_stat_inner_from_dict = WeaponResponseInnerBaseStatInner.from_dict(weapon_response_inner_base_stat_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


