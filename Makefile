#NEXON_PYTHON_CLIENTS:=tfd_sdk/clients/python
ROOT_DIR=.

SCRIPTS=$(ROOT_DIR)/scripts
OPENAPI_SCHEMAS=$(shell find openapi -name '*openapi.yml' -print)

SDK_CLIENTS:=tfd_sdk/clients
#PYTHON_CLIENTS:=$(dir $(shell find tfd_sdk -name 'pyproject.toml' -print))
PYTHON_CLIENTS:=$(dir $(shell find tfd_sdk -name 'tfd_clients' -type d -print))

OPENAPI_GENERATE:=$(shell find $(SCRIPTS) -name openapi-generate.sh -print)


.PHONY: openapi-python-client
openapi-python-client: $(OPENAPI_SCHEMAS)
	@echo 'Schemas: ' $(OPENAPI_SCHEMAS)
	@echo 'OpenAPI Generate: ' $(OPENAPI_GENERATE)
	$(OPENAPI_GENERATE) generate

.PHONY: clean
clean: clean-python-sdk

.PHONY: clean-python-sdk
clean-python-sdk: $(PYTHON_CLIENTS)
	rm -r $(PYTHON_CLIENTS)