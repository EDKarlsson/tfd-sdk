# coding: utf-8

"""
    The First Descendant Metadata API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from meta_client.models.reactor_response_inner_reactor_skill_power_inner_skill_power_coefficient_inner import ReactorResponseInnerReactorSkillPowerInnerSkillPowerCoefficientInner

class TestReactorResponseInnerReactorSkillPowerInnerSkillPowerCoefficientInner(unittest.TestCase):
    """ReactorResponseInnerReactorSkillPowerInnerSkillPowerCoefficientInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReactorResponseInnerReactorSkillPowerInnerSkillPowerCoefficientInner:
        """Test ReactorResponseInnerReactorSkillPowerInnerSkillPowerCoefficientInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReactorResponseInnerReactorSkillPowerInnerSkillPowerCoefficientInner`
        """
        model = ReactorResponseInnerReactorSkillPowerInnerSkillPowerCoefficientInner()
        if include_optional:
            return ReactorResponseInnerReactorSkillPowerInnerSkillPowerCoefficientInner(
                coefficient_stat_id = '',
                coefficient_stat_value = 1.337
            )
        else:
            return ReactorResponseInnerReactorSkillPowerInnerSkillPowerCoefficientInner(
        )
        """

    def testReactorResponseInnerReactorSkillPowerInnerSkillPowerCoefficientInner(self):
        """Test ReactorResponseInnerReactorSkillPowerInnerSkillPowerCoefficientInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()