from dataclasses import dataclass, field
from pathlib import Path
from typing import Tuple

from pyckaxe.lib.pack.namespace import Namespace
from pyckaxe.lib.pack.physical_registry_location import PhysicalRegistryLocation
from pyckaxe.lib.pack.resource_location import ResourceLocation

__all__ = ("PhysicalResourceLocation",)


@dataclass(frozen=True)
class PhysicalResourceLocation(ResourceLocation):
    """An absolute resource location, tied to an absolute registry location."""

    parts: Tuple[str, ...]
    registry_location: PhysicalRegistryLocation

    namespace: Namespace = field(init=False)

    def __post_init__(self):
        # TODO #post-init-frozen #refactor
        object.__setattr__(self, "namespace", self.registry_location.namespace)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return str(self)

    @property
    def path(self) -> Path:
        return self.registry_location.path.joinpath(*self.parts)
