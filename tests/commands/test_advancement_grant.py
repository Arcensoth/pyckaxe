from pyckaxe import commands, selectors


def test_advancement_grant():
    assert 'advancement grant' == str(commands.advancement.grant)


def test_advancement_grant_targets():
    assert 'advancement grant @a' == str(commands.advancement.grant.targets(selectors.all_players))


def test_advancement_grant_call():
    assert 'advancement grant @a' == str(commands.advancement.grant(selectors.all_players))


def test_advancement_grant_call_everything():
    assert 'advancement grant @a everything' == str(commands.advancement.grant(selectors.all_players).everything)


def test_advancement_grant_call_from():
    assert 'advancement grant @a from' == str(commands.advancement.grant(selectors.all_players).from_)


def test_advancement_grant_call_from_advancement():
    assert 'advancement grant @a from mynamespace:myadvancement' == str(
        commands.advancement.grant(selectors.all_players).from_.advancement('mynamespace:myadvancement'))


def test_advancement_grant_call_from_call():
    assert 'advancement grant @a from mynamespace:myadvancement' == str(
        commands.advancement.grant(selectors.all_players).from_('mynamespace:myadvancement'))


def test_advancement_grant_call_only_advancement():
    assert 'advancement grant @a only mynamespace:myadvancement' == str(
        commands.advancement.grant(selectors.all_players).only.advancement('mynamespace:myadvancement'))


def test_advancement_grant_call_only_advancement_criteria():
    assert 'advancement grant @a only mynamespace:myadvancement mycriteria' == str(
        commands.advancement.grant(selectors.all_players).only.advancement('mynamespace:myadvancement')
            .criteria('mycriteria'))


def test_advancement_grant_call_only_call():
    assert 'advancement grant @a only mynamespace:myadvancement mycriteria' == str(
        commands.advancement.grant(selectors.all_players).only('mynamespace:myadvancement', 'mycriteria'))


def test_advancement_grant_call_through():
    assert 'advancement grant @a through' == str(commands.advancement.grant(selectors.all_players).through)


def test_advancement_grant_call_through_advancement():
    assert 'advancement grant @a through mynamespace:myadvancement' == str(
        commands.advancement.grant(selectors.all_players).through.advancement('mynamespace:myadvancement'))


def test_advancement_grant_call_through_call():
    assert 'advancement grant @a through mynamespace:myadvancement' == str(
        commands.advancement.grant(selectors.all_players).through('mynamespace:myadvancement'))


def test_advancement_grant_call_until():
    assert 'advancement grant @a until' == str(commands.advancement.grant(selectors.all_players).until)


def test_advancement_grant_call_until_advancement():
    assert 'advancement grant @a until mynamespace:myadvancement' == str(
        commands.advancement.grant(selectors.all_players).until.advancement('mynamespace:myadvancement'))


def test_advancement_grant_call_until_call():
    assert 'advancement grant @a until mynamespace:myadvancement' == str(
        commands.advancement.grant(selectors.all_players).until('mynamespace:myadvancement'))
