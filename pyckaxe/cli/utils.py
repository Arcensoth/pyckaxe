import asyncio
from functools import wraps
from typing import Any


# https://github.com/pallets/click/issues/85#issuecomment-503464628
def asyncify(f: Any) -> Any:
    @wraps(f)
    def wrapper(*args: Any, **kwargs: Any):
        return asyncio.run(f(*args, **kwargs))

    return wrapper
