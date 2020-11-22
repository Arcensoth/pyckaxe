from abc import abstractmethod
from typing import Any, Iterable, Tuple

from pyckaxe.command.abc.command_token import CommandToken


class BlockStateBase(CommandToken):
    # @implements CommandToken
    def command_stringify(self) -> str:
        innards = ",".join(f"{k}={v}" for k, v in self._items())
        return f"[{innards}]"

    @abstractmethod
    def _items(self) -> Iterable[Tuple[str, Any]]:
        ...
