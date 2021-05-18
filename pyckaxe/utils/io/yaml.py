import asyncio
from pathlib import Path
from typing import Any, Dict

from pyckaxe.lib.types import JsonValue

__all__ = (
    "YamlNotInstalledError",
    "load_yaml",
    "load_yaml_async",
    "dump_yaml",
    "dump_yaml_async",
)


try:
    import yaml

    _is_yaml_installed = True
except:
    _is_yaml_installed = False


class YamlNotInstalledError(Exception):
    def __init__(self, path: Path):
        super().__init__(f"PyYAML must be installed to load/dump YAML file at: {path}")


def load_yaml(
    path: Path,
    options: Dict[str, Any] = {},
) -> JsonValue:
    """Load a YAML file synchronously."""
    if not _is_yaml_installed:
        raise YamlNotInstalledError(path)
    with path.open("r") as fp:
        return yaml.safe_load(fp, **options)


def dump_yaml(
    data: JsonValue,
    path: Path,
    options: Dict[str, Any] = {},
):
    """Dump a YAML file synchronously."""
    if not _is_yaml_installed:
        raise YamlNotInstalledError(path)
    with path.open("w") as fp:
        yaml.safe_dump(data, fp, **options)


async def load_yaml_async(
    path: Path,
    options: Dict[str, Any] = {},
) -> JsonValue:
    """Load a YAML file asynchronously."""
    loop = asyncio.get_running_loop()
    data = await loop.run_in_executor(None, load_yaml, path, options)
    return data


async def dump_yaml_async(
    data: JsonValue,
    path: Path,
    options: Dict[str, Any] = {},
):
    """Dump a YAML file asynchronously."""
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, dump_yaml, data, path, options)
