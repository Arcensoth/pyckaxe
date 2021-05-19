from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

from pyckaxe.lib.pack.physical_namespace import PhysicalNamespace
from pyckaxe.lib.pack.physical_registry_location import PhysicalRegistryLocation
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation
from pyckaxe.lib.pack.resource_location import ResourceLocation

__all__ = ("CommonResourceLocationResolver",)


# @implements ResourceLocationResolver
@dataclass
class CommonResourceLocationResolver:
    """
    Resolves absolute resource locations from relative ones.

    Attributes
    ----------
    registry_location
        An absolute registry location used to resolve resource locations.
    """

    path: Path
    parts: Tuple[str, ...]

    # @implements ResourceLocationResolver
    def __call__(self, location: ResourceLocation) -> PhysicalResourceLocation:
        return self.resolve(location)

    def resolve(self, location: ResourceLocation) -> PhysicalResourceLocation:
        """Resolve an absolute resource location from a relative one."""
        physical_namespace = PhysicalNamespace(
            path=self.path / location.namespace.name,
        )
        physical_registry_location = PhysicalRegistryLocation(
            namespace=physical_namespace,
            parts=self.parts,
        )
        return PhysicalResourceLocation(
            parts=location.parts,
            registry_location=physical_registry_location,
        )
