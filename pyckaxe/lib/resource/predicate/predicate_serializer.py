from dataclasses import dataclass
from typing import Any

from pyckaxe.lib.resource.predicate.predicate import Predicate

__all__ = ("PredicateSerializer",)


# @implements ResourceSerializer[Predicate, Any]
@dataclass
class PredicateSerializer:
    # @implements ResourceSerializer[Predicate, Any]
    def __call__(self, resource: Predicate) -> Any:
        return self.serialize(resource)

    def serialize(self, predicate: Predicate) -> Any:
        return predicate.data
