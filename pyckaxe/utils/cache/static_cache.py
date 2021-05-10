from typing import Dict, Iterator, Mapping, MutableMapping, Optional, TypeVar

__all__ = ("StaticCache",)


KT = TypeVar("KT")
VT = TypeVar("VT")


# @implements Cache
class StaticCache(MutableMapping[KT, VT]):
    """
    A cache with a pre-defined set of entries that never grows.

    Pass a `Mapping` of keys -> values to populate the initial cache.

    Passing nothing will result in an effective no-op cache. This can be used to
    emulate the `Cache` protocol without ever actually caching anything.

    Attributes
    ----------
    _cache
        The internal cache, using a dictionary.
    """

    def __init__(self, cache: Optional[Mapping[KT, VT]] = None):
        self._cache: Dict[KT, VT] = {k: v for k, v in cache.items()} if cache else {}

    # @implements MutableMapping
    def __setitem__(self, key: KT, value: VT):
        pass

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
