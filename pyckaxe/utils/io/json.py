import asyncio
import json
from pathlib import Path
from typing import Any, Dict

from pyckaxe.lib.types import JsonValue

__all__ = (
    "load_json",
    "load_json_async",
    "dump_json",
    "dump_json_async",
)


def load_json(
    path: Path,
    options: Dict[str, Any] = {},
) -> JsonValue:
    """Load a JSON file synchronously."""
    with open(path) as fp:
        data = json.load(fp, **options)
    return data


def dump_json(
    data: JsonValue,
    path: Path,
    options: Dict[str, Any] = {},
):
    """Dump a JSON file synchronously."""
    with open(path, "w") as fp:
        json.dump(data, fp, **options)


async def load_json_async(
    path: Path,
    options: Dict[str, Any] = {},
) -> JsonValue:
    """Load a JSON file asynchronously."""
    loop = asyncio.get_running_loop()
    data = await loop.run_in_executor(None, load_json, path, options)
    return data


async def dump_json_async(
    data: JsonValue,
    path: Path,
    options: Dict[str, Any] = {},
):
    """Dump a JSON file asynchronously."""
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, dump_json, data, path, options)
