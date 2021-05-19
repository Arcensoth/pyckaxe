import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pyckaxe.lib.text_component import TextComponent


class InvalidPackMetaError(Exception):
    def __init__(self, error: Exception, raw: Any):
        super().__init__(f"Invalid pack meta, caused by: {error}")
        self.error: Exception = error
        self.raw: Any = raw


@dataclass
class PackMeta:
    pack_format: int
    description: TextComponent

    @staticmethod
    async def load(path: Path) -> "PackMeta":
        with open(path, "r") as fp:
            raw = json.load(fp)
        try:
            pack_format = raw["pack"]["pack_format"]
            description = TextComponent(raw["pack"]["description"])
            return PackMeta(
                pack_format=pack_format,
                description=description,
            )
        except Exception as error:
            raise InvalidPackMetaError(error, raw)
