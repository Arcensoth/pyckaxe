from dataclasses import dataclass
from typing import Dict, List

from nbtlib.contrib.minecraft.structure import StructureFileData

from pyckaxe.lib.nbt import NbtCompound
from pyckaxe.lib.position import Position
from pyckaxe.lib.resource.structure.structure import (
    Structure,
    StructureBlockEntry,
    StructureEntityEntry,
    StructurePaletteEntry,
)
from pyckaxe.lib.types import JsonValue

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
                "size": self.serialize_size(structure.size),
                "palette": self.serialize_palette(structure.palette),
                "blocks": self.serialize_blocks(structure.blocks),
                "entities": self.serialize_entities(structure.entities),
            }
        )

    def serialize_size(self, size: Position) -> JsonValue:
        return size.unpack_ints()

    def serialize_palette(self, palette: List[StructurePaletteEntry]) -> JsonValue:
        serialized_palette: List[JsonValue] = []
        for palette_entry in palette:
            serialized_palette_entry: Dict[str, JsonValue] = {
                "Name": palette_entry.block.name,
            }
            if palette_entry.block.state:
                block_state_nbt = palette_entry.block.state.to_nbt()
                serialized_palette_entry["Properties"] = block_state_nbt
            serialized_palette.append(serialized_palette_entry)
        return serialized_palette

    def serialize_blocks(self, blocks: List[StructureBlockEntry]) -> JsonValue:
        serialized_blocks: List[JsonValue] = []
        for block_entry in blocks:
            serialized_block_entry: Dict[str, JsonValue] = {
                "state": block_entry.state,
                "pos": block_entry.pos.unpack_ints(),
            }
            if block_entry.nbt:
                serialized_block_entry["nbt"] = block_entry.nbt
            serialized_blocks.append(serialized_block_entry)
        return serialized_blocks

    def serialize_entities(self, entities: List[StructureEntityEntry]) -> JsonValue:
        return [
            {
                "pos": entity_entry.pos.unpack_floats(),
                "blockPos": entity_entry.pos.unpack_ints(),
                "nbt": entity_entry.nbt,
            }
            for entity_entry in entities
        ]
