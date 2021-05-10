from typing import Dict, Iterator, MutableMapping, TypeVar

__all__ = ("UnboundedCache",)


KT = TypeVar("KT")
VT = TypeVar("VT")


# @implements Cache
class UnboundedCache(MutableMapping[KT, VT]):
    """
    An unbounded cache that grows indefinitely.

    Attributes
    ----------
    _cache
        The internal cache, using a dictionary.
    """

    def __init__(self):
        self._cache: Dict[KT, VT] = {}

    # @implements MutableMapping
    def __setitem__(self, key: KT, value: VT):
        self._cache[key] = value

    # @implements MutableMapping
    def __getitem__(self, key: KT) -> VT:
        return self._cache[key]

    # @implements MutableMapping
    def __delitem__(self, key: KT):
        del self._cache[key]

    # @implements MutableMapping
    def __len__(self) -> int:
        return len(self._cache)

    # @implements MutableMapping
    def __iter__(self) -> Iterator[KT]:
        return iter(self._cache)
