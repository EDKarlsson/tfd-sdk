# coding: utf-8

"""
    The First Descendant Metadata API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from meta_client.models.reward_response_inner_battle_zone_inner_reward_inner import RewardResponseInnerBattleZoneInnerRewardInner

class TestRewardResponseInnerBattleZoneInnerRewardInner(unittest.TestCase):
    """RewardResponseInnerBattleZoneInnerRewardInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RewardResponseInnerBattleZoneInnerRewardInner:
        """Test RewardResponseInnerBattleZoneInnerRewardInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RewardResponseInnerBattleZoneInnerRewardInner`
        """
        model = RewardResponseInnerBattleZoneInnerRewardInner()
        if include_optional:
            return RewardResponseInnerBattleZoneInnerRewardInner(
                rotation = 1.337,
                reward_type = '',
                reactor_element_type = '',
                weapon_rounds_type = '',
                arche_type = ''
            )
        else:
            return RewardResponseInnerBattleZoneInnerRewardInner(
        )
        """

    def testRewardResponseInnerBattleZoneInnerRewardInner(self):
        """Test RewardResponseInnerBattleZoneInnerRewardInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
