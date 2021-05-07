from dataclasses import dataclass

from nbtlib.contrib.minecraft.structure import StructureFileData

from pyckaxe.lib.nbt import NbtCompound
from pyckaxe.lib.resource.structure.structure import Structure

__all__ = ("StructureSerializer",)


# @implements ResourceSerializer[Structure, NbtCompound]
@dataclass
class StructureSerializer:
    data_version: int

    # @implements ResourceSerializer[Structure, NbtCompound]
    def __call__(self, resource: Structure) -> NbtCompound:
        return self.serialize(resource)

    def serialize(self, structure: Structure) -> NbtCompound:
        return StructureFileData(
            {
                "DataVersion": self.data_version,
                "size": [
                    structure.size.x.value,
                    structure.size.y.value,
                    structure.size.z.value,
                ],
                "palette": structure.palette,
                "blocks": structure.blocks,
                "entities": structure.entities,
            }
        )
