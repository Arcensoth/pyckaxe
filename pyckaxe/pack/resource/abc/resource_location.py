from pathlib import Path
from typing import Any, Coroutine, Dict, Generic, Tuple, Type, TypeVar

from pyckaxe.command.abc.command_token import CommandToken
from pyckaxe.pack.namespace import Namespace
from pyckaxe.pack.pack_context import PackContext
from pyckaxe.pack.registry_location import RegistryLocation
from pyckaxe.pack.resource.abc.resource import Resource
from pyckaxe.utils.fields import DEFAULT, get_field

ResourceLocationType = TypeVar("ResourceLocationType", bound="ResourceLocation")
ResourceType = TypeVar("ResourceType", bound=Resource)


class ResourceLocation(CommandToken, Generic[ResourceType]):
    resource_class: Type[Resource] = Resource
    registry_parts: Tuple[str, ...] = tuple()

    @classmethod
    def from_string(cls: Type[ResourceLocationType], name: str) -> ResourceLocationType:
        namespace = Namespace(name.split(":")[0])
        parts = tuple(name.split(":")[1].split("/"))
        return cls(namespace, parts)

    @classmethod
    def from_field(
        cls: Type[ResourceLocationType], raw: Dict[str, Any], field: str, default: Any = DEFAULT
    ) -> ResourceLocationType:
        raw_resource_location = get_field(raw, field, type=str, default=default)
        resource_location = cls.from_string(raw_resource_location)
        return resource_location

    def __init__(self, namespace: Namespace, parts: Tuple[str, ...]):
        assert isinstance(namespace, Namespace)
        assert isinstance(parts, tuple)
        self.registry_location: RegistryLocation = RegistryLocation(namespace, self.registry_parts)
        self.parts: Tuple[str, ...] = parts

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, ResourceLocation) and self.name == o.name

    def __call__(self, pack_context: PackContext) -> Coroutine[Any, Any, ResourceType]:
        return self.resolve_resource(pack_context)

    def extend(self: ResourceLocationType, *parts: str) -> ResourceLocationType:
        resource_cls = self.__class__
        resource = resource_cls(self.namespace, (*self.parts, *parts))
        return resource

    def resolve_path(self, pack_context: PackContext) -> Path:
        registry_path = self.registry_location.resolve_path(pack_context)
        resource_path = Path(registry_path.joinpath(*self.parts))
        return resource_path

    async def resolve_resource(self, pack_context: PackContext) -> ResourceType:
        resource_path = self.resolve_path(pack_context)
        resource = await self.resource_class.load(resource_path)
        return resource

    # @implements CommandToken
    def command_stringify(self) -> str:
        return self.name

    @property
    def namespace(self) -> Namespace:
        return self.registry_location.namespace

    @property
    def name(self) -> str:
        trail = "/".join(self.parts)
        return f"{self.namespace}:{trail}"
