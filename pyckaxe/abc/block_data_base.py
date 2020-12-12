from abc import abstractmethod

from nbtlib import tag
from pyckaxe.command.abc.command_token import CommandToken


class BlockDataBase(CommandToken):
    # @implements CommandToken
    def command_stringify(self) -> str:
        return str(self._nbt().snbt())

    @abstractmethod
    def _nbt(self) -> tag.Compound:
        ...
