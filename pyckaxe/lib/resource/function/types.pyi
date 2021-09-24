from typing import Union

from pyckaxe.lib.pack.resource_location import ClassifiedResourceLocation
from pyckaxe.lib.pack.resource_processing_context import ResourceProcessingContext
from pyckaxe.lib.resource.function.function import Function

FunctionLocation = ClassifiedResourceLocation[Function]
FunctionOrLocation = Union[Function, FunctionLocation]
FunctionProcessingContext = ResourceProcessingContext[Function]
