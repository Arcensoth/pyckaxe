from pyckaxe.command.commands.root import RootCommand

commands = RootCommand()


class Selector:
    all_players = '@a'
    entities = '@e'
    random = '@r'
    self = '@s'


class Positions:
    relative = '~ ~ ~'


class Rotations:
    relative = '~ ~'


class Anchors:
    feet = 'feet'
    eyes = 'eyes'


class Blocks:
    dirt = 'minecraft:dirt'
    grass = 'minecraft:grass'
    air = 'minecraft:air'


class Items:
    diamond = 'minecraft:diamond'


class Effects:
    slowness = 'minecraft:slowness'


selectors = Selector
positions = Positions
rotations = Rotations
anchors = Anchors
blocks = Blocks
items = Items
effects = Effects
