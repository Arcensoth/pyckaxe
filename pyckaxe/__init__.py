from pyckaxe.command.commands.root import RootCommand

commands = RootCommand()


class Selector:
    all_players = '@a'
    entities = '@e'
    random = '@r'
    self = '@s'


class Positions:
    relative = '~ ~ ~'


class Blocks:
    dirt = 'minecraft:dirt'
    grass = 'minecraft:grass'
    air = 'minecraft:air'


selectors = Selector
positions = Positions
blocks = Blocks
