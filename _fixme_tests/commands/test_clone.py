from pyckaxe import blocks, commands


def test_clone():
    assert "clone" == str(commands.clone)


def test_clone_begin():
    assert "clone ~ ~ ~" == str(commands.clone.begin([0, 0, 0]))


def test_clone_begin_end():
    assert "clone ~ ~ ~ ~ ~ ~" == str(commands.clone.begin([0, 0, 0]).end([0, 0, 0]))


def test_clone_begin_end_destination():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~" == str(
        commands.clone.begin([0, 0, 0]).end([0, 0, 0]).destination([0, 0, 0])
    )


def test_clone_call():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~" == str(commands.clone([0, 0, 0], [0, 0, 0], [0, 0, 0]))


def test_clone_call_filtered():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ filtered" == str(
        commands.clone([0, 0, 0], [0, 0, 0], [0, 0, 0]).filtered
    )


def test_clone_call_filtered_filter():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ filtered minecraft:dirt" == str(
        commands.clone([0, 0, 0], [0, 0, 0], [0, 0, 0]).filtered.filter(blocks.dirt)
    )


def test_clone_call_filtered_call():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ filtered minecraft:dirt" == str(
        commands.clone([0, 0, 0], [0, 0, 0], [0, 0, 0]).filtered(blocks.dirt)
    )


def test_clone_call_filtered_call_force():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ filtered minecraft:dirt force" == str(
        commands.clone([0, 0, 0], [0, 0, 0], [0, 0, 0]).filtered(blocks.dirt).force
    )


def test_clone_call_filtered_call_move():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ filtered minecraft:dirt move" == str(
        commands.clone([0, 0, 0], [0, 0, 0], [0, 0, 0]).filtered(blocks.dirt).move
    )


def test_clone_call_filtered_call_normal():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ filtered minecraft:dirt normal" == str(
        commands.clone([0, 0, 0], [0, 0, 0], [0, 0, 0]).filtered(blocks.dirt).normal
    )


def test_clone_call_masked():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ masked" == str(
        commands.clone([0, 0, 0], [0, 0, 0], [0, 0, 0]).masked
    )


def test_clone_call_masked_force():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ masked force" == str(
        commands.clone([0, 0, 0], [0, 0, 0], [0, 0, 0]).masked.force
    )


def test_clone_call_masked_move():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ masked move" == str(
        commands.clone([0, 0, 0], [0, 0, 0], [0, 0, 0]).masked.move
    )


def test_clone_call_masked_normal():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ masked normal" == str(
        commands.clone([0, 0, 0], [0, 0, 0], [0, 0, 0]).masked.normal
    )


def test_clone_call_replace():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ replace" == str(
        commands.clone([0, 0, 0], [0, 0, 0], [0, 0, 0]).replace
    )


def test_clone_call_replace_force():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ replace force" == str(
        commands.clone([0, 0, 0], [0, 0, 0], [0, 0, 0]).replace.force
    )


def test_clone_call_replace_move():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ replace move" == str(
        commands.clone([0, 0, 0], [0, 0, 0], [0, 0, 0]).replace.move
    )


def test_clone_call_replace_normal():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ replace normal" == str(
        commands.clone([0, 0, 0], [0, 0, 0], [0, 0, 0]).replace.normal
    )
