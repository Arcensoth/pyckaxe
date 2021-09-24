from dataclasses import dataclass
from typing import Any, List

from pyckaxe.lib.pack.abc.resource import Resource

__all__ = ("Function",)


@dataclass
class Function(Resource):
    lines: List[Any]
