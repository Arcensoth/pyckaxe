from typing import Any, cast

__all__ = ("DEFAULT",)


# Unique object that can be used as a default for nullable fields.
DEFAULT = cast(Any, object())
