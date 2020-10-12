import json
from pathlib import Path

try:
    import yaml

    YAML_INSTALLED = True
except:
    YAML_INSTALLED = False


class ResourceError(Exception):
    def __init__(self, path: Path, message: str):
        super().__init__(message)
        self.path: Path = path


class NoSuchResourceError(ResourceError):
    def __init__(self, partial_path: Path):
        super().__init__(
            partial_path, f"Unable to find resource matching partial path: {partial_path}"
        )


class DuplicateResourceError(ResourceError):
    def __init__(self, partial_path: Path):
        super().__init__(
            partial_path, f"Encountered duplicate resources matching partial path: {partial_path}"
        )


class UnsupportedResourceExtensionError(ResourceError):
    def __init__(self, path: Path):
        super().__init__(path, f"Unsupported file extension for resource at: {path}")


class YamlNotInstalledError(ResourceError):
    def __init__(self, path: Path):
        super().__init__(path, f"PyYAML must be installed to load YAML resource at: {path}")


class MalformedResourceError(ResourceError):
    def __init__(self, path: Path, cause: Exception):
        super().__init__(path, f"Failed to load malformed resource at {path} due to: {cause}")
        self.cause: Exception = cause


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
            try:
                return json.load(fp)
            except Exception as ex:
                raise MalformedResourceError(path, ex)
    elif path.suffix in (".yaml", ".yml"):
        if YAML_INSTALLED:
            with open(path, "r") as fp:
                try:
                    return yaml.safe_load(fp)
                except Exception as ex:
                    raise MalformedResourceError(path, ex)
        else:
            raise YamlNotInstalledError(path)
    else:
        raise UnsupportedResourceExtensionError(path)


async def load_nbt_resource(partial_path: Path) -> bytes:
    path = await get_resource_path(partial_path)
    with open(path, "rb") as fp:
        return fp.read()
