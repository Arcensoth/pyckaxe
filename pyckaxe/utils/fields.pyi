from typing import Any, Callable, Dict, Optional, Type, TypeVar

FieldType = TypeVar("FieldType")

# with type
def get_field(
    raw: Dict[str, Any],
    field: str,
    type: Type[FieldType],
    check: Optional[Callable[[FieldType], bool]] = ...,
    default: Any = ...,
    convert: Optional[type] = ...,
) -> FieldType: ...

# without type
def get_field(
    raw: Dict[str, Any],
    field: str,
    check: Optional[Callable[[Any], bool]] = ...,
    default: Any = ...,
    convert: Optional[type] = ...,
) -> Any: ...
