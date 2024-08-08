# coding: utf-8

"""
    The First Descendant API SDK

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "tfd-sdk"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.11"
REQUIRES = [
    "pydantic >= 2.8.2",
    "python-dateutil >= 2.8.2",
    "pyyaml >= 6.0.2",
    "typing-extensions >= 4.7.1",
    "urllib3 >= 1.25.3, < 2.1.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="The First Descendant SDK",
    author="Dan Karlsson",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "The First Descendant API SDK"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
    """,  # noqa: E501
    package_data={"meta_client": ["py.typed"]},
)
