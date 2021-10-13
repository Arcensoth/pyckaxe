from dataclasses import dataclass
from typing import Any, List, TypeAlias

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_collection import ResourceCollection
from pyckaxe.lib.pack.resource_link import ResourceLink
from pyckaxe.lib.pack.resource_location import ClassifiedResourceLocation
from pyckaxe.lib.pack.resource_processing_context import ResourceProcessingContext

__all__ = (
    "Function",
    "FunctionLocation",
    "FunctionLink",
    "FunctionCollection",
    "FunctionProcessingContext",
)


@dataclass
class Function(Resource):
    lines: List[Any]


FunctionLocation: TypeAlias = ClassifiedResourceLocation[Function]
FunctionLink: TypeAlias = ResourceLink[Function]
FunctionCollection: TypeAlias = ResourceCollection[Function]
FunctionProcessingContext: TypeAlias = ResourceProcessingContext[Function]
