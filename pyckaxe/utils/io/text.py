import asyncio
from pathlib import Path
from typing import Any

__all__ = (
    "load_text",
    "load_text_async",
    "dump_text",
    "dump_text_async",
)


def load_text(path: Path, **options: Any) -> str:
    """ Load a text file synchronously. """
    with open(path, **options) as fp:
        text = fp.read()
    return text


def dump_text(text: str, path: Path, mkdir: bool = False, **options: Any):
    """ Dump a text file synchronously. """
    if mkdir:
        path.mkdir(parents=True, exist_ok=True)
    with open(path, "w", **options) as fp:
        fp.write(text)


async def load_text_async(path: Path, **options: Any) -> str:
    """ Load a text file asynchronously. """
    loop = asyncio.get_running_loop()
    data = await loop.run_in_executor(None, load_text, path, **options)
    return data


async def dump_text_async(text: str, path: Path, mkdir: bool = False, **options: Any):
    """ Dump a text file asynchronously. """
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, dump_text, text, path, mkdir, **options)
