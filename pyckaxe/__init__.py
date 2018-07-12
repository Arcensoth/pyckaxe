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


class Entities:
    area_effect_cloud = 'minecraft:area_effect_cloud'


class Items:
    diamond = 'minecraft:diamond'


class Effects:
    slowness = 'minecraft:slowness'


class SoundSources:
    ambient = 'ambient'
    block = 'block'
    hostile = 'hostile'
    master = 'master'
    music = 'music'
    neutral = 'neutral'
    player = 'player'
    record = 'record'
    voice = 'voice'
    weather = 'weather'


selectors = Selector
positions = Positions
rotations = Rotations
anchors = Anchors
blocks = Blocks
entities = Entities
items = Items
effects = Effects
sound_sources = SoundSources
