from pyckaxe.commands.v1_16 import commands


def test_say():
    assert "say" == str(commands.say)


def test_say_message():
    assert "say hello" == str(commands.say.message("hello"))


def test_say_call():
    assert "say hello" == str(commands.say("hello"))
