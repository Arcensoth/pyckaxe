from dataclasses import dataclass
from typing import Any

from pyckaxe.lib.pack.abc.resource import Resource

__all__ = ("LootTable",)


@dataclass
class LootTable(Resource):
    data: Any
