from dataclasses import dataclass
from pathlib import Path

from pyckaxe.lib.pack.physical_namespace import PhysicalNamespace
from pyckaxe.lib.pack.registry_location import RegistryLocation

__all__ = ("PhysicalRegistryLocation",)


@dataclass
class PhysicalRegistryLocation(RegistryLocation):
    """ An absolute registry location, tied to an absolute namespace. """

    namespace: PhysicalNamespace

    @property
    def path(self) -> Path:
        return self.namespace.path.joinpath(*self.parts)
