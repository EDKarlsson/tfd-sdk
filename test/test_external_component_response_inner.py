# coding: utf-8

"""
    The First Descendant Metadata API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from meta_client.models.external_component_response_inner import ExternalComponentResponseInner

class TestExternalComponentResponseInner(unittest.TestCase):
    """ExternalComponentResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExternalComponentResponseInner:
        """Test ExternalComponentResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExternalComponentResponseInner`
        """
        model = ExternalComponentResponseInner()
        if include_optional:
            return ExternalComponentResponseInner(
                external_component_id = '',
                external_component_name = '',
                image_url = '',
                external_component_equipment_type = '',
                external_component_tier = '',
                base_stat = [
                    meta_client.models.external_component_response_inner_base_stat_inner.ExternalComponentResponse_inner_base_stat_inner(
                        level = 1.337, 
                        stat_id = '', 
                        stat_value = 1.337, )
                    ],
                set_option_detail = [
                    meta_client.models.external_component_response_inner_set_option_detail_inner.ExternalComponentResponse_inner_set_option_detail_inner(
                        set_option = '', 
                        set_count = 1.337, 
                        set_option_effect = '', )
                    ]
            )
        else:
            return ExternalComponentResponseInner(
        )
        """

    def testExternalComponentResponseInner(self):
        """Test ExternalComponentResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
