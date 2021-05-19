from typing import Iterator

__all__ = ("walk_exception",)


def walk_exception(ex: BaseException) -> Iterator[BaseException]:
    """Iterate over the causes of an exception."""
    cause = ex.__cause__
    while cause is not None:
        yield cause
        cause = cause.__cause__
