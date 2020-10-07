from pyckaxe.commands.v1_16 import commands


def test_trigger():
    assert "trigger" == str(commands.trigger)


def test_trigger_objective():
    assert "trigger myobj" == str(commands.trigger.objective("myobj"))


def test_trigger_objective_call():
    assert "trigger myobj" == str(commands.trigger("myobj"))


def test_trigger_objective_call_add():
    assert "trigger myobj add" == str(commands.trigger("myobj").add)


def test_trigger_objective_call_set():
    assert "trigger myobj set" == str(commands.trigger("myobj").set)


def test_trigger_objective_call_add_value():
    assert "trigger myobj add 1" == str(commands.trigger("myobj").add.value(1))


def test_trigger_objective_call_set_value():
    assert "trigger myobj set 1" == str(commands.trigger("myobj").set.value(1))


def test_trigger_objective_call_add_value_call():
    assert "trigger myobj add 1" == str(commands.trigger("myobj").add(1))


def test_trigger_objective_call_set_value_call():
    assert "trigger myobj set 1" == str(commands.trigger("myobj").set(1))
