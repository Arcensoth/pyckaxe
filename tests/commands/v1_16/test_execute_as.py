from pyckaxe import selectors
from pyckaxe.commands.v1_16 import commands


def test_execute_as():
    assert "execute as" == str(commands.execute.as_)


def test_execute_as_targets():
    assert "execute as @a" == str(commands.execute.as_.targets(selectors.all_players))


def test_execute_as_call():
    assert "execute as @a" == str(commands.execute.as_(selectors.all_players))
