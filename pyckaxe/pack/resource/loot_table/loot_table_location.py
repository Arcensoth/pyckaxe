from pyckaxe.pack.resource.abc.resource_location import ResourceLocation
from pyckaxe.pack.resource.loot_table import LootTable


class LootTableLocation(ResourceLocation[LootTable]):
    resource_class = LootTable
    registry_parts = ("loot_tables",)
