from dataclasses import dataclass
from pathlib import Path


@dataclass
class PackContext:
    path: Path

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.path)

    @property
    def name(self) -> str:
        return self.path.name

    @property
    def pack_meta_path(self) -> Path:
        return self.path / "pack.mcmeta"

    @property
    def data_path(self) -> Path:
        return self.path / "data"

    @property
    def assets_path(self) -> Path:
        return self.path / "assets"
