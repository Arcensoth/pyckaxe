from pyckaxe import commands, selectors


def test_scoreboard_players():
    assert "scoreboard players" == str(commands.scoreboard.players)


# scoreboard players add


def test_scoreboard_players_add():
    assert "scoreboard players add" == str(commands.scoreboard.players.add)


def test_scoreboard_players_add_targets():
    assert "scoreboard players add @a" == str(
        commands.scoreboard.players.add.targets(selectors.all_players)
    )


def test_scoreboard_players_add_targets_objective():
    assert "scoreboard players add @a myobj" == str(
        commands.scoreboard.players.add.targets(selectors.all_players).objective("myobj")
    )


def test_scoreboard_players_add_targets_objective_score():
    assert "scoreboard players add @a myobj 1" == str(
        commands.scoreboard.players.add.targets(selectors.all_players).objective("myobj").score(1)
    )


def test_scoreboard_players_add_call():
    assert "scoreboard players add @a myobj 1" == str(
        commands.scoreboard.players.add(selectors.all_players, "myobj", 1)
    )


# scoreboard players enable


def test_scoreboard_players_enable():
    assert "scoreboard players enable" == str(commands.scoreboard.players.enable)


def test_scoreboard_players_enable_targets():
    assert "scoreboard players enable @a" == str(
        commands.scoreboard.players.enable.targets(selectors.all_players)
    )


def test_scoreboard_players_enable_targets_objective():
    assert "scoreboard players enable @a myobj" == str(
        commands.scoreboard.players.enable.targets(selectors.all_players).objective("myobj")
    )


def test_scoreboard_players_enable_call():
    assert "scoreboard players enable @a myobj" == str(
        commands.scoreboard.players.enable(selectors.all_players, "myobj")
    )


# scoreboard players get


def test_scoreboard_players_get():
    assert "scoreboard players get" == str(commands.scoreboard.players.get)


def test_scoreboard_players_get_targets():
    assert "scoreboard players get @a" == str(
        commands.scoreboard.players.get.targets(selectors.all_players)
    )


def test_scoreboard_players_get_targets_objective():
    assert "scoreboard players get @a myobj" == str(
        commands.scoreboard.players.get.targets(selectors.all_players).objective("myobj")
    )


def test_scoreboard_players_get_call():
    assert "scoreboard players get @a myobj" == str(
        commands.scoreboard.players.get(selectors.all_players, "myobj")
    )


# scoreboard players list


def test_scoreboard_players_list():
    assert "scoreboard players list" == str(commands.scoreboard.players.list)


def test_scoreboard_players_list_targets():
    assert "scoreboard players list @a" == str(
        commands.scoreboard.players.list.targets(selectors.all_players)
    )


def test_scoreboard_players_list_call():
    assert "scoreboard players list @a" == str(
        commands.scoreboard.players.list(selectors.all_players)
    )


# scoreboard players operation


def test_scoreboard_players_operation():
    assert "scoreboard players operation" == str(commands.scoreboard.players.operation)


def test_scoreboard_players_operation_targets():
    assert "scoreboard players operation @a" == str(
        commands.scoreboard.players.operation.targets(selectors.all_players)
    )


def test_scoreboard_players_operation_targets_objective():
    assert "scoreboard players operation @a myobj" == str(
        commands.scoreboard.players.operation.targets(selectors.all_players).objective("myobj")
    )


def test_scoreboard_players_operation_targets_objective_operation():
    assert "scoreboard players operation @a myobj =" == str(
        commands.scoreboard.players.operation.targets(selectors.all_players)
        .objective("myobj")
        .assign
    )


def test_scoreboard_players_operation_targets_objective_operation_source():
    assert "scoreboard players operation @a myobj = @r" == str(
        commands.scoreboard.players.operation.targets(selectors.all_players)
        .objective("myobj")
        .assign.source(selectors.random)
    )


def test_scoreboard_players_operation_targets_objective_operation_source_objective():
    assert "scoreboard players operation @a myobj = @r anotherobj" == str(
        commands.scoreboard.players.operation.targets(selectors.all_players)
        .objective("myobj")
        .assign.source(selectors.random)
        .objective("anotherobj")
    )


def test_scoreboard_players_operation_call():
    assert "scoreboard players operation @a myobj = @r anotherobj" == str(
        commands.scoreboard.players.operation(selectors.all_players, "myobj").assign(
            selectors.random,
            "anotherobj",
        )
    )


# scoreboard players remove


def test_scoreboard_players_remove():
    assert "scoreboard players remove" == str(commands.scoreboard.players.remove)


def test_scoreboard_players_remove_targets():
    assert "scoreboard players remove @a" == str(
        commands.scoreboard.players.remove.targets(selectors.all_players)
    )


def test_scoreboard_players_remove_targets_objective():
    assert "scoreboard players remove @a myobj" == str(
        commands.scoreboard.players.remove.targets(selectors.all_players).objective("myobj")
    )


def test_scoreboard_players_remove_targets_objective_score():
    assert "scoreboard players remove @a myobj 1" == str(
        commands.scoreboard.players.remove.targets(selectors.all_players)
        .objective("myobj")
        .score(1)
    )


def test_scoreboard_players_remove_call():
    assert "scoreboard players remove @a myobj 1" == str(
        commands.scoreboard.players.remove(selectors.all_players, "myobj", 1)
    )


# scoreboard players reset


def test_scoreboard_players_reset():
    assert "scoreboard players reset" == str(commands.scoreboard.players.reset)


def test_scoreboard_players_reset_targets():
    assert "scoreboard players reset @a" == str(
        commands.scoreboard.players.reset.targets(selectors.all_players)
    )


def test_scoreboard_players_reset_targets_objective():
    assert "scoreboard players reset @a myobj" == str(
        commands.scoreboard.players.reset.targets(selectors.all_players).objective("myobj")
    )


def test_scoreboard_players_reset_call():
    assert "scoreboard players reset @a myobj" == str(
        commands.scoreboard.players.reset(selectors.all_players, "myobj")
    )


# scoreboard players set


def test_scoreboard_players_set():
    assert "scoreboard players set" == str(commands.scoreboard.players.set)


def test_scoreboard_players_set_targets():
    assert "scoreboard players set @a" == str(
        commands.scoreboard.players.set.targets(selectors.all_players)
    )


def test_scoreboard_players_set_targets_objective():
    assert "scoreboard players set @a myobj" == str(
        commands.scoreboard.players.set.targets(selectors.all_players).objective("myobj")
    )


def test_scoreboard_players_set_targets_objective_score():
    assert "scoreboard players set @a myobj 1" == str(
        commands.scoreboard.players.set.targets(selectors.all_players).objective("myobj").score(1)
    )


def test_scoreboard_players_set_call():
    assert "scoreboard players set @a myobj 1" == str(
        commands.scoreboard.players.set(selectors.all_players, "myobj", 1)
    )
