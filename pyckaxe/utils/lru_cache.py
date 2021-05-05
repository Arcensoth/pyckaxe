from typing import Dict, MutableMapping, TypeVar

__all__ = ("LRUCache",)


KT = TypeVar("KT")
VT = TypeVar("VT")


class LRUCache(MutableMapping[KT, VT]):
    """
    A LRU cache implemented using dictionary insertion order.

    Attributes
    ----------
    size
        The maximum number of items the cache should hold.
    _cache
        The internal cache, using a dictionary.
    """

    def __init__(self, size: int):
        self.size: int = size
        self._cache: Dict[KT, VT] = {}

    # @implements MutableMapping
    def __setitem__(self, key: KT, value: VT):
        # If we've hit max size, remove the first (and least-recently used) item.
        if len(self._cache) >= self.size:
            key_to_remove = next(iter(self._cache.keys()))
            del self._cache[key_to_remove]
        self._cache.__setitem__(key, value)

    # @implements MutableMapping
    def __getitem__(self, key: KT) -> VT:
        # Reinsert an item whenever it's accessed. This updates it's insertion order in
        # the internal dictionary, allowing us to easily implement LRU.
        value = self._cache.pop(key)
        self._cache[key] = value
        return value

    # @implements MutableMapping
    def __delitem__(self, key: KT):
        self._cache.__delitem__(key)

    # @implements MutableMapping
    def __len__(self):
        return self._cache.__len__()

    # @implements MutableMapping
    def __iter__(self):
        return self._cache.__iter__()
