import re
from typing import Any

from nbtlib import tag

BYTE_PATTERN = re.compile(r"^(-?\d)[bB]$")
SHORT_PATTERN = re.compile(r"^(-?\d)[sS]$")
LONG_PATTERN = re.compile(r"^(-?\d)[lL]$")
FLOAT_PATTERN = re.compile(r"^(-?\d)[fF]$")
DOUBLE_PATTERN = re.compile(r"^(-?\d)[dD]$")


def to_nbt(value: Any):
    if isinstance(value, str):
        if (match := BYTE_PATTERN.match(value)) :
            return tag.Byte(int(match.groups()[0]))
        if (match := SHORT_PATTERN.match(value)) :
            return tag.Short(int(match.groups()[0]))
        if (match := LONG_PATTERN.match(value)) :
            return tag.Long(int(match.groups()[0]))
        if (match := FLOAT_PATTERN.match(value)) :
            return tag.Float(float(match.groups()[0]))
        if (match := DOUBLE_PATTERN.match(value)) :
            return tag.Double(float(match.groups()[0]))
        return tag.String(value)
    if isinstance(value, int):
        return tag.Int(value)
    if isinstance(value, float):
        return tag.Float(value)
    if isinstance(value, dict):
        return tag.Compound({k: to_nbt(v) for k, v in value.items()})
    if isinstance(value, list):
        return tag.List([to_nbt(v) for v in value])
    raise ValueError(
        f"Cannot convert value of type {value.__class__.__name__} to data tag: {value}"
    )
