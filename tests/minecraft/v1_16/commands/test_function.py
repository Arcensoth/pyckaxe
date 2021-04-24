from pyckaxe.minecraft import commands


def test_function():
    c1 = commands.function
    assert str(c1) == "function"


def test_function_dot_name():
    c1 = commands.function.name("foo:bar")
    assert str(c1) == "function foo:bar"


def test_function_call_name():
    c1 = commands.function("foo:bar")
    assert str(c1) == "function foo:bar"
