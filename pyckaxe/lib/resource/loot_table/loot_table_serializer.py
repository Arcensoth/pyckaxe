from dataclasses import dataclass
from typing import Any

from pyckaxe.lib.resource.loot_table.loot_table import LootTable

__all__ = ("LootTableSerializer",)


# @implements ResourceSerializer[LootTable, Any]
@dataclass
class LootTableSerializer:
    # @implements ResourceSerializer[LootTable, Any]
    def __call__(self, resource: LootTable) -> Any:
        return self.serialize(resource)

    def serialize(self, loot_table: LootTable) -> Any:
        return loot_table.data
