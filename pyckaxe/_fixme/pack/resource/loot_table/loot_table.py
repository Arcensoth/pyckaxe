from dataclasses import dataclass

from pyckaxe.pack.resource.abc.resource import DictResource


@dataclass
class LootTable(DictResource):
    data: dict

    # @implements Resource
    @staticmethod
    async def deserialize(raw: dict, **options) -> "LootTable":
        assert isinstance(raw, dict)
        return LootTable(data=raw)

    # @implements Serializable
    async def serialize(self, **options) -> dict:
        return self.data
