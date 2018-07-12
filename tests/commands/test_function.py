from pyckaxe import commands


def test_function():
    assert 'function' == str(commands.function)


def test_function_name():
    assert 'function myfunction' == str(commands.function.name('myfunction'))


def test_function_call():
    assert 'function myfunction' == str(commands.function('myfunction'))
