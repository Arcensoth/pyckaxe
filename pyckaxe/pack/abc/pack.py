from abc import ABC

from pyckaxe.pack.pack_context import PackContext
from pyckaxe.pack.pack_meta import PackMeta


class Pack(ABC):
    """ Anything common to both data and resource packs. """

    def __init__(self, context: PackContext):
        assert isinstance(context, PackContext)
        self.context: PackContext = context

    def __str__(self) -> str:
        return self.context.name

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.context.name}>"

    @property
    def name(self) -> str:
        return self.context.name

    @property
    def path(self) -> str:
        return self.context.path

    async def get_meta(self) -> PackMeta:
        meta_path = self.context.pack_meta_path
        meta = await PackMeta.from_path(meta_path)
        return meta
