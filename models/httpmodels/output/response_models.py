from entrypoints import entry_point_pattern
from pydantic import BaseModel
from typing import Any, Dict, AnyStr, List, Union, Optional

class HTTPResponse(BaseModel):
    status_code: int
    message: str
    result:Optional[int]