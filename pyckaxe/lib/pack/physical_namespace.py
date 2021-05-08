from dataclasses import dataclass, field
from pathlib import Path

from pyckaxe.lib.pack.namespace import Namespace

__all__ = ("PhysicalNamespace",)


@dataclass
class PhysicalNamespace(Namespace):
    """ An absolute namespace, tied to a physical path. """

    path: Path

    name: str = field(init=False)

    def __post_init__(self):
        self.name = self.path.name
