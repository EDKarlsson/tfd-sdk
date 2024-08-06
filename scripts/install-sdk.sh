#!/bin/bash

specs=(meta account module)
spec_dir=${PWD}/spec

# default
command=
pkg_owner=tfd
output_dir=${PWD}/out
lang=python
dry=
verbose=

# for arg in "$@"
while [ -n "$1" ]; do
  case "$1" in
  -p|--package)
    pkg_owner="$2"
    ;;
  -o|--out)
    output_dir="$2"
    ;;
  -l|--language)
    lang="$2"
    ;;
  --dry)
    dry=true
    ;;
  -v|--verbose)
    verbose=true
    ;;
  generate|install)
    command=$1
    ;;
  esac
  shift
done


if [[ $verbose ]]; then
    echo " - output     = ${output_dir}"
    echo " - command    = ${command}"
    echo " - pkg_owner  = ${pkg_owner}"
    echo " - output_dir = ${output_dir}"
    echo " - language   = ${language}"
    echo " - dry        = ${dry}"
fi

if [[ "$dry" == true ]] ; then
    printf -- '-%.0s' {1..133}
    printf '\n'
    printf ' > dry: '
    printf ' %-10s | ' "spec"
    printf ' %-50s | ' "yml_file"
    printf ' %-30s | ' "sdk_path"
    printf ' %-20s |\n' "pkg_name"
    printf -- '-%.0s' {1..133}
    printf '\n'
fi

for spec in "${specs[@]}"
do
  yml_file=$(find "$spec_dir" -name "*$spec*" -exec basename {} \;)

  sdk_path="${output_dir}/${language}/${pkg_owner}/${spec}"
  pkg_name=${pkg_owner}_${spec}_client

  if [[ $command == "generate" ]]; then
    # generate api sdk
    openapi-generator generate -i "${spec_dir}/${yml_file}" -g "${lang}" -o "$sdk_path" --package-name "${pkg_name}"
  elif [[ $command == "install" ]]; then

    # fix authors field
    toml_file="${sdk_path}/pyproject.toml"
    if [ -f $toml_file ]; then
      sed -i -E 's/help_openapi@nexon/Nexon/' $toml_file 
    fi

    # pushd "$sdk_path" && poetry install && popd
    pushd "$sdk_path" && python setup.py install --user && popd

  elif [[ "$dry" == true ]] ; then
    printf ' > dry: '
    printf ' %-10s | ' "$spec"
    printf ' %-50s | ' "$yml_file"
    printf ' %-30s | ' "$sdk_path"
    printf ' %-20s |\n' "$pkg_name"
  else
    echo "No command specified"
  fi
done
