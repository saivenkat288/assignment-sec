from entrypoints import entry_point_pattern
from pydantic import BaseModel
from typing import Any, Dict, AnyStr, List, Union, Optional

class AuthParams(BaseModel):
    email: str
    password: str


