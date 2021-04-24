from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, AsyncIterable, Generic, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.located_resource import LocatedResource
from pyckaxe.lib.pack.resource_build_context import ResourceBuildContext

__all__ = ("ResourceBuilder",)


ResourceType = TypeVar("ResourceType", bound=Resource)
OptionsType = TypeVar("OptionsType")


@dataclass
class ResourceBuilder(ABC, Generic[ResourceType, OptionsType]):
    @abstractmethod
    def build_resources(
        self, ctx: ResourceBuildContext[ResourceType, OptionsType]
    ) -> AsyncIterable[LocatedResource[Any]]:
        """ Produce [LocatedResource]s from another [Resource]. """
