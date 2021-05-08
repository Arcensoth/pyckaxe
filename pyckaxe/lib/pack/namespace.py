from dataclasses import dataclass

__all__ = ("Namespace",)


@dataclass
class Namespace:
    """ A relative namespace, independent of any physical location. """

    name: str

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)
