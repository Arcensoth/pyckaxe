from collections.abc import MutableMapping
from dataclasses import dataclass, field
from typing import AsyncIterable, Dict, Iterator, Tuple, Type, TypeVar

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


RT = TypeVar("RT", bound=Resource)
RT_co = TypeVar("RT_co", bound=Resource, covariant=True)


@dataclass
class ResourceTransformerSet(
    MutableMapping[Type[Resource], ResourceTransformer[RT_co]]
):
    """
    Delegates a `ResourceTransformer` based on the type of `Resource`.
    """

    _transformers: Dict[Type[Resource], ResourceTransformer[RT_co]] = field(
        default_factory=dict
    )

    # @implements MutableMapping
    def __setitem__(self, key: Type[RT], value: ResourceTransformer[RT_co]):
        self._transformers[key] = value

    # @implements MutableMapping
    def __getitem__(self, key: Type[RT]) -> ResourceTransformer[RT_co]:
        for cls in key.mro():
            if issubclass(cls, Resource):
                if (transformer := self._transformers.get(cls)) is not None:
                    return transformer
        raise NoTransformerAvailableError(key)

    # @implements MutableMapping
    def __delitem__(self, key: Type[RT]):
        del self._transformers[key]

    # @implements MutableMapping
    def __len__(self):
        return len(self._transformers)

    # @implements MutableMapping
    def __iter__(self) -> Iterator[Type[Resource]]:
        return iter(self._transformers)

    def __call__(
        self, ctx: ResourceProcessingContext[RT_co]
    ) -> AsyncIterable[Tuple[Resource, ResourceLocation]]:
        return self.transform(ctx)

    async def transform(
        self,
        ctx: ResourceProcessingContext[RT_co],
    ) -> AsyncIterable[Tuple[Resource, ResourceLocation]]:
        """Turn the input resource into any number of output resources."""
        resource_type = type(ctx.resource)
        try:
            transformer = self[resource_type]
            async for resource, location in transformer(ctx):
                yield resource, location
        except Exception as ex:
            raise FailedToTransformResourceError(ctx.location) from ex
