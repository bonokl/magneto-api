from enum import Enum

from pydantic import BaseModel, Field


class FunctionType(str, Enum):
    STATIC = "static"


class Function(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=128)
    function_type: FunctionType

    class Config:
        from_attributes = True
