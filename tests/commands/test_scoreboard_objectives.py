from pyckaxe import commands, scoreboard_slots


def test_scoreboard_objectives():
    assert 'scoreboard objectives' == str(commands.scoreboard.objectives)


# scoreboard objectives add


def test_scoreboard_objectives_add():
    assert 'scoreboard objectives add' == str(commands.scoreboard.objectives.add)


def test_scoreboard_objectives_add_objective():
    assert 'scoreboard objectives add myobj' == str(commands.scoreboard.objectives.add.objective('myobj'))


def test_scoreboard_objectives_add_objective_criteria():
    assert 'scoreboard objectives add myobj dummy' == str(
        commands.scoreboard.objectives.add.objective('myobj').criteria('dummy'))


def test_scoreboard_objectives_add_objective_criteria_display_name():
    assert 'scoreboard objectives add myobj dummy My Objective' == str(
        commands.scoreboard.objectives.add.objective('myobj').criteria('dummy').display_name('My Objective'))


def test_scoreboard_objectives_add_call():
    assert 'scoreboard objectives add myobj dummy My Objective' == str(
        commands.scoreboard.objectives.add('myobj', 'dummy', 'My Objective'))


# scoreboard objectives list


def test_scoreboard_objectives_list():
    assert 'scoreboard objectives list' == str(commands.scoreboard.objectives.list)


# scoreboard objectives modify


def test_scoreboard_objectives_modify():
    assert 'scoreboard objectives modify' == str(commands.scoreboard.objectives.modify)


def test_scoreboard_objectives_modify_objective():
    assert 'scoreboard objectives modify myobj' == str(commands.scoreboard.objectives.modify.objective('myobj'))


def test_scoreboard_objectives_modify_call():
    assert 'scoreboard objectives modify myobj' == str(commands.scoreboard.objectives.modify('myobj'))


def test_scoreboard_objectives_modify_call_displayname():
    assert 'scoreboard objectives modify myobj displayname' == str(
        commands.scoreboard.objectives.modify('myobj').displayname)


def test_scoreboard_objectives_modify_call_displayname_display_name():
    assert 'scoreboard objectives modify myobj displayname anotherobj' == str(
        commands.scoreboard.objectives.modify('myobj').displayname.display_name('anotherobj'))


def test_scoreboard_objectives_modify_call_displayname_call():
    assert 'scoreboard objectives modify myobj displayname anotherobj' == str(
        commands.scoreboard.objectives.modify('myobj').displayname('anotherobj'))


# scoreboard objectives remove


def test_scoreboard_objectives_remove():
    assert 'scoreboard objectives remove' == str(commands.scoreboard.objectives.remove)


def test_scoreboard_objectives_remove_objective():
    assert 'scoreboard objectives remove myobj' == str(commands.scoreboard.objectives.remove.objective('myobj'))


def test_scoreboard_objectives_remove_call():
    assert 'scoreboard objectives remove myobj' == str(commands.scoreboard.objectives.remove('myobj'))


# scoreboard objectives setdisplay


def test_scoreboard_objectives_setdisplay():
    assert 'scoreboard objectives setdisplay' == str(commands.scoreboard.objectives.setdisplay)


def test_scoreboard_objectives_setdisplay_slot():
    assert 'scoreboard objectives setdisplay sidebar' == str(
        commands.scoreboard.objectives.setdisplay.slot(scoreboard_slots.sidebar))


def test_scoreboard_objectives_setdisplay_slot_objective():
    assert 'scoreboard objectives setdisplay sidebar myobj' == str(
        commands.scoreboard.objectives.setdisplay.slot(scoreboard_slots.sidebar).objective('myobj'))


def test_scoreboard_objectives_setdisplay_call():
    assert 'scoreboard objectives setdisplay sidebar myobj' == str(
        commands.scoreboard.objectives.setdisplay(scoreboard_slots.sidebar, 'myobj'))


def test_scoreboard_objectives_setdisplay_slot_with_dots():
    assert 'scoreboard objectives setdisplay sidebar.team.red myobj' == str(
        commands.scoreboard.objectives.setdisplay(scoreboard_slots.sidebar_team_red, 'myobj'))
