from pyckaxe.block import Block
from pyckaxe.block_predicate import BlockPredicate
from pyckaxe.block_state import BlockState
from pyckaxe.command import Command
from pyckaxe.coordinate import Coordinate
from pyckaxe.position import Position
from pyckaxe.text_component import TextComponent


class Selector:
    all_players = "@a"
    entities = "@e"
    random = "@r"
    self = "@s"


class Rotations:
    relative = "~ ~"


class Anchors:
    feet = "feet"
    eyes = "eyes"


class Entities:
    area_effect_cloud = "minecraft:area_effect_cloud"


class Items:
    diamond = "minecraft:diamond"


class ItemSlots:
    slot_armor_chest = "slot.armor.chest"
    slot_armor_feet = "slot.armor.feet"
    slot_armor_head = "slot.armor.head"
    slot_armor_legs = "slot.armor.legs"
    slot_weapon_mainhand = "slot.weapon.mainhand"
    slot_weapon_offhand = "slot.weapon.offhand"
    slot_container_13 = "slot.container.13"


class Effects:
    slowness = "minecraft:slowness"


class SoundSources:
    ambient = "ambient"
    block = "block"
    hostile = "hostile"
    master = "master"
    music = "music"
    neutral = "neutral"
    player = "player"
    record = "record"
    voice = "voice"
    weather = "weather"


class ScoreboardOperations:
    add = "+="
    subtract = "-="
    multiply = "*="
    divide = "/="
    modulo = "%="
    assign = "="
    min = "<"
    max = ">"
    swap = "><"


class ScoreboardSlots:
    below_name = "belowName"
    list = "list"
    sidebar = "sidebar"
    sidebar_team_black = "sidebar.team.black"
    sidebar_team_dark_blue = "sidebar.team.dark_blue"
    sidebar_team_dark_green = "sidebar.team.dark_green"
    sidebar_team_dark_aqua = "sidebar.team.dark_aqua"
    sidebar_team_dark_red = "sidebar.team.dark_red"
    sidebar_team_dark_purple = "sidebar.team.dark_purple"
    sidebar_team_gold = "sidebar.team.gold"
    sidebar_team_gray = "sidebar.team.gray"
    sidebar_team_dark_gray = "sidebar.team.dark_gray"
    sidebar_team_blue = "sidebar.team.blue"
    sidebar_team_green = "sidebar.team.green"
    sidebar_team_aqua = "sidebar.team.aqua"
    sidebar_team_red = "sidebar.team.red"
    sidebar_team_light_purple = "sidebar.team.light_purple"
    sidebar_team_yellow = "sidebar.team.yellow"
    sidebar_team_white = "sidebar.team.white"


selectors = Selector
rotations = Rotations
anchors = Anchors
entities = Entities
items = Items
item_slots = ItemSlots
effects = Effects
sound_sources = SoundSources
scoreboard_operations = ScoreboardOperations
scoreboard_slots = ScoreboardSlots
