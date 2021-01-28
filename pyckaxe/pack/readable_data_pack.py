from pathlib import Path
from typing import AsyncIterable, List, Tuple, Type, TypeVar

from pyckaxe.pack.namespace import Namespace
from pyckaxe.pack.readable_pack import ReadablePack
from pyckaxe.pack.readable_registry_node import ReadableRegistryNode
from pyckaxe.pack.registry_location import RegistryLocation

ReadableRegistryNodeType = TypeVar(
    "ReadableRegistryNodeType", bound=ReadableRegistryNode
)


class ReadableDataPack(ReadablePack):
    async def iter_namespaces(self) -> AsyncIterable[Tuple[Namespace, Path]]:
        data_path = self.context.data_path
        namespace_dirs = [f for f in data_path.iterdir() if f.is_dir()]
        for namespace_dir in namespace_dirs:
            namespace = Namespace(namespace_dir.name)
            yield namespace, namespace_dir

    async def iter_all_registry_locations(
        self,
    ) -> AsyncIterable[Tuple[RegistryLocation, Path]]:
        async for namespace, namespace_dir in self.iter_namespaces():
            registry_dirs = [f for f in namespace_dir.iterdir() if f.is_dir()]
            for registry_dir in registry_dirs:
                registry_parts = (registry_dir.name,)
                registry_location = RegistryLocation(namespace, registry_parts)
                yield registry_location, registry_dir

    async def iter_registry_locations_with_name(
        self, registry_name: str
    ) -> AsyncIterable[Tuple[RegistryLocation, Path]]:
        async for namespace, namespace_dir in self.iter_namespaces():
            registry_dir = namespace_dir / registry_name
            if registry_dir.exists():
                registry_parts = (registry_dir.name,)
                registry_location = RegistryLocation(namespace, registry_parts)
                yield registry_location, registry_dir

    async def collect_registry_locations_with_name(
        self, registry_name: str
    ) -> List[RegistryLocation]:
        registry_locations = []
        async for registry_location, registry_path in self.iter_registry_locations_with_name(
            registry_name
        ):
            registry_locations.append(registry_location)
        return registry_locations

    async def iter_registries(
        self,
        registry_name: str,
        registry_class: Type[ReadableRegistryNodeType],
    ) -> AsyncIterable[ReadableRegistryNodeType]:
        async for registry_location, registry_path in self.iter_registry_locations_with_name(
            registry_name
        ):
            yield registry_class(registry_location, registry_path)

    async def collect_registries(
        self,
        registry_name: str,
        registry_class: Type[ReadableRegistryNodeType],
    ) -> List[ReadableRegistryNodeType]:
        registries = []
        async for registry in self.iter_registries(registry_name, registry_class):
            registries.append(registry)
        return registries
