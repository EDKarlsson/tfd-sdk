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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from meta.models.reward_response_inner_battle_zone_inner import RewardResponseInnerBattleZoneInner
from typing import Optional, Set
from typing_extensions import Self

class RewardResponseInner(BaseModel):
    """
    RewardResponseInner
    """ # noqa: E501
    map_id: Optional[StrictStr] = Field(default=None, description="Map identifier")
    map_name: Optional[StrictStr] = Field(default=None, description="Map name")
    battle_zone: Optional[List[RewardResponseInnerBattleZoneInner]] = Field(default=None, description="Battlefield information")
    __properties: ClassVar[List[str]] = ["map_id", "map_name", "battle_zone"]

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
        """Create an instance of RewardResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in battle_zone (list)
        _items = []
        if self.battle_zone:
            for _item in self.battle_zone:
                if _item:
                    _items.append(_item.to_dict())
            _dict['battle_zone'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RewardResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "map_id": obj.get("map_id"),
            "map_name": obj.get("map_name"),
            "battle_zone": [RewardResponseInnerBattleZoneInner.from_dict(_item) for _item in obj["battle_zone"]] if obj.get("battle_zone") is not None else None
        })
        return _obj


