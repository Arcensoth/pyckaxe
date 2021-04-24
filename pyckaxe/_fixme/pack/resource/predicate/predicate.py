from dataclasses import dataclass

from pyckaxe.pack.resource.abc.resource import DictResource


@dataclass
class Predicate(DictResource):
    data: dict

    # @implements Resource
    @staticmethod
    async def deserialize(raw: dict, **options) -> "Predicate":
        assert isinstance(raw, dict)
        return Predicate(data=raw)

    # @implements Serializable
    async def serialize(self, **options) -> dict:
        return self.data
