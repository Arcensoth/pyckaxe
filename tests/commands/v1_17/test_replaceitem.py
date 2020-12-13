from pyckaxe import commands, item_slots, items, selectors


def test_replaceitem():
    assert "replaceitem" == str(commands.replaceitem)


def test_replaceitem_block():
    assert "replaceitem block" == str(commands.replaceitem.block)


def test_replaceitem_block_position():
    assert "replaceitem block ~ ~ ~" == str(commands.replaceitem.block.position([0, 0, 0]))


def test_replaceitem_block_position_slot():
    assert "replaceitem block ~ ~ ~ slot.container.13" == str(
        commands.replaceitem.block.position([0, 0, 0]).slot(item_slots.slot_container_13)
    )


def test_replaceitem_block_position_slot_item():
    assert "replaceitem block ~ ~ ~ slot.container.13 minecraft:diamond" == str(
        commands.replaceitem.block.position([0, 0, 0])
        .slot(item_slots.slot_container_13)
        .item(items.diamond)
    )


def test_replaceitem_block_position_slot_item_count():
    assert "replaceitem block ~ ~ ~ slot.container.13 minecraft:diamond 64" == str(
        commands.replaceitem.block.position([0, 0, 0])
        .slot(item_slots.slot_container_13)
        .item(items.diamond)
        .count(64)
    )


def test_replaceitem_block_call():
    assert "replaceitem block ~ ~ ~ slot.container.13 minecraft:diamond 64" == str(
        commands.replaceitem.block([0, 0, 0], item_slots.slot_container_13, items.diamond, 64)
    )


def test_replaceitem_entity():
    assert "replaceitem entity" == str(commands.replaceitem.entity)


def test_replaceitem_entity_targets():
    assert "replaceitem entity @a" == str(
        commands.replaceitem.entity.targets(selectors.all_players)
    )


def test_replaceitem_entity_targets_slot():
    assert "replaceitem entity @a slot.weapon.mainhand" == str(
        commands.replaceitem.entity.targets(selectors.all_players).slot(
            item_slots.slot_weapon_mainhand
        )
    )


def test_replaceitem_entity_targets_slot_item():
    assert "replaceitem entity @a slot.weapon.mainhand minecraft:diamond" == str(
        commands.replaceitem.entity.targets(selectors.all_players)
        .slot(item_slots.slot_weapon_mainhand)
        .item(items.diamond)
    )


def test_replaceitem_entity_targets_slot_item_count():
    assert "replaceitem entity @a slot.weapon.mainhand minecraft:diamond 64" == str(
        commands.replaceitem.entity.targets(selectors.all_players)
        .slot(item_slots.slot_weapon_mainhand)
        .item(items.diamond)
        .count(64)
    )


def test_replaceitem_entity_call():
    assert "replaceitem entity @a slot.weapon.mainhand minecraft:diamond 64" == str(
        commands.replaceitem.entity(
            selectors.all_players, item_slots.slot_weapon_mainhand, items.diamond, 64
        )
    )