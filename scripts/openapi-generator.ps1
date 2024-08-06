docker run --rm -v "$([System.Environment]::CurrentDirectory)\spec:/local" -v "$([System.Environment]::CurrentDirectory)\out:/local/out" openapitools/openapi-generator-cli generate -i "/local/tfd_meta_22_en_script20240725041303.yaml" -g python -o "/local/out/python/tfd/meta" --package-name "tfd_meta_api"
docker run --rm -v "$([System.Environment]::CurrentDirectory)\spec:/local" -v "$([System.Environment]::CurrentDirectory)\out:/local/out" openapitools/openapi-generator-cli generate -i "/local/tfd_account_info_20_en_script20240701043611.yaml" -g python -o "/local/out/python/tfd/account" --package-name "tfd_account_api"
docker run --rm -v "$([System.Environment]::CurrentDirectory)\spec:/local" -v "$([System.Environment]::CurrentDirectory)\out:/local/out" openapitools/openapi-generator-cli generate -i "/local/tfd_module_rec_24_en_script20240703235909.yaml" -g python -o "/local/out/python/tfd/module" --package-name "tfd_module_api"


# Should create something more dynamic and clean solution for getting the file names but meh since I don't dev on windows often

# function Test-Generate {
#     $dockerString = @"
# docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
#         -i https://raw.githubusercontent.com/openapitools/openapi-generator/master/modules/openapi-generator/src/test/resources/3_0/petstore.yaml \
#         -g go \
#         -o /local/out/go
# "@
#     Write-Host $dockerString
#     Write-Host $pwd | Select-Object -ExpandProperty Path
#     $currentDir = ([System.Environment]::CurrentDirectory)
#     Write-Host $currentDir
# }

# function Generate {

#     # [CmdLetBinding()]
#     # param (
#     #     $schema,
#     #     $language,
#     #     $output
#     # )
#     $currentDir = ([System.Environment]::CurrentDirectory)
#     Write-Host $currentDir
#    Start-Process -FilePath  "C:\Program Files\Docker\Docker\resources\bin\docker.exe" -ArgumentList "run --rm -v ${currentDir}:/local openapitools/openapi-generator-cli generate -i ${currentDir}/spec/tfd_meta_22_en_script20240725041303.yaml -g python -o ${currentDir}/out/python/tdf/meta"
# }

# # Test-Generate
# Generate