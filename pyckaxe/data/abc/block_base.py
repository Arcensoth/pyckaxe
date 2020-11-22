from typing import Iterable

from pyckaxe.command.abc.command_token import CommandToken


class BlockBase(CommandToken):
    # @implements CommandToken
    def command_stringify(self) -> str:
        return "".join(self._command_stringify())

    def _command_stringify(self) -> Iterable[str]:
        yield self.NAME
        if self.state is not None:
            yield self.state.command_stringify()
        if self.data is not None:
            yield self.data.command_stringify()
