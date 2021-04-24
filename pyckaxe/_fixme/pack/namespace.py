from pathlib import Path

from pyckaxe.pack.pack_context import PackContext


class Namespace:
    def __init__(self, name: str):
        assert isinstance(name, str)
        self.name: str = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Namespace) and self.name == o.name

    def resolve_path(self, pack_context: PackContext) -> Path:
        return Path(pack_context.data_path / self.name)
