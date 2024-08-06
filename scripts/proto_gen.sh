#!/bin/bash

specs=(meta account module)
spec_dir=${PWD}/spec

for spec in "${specs[@]}"
do
  yml_file=$(find "$spec_dir" -name "*$spec*" -exec basename {} \;)
  echo " - $spec: $yml_file"
  protobuf_path="./out/protobuf/tfd/${spec}"

  # generate api sdk
  openapi-generator generate -i "${spec_dir}/${yml_file}" -g protobuf-schema -o "$protobuf_path" --package-name "tfd_${spec}_proto"
done
