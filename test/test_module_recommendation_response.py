# coding: utf-8

"""
    The First Descendant Module Recommendation API

    - Game data for The First Descendant becomes available after 10 minutes on average. - Please note that the OUID may change due to game content updates. Be cautious when renewing services based on the OUID. - For the interpretation of various ID values such as those for descendants, weapons, etc., please refer to the separately provided metadata API (/meta/). - Recommended modules are provided based on the successful records of Void Intercept Battles. Therefore, if there are insufficient records matching the search criteria, the query responses may be empty.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from recommendation_client.models.module_recommendation_response import ModuleRecommendationResponse

class TestModuleRecommendationResponse(unittest.TestCase):
    """ModuleRecommendationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModuleRecommendationResponse:
        """Test ModuleRecommendationResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModuleRecommendationResponse`
        """
        model = ModuleRecommendationResponse()
        if include_optional:
            return ModuleRecommendationResponse(
                descendant = recommendation_client.models.module_recommendation_response_descendant.ModuleRecommendationResponse_descendant(
                    descendant_id = '', 
                    recommendation = [
                        recommendation_client.models.module_recommendation_response_descendant_recommendation_inner.ModuleRecommendationResponse_descendant_recommendation_inner(
                            module_id = '', )
                        ], ),
                weapon = recommendation_client.models.module_recommendation_response_weapon.ModuleRecommendationResponse_weapon(
                    weapon_id = '', 
                    recommendation = [
                        recommendation_client.models.module_recommendation_response_descendant_recommendation_inner.ModuleRecommendationResponse_descendant_recommendation_inner(
                            module_id = '', )
                        ], )
            )
        else:
            return ModuleRecommendationResponse(
        )
        """

    def testModuleRecommendationResponse(self):
        """Test ModuleRecommendationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()