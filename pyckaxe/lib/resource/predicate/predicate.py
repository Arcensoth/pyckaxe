from dataclasses import dataclass
from typing import Any, TypeAlias

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_collection import ResourceCollection
from pyckaxe.lib.pack.resource_link import ResourceLink
from pyckaxe.lib.pack.resource_location import ClassifiedResourceLocation
from pyckaxe.lib.pack.resource_processing_context import ResourceProcessingContext

__all__ = (
    "Predicate",
    "PredicateLocation",
    "PredicateLink",
    "PredicateCollection",
    "PredicateProcessingContext",
)


@dataclass
class Predicate(Resource):
    data: Any


PredicateLocation: TypeAlias = ClassifiedResourceLocation[Predicate]
PredicateLink: TypeAlias = ResourceLink[Predicate]
PredicateCollection: TypeAlias = ResourceCollection[Predicate]
PredicateProcessingContext: TypeAlias = ResourceProcessingContext[Predicate]
