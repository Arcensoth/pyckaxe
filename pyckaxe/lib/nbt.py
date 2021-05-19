import re
from typing import Any, Dict, List, Tuple, Union, cast

from nbtlib.path import Path as NbtPath
from nbtlib.tag import Base as NbtBase
from nbtlib.tag import Byte as NbtByte
from nbtlib.tag import Compound as NbtCompound
from nbtlib.tag import Double as NbtDouble
from nbtlib.tag import Float as NbtFloat
from nbtlib.tag import Int as NbtInt
from nbtlib.tag import List as NbtList
from nbtlib.tag import Long as NbtLong
from nbtlib.tag import Short as NbtShort
from nbtlib.tag import String as NbtString

__all__ = (
    "NbtPath",
    "NbtBase",
    "NbtByte",
    "NbtCompound",
    "NbtDouble",
    "NbtFloat",
    "NbtInt",
    "NbtList",
    "NbtLong",
    "NbtShort",
    "NbtString",
    "NbtConvertible",
    "NbtPathConvertible",
    "to_nbt",
    "to_nbt_compound",
    "to_nbt_path",
)

BYTE_PATTERN = re.compile(r"^(-?\d+)[bB]$")
SHORT_PATTERN = re.compile(r"^(-?\d+)[sS]$")
LONG_PATTERN = re.compile(r"^(-?\d+)[lL]$")
FLOAT_PATTERN = re.compile(r"^(-?\d+)[fF]$")
DOUBLE_PATTERN = re.compile(r"^(-?\d+)[dD]$")


NbtConvertible = Union[
    Dict[str, "NbtConvertible"],
    List["NbtConvertible"],
    Tuple["NbtConvertible", ...],
    str,
    int,
    float,
    bool,
    NbtBase,
]
NbtPathConvertible = Union[NbtPath, str]


def to_nbt(value: Any) -> NbtBase:
    if isinstance(value, NbtBase):
        return value
    if isinstance(value, str):
        if match := BYTE_PATTERN.match(value):
            return NbtByte(int(match.groups()[0]))
        if match := SHORT_PATTERN.match(value):
            return NbtShort(int(match.groups()[0]))
        if match := LONG_PATTERN.match(value):
            return NbtLong(int(match.groups()[0]))
        if match := FLOAT_PATTERN.match(value):
            return NbtFloat(float(match.groups()[0]))
        if match := DOUBLE_PATTERN.match(value):
            return NbtDouble(float(match.groups()[0]))
        return NbtString(value)
    if isinstance(value, bool):
        return NbtByte(value)
    if isinstance(value, int):
        return NbtInt(value)
    if isinstance(value, float):
        return NbtFloat(value)
    if isinstance(value, dict):
        value = cast(Dict[str, Any], value)
        return NbtCompound({k: to_nbt(v) for k, v in value.items()})
    if isinstance(value, (list, tuple)):
        value = cast(List[Any], value)
        return NbtList([to_nbt(v) for v in value])
    raise ValueError(f"Cannot convert value to NBT: {value}")


def to_nbt_compound(value: Dict[str, Any]) -> NbtCompound:
    nbt = to_nbt(value)
    if isinstance(nbt, NbtCompound):
        return nbt
    raise ValueError(f"Cannot convert value to NBT compound: {value}")


def to_nbt_path(value: NbtPathConvertible) -> NbtPath:
    return NbtPath(value)
