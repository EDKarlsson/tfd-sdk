# coding: utf-8

"""
    The First Descendant Metadata API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from meta.models.weapon_response_inner_firearm_atk_inner_firearm_inner import WeaponResponseInnerFirearmAtkInnerFirearmInner
from typing import Optional, Set
from typing_extensions import Self

class WeaponResponseInnerFirearmAtkInner(BaseModel):
    """
    WeaponResponseInnerFirearmAtkInner
    """ # noqa: E501
    level: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Firearm level")
    firearm: Optional[List[WeaponResponseInnerFirearmAtkInnerFirearmInner]] = Field(default=None, description="Firearm ATK")
    __properties: ClassVar[List[str]] = ["level", "firearm"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WeaponResponseInnerFirearmAtkInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in firearm (list)
        _items = []
        if self.firearm:
            for _item in self.firearm:
                if _item:
                    _items.append(_item.to_dict())
            _dict['firearm'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WeaponResponseInnerFirearmAtkInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "level": obj.get("level"),
            "firearm": [WeaponResponseInnerFirearmAtkInnerFirearmInner.from_dict(_item) for _item in obj["firearm"]] if obj.get("firearm") is not None else None
        })
        return _obj


