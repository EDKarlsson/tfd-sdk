import pathlib
import yaml
import json

PROJ_DIR = pathlib.Path(".").resolve()


def get_specs(spec_glob="*.openapi.yml"):
    # return dict([(p.name.split(".")[0], p) for p in PROJ_DIR.glob("./openapi/*.openapi.yml")])
    return dict([(p.name.split(".")[0], p) for p in PROJ_DIR.glob(f"./openapi/{spec_glob}")])


def get_spec_defaults() -> dict:
    return get_specs(spec_glob="*.defaults.yml")


def to_json(yml_obj: dict) -> dict:
    return json.loads(json.dumps(yml_obj))


def main():
    specs = get_specs()
    defaults = get_spec_defaults()

    print(defaults)

    with open(specs['meta'], "rb") as yml_file:
        yml_obj: dict = yaml.safe_load(yml_file)
        tags = json_obj['tags']
        print(yml_obj.keys())

        print(json_obj.keys())
        print(tags)
        # print(yaml.dump(yml_obj))


if __name__ == "__main__":
    main()
