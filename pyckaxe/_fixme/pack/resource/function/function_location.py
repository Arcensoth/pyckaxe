from pyckaxe.pack.resource.abc.resource_location import ResourceLocation
from pyckaxe.pack.resource.function.function import Function


class FunctionLocation(ResourceLocation[Function]):
    resource_class = Function
    registry_parts = ("functions",)
