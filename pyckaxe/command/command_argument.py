from dataclasses import dataclass
from typing import Any, Callable, ClassVar, Generic, Iterable, Optional, Type, TypeVar

from pyckaxe.command.command_node import CommandNode

__all__ = (
    "CommandArgument",
    "command_argument",
)


ArgumentType = TypeVar("ArgumentType")


@dataclass
class CommandArgument(CommandNode, Generic[ArgumentType]):
    """ A node in the command hierarchy that resolves to a dynamic argument. """

    _tokenizer: ClassVar[Callable[[ArgumentType], str]] = str

    def __init__(self, parent: Optional[CommandNode], argument: ArgumentType):
        super().__init__(parent)
        self._argument: ArgumentType = argument

    # @overrides CommandNode
    def _command_tokens(self) -> Iterable[str]:
        yield from super()._command_tokens()
        yield self._tokenizer(self._argument)


WrappedType = TypeVar("WrappedType", bound=CommandArgument[Any])


def command_argument(
    type_: Type[ArgumentType],
    tokenizer: Optional[Callable[[ArgumentType], str]] = None,
) -> Callable[[Type[WrappedType]], Type[WrappedType]]:
    """
    Class decorator that streamlines the process of declaring a new type of argument.

    Sets the [_tokenizer] class field to the given function, if any.
    """

    def wrap(cls: Type[WrappedType]) -> Type[WrappedType]:
        if tokenizer is not None:
            setattr(cls, "_tokenizer", tokenizer)
        return cls

    return wrap
