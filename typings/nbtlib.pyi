from typing import Optional

from nbtlib.nbt import Root
from nbtlib.tag import Compound

def load(
    filename: str,
    *,
    gzipped: Optional[bool] = ...,
    byteorder: str = ...,
) -> Compound: ...

class File(Root):
    def save(
        self,
        filename: Optional[str] = ...,
        *,
        gzipped: Optional[bool] = ...,
        byteorder: Optional[bool] = ...,
    ) -> None: ...
