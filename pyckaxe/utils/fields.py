from typing import Any, Callable, Dict, Optional, Type, TypeVar


class MissingRequiredFieldError(Exception):
    def __init__(self, raw: Dict[str, Any], field: str):
        self.raw: Dict[str, Any] = raw
        self.field: str = field
        super().__init__(
            f"Field '{self.field}' is required but missing, in: {self.raw}"
        )


class InvalidFieldTypeError(Exception):
    def __init__(self, raw: Dict[str, Any], field: str, field_type: type):
        self.raw: Dict[str, Any] = raw
        self.field: str = field
        self.field_type: type = field_type
        super().__init__(
            f"Field '{self.field}' is not of expected type <{self.field_type}>, in: {self.raw}"
        )


class MalformedFieldError(Exception):
    def __init__(self, raw: Dict[str, Any], field: str):
        self.raw: Dict[str, Any] = raw
        self.field: str = field
        super().__init__(f"Field '{self.field}' is malformed, in: {self.raw}")


FieldType = TypeVar("FieldType")

DEFAULT = object()


def get_field(
    raw: Dict[str, Any],
    field: str,
    type: Optional[Type[FieldType]] = None,
    check: Optional[Callable[[FieldType], bool]] = None,
    default: Any = DEFAULT,
    convert: Optional[type] = None,
) -> FieldType:
    value = raw.get(field)
    if value is None:
        if default is not DEFAULT:
            return default
        raise MissingRequiredFieldError(raw, field)
    if (type is not None) and (not isinstance(value, type)):
        raise InvalidFieldTypeError(raw, field, type)
    if (check is not None) and (not check(value)):
        raise MalformedFieldError(raw, field)
    if convert is not None:
        return convert(value)
    return value
