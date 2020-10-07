from typing import Callable, Type, TypeVar


class MissingRequiredFieldError(Exception):
    def __init__(self, raw: dict, field: str):
        self.raw: dict = raw
        self.field: str = field
        super().__init__(f"Field '{self.field}' is required but missing, in: {self.raw}")


class InvalidFieldTypeError(Exception):
    def __init__(self, raw: dict, field: str, field_type: Type):
        self.raw: dict = raw
        self.field: str = field
        self.field_type: Type = field_type
        super().__init__(
            f"Field '{self.field}' is not of expected type <{self.field_type}>, in: {self.raw}"
        )


class MalformedFieldError(Exception):
    def __init__(self, raw: dict, field: str):
        self.raw: dict = raw
        self.field: str = field
        super().__init__(f"Field '{self.field}' is malformed, in: {self.raw}")


FieldType = TypeVar("FieldType")


def get_field(
    raw: dict, field: str, type: Type[FieldType] = None, check: Callable[[FieldType], bool] = None
) -> FieldType:
    value = raw.get(field)
    if type is not None:
        if value is None:
            raise MissingRequiredFieldError(raw, field)
        if not isinstance(value, type):
            raise InvalidFieldTypeError(raw, field, type)
    if check is not None:
        if not check(value):
            raise MalformedFieldError(raw, field)
    return value
