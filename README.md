![logo]

# pyckaxe
An expressive Minecraft utility library revolving around data manipulation and generation.

[![build-badge-master]](https://travis-ci.org/Arcensoth/pyckaxe)
[![quality-badge-master]](https://app.codacy.com/project/Arcensoth/pyckaxe/dashboard)
[![coverage-badge-master]](https://codecov.io/gh/Arcensoth/pyckaxe/branch/master)
[![package-badge]](https://pypi.python.org/pypi/pyckaxe/)
[![version-badge]](https://pypi.python.org/pypi/pyckaxe/)

You may be interested in `pyckaxe` if you:

- are a technical/creative player, or
- make adventure maps or minigames, or
- use command/data generators, or
- write your own generators, or
- work on large/complex projects, or
- just want to over-engineer something.

The goal of `pyckaxe` is to provide a flexible suite of development tools for technical Minecraft players:

- A complete hierarchy of **commands** and their subcommands, as well as frequently used **selectors** and **positions** to go along with them.
- A thorough collection of game object and **data tag (NBT)** representations, for things like **blocks**, **items**, and **entities**.
- Auto-completion, argument suggestion, and type validation for all representations.
- Utilities for building datapacks and resources via custom-written generators.

## Checklist
### Commands
- [ ] advancement
- [ ] ban
- [ ] ban_ip
- [ ] banlist
- [ ] bossbar
- [x] clear
- [ ] clone
- [ ] data
- [ ] datapack
- [ ] debug
- [ ] defaultgamemode
- [ ] deop
- [ ] difficulty
- [x] effect
- [ ] enchant
- [ ] execute
    - [ ] align
    - [ ] anchored
    - [x] as
    - [x] at
    - [ ] facing
    - [x] if/unless block
    - [ ] if/unless blocks
    - [ ] if/unless entity
    - [ ] if/unless score
    - [ ] in
    - [ ] positioned
    - [ ] rotated
    - [x] run
    - [ ] store
- [ ] experience
- [ ] fill
- [ ] function
- [ ] gamemode
- [ ] gamerule
- [ ] give
- [ ] help
- [ ] kick
- [ ] kill
- [ ] list
- [ ] locate
- [ ] me
- [ ] msg
- [ ] op
- [ ] pardon
- [ ] pardon_ip
- [ ] particle
- [ ] playsound
- [ ] publish
- [ ] recipe
- [ ] reload
- [ ] replaceitem
- [ ] save_all
- [ ] save_off
- [ ] save_on
- [x] say
- [ ] scoreboard
- [ ] seed
- [x] setblock
- [ ] setidletimeout
- [ ] setworldspawn
- [ ] spawnpoint
- [ ] spreadplayers
- [ ] stop
- [ ] stopsound
- [ ] summon
- [x] tag
- [ ] team
- [x] teleport
- [ ] tell
- [ ] tellraw
- [x] time
- [ ] title
- [x] tp
- [x] trigger
- [ ] w
- [ ] weather
- [ ] whitelist
- [ ] worldborder
- [ ] xp

[logo]: https://i.imgur.com/FkxD7fJ.png
[build-badge-master]: https://img.shields.io/travis/Arcensoth/pyckaxe/master.svg?label=build
[quality-badge-master]: https://img.shields.io/codacy/grade/a01ea39de1ed48319c18365ad5545f65/master.svg?label=quality
[coverage-badge-master]: https://img.shields.io/codecov/c/github/Arcensoth/pyckaxe/master.svg?label=coverage
[package-badge]: https://img.shields.io/pypi/v/pyckaxe.svg
[version-badge]: https://img.shields.io/pypi/pyversions/pyckaxe.svg
