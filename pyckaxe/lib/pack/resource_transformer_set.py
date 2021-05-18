from dataclasses import dataclass, field
from typing import AsyncIterable, Dict, Iterator, Tuple, Type, TypeVar, cast

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.abc.resource_transformer import ResourceTransformer
from pyckaxe.lib.pack.resource_location import ResourceLocation
from pyckaxe.lib.pack.resource_processing_context import ResourceProcessingContext

__all__ = (
    "ResourceTransformerError",
    "FailedToTransformResourceError",
    "NoTransformerAvailableError",
    "ResourceTransformerSet",
)


ResourceType = TypeVar("ResourceType", bound=Resource)


class ResourceTransformerError(Exception):
    pass


class FailedToTransformResourceError(ResourceTransformerError):
    def __init__(self, location: ResourceLocation):
        super().__init__(f"Failed to transform resource at: {location}")


class NoTransformerAvailableError(ResourceTransformerError):
    def __init__(self, resource_type: Type[Resource]):
        super().__init__(
            f"No resource transformer mapped for resource type {resource_type.__name__}"
        )


@dataclass
class ResourceTransformerSet:
    """
    Delegates a `ResourceTransformer` based on the type of `Resource`.
    """

    _transformers: Dict[Type[Resource], ResourceTransformer[Resource]] = field(
        default_factory=dict
    )

    def __setitem__(
        self, key: Type[ResourceType], value: ResourceTransformer[ResourceType]
    ):
        self._transformers[key] = cast(ResourceTransformer[Resource], value)

    def __getitem__(self, key: Type[ResourceType]) -> ResourceTransformer[ResourceType]:
        for cls in key.mro():
            if transformer := self._transformers.get(cls):
                return transformer
        raise NoTransformerAvailableError(key)

    def __delitem__(self, key: Type[ResourceType]):
        self._transformers.__delitem__(key)

    def __len__(self):
        return self._transformers.__len__()

    def __iter__(self) -> Iterator[ResourceTransformer[Resource]]:
        return self._transformers.values().__iter__()

    def __call__(
        self, ctx: ResourceProcessingContext[ResourceType]
    ) -> AsyncIterable[Tuple[Resource, ResourceLocation]]:
        return self.transform(ctx)

    async def transform(
        self,
        ctx: ResourceProcessingContext[ResourceType],
    ) -> AsyncIterable[Tuple[Resource, ResourceLocation]]:
        """Turn the input resource into any number of output resources."""
        resource_type = type(ctx.resource)
        try:
            transformer = self[resource_type]
            async for resource, location in transformer(ctx):
                yield resource, location
        except Exception as ex:
            raise FailedToTransformResourceError(ctx.location) from ex
