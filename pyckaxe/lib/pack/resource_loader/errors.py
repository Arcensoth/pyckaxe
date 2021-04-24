from pathlib import Path

__all__ = (
    "ResourceLoaderError",
    "NoSuchResourceError",
    "DuplicateResourceError",
    "FailedToLoadResourceError",
    "UnsupportedResourceExtensionError",
)


class ResourceLoaderError(Exception):
    def __init__(self, path: Path, message: str):
        super().__init__(message)
        self.path: Path = path


class NoSuchResourceError(ResourceLoaderError):
    def __init__(self, partial_path: Path):
        super().__init__(
            partial_path,
            f"Unable to find resource matching partial path: {partial_path}",
        )


class DuplicateResourceError(ResourceLoaderError):
    def __init__(self, partial_path: Path):
        super().__init__(
            partial_path,
            f"Encountered duplicate resources matching partial path: {partial_path}",
        )


class FailedToLoadResourceError(ResourceLoaderError):
    def __init__(self, path: Path):
        super().__init__(path, f"Failed to load resource at: {path}")


class UnsupportedResourceExtensionError(ResourceLoaderError):
    def __init__(self, path: Path):
        super().__init__(path, f"Unsupported file extension for resource at: {path}")
