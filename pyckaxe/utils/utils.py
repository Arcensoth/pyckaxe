""" General utilities not specific to Minecraft. """

from typing import Any, Mapping

__all__ = ("is_submapping",)


def is_submapping(subdict: Mapping[str, Any], superdict: Mapping[str, Any]) -> bool:
    sub_items = subdict.items()
    super_items = superdict.items()
    return all((item in super_items) for item in sub_items)
