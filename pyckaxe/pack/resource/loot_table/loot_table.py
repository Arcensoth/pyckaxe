from dataclasses import dataclass

from pyckaxe.pack.resource.abc.resource import DictResource


@dataclass
class LootTable(DictResource):
    data: dict

    # @implements Resource
    @staticmethod
    async def from_raw(raw: dict) -> "LootTable":
        assert isinstance(raw, dict)
        return LootTable(data=raw)
