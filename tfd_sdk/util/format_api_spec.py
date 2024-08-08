import pathlib
from pathlib import Path

import yaml
import json

PROJ_DIR = pathlib.Path(".").resolve()


def get_specs(spec_glob="*.openapi.yml") -> dict[str, Path]:
    return dict(
        [(p.name.split(".")[0], p) for p in PROJ_DIR.glob(f"./openapi/{spec_glob}")]
    )


def get_spec_defaults() -> dict[str, Path]:
    return {"defaults": get_specs(spec_glob="*.defaults.yml").pop("openapi")}
    # return get_specs(spec_glob="*.defaults.yml")


def to_json(yml_obj: dict) -> dict:
    return json.loads(json.dumps(yml_obj))


def print_specs(specs: dict) -> None:
    print("Specs:")
    for k, v in specs.items():
        print(f"\t{k}: {v}")


def main():
    specs = get_specs()
    defaults = get_spec_defaults()

    print_specs(specs)
    print_specs(defaults)

    with open(defaults["defaults"], "rb") as defaults_file:
        defaults_dict: dict = yaml.safe_load(defaults_file)

    with open(specs["meta"], "rb") as yml_file:
        yml_obj: dict = yaml.safe_load(yml_file)


if __name__ == "__main__":
    main()
