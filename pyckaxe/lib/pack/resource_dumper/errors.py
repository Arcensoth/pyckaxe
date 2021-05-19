from pathlib import Path

__all__ = (
    "ResourceDumperError",
    "FailedToDumpResourceError",
    "NonFileResourceExistsError",
)


class ResourceDumperError(Exception):
    def __init__(self, path: Path, message: str):
        super().__init__(message)
        self.path: Path = path


class FailedToDumpResourceError(ResourceDumperError):
    def __init__(self, path: Path):
        super().__init__(path, f"Failed to dump resource to: {path}")


class NonFileResourceExistsError(ResourceDumperError):
    def __init__(self, path: Path):
        super().__init__(path, f"Cannot dump resource to existing non-file at: {path}")
