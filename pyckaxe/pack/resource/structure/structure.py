from dataclasses import dataclass
from typing import List

import nbtlib
from nbtlib.contrib.minecraft.structure import StructureFileData
from pyckaxe.pack.resource.abc.resource import NbtResource
from pyckaxe.position import Position
from pyckaxe.utils.fields import get_field

DATA_VERSION = 2682  # 20w46a


@dataclass
class Structure(NbtResource):
    size: Position
    palette: List[dict]
    blocks: List[dict]
    entities: List[dict]
    data_version: int = DATA_VERSION

    # @implements Resource
    @staticmethod
    async def deserialize(raw: nbtlib.Compound) -> "Structure":
        assert isinstance(raw, nbtlib.Compound)
        return Structure(
            size=~Position.from_field(raw, "size"),
            palette=get_field(raw, "palette", type=list, default=[]),
            blocks=get_field(raw, "blocks", type=list, default=[]),
            entities=get_field(raw, "entities", type=list, default=[]),
            data_version=get_field(raw, "DataVersion", type=int, default=DATA_VERSION),
        )

    # @implements Resource
    async def serialize(self) -> nbtlib.Compound:
        return StructureFileData(
            {
                "size": [self.size.x, self.size.y, self.size.z],
                "palette": self.palette,
                "blocks": self.blocks,
                "entities": self.entities,
                "DataVersion": self.data_version,
            }
        )
