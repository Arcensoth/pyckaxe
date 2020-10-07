import json
from pathlib import Path

try:
    import yaml

    YAML_INSTALLED = True
except:
    YAML_INSTALLED = False


class NoSuchResourceError(Exception):
    def __init__(self, path: Path):
        super().__init__(f"Unable to find resource: {path}")
        self.path: Path = path


class UnsupportedResourceExtensionError(Exception):
    def __init__(self, path: Path):
        super().__init__(f"Unsupported file extension for resource: {path}")
        self.path: Path = path


class YamlNotInstalledError(Exception):
    def __init__(self, path: Path):
        super().__init__(f"PyYAML must be installed to load YAML resource: {path}")
        self.path: Path = path


async def get_matching_paths(partial_path: Path) -> Path:
    matching_paths = list(partial_path.parent.glob(f"{partial_path.name}.*"))
    if len(matching_paths) > 0:
        return matching_paths[0]
    raise NoSuchResourceError(partial_path)


async def load_raw_resource(partial_path: Path) -> str:
    path = await get_matching_paths(partial_path)
    with open(path, "r") as fp:
        return fp.read()


async def load_dict_resource(partial_path: Path) -> dict:
    path = await get_matching_paths(partial_path)
    if path.suffix == ".json":
        with open(path, "r") as fp:
            return json.load(fp)
    elif path.suffix in (".yaml", ".yml"):
        if YAML_INSTALLED:
            with open(path, "r") as fp:
                return yaml.safe_load(fp)
        else:
            raise YamlNotInstalledError(path)
    else:
        raise UnsupportedResourceExtensionError(path)
