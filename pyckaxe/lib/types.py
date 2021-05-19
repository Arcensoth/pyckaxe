from typing import Dict, List, Tuple, Union

__all__ = ("JsonValue",)

# +-------------------+---------------+
# | Python            | JSON          |
# +===================+===============+
# | dict              | object        |
# +-------------------+---------------+
# | list, tuple       | array         |
# +-------------------+---------------+
# | str               | string        |
# +-------------------+---------------+
# | int, float        | number        |
# +-------------------+---------------+
# | True              | true          |
# +-------------------+---------------+
# | False             | false         |
# +-------------------+---------------+
# | None              | null          |
# +-------------------+---------------+
JsonValue = Union[
    Dict[str, "JsonValue"],
    List["JsonValue"],
    Tuple["JsonValue", ...],
    str,
    int,
    float,
    bool,
    None,
]
