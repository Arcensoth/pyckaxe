from dataclasses import dataclass
from typing import Any, TypeAlias

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_collection import ResourceCollection
from pyckaxe.lib.pack.resource_link import ResourceLink
from pyckaxe.lib.pack.resource_location import ClassifiedResourceLocation
from pyckaxe.lib.pack.resource_processing_context import ResourceProcessingContext

__all__ = (
    "LootTable",
    "LootTableLocation",
    "LootTableLink",
    "LootTableCollection",
    "LootTableProcessingContext",
)


@dataclass
class LootTable(Resource):
    data: Any


LootTableLocation: TypeAlias = ClassifiedResourceLocation[LootTable]
LootTableLink: TypeAlias = ResourceLink[LootTable]
LootTableCollection: TypeAlias = ResourceCollection[LootTable]
LootTableProcessingContext: TypeAlias = ResourceProcessingContext[LootTable]
