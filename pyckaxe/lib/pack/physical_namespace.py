from dataclasses import dataclass, field
from pathlib import Path

from pyckaxe.lib.pack.namespace import Namespace

__all__ = ("PhysicalNamespace",)


@dataclass(frozen=True)
class PhysicalNamespace(Namespace):
    """An absolute namespace, tied to a physical path."""

    path: Path

    name: str = field(init=False)

    def __post_init__(self):
        # TODO #post-init-frozen #refactor
        object.__setattr__(self, "name", self.path.name)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return str(self)
