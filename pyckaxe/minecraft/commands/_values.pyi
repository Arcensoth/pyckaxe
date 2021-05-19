from .function import FunctionCommand
from .setblock import SetblockCommand

# NOTE These stubs help Pylance recognize the descriptors correctly.
#   Without them, Pylance complains about an unknown variable type when accessing the
#   the descriptors - but only from *outside* of Pyckaxe itself.

class commands:
    function: FunctionCommand
    setblock: SetblockCommand
