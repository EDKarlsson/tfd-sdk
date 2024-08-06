#!/bin/bash

curl -X 'GET' \
  'https://openapi.nexon.com/game/tfd/?id=21' \
  -H 'accept: application/json' \
  -H "x-nxopen-api-key: $NEXON_API_KEY" > tfd-page.html

