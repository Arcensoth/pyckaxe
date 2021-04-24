from .function import FunctionCommand
from .setblock import SetblockCommand


class function:
    def __get__(self, *_) -> FunctionCommand:
        return FunctionCommand(None)


class setblock:
    def __get__(self, *_) -> SetblockCommand:
        return SetblockCommand(None)
