from __future__ import annotations

import string
from collections import defaultdict
from dataclasses import dataclass
from typing import (
    ClassVar,
    DefaultDict,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
)

from pyckaxe.lib.block import Block
from pyckaxe.lib.position import ORIGIN, Position, PositionConvertible

__all__ = ("BlockMap",)


BlockMapKey = Union[Tuple[int, int, int], Position]


@dataclass
class BlockMap:
    size: Position

    # y -> x -> z
    _block_map: DefaultDict[int, DefaultDict[int, Dict[int, Block]]]

    SYMBOLS: ClassVar[str] = string.digits + string.ascii_letters

    def __init__(self, size: PositionConvertible):
        self.size = Position.convert(size)
        self._block_map = defaultdict(lambda: defaultdict(dict))

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return self.to_ascii()

    def __setitem__(self, key: BlockMapKey, value: Block):
        x, y, z = self._unpack_xyz(key)
        if not self._in_bounds(x, y, z):
            raise ValueError(
                f"Position ({x}, {y}, {z}) exceeds block map size ({self.size})"
            )
        self._block_map[y][x][z] = value

    def __getitem__(self, key: BlockMapKey) -> Block:
        x, y, z = self._unpack_xyz(key)
        return self._block_map[y][x][z]

    def __delitem__(self, key: BlockMapKey):
        x, y, z = self._unpack_xyz(key)
        del self._block_map[y][x][z]

    def __iter__(self) -> Iterator[Tuple[Position, Block]]:
        for y, layer in self._block_map.items():
            for x, row in layer.items():
                for z, block in row.items():
                    yield Position.from_xyz(x, y, z), block

    def _unpack_xyz(self, key: BlockMapKey) -> Tuple[int, int, int]:
        if isinstance(key, Position):
            return key.unpack_ints()
        return key

    def _in_bounds(self, x: int, y: int, z: int) -> bool:
        return (
            (x < self.size.x.value)
            and (y < self.size.y.value)
            and (z < self.size.z.value)
        )

    def get(self, key: BlockMapKey) -> Optional[Block]:
        x, y, z = self._unpack_xyz(key)
        row = self._block_map[y][x]
        return row.get(z)

    def remove_blocks(self, blocks: List[Block]):
        for position, block in self:
            if block in blocks:
                del self[position]
                continue

    def keep_blocks(self, blocks: List[Block]):
        positions_to_remove: List[Position] = []
        # Collect positions to remove first because we can't mutate during iteration.
        for position, block in self:
            if block in blocks:
                continue
            positions_to_remove.append(position)
        for position in positions_to_remove:
            del self[position]

    def replace_blocks(self, blocks: List[Block], replacement: Block):
        for position, block in self:
            if block in blocks:
                self[position] = replacement
                continue

    def scan(self, block: Block) -> Iterable[Position]:
        yield from (position for position, b in self if b == block)

    def merge(self, other: BlockMap, position: Position = ORIGIN):
        for offset, block in other:
            self[position + offset] = block

    def to_ascii(self) -> str:
        next_symbol_index = 0
        symbol_by_block: Dict[Block, str] = {}
        layers: List[str] = []
        size_x, size_y, size_z = self.size.unpack_ints()
        for y in range(size_y):
            rows: List[str] = []
            for x in range(size_x):
                line: str = ""
                for z in range(size_z):
                    block = self.get((x, y, z))
                    if block is None:
                        line += "."
                        continue
                    symbol = symbol_by_block.get(block)
                    if symbol is None:
                        symbol = self.SYMBOLS[next_symbol_index]
                        next_symbol_index = (next_symbol_index + 1) % len(self.SYMBOLS)
                        symbol_by_block[block] = symbol
                    line += symbol
                rows.append(line)
            layer = "\n".join(rows)
            layers.append(layer)
        reversed_layers = reversed(layers)
        output = "\n\n".join(reversed_layers)
        return output
