# coding: utf-8

"""
    The First Descendant User API

    - Game data for The First Descendant becomes available after 10 minutes on average. - Please note that the OUID may change due to game content updates. Be cautious when renewing services based on the OUID. - For the interpretation of various ID values such as those for descendants, weapons, etc., please refer to the separately provided metadata API (/meta/). - Nickname must distinguish between uppercase and lowercase letters.

    The version of the OpenAPI document: 1.0.0
    Contact: help_openapi@nexon.co.kr
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from user_client.models.user_weapon import UserWeapon

class TestUserWeapon(unittest.TestCase):
    """UserWeapon unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserWeapon:
        """Test UserWeapon
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserWeapon`
        """
        model = UserWeapon()
        if include_optional:
            return UserWeapon(
                ouid = '',
                user_name = 'Nickname#1234',
                weapon = [
                    user_client.models.user_weapon_weapon_inner.UserWeapon_weapon_inner(
                        module_max_capacity = 1.337, 
                        module_capacity = 1.337, 
                        weapon_slot_id = '', 
                        weapon_id = '', 
                        weapon_level = 1.337, 
                        perk_ability_enchant_level = 1.337, 
                        weapon_additional_stat = [
                            user_client.models.user_weapon_weapon_inner_weapon_additional_stat_inner.UserWeapon_weapon_inner_weapon_additional_stat_inner(
                                additional_stat_name = '', 
                                additional_stat_value = '', )
                            ], 
                        module = [
                            user_client.models.user_descendant_module_inner.UserDescendant_module_inner(
                                module_slot_id = '', 
                                module_id = '', 
                                module_enchant_level = 1.337, )
                            ], )
                    ]
            )
        else:
            return UserWeapon(
        )
        """

    def testUserWeapon(self):
        """Test UserWeapon"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()