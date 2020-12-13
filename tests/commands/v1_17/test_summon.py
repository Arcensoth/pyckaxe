from pyckaxe import Position, commands, entities


def test_summon():
    assert "summon" == str(commands.summon)


def test_summon_entity():
    assert "summon minecraft:area_effect_cloud" == str(
        commands.summon.entity(entities.area_effect_cloud)
    )


def test_summon_entity_position():
    assert "summon minecraft:area_effect_cloud ~ ~ ~" == str(
        commands.summon.entity(entities.area_effect_cloud).position(~Position.zero())
    )


def test_summon_entity_position_nbt():
    assert "summon minecraft:area_effect_cloud ~ ~ ~ {Duration:100}" == str(
        commands.summon.entity(entities.area_effect_cloud)
        .position(~Position.zero())
        .nbt("{Duration:100}")
    )


def test_summon_call():
    assert "summon minecraft:area_effect_cloud ~ ~ ~ {Duration:100}" == str(
        commands.summon(entities.area_effect_cloud, ~Position.zero(), "{Duration:100}")
    )
