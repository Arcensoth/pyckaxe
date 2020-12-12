from pyckaxe import selectors
from pyckaxe import commands


def test_kill():
    assert "kill" == str(commands.kill)


def test_kill_targets():
    assert "kill @a" == str(commands.kill.targets(selectors.all_players))


def test_kill_call():
    assert "kill @a" == str(commands.kill(selectors.all_players))
