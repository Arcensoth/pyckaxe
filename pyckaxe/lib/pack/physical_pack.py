from dataclasses import dataclass, field
from pathlib import Path
from typing import AsyncIterable, List

from pyckaxe.lib.pack.pack_context import PackContext
from pyckaxe.lib.pack.pack_meta import PackMeta
from pyckaxe.lib.pack.physical_namespace import PhysicalNamespace
from pyckaxe.lib.pack.physical_registry_location import PhysicalRegistryLocation

__all__ = ("PhysicalPack",)


@dataclass
class PhysicalPack:
    """
    A pack that has a physical, readable directory associated with it.

    Attributes
    ----------
    path
        The path to the root of the pack.
    """

    path: Path

    context: PackContext = field(init=False)

    def __post_init__(self):
        self.context = PackContext(self.path)

    def __str__(self) -> str:
        return self.name

    @property
    def name(self) -> str:
        return self.path.name

    async def get_meta(self) -> PackMeta:
        meta_path = self.context.pack_meta_path
        meta = await PackMeta.load(meta_path)
        return meta

    async def iter_namespaces(self) -> AsyncIterable[PhysicalNamespace]:
        namespace_dirs: List[Path] = []
        # data pack data
        data_path = self.context.data_path
        if data_path.is_dir():
            data_dirs = [f for f in data_path.iterdir() if f.is_dir()]
            namespace_dirs.extend(data_dirs)
        # resource pack assets
        assets_path = self.context.assets_path
        if assets_path.is_dir():
            assets_dirs = [f for f in assets_path.iterdir() if f.is_dir()]
            namespace_dirs.extend(assets_dirs)
        # combine them all
        for namespace_dir in namespace_dirs:
            namespace = PhysicalNamespace(path=namespace_dir)
            yield namespace

    async def iter_registries(
        self, *parts: str
    ) -> AsyncIterable[PhysicalRegistryLocation]:
        async for namespace in self.iter_namespaces():
            registry_path = namespace.path.joinpath(*parts)
            if registry_path.is_dir():
                delta = registry_path.relative_to(namespace.path)
                registry_parts = delta.parts
                registry_location = PhysicalRegistryLocation(
                    namespace=namespace, parts=registry_parts
                )
                yield registry_location

    async def get_registries(self, *parts: str) -> List[PhysicalRegistryLocation]:
        return [
            registry_location
            async for registry_location in self.iter_registries(*parts)
        ]
