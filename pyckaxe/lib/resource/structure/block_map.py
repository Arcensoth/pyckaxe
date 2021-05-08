from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Set, Tuple

from pyckaxe.lib.block import Block
from pyckaxe.lib.position import Position

__all__ = (
    "BlockMapEntry",
    "BlockMap",
)


@dataclass
class BlockMapEntry:
    block: Block
    palette_key: str


@dataclass
class BlockMap:
    size: Position

    _map: Dict[Position, BlockMapEntry] = field(default_factory=dict)

    def set_entry(self, position: Position, entry: BlockMapEntry):
        if position.exceeds(self.size):
            raise ValueError(
                f"Position ({position}) exceeds block map size ({self.size})"
            )
        self._map[position] = entry

    def set_block(self, position: Position, block: Block, palette_key: str):
        entry = BlockMapEntry(block=block, palette_key=palette_key)
        self.set_entry(position, entry)

    def void(self, position: Position):
        if position in self._map:
            del self._map[position]

    def filter(self, filter_keys: Set[str]):
        for position, entry in self.walk():
            if not entry.palette_key in filter_keys:
                self.void(position)

    def sorted_positions(self) -> List[Position]:
        positions = list(self._map.keys())
        positions.sort(key=lambda position: (position.y, position.x, position.z))
        return positions

    def walk(self) -> Iterable[Tuple[Position, BlockMapEntry]]:
        for position in self.sorted_positions():
            entry = self._map[position]
            yield position, entry

    def scan(self, palette_key: str) -> Iterable[Position]:
        yield from (
            position
            for position, entry in self.walk()
            if entry.palette_key == palette_key
        )

    def merge(self, other: "BlockMap", position: Position):
        for offset, other_entry in other.walk():
            self.set_entry(position + offset, other_entry)

    def to_ascii(self) -> str:
        symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        next_symbol_index = 0
        symbol_by_palette_key: Dict[str, str] = {}
        lines: List[str] = []
        size_x, size_y, size_z = self.size.unpack_ints()
        for y in range(size_y):
            for x in range(size_x):
                line: str = ""
                for z in range(size_z):
                    pos = Position.from_xyz(x, y, z)
                    entry = self._map.get(pos)
                    if entry is None:
                        line += "."
                        continue
                    symbol = symbol_by_palette_key.get(entry.palette_key)
                    if symbol is None:
                        symbol = symbols[next_symbol_index]
                        next_symbol_index = (next_symbol_index + 1) % len(symbols)
                        symbol_by_palette_key[entry.palette_key] = symbol
                    line += symbol
                lines.append(line)
            lines.append("")
        output = "\n".join(lines)
        return output
