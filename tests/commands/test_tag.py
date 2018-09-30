from pyckaxe import commands, selectors


def test_tag():
    assert "tag" == str(commands.tag)


def test_tag_targets():
    assert "tag @a" == str(commands.tag.targets(selectors.all_players))


def test_tag_call():
    assert "tag @a" == str(commands.tag(selectors.all_players))


def test_tag_targets_list():
    assert "tag @a list" == str(commands.tag.targets(selectors.all_players).list)


def test_tag_call_list():
    assert "tag @a list" == str(commands.tag(selectors.all_players).list)


def test_tag_call_add():
    assert "tag @a add" == str(commands.tag(selectors.all_players).add)


def test_tag_call_add_tag():
    assert "tag @a add sometag" == str(
        commands.tag(selectors.all_players).add.tag("sometag")
    )


def test_tag_call_add_call():
    assert "tag @a add sometag" == str(
        commands.tag(selectors.all_players).add("sometag")
    )


def test_tag_call_remove():
    assert "tag @a remove" == str(commands.tag(selectors.all_players).remove)


def test_tag_call_remove_tag():
    assert "tag @a remove sometag" == str(
        commands.tag(selectors.all_players).remove.tag("sometag")
    )


def test_tag_call_remove_call():
    assert "tag @a remove sometag" == str(
        commands.tag(selectors.all_players).remove("sometag")
    )
