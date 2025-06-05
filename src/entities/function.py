from pydantic import BaseModel, Field
from typing import Optional

class Function(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=128)
    description: Optional[str] = None

    class Config:
        orm_mode = True

