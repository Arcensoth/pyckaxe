from dataclasses import dataclass

from pyckaxe.lib.resource.function.function import Function

__all__ = ("FunctionSerializer",)


# @implements ResourceSerializer[Function, str]
@dataclass
class FunctionSerializer:
    # @implements ResourceSerializer[Function, str]
    def __call__(self, resource: Function) -> str:
        return self.serialize(resource)

    def serialize(self, function: Function) -> str:
        return "\n".join(str(line) for line in function.lines)
