from typing import Union

from pyckaxe.lib.pack.resource_location import ClassifiedResourceLocation
from pyckaxe.lib.pack.resource_processing_context import ResourceProcessingContext
from pyckaxe.lib.resource.structure.structure import Structure

StructureLocation = ClassifiedResourceLocation[Structure]
StructureOrLocation = Union[Structure, StructureLocation]
StructureProcessingContext = ResourceProcessingContext[Structure]
