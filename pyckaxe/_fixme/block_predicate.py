from dataclasses import dataclass
from typing import Union

from pyckaxe.abc.block_base import BlockBase
from pyckaxe.block import Block

AnyBlockPredicate = Union["BlockPredicate", Block, BlockBase]


@dataclass
class BlockPredicate(Block):
    pass
