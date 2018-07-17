import pytest

from pyckaxe.command.abc.command import CommandNode
from pyckaxe.command.raw_command import RawCommand


def test_command_convert_str():
    assert 'mystring' == str(CommandNode(None, 'mystring'))


def test_command_convert_int():
    assert '123' == str(CommandNode(None, 123))


def test_command_convert_int_neg():
    assert '-321' == str(CommandNode(None, -321))


def test_command_convert_float():
    assert '1.13' == str(CommandNode(None, 1.13))


def test_command_convert_float_neg():
    assert '-1.12' == str(CommandNode(None, -1.12))


def test_command_convert_float_whole():
    assert '1.0' == str(CommandNode(None, 1.0))


def test_command_convert_bool_true():
    assert 'true' == str(CommandNode(None, True))


def test_command_convert_bool_false():
    assert 'false' == str(CommandNode(None, False))


def test_command_convert_none():
    with pytest.raises(ValueError):
        str(CommandNode(None, None))


def test_raw_command():
    assert 'this is not a real command' == str(RawCommand('this is not a real command'))
