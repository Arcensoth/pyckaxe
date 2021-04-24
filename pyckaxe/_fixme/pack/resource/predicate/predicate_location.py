from pyckaxe.pack.resource.abc.resource_location import ResourceLocation
from pyckaxe.pack.resource.predicate.predicate import Predicate


class PredicateLocation(ResourceLocation[Predicate]):
    resource_class = Predicate
    registry_parts = ("predicates",)
