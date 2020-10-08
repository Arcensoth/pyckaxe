import json
from pathlib import Path

try:
    import yaml

    YAML_INSTALLED = True
except:
    YAML_INSTALLED = False


class NoSuchResourceError(Exception):
    def __init__(self, partial_path: Path):
        super().__init__(f"Unable to find resource matching partial path: {partial_path}")
        self.partial_path: Path = partial_path


class DuplicateResourceError(Exception):
    def __init__(self, partial_path: Path):
        super().__init__(f"Encountered duplicate resources matching partial path: {partial_path}")
        self.partial_path: Path = partial_path


class UnsupportedResourceExtensionError(Exception):
    def __init__(self, path: Path):
        super().__init__(f"Unsupported file extension for resource at: {path}")
        self.path: Path = path


class YamlNotInstalledError(Exception):
    def __init__(self, path: Path):
        super().__init__(f"PyYAML must be installed to load YAML resource at: {path}")
        self.path: Path = path


async def get_resource_path(partial_path: Path) -> Path:
    matching_paths = list(partial_path.parent.glob(f"{partial_path.name}.*"))
    if len(matching_paths) <= 0:
        raise NoSuchResourceError(partial_path)
    if len(matching_paths) > 1:
        raise DuplicateResourceError(partial_path)
    return matching_paths[0]


async def load_raw_resource(partial_path: Path) -> str:
    path = await get_resource_path(partial_path)
    with open(path, "r") as fp:
        return fp.read()


async def load_dict_resource(partial_path: Path) -> dict:
    path = await get_resource_path(partial_path)
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
