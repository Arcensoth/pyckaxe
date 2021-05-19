from dataclasses import dataclass, field
from typing import Dict, List, Optional, Type, TypeVar

from pyckaxe.lib.block import Block
from pyckaxe.lib.block_map import BlockMap
from pyckaxe.lib.nbt import NbtCompound
from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.position import Position

__all__ = ("Structure",)


SelfType = TypeVar("SelfType", bound="Structure")


@dataclass
class StructurePaletteEntry:
    index: int
    block: Block


@dataclass
class StructureBlockEntry:
    state: int
    pos: Position
    nbt: Optional[NbtCompound] = None


@dataclass
class StructureEntityEntry:
    pos: Position
    nbt: NbtCompound


@dataclass
class Structure(Resource):
    size: Position
    palette: List[StructurePaletteEntry] = field(default_factory=list)
    blocks: List[StructureBlockEntry] = field(default_factory=list)
    entities: List[StructureEntityEntry] = field(default_factory=list)

    @classmethod
    def from_block_map(cls: Type[SelfType], block_map: BlockMap) -> SelfType:
        # Create the flat list of blocks, building a minimal palette as we go.
        palette_map: Dict[str, StructurePaletteEntry] = {}
        blocks: List[StructureBlockEntry] = []
        for position, block in block_map:
            # Grab the corresponding palette entry from the palette map.
            palette_map_key = (
                block.name if block.state is None else f"{block.name}{block.state}"
            )
            palette_map_entry = palette_map.get(palette_map_key)
            if palette_map_entry is None:
                # Create a new entry in the palette map for new block-state combos.
                palette_map_entry = StructurePaletteEntry(
                    index=len(palette_map), block=block
                )
                palette_map[palette_map_key] = palette_map_entry
            # Create and append a new block entry using the palette entry's index.
            output_block_entry = StructureBlockEntry(
                state=palette_map_entry.index,
                pos=position,
            )
            # Note NBT is part of the block entry, not the palette.
            if block.data:
                output_block_entry.nbt = block.data
            blocks.append(output_block_entry)

        # Convert the palette map into the final palette, sorted by index.
        palette = sorted(palette_map.values(), key=lambda entry: entry.index)

        # Create and return the final output structure.
        return cls(
            size=block_map.size,
            palette=palette,
            blocks=blocks,
        )

    def to_block_map(self) -> BlockMap:
        block_map = BlockMap(size=self.size)
        for block_entry in self.blocks:
            palette_index = block_entry.state
            palette_entry = self.palette[palette_index]
            block_map[block_entry.pos] = palette_entry.block
        return block_map
