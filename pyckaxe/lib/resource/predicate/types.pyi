from typing import Union

from pyckaxe.lib.pack.resource_location import ClassifiedResourceLocation
from pyckaxe.lib.pack.resource_processing_context import ResourceProcessingContext
from pyckaxe.lib.resource.predicate.predicate import Predicate

PredicateLocation = ClassifiedResourceLocation[Predicate]
PredicateOrLocation = Union[Predicate, PredicateLocation]
PredicateProcessingContext = ResourceProcessingContext[Predicate]
