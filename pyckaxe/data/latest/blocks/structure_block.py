from dataclasses import dataclass
from typing import Any, Iterable, Optional, Tuple

from nbtlib import tag
from nbtlib.schema import CompoundSchema
from pyckaxe.data.abc.block_base import BlockBase
from pyckaxe.data.abc.block_data_base import BlockDataBase
from pyckaxe.data.abc.block_state_base import BlockStateBase
from pyckaxe.position import Position
from pyckaxe.safe_enum import SafeEnum


@dataclass
class StructureBlockState(BlockStateBase):
    class Mode(SafeEnum):
        SAVE = "save"
        LOAD = "load"
        CORNER = "corner"
        DATA = "data"

    mode: Optional[Mode] = None

    # @implements BlockStateBase
    def _items(self) -> Iterable[Tuple[str, Any]]:
        yield "mode", self.mode.value


@dataclass
class StructureBlockData(BlockDataBase):
    class Rotation(SafeEnum):
        NONE = "NONE"
        CLOCKWISE_90 = "CLOCKWISE_90"
        CLOCKWISE_180 = "CLOCKWISE_180"
        COUNTERCLOCKWISE_90 = "COUNTERCLOCKWISE_90"

    class Mirror(SafeEnum):
        NONE = "NONE"
        LEFT_RIGHT = "LEFT_RIGHT"
        FRONT_BACK = "FRONT_BACK"

    class Mode(SafeEnum):
        SAVE = "SAVE"
        LOAD = "LOAD"
        CORNER = "CORNER"
        DATA = "DATA"

    name: Optional[str] = None
    author: Optional[str] = None
    metadata: Optional[str] = None
    pos: Optional[Position] = None
    size: Optional[Position] = None
    rotation: Optional[Rotation] = None
    mirror: Optional[Mirror] = None
    mode: Optional[Mode] = None
    integrity: Optional[float] = None
    seed: Optional[int] = None
    ignore_entities: Optional[bool] = None
    showboundingbox: Optional[bool] = None
    powered: Optional[bool] = None

    class _Schema(CompoundSchema):
        schema = {
            "name": tag.String,
            "author": tag.String,
            "metadata": tag.String,
            "posX": tag.Int,
            "posY": tag.Int,
            "posZ": tag.Int,
            "sizeX": tag.Int,
            "sizeY": tag.Int,
            "sizeZ": tag.Int,
            "rotation": tag.String,
            "mirror": tag.String,
            "mode": tag.String,
            "integrity": tag.Float,
            "seed": tag.Long,
            "ignoreEntities": tag.Byte,
            "showboundingbox": tag.Byte,
            "powered": tag.Byte,
        }

    # @implements BlockDataBase
    def _nbt(self) -> tag.Compound:
        return StructureBlockData._Schema(
            {
                k: v
                for k, v in {
                    "name": self.name,
                    "author": self.author,
                    "metadata": self.metadata,
                    "posX": self.pos.x.value if self.pos is not None else None,
                    "posY": self.pos.y.value if self.pos is not None else None,
                    "posZ": self.pos.z.value if self.pos is not None else None,
                    "sizeX": self.size.x.value if self.size is not None else None,
                    "sizeY": self.size.y.value if self.size is not None else None,
                    "sizeZ": self.size.z.value if self.size is not None else None,
                    "rotation": self.rotation.value if self.rotation is not None else None,
                    "mirror": self.mirror.value if self.mirror is not None else None,
                    "mode": self.mode.value if self.mode is not None else None,
                    "integrity": self.integrity,
                    "seed": self.seed,
                    "ignoreEntities": self.ignore_entities,
                    "showboundingbox": self.showboundingbox,
                    "powered": self.powered,
                }.items()
                if v is not None
            }
        )


@dataclass
class StructureBlock(BlockBase):
    NAME = "structure_block"

    state: Optional[StructureBlockState]
    data: Optional[StructureBlockData]
