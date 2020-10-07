from pathlib import Path


class MalformedResourceError(Exception):
    def __init__(self, path: Path):
        super().__init__(f"Failed to load malformed resource: {path}")
        self.path: Path = path
