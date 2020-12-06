from pyckaxe.pack.resource.abc.located_resource import LocatedResource
from pyckaxe.pack.resource.function.function import Function
from pyckaxe.pack.resource.function.function_location import FunctionLocation


class LocatedFunction(LocatedResource[Function, FunctionLocation]):
    pass
