from dataclasses import dataclass, field
from typing import Iterator, List

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.abc.resource_scanner import ResourceScanner

__all__ = ("ResourceScannerSet",)


@dataclass
class ResourceScannerSet:
    """
    Scans for several types of `Resource` using a group of `ResourceScanner`s.
    """

    _scanners: List[ResourceScanner[Resource]] = field(init=False)

    def __init__(self, *scanners: ResourceScanner[Resource]):
        self._scanners = list(scanners)

    def __len__(self):
        return self._scanners.__len__()

    def __iter__(self) -> Iterator[ResourceScanner[Resource]]:
        return self._scanners.__iter__()
