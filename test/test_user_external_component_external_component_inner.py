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

from user_client.models.user_external_component_external_component_inner import UserExternalComponentExternalComponentInner

class TestUserExternalComponentExternalComponentInner(unittest.TestCase):
    """UserExternalComponentExternalComponentInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserExternalComponentExternalComponentInner:
        """Test UserExternalComponentExternalComponentInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserExternalComponentExternalComponentInner`
        """
        model = UserExternalComponentExternalComponentInner()
        if include_optional:
            return UserExternalComponentExternalComponentInner(
                external_component_slot_id = '',
                external_component_id = '',
                external_component_level = 1.337,
                external_component_additional_stat = [
                    user_client.models.user_external_component_external_component_inner_external_component_additional_stat_inner.UserExternalComponent_external_component_inner_external_component_additional_stat_inner(
                        additional_stat_name = '', 
                        additional_stat_value = '', )
                    ]
            )
        else:
            return UserExternalComponentExternalComponentInner(
        )
        """

    def testUserExternalComponentExternalComponentInner(self):
        """Test UserExternalComponentExternalComponentInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
