from pyckaxe.commands.v1_16 import commands


def test_scoreboard():
    assert "scoreboard" == str(commands.scoreboard)
