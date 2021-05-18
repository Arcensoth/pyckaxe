from dataclasses import dataclass

__all__ = ("Namespace",)


@dataclass(frozen=True)
class Namespace:
    """A relative namespace, independent of any physical location."""

    name: str

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return str(self)
