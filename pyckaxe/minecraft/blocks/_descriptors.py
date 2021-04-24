from pyckaxe.lib import Block

from .structure_block import StructureBlock


class air:
    def __get__(self, *_) -> Block:
        return Block("minecraft:air")


class structure_block:
    def __get__(self, *_) -> StructureBlock:
        return StructureBlock()
