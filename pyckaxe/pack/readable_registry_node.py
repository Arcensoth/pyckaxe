from pathlib import Path

from pyckaxe.pack.namespace import Namespace
from pyckaxe.pack.registry_location import RegistryLocation


class ReadableRegistryNode:
    """
    A registry node that has a physical, readable directory associated with it.

    May contain further registry nodes (as with tags or worldgen) or actual resources.
    """

    def __init__(self, registry_location: RegistryLocation, path: Path):
        assert isinstance(registry_location, RegistryLocation)
        assert isinstance(path, Path)
        self.registry_location: RegistryLocation = registry_location
        self.path: Path = path

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"

    @property
    def name(self) -> str:
        return self.registry_location.name
