from typing import Iterable, Union

AnyTextComponent = Union[str, list, dict]


class TextComponent:
    def __init__(self, data: AnyTextComponent):
        self.data: AnyTextComponent = data

    @staticmethod
    def flatten(node: AnyTextComponent) -> str:
        return "".join(TextComponent.iter_flatten(node))

    @staticmethod
    def iter_flatten(node: AnyTextComponent) -> Iterable[str]:
        if isinstance(node, str):
            yield node
        elif isinstance(node, list):
            yield from (TextComponent.flatten(subnode) for subnode in node)
        elif isinstance(node, dict):
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
        return prefix + TextComponent.flatten(self.data).replace("\n", f"\n{prefix}")
