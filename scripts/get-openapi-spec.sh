#!/bin/bash

curl -X 'GET' \
  'https://openapi.nexon.com/game/tfd/?id=21' \
  -H 'accept: application/json' \
  -H 'x-nxopen-api-key: test_1e3bf1148dd58548a6b67c5a068e989e592fdedc61c83b310eed87c6e80cf56fefe8d04e6d233bd35cf2fabdeb93fb0d' > tfd-page.html