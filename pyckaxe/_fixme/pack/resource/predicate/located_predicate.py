from pyckaxe.pack.resource.abc.located_resource import LocatedResource
from pyckaxe.pack.resource.predicate.predicate import Predicate
from pyckaxe.pack.resource.predicate.predicate_location import PredicateLocation


class LocatedPredicate(LocatedResource[Predicate, PredicateLocation]):
    pass
