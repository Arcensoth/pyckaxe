from pyckaxe import anchors, commands, rotations, selectors


def test_teleport():
    assert "teleport" == str(commands.teleport)


def test_teleport_destination():
    assert "teleport @r" == str(commands.teleport.destination(selectors.random))


def test_teleport_location():
    assert "teleport ~ ~ ~" == str(commands.teleport.location([0, 0, 0]))


def test_teleport_targets():
    assert "teleport @a" == str(commands.teleport.targets(selectors.all_players))


def test_teleport_targets_destination():
    assert "teleport @a @r" == str(
        commands.teleport.targets(selectors.all_players).destination(selectors.random)
    )


def test_teleport_targets_location():
    assert "teleport @a ~ ~ ~" == str(
        commands.teleport.targets(selectors.all_players).location([0, 0, 0])
    )


def test_teleport_call():
    assert "teleport @a ~ ~ ~" == str(commands.teleport(selectors.all_players, [0, 0, 0]))


def test_teleport_call_rotation():
    assert "teleport @a ~ ~ ~ ~ ~" == str(
        commands.teleport(selectors.all_players, [0, 0, 0]).rotation(rotations.relative)
    )


def test_teleport_call_call():
    assert "teleport @a ~ ~ ~ ~ ~" == str(
        commands.teleport(selectors.all_players, [0, 0, 0])(rotations.relative)
    )


def test_teleport_call_facing():
    assert "teleport @a ~ ~ ~ facing" == str(
        commands.teleport(selectors.all_players, [0, 0, 0]).facing
    )


def test_teleport_call_facing_location():
    assert "teleport @a ~ ~ ~ facing ~ ~ ~" == str(
        commands.teleport(selectors.all_players, [0, 0, 0]).facing.location([0, 0, 0])
    )


def test_teleport_call_facing_call():
    assert "teleport @a ~ ~ ~ facing ~ ~ ~" == str(
        commands.teleport(selectors.all_players, [0, 0, 0]).facing([0, 0, 0])
    )


def test_teleport_call_facing_entity():
    assert "teleport @a ~ ~ ~ facing entity" == str(
        commands.teleport(selectors.all_players, [0, 0, 0]).facing.entity
    )


def test_teleport_call_facing_entity_entity():
    assert "teleport @a ~ ~ ~ facing entity @r" == str(
        commands.teleport(selectors.all_players, [0, 0, 0]).facing.entity.entity(selectors.random)
    )


def test_teleport_call_facing_entity_entity_anchor():
    assert "teleport @a ~ ~ ~ facing entity @r eyes" == str(
        commands.teleport(selectors.all_players, [0, 0, 0])
        .facing.entity.entity(selectors.random)
        .anchor(anchors.eyes)
    )


def test_teleport_call_facing_entity_call():
    assert "teleport @a ~ ~ ~ facing entity @r eyes" == str(
        commands.teleport(selectors.all_players, [0, 0, 0]).facing.entity(
            selectors.random, anchors.eyes
        )
    )
