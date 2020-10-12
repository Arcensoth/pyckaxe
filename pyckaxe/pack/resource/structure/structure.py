from dataclasses import dataclass

from pyckaxe.pack.resource.abc.resource import NbtResource


@dataclass
class Structure(NbtResource):
    data: bytes

    # @implements Resource
    @staticmethod
    async def deserialize(raw: bytes) -> "Structure":
        assert isinstance(raw, bytes)
        return Structure(data=raw)

    # @implements Resource
    async def serialize(self) -> bytes:
        return self.data
