from dataclasses import dataclass
from pathlib import Path

from pyckaxe.lib.pack.namespace import Namespace

__all__ = ("PhysicalNamespace",)


@dataclass
class PhysicalNamespace(Namespace):
    """ An absolute namespace, tied to a physical path. """

    path: Path
