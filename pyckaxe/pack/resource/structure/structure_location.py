from pyckaxe.pack.resource.abc.resource_location import ResourceLocation
from pyckaxe.pack.resource.structure.structure import Structure


class StructureLocation(ResourceLocation[Structure]):
    resource_class = Structure
    registry_parts = ("structures",)
