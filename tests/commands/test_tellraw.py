from pyckaxe import commands, selectors


def test_tellraw():
    assert 'tellraw' == str(commands.tellraw)


def test_tellraw_targets():
    assert 'tellraw @a' == str(commands.tellraw.targets(selectors.all_players))


def test_tellraw_targets_message_with_str():
    assert 'tellraw @a {"text": "hello"}' == str(
        commands.tellraw.targets(selectors.all_players).message('{"text": "hello"}'))


# TODO enable once type generics and implicit conversions are implemented
# def test_tellraw_targets_message_with_dict():
#     assert 'tellraw @a {"text": "hello"}' == str(
#         commands.tellraw.targets(selectors.all_players).message({'text': 'hello'}))
#
#
# def test_tellraw_targets_message_with_list():
#     assert 'tellraw @a [{"text": "hello"}]' == str(
#         commands.tellraw.targets(selectors.all_players).message([{'text': 'hello'}]))


def test_tellraw_call():
    assert 'tellraw @a [{"text": "hello"}]' == str(
        commands.tellraw(selectors.all_players, '{"text": "hello"}'))
