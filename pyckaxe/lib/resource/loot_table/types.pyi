from typing import Union

from pyckaxe.lib.pack.resource_location import ClassifiedResourceLocation
from pyckaxe.lib.pack.resource_processing_context import ResourceProcessingContext
from pyckaxe.lib.resource.loot_table.loot_table import LootTable

LootTableLocation = ClassifiedResourceLocation[LootTable]
LootTableOrLocation = Union[LootTable, LootTableLocation]
LootTableProcessingContext = ResourceProcessingContext[LootTable]
