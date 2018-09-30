from pyckaxe import blocks, commands, positions


def test_clone():
    assert "clone" == str(commands.clone)


def test_clone_begin():
    assert "clone ~ ~ ~" == str(commands.clone.begin(positions.relative))


def test_clone_begin_end():
    assert "clone ~ ~ ~ ~ ~ ~" == str(
        commands.clone.begin(positions.relative).end(positions.relative)
    )


def test_clone_begin_end_destination():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~" == str(
        commands.clone.begin(positions.relative)
        .end(positions.relative)
        .destination(positions.relative)
    )


def test_clone_call():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~" == str(
        commands.clone(positions.relative, positions.relative, positions.relative)
    )


def test_clone_call_filtered():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ filtered" == str(
        commands.clone(
            positions.relative, positions.relative, positions.relative
        ).filtered
    )


def test_clone_call_filtered_filter():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ filtered minecraft:dirt" == str(
        commands.clone(
            positions.relative, positions.relative, positions.relative
        ).filtered.filter(blocks.dirt)
    )


def test_clone_call_filtered_call():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ filtered minecraft:dirt" == str(
        commands.clone(
            positions.relative, positions.relative, positions.relative
        ).filtered(blocks.dirt)
    )


def test_clone_call_filtered_call_force():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ filtered minecraft:dirt force" == str(
        commands.clone(positions.relative, positions.relative, positions.relative)
        .filtered(blocks.dirt)
        .force
    )


def test_clone_call_filtered_call_move():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ filtered minecraft:dirt move" == str(
        commands.clone(positions.relative, positions.relative, positions.relative)
        .filtered(blocks.dirt)
        .move
    )


def test_clone_call_filtered_call_normal():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ filtered minecraft:dirt normal" == str(
        commands.clone(positions.relative, positions.relative, positions.relative)
        .filtered(blocks.dirt)
        .normal
    )


def test_clone_call_masked():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ masked" == str(
        commands.clone(
            positions.relative, positions.relative, positions.relative
        ).masked
    )


def test_clone_call_masked_force():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ masked force" == str(
        commands.clone(
            positions.relative, positions.relative, positions.relative
        ).masked.force
    )


def test_clone_call_masked_move():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ masked move" == str(
        commands.clone(
            positions.relative, positions.relative, positions.relative
        ).masked.move
    )


def test_clone_call_masked_normal():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ masked normal" == str(
        commands.clone(
            positions.relative, positions.relative, positions.relative
        ).masked.normal
    )


def test_clone_call_replace():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ replace" == str(
        commands.clone(
            positions.relative, positions.relative, positions.relative
        ).replace
    )


def test_clone_call_replace_force():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ replace force" == str(
        commands.clone(
            positions.relative, positions.relative, positions.relative
        ).replace.force
    )


def test_clone_call_replace_move():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ replace move" == str(
        commands.clone(
            positions.relative, positions.relative, positions.relative
        ).replace.move
    )


def test_clone_call_replace_normal():
    assert "clone ~ ~ ~ ~ ~ ~ ~ ~ ~ replace normal" == str(
        commands.clone(
            positions.relative, positions.relative, positions.relative
        ).replace.normal
    )
