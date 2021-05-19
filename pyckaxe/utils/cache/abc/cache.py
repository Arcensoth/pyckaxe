from typing import Iterator, Optional, Protocol, TypeVar

__all__ = ("Cache",)


KT = TypeVar("KT")
VT = TypeVar("VT")


class Cache(Protocol[KT, VT]):
    def __setitem__(self, key: KT, value: VT):
        ...

    def __getitem__(self, key: KT) -> VT:
        ...

    def __delitem__(self, key: KT):
        ...

    def __len__(self) -> int:
        ...

    def __iter__(self) -> Iterator[KT]:
        ...

    def get(self, key: KT) -> Optional[VT]:
        ...
