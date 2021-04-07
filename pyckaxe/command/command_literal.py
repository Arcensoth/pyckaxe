from typing import Callable, ClassVar, Iterable, Optional, Type, TypeVar

from pyckaxe.command.command_node import CommandNode

__all__ = (
    "CommandLiteral",
    "command_literal",
)


SelfType = TypeVar("SelfType", bound="CommandNode")


class CommandLiteral(CommandNode):
    """ A node in the command hierarchy that resolves to a literal string. """

    _literal: ClassVar[Optional[str]] = None

    def __call__(self: SelfType) -> SelfType:
        """
        Return the node itself, with no effect.

        This can be used to influence code formatters such as black to split the
        command via method-chaining (fluent interface) style.
        """
        return self

    # @overrides CommandNode
    def _command_tokens(self) -> Iterable[str]:
        yield from super()._command_tokens()
        if self._literal is not None:
            yield self._literal


WrappedType = TypeVar("WrappedType", bound=CommandLiteral)


def command_literal(literal: str) -> Callable[[Type[WrappedType]], Type[WrappedType]]:
    """
    Class decorator that streamlines the process of declaring a new type of literal.

    Simply sets the [_literal] class field to the given literal.
    """

    def wrap(cls: Type[WrappedType]) -> Type[WrappedType]:
        setattr(cls, "_literal", literal)
        return cls

    return wrap
