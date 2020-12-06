from pyckaxe.pack.resource.abc.located_resource import LocatedResource
from pyckaxe.pack.resource.loot_table.loot_table import LootTable
from pyckaxe.pack.resource.loot_table.loot_table_location import LootTableLocation


class LocatedLootTable(LocatedResource[LootTable, LootTableLocation]):
    pass
