from pyckaxe import Position, anchors, commands, rotations, selectors


def test_teleport():
    assert "teleport" == str(commands.teleport)


def test_teleport_destination():
    assert "teleport @r" == str(commands.teleport.destination(selectors.random))


def test_teleport_location():
    assert "teleport ~ ~ ~" == str(commands.teleport.location(~Position.zero()))


def test_teleport_targets():
    assert "teleport @a" == str(commands.teleport.targets(selectors.all_players))


def test_teleport_targets_destination():
    assert "teleport @a @r" == str(
        commands.teleport.targets(selectors.all_players).destination(selectors.random)
    )


def test_teleport_targets_location():
    assert "teleport @a ~ ~ ~" == str(
        commands.teleport.targets(selectors.all_players).location(~Position.zero())
    )


def test_teleport_call():
    assert "teleport @a ~ ~ ~" == str(commands.teleport(selectors.all_players, ~Position.zero()))


def test_teleport_call_rotation():
    assert "teleport @a ~ ~ ~ ~ ~" == str(
        commands.teleport(selectors.all_players, ~Position.zero()).rotation(rotations.relative)
    )


def test_teleport_call_call():
    assert "teleport @a ~ ~ ~ ~ ~" == str(
        commands.teleport(selectors.all_players, ~Position.zero())(rotations.relative)
    )


def test_teleport_call_facing():
    assert "teleport @a ~ ~ ~ facing" == str(
        commands.teleport(selectors.all_players, ~Position.zero()).facing
    )


def test_teleport_call_facing_location():
    assert "teleport @a ~ ~ ~ facing ~ ~ ~" == str(
        commands.teleport(selectors.all_players, ~Position.zero()).facing.location(~Position.zero())
    )


def test_teleport_call_facing_call():
    assert "teleport @a ~ ~ ~ facing ~ ~ ~" == str(
        commands.teleport(selectors.all_players, ~Position.zero()).facing(~Position.zero())
    )


def test_teleport_call_facing_entity():
    assert "teleport @a ~ ~ ~ facing entity" == str(
        commands.teleport(selectors.all_players, ~Position.zero()).facing.entity
    )


def test_teleport_call_facing_entity_entity():
    assert "teleport @a ~ ~ ~ facing entity @r" == str(
        commands.teleport(selectors.all_players, ~Position.zero()).facing.entity.entity(
            selectors.random
        )
    )


def test_teleport_call_facing_entity_entity_anchor():
    assert "teleport @a ~ ~ ~ facing entity @r eyes" == str(
        commands.teleport(selectors.all_players, ~Position.zero())
        .facing.entity.entity(selectors.random)
        .anchor(anchors.eyes)
    )


def test_teleport_call_facing_entity_call():
    assert "teleport @a ~ ~ ~ facing entity @r eyes" == str(
        commands.teleport(selectors.all_players, ~Position.zero()).facing.entity(
            selectors.random, anchors.eyes
        )
    )
