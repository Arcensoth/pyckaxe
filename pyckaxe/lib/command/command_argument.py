from typing import (
    Any,
    Callable,
    ClassVar,
    Generic,
    Iterator,
    Optional,
    Type,
    TypeVar,
    cast,
)

from pyckaxe.lib.command.command_node import CommandNode

__all__ = (
    "CommandArgument",
    "command_argument",
)


ArgumentType = TypeVar("ArgumentType")


class CommandArgument(CommandNode, Generic[ArgumentType]):
    """A node in the command hierarchy that resolves to a dynamic argument."""

    _tokenizer: ClassVar[Callable[[ArgumentType], str]] = str

    def __init__(self, parent: Optional[CommandNode], argument: ArgumentType):
        super().__init__(parent)
        self._argument: ArgumentType = argument

    # @overrides CommandNode
    def __iter__(self) -> Iterator[str]:
        yield from super().__iter__()
        tokenizer = cast(Callable[[ArgumentType], str], self._tokenizer)
        yield tokenizer(self._argument)


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
