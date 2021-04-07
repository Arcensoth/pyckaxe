from typing import Union

from pyckaxe.abc.block_base import BlockBase
from pyckaxe.block import Block

# TODO Remove this in favour of [BlockBase.Thing]... eventually. #refactor

AnyBlock = Union[Block, BlockBase]
BlockThing = Union[str, Block, BlockBase]


def thing_to_block(obj: BlockThing) -> AnyBlock:
    if isinstance(obj, (Block, BlockBase)):
        return obj
    return Block(obj)
