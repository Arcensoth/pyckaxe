from pyckaxe import commands, selectors


def test_advancement_revoke():
    assert "advancement revoke" == str(commands.advancement.revoke)


def test_advancement_revoke_targets():
    assert "advancement revoke @a" == str(
        commands.advancement.revoke.targets(selectors.all_players)
    )


def test_advancement_revoke_call():
    assert "advancement revoke @a" == str(
        commands.advancement.revoke(selectors.all_players)
    )


def test_advancement_revoke_call_everything():
    assert "advancement revoke @a everything" == str(
        commands.advancement.revoke(selectors.all_players).everything
    )


def test_advancement_revoke_call_from():
    assert "advancement revoke @a from" == str(
        commands.advancement.revoke(selectors.all_players).from_
    )


def test_advancement_revoke_call_from_advancement():
    assert "advancement revoke @a from mynamespace:myadvancement" == str(
        commands.advancement.revoke(selectors.all_players).from_.advancement(
            "mynamespace:myadvancement"
        )
    )


def test_advancement_revoke_call_from_call():
    assert "advancement revoke @a from mynamespace:myadvancement" == str(
        commands.advancement.revoke(selectors.all_players).from_(
            "mynamespace:myadvancement"
        )
    )


def test_advancement_revoke_call_only_advancement():
    assert "advancement revoke @a only mynamespace:myadvancement" == str(
        commands.advancement.revoke(selectors.all_players).only.advancement(
            "mynamespace:myadvancement"
        )
    )


def test_advancement_revoke_call_only_advancement_criteria():
    assert "advancement revoke @a only mynamespace:myadvancement mycriteria" == str(
        commands.advancement.revoke(selectors.all_players)
        .only.advancement("mynamespace:myadvancement")
        .criteria("mycriteria")
    )


def test_advancement_revoke_call_only_call():
    assert "advancement revoke @a only mynamespace:myadvancement mycriteria" == str(
        commands.advancement.revoke(selectors.all_players).only(
            "mynamespace:myadvancement", "mycriteria"
        )
    )


def test_advancement_revoke_call_through():
    assert "advancement revoke @a through" == str(
        commands.advancement.revoke(selectors.all_players).through
    )


def test_advancement_revoke_call_through_advancement():
    assert "advancement revoke @a through mynamespace:myadvancement" == str(
        commands.advancement.revoke(selectors.all_players).through.advancement(
            "mynamespace:myadvancement"
        )
    )


def test_advancement_revoke_call_through_call():
    assert "advancement revoke @a through mynamespace:myadvancement" == str(
        commands.advancement.revoke(selectors.all_players).through(
            "mynamespace:myadvancement"
        )
    )


def test_advancement_revoke_call_until():
    assert "advancement revoke @a until" == str(
        commands.advancement.revoke(selectors.all_players).until
    )


def test_advancement_revoke_call_until_advancement():
    assert "advancement revoke @a until mynamespace:myadvancement" == str(
        commands.advancement.revoke(selectors.all_players).until.advancement(
            "mynamespace:myadvancement"
        )
    )


def test_advancement_revoke_call_until_call():
    assert "advancement revoke @a until mynamespace:myadvancement" == str(
        commands.advancement.revoke(selectors.all_players).until(
            "mynamespace:myadvancement"
        )
    )
