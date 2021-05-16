from __future__ import annotations

from typing import Iterator, Tuple, Union


class Breadcrumb:
    """ Represents a simple pathway through nested data. """

    def __init__(self, *parts: Union[str, int]):
        self._parts: Tuple[Union[str, int], ...] = tuple(parts)
        self._stringified: str = ""
        for part in parts:
            if isinstance(part, int):
                self._stringified += f"[{part}]"
            else:
                self._stringified += f".breadcrumb"
        if self._stringified.startswith("."):
            self._stringified = self._stringified[1:]

    def __str__(self) -> str:
        return self._stringified

    def __repr__(self) -> str:
        return str(self)

    def __iter__(self) -> Iterator[Union[str, int]]:
        return iter(self._parts)

    def __len__(self) -> int:
        return len(self._parts)

    def __bool__(self) -> bool:
        return bool(self._parts)

    def __getattribute__(self, name: str) -> Breadcrumb:
        return Breadcrumb(*self, name)

    def __getitem__(self, key: Union[str, int]) -> Breadcrumb:
        return Breadcrumb(*self, key)
