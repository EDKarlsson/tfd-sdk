# coding: utf-8

"""
    The First Descendant User API

    - Game data for The First Descendant becomes available after 10 minutes on average. - Please note that the OUID may change due to game content updates. Be cautious when renewing services based on the OUID. - For the interpretation of various ID values such as those for descendants, weapons, etc., please refer to the separately provided metadata API (/meta/). - Nickname must distinguish between uppercase and lowercase letters.

    The version of the OpenAPI document: 1.0.0
    Contact: help_openapi@nexon.co.kr
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UserWeaponWeaponInnerWeaponAdditionalStatInner(BaseModel):
    """
    UserWeaponWeaponInnerWeaponAdditionalStatInner
    """ # noqa: E501
    additional_stat_name: Optional[StrictStr] = Field(default=None, description="Weapon random option name")
    additional_stat_value: Optional[StrictStr] = Field(default=None, description="Weapon random option value")
    __properties: ClassVar[List[str]] = ["additional_stat_name", "additional_stat_value"]

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
        """Create an instance of UserWeaponWeaponInnerWeaponAdditionalStatInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserWeaponWeaponInnerWeaponAdditionalStatInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "additional_stat_name": obj.get("additional_stat_name"),
            "additional_stat_value": obj.get("additional_stat_value")
        })
        return _obj


