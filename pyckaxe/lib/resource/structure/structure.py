from dataclasses import dataclass, field
from typing import Any, Dict, List

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.position import Position

__all__ = ("Structure",)


@dataclass
class Structure(Resource):
    size: Position
    palette: List[Dict[str, Any]] = field(default_factory=list)
    blocks: List[Dict[str, Any]] = field(default_factory=list)
    entities: List[Dict[str, Any]] = field(default_factory=list)
