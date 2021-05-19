import itertools
from typing import Dict, Iterator, MutableMapping, TypeVar

__all__ = ("LRUCache",)


KT = TypeVar("KT")
VT = TypeVar("VT")


# @implements Cache
class LRUCache(MutableMapping[KT, VT]):
    """
    A simple LRU cache implemented using dictionary insertion order.

    Requires a positive integer `size` to be explicitly passed.

    Attributes
    ----------
    size
        The maximum number of items the cache should hold.
    _cache
        The internal cache, using a dictionary.
    """

    def __init__(self, size: int):
        if size <= 0:
            raise ValueError("size must be a positive integer")
        self.size: int = size
        self._cache: Dict[KT, VT] = {}

    # @implements MutableMapping
    def __setitem__(self, key: KT, value: VT):
        # If we've hit max size, remove the first (and least-recently used) item.
        shrink_by = len(self._cache) + 1 - self.size
        if shrink_by > 0:
            # Get the keys first, so we aren't mutating the dict during iteration.
            keys_to_remove = list(itertools.islice(self._cache.keys(), shrink_by))
            for key_to_remove in keys_to_remove:
                del self._cache[key_to_remove]
        self._cache[key] = value

    # @implements MutableMapping
    def __getitem__(self, key: KT) -> VT:
        # Reinsert an item whenever it's accessed. This updates it's insertion order in
        # the internal dictionary, allowing us to easily implement LRU.
        value = self._cache.pop(key)
        self._cache[key] = value
        return value

    # @implements MutableMapping
    def __delitem__(self, key: KT):
        del self._cache[key]

    # @implements MutableMapping
    def __len__(self) -> int:
        return len(self._cache)

    # @implements MutableMapping
    def __iter__(self) -> Iterator[KT]:
        return iter(self._cache)
