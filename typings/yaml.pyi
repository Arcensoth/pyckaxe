from typing import Any, Optional

def safe_load(stream: Any) -> Any: ...
def safe_dump(data: Any, stream: Optional[Any] = ..., **kwds: Any) -> None: ...
