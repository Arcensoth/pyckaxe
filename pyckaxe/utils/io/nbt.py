import asyncio
from pathlib import Path
from typing import Any, Dict

import nbtlib

from pyckaxe.lib.nbt import NbtCompound

__all__ = (
    "load_nbt",
    "load_nbt_async",
    "dump_nbt",
    "dump_nbt_async",
)


def load_nbt(
    path: Path,
    options: Dict[str, Any] = {},
) -> NbtCompound:
    """Load a NBT file synchronously."""
    return nbtlib.load(str(path), **options)


def dump_nbt(
    root: NbtCompound,
    path: Path,
    options: Dict[str, Any] = {},
):
    """Dump a NBT file synchronously."""
    nbtfile = nbtlib.File({"": root})
    nbtfile.save(str(path), **options)


async def load_nbt_async(
    path: Path,
    options: Dict[str, Any] = {},
) -> NbtCompound:
    """Load a NBT file asynchronously."""
    loop = asyncio.get_running_loop()
    root = await loop.run_in_executor(None, load_nbt, path, options)
    return root


async def dump_nbt_async(
    root: NbtCompound,
    path: Path,
    options: Dict[str, Any] = {},
):
    """Dump a NBT file asynchronously."""
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, dump_nbt, root, path, options)
