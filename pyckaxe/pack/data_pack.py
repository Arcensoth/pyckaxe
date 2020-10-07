from pathlib import Path
from typing import Iterable, List, Tuple

from pyckaxe.pack.abc.pack import Pack
from pyckaxe.pack.namespace import Namespace
from pyckaxe.pack.registry_location import RegistryLocation


class DataPack(Pack):
    async def iter_namespaces(self) -> Iterable[Tuple[Namespace, Path]]:
        data_path = self.context.data_path
        namespace_dirs = [f for f in data_path.iterdir() if f.is_dir()]
        for namespace_dir in namespace_dirs:
            namespace = Namespace(namespace_dir.name)
            yield namespace, namespace_dir

    async def iter_all_registries(self) -> Iterable[Tuple[RegistryLocation, Path]]:
        async for namespace, namespace_dir in self.iter_namespaces():
            namespace: Namespace
            namespace_dir: Path
            registry_dirs = [f for f in namespace_dir.iterdir() if f.is_dir()]
            for registry_dir in registry_dirs:
                registry_parts = (registry_dir.name,)
                registry_location = RegistryLocation(namespace, registry_parts)
                yield registry_location, registry_dir

    async def iter_registries_with_name(
        self, registry_name: str
    ) -> Iterable[Tuple[RegistryLocation, Path]]:
        async for namespace, namespace_dir in self.iter_namespaces():
            namespace: Namespace
            namespace_dir: Path
            registry_dir = namespace_dir / registry_name
            if registry_dir.exists():
                registry_parts = (registry_dir.name,)
                registry_location = RegistryLocation(namespace, registry_parts)
                yield registry_location, registry_dir

    async def collect_registries_with_name(self, registry_name: str) -> Iterable[RegistryLocation]:
        registry_locations = []
        async for registry_location, registry_path in self.iter_registries_with_name(registry_name):
            registry_locations.append(registry_location)
        return registry_locations
