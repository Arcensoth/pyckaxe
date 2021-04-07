from dataclasses import dataclass, field
from pathlib import Path

from pyckaxe.pack.pack_context import PackContext
from pyckaxe.pack.pack_meta import PackMeta


@dataclass
class ReadablePack:
    """ A pack that has a physical, readable directory associated with it. """

    path: Path
    context: PackContext = field(init=False)

    def __post_init__(self):
        self.context = PackContext(self.path)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"

    @property
    def name(self) -> str:
        return self.path.name

    async def get_meta(self) -> PackMeta:
        meta_path = self.context.pack_meta_path
        meta = await PackMeta.load(meta_path)
        return meta
