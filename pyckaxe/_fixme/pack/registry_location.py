from pathlib import Path
from typing import Tuple

from pyckaxe.pack.namespace import Namespace
from pyckaxe.pack.pack_context import PackContext


class RegistryLocation:
    def __init__(self, namespace: Namespace, parts: Tuple[str]):
        assert isinstance(namespace, Namespace)
        assert isinstance(parts, tuple)
        self.namespace: Namespace = namespace
        self.parts: Tuple[str] = parts

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, RegistryLocation) and self.name == o.name

    def resolve_path(self, pack_context: PackContext) -> Path:
        namespace_path = self.namespace.resolve_path(pack_context)
        return Path(namespace_path.joinpath(*self.parts))

    @property
    def name(self) -> str:
        parts_str = "/".join(self.parts)
        return f"{self.namespace}[{parts_str}]"
