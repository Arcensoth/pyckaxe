from pathlib import Path


class PackContext:
    def __init__(self, path: Path):
        self.path: Path = path

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"

    def __hash__(self) -> int:
        return hash(self.path)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, PackContext) and self.path == o.path

    @property
    def name(self) -> str:
        return self.path.name

    @property
    def pack_meta_path(self) -> Path:
        return self.path / "pack.mcmeta"

    @property
    def data_path(self) -> Path:
        return self.path / "data"
