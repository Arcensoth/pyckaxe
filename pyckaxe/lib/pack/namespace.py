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

    # DELETEME still used?
    # def resolve_path(self, pack_context: PackContext) -> Path:
    #     return Path(pack_context.data_path / self.name)
