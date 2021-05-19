from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, cast

from pyckaxe.lib.types import JsonValue

__all__ = ("TextComponent",)


@dataclass
class TextComponent:
    data: JsonValue

    @staticmethod
    def flatten(node: Any) -> str:
        return "".join(TextComponent.iter_flatten(node))

    @staticmethod
    def iter_flatten(node: Any) -> Iterable[str]:
        if isinstance(node, list):
            node = cast(List[Any], node)
            yield from (TextComponent.flatten(subnode) for subnode in node)
        elif isinstance(node, dict):
            node = cast(Dict[str, Any], node)
            yield from (
                TextComponent.flatten(subnode)
                for key, subnode in node.items()
                if key == "text"
            )
        else:
            yield str(node)

    @property
    def flat(self) -> str:
        return TextComponent.flatten(self.data)

    def indent(self, prefix: str) -> str:
        return prefix + self.flat.replace("\n", f"\n{prefix}")
