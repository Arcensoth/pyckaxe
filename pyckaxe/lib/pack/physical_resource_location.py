from dataclasses import dataclass
from pathlib import Path

from pyckaxe.lib.pack.physical_namespace import PhysicalNamespace
from pyckaxe.lib.pack.physical_registry_location import PhysicalRegistryLocation
from pyckaxe.lib.pack.resource_location import ResourceLocation

__all__ = ("PhysicalResourceLocation",)


@dataclass
class PhysicalResourceLocation(ResourceLocation):
    """ An absolute resource location, tied to an absolute registry location. """

    namespace: PhysicalNamespace
    registry_location: PhysicalRegistryLocation

    @property
    def path(self) -> Path:
        return self.registry_location.path.joinpath(*self.parts)
