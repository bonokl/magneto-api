from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class CreateDesign(BaseModel):
    name: str = Field(..., min_length=1, max_length=256)
    function_id: int
    magnet_id: int
    sensor_ids: List[int]

class UpdateDesign(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=256)
    function_id: Optional[int] = None
    magnet_id: Optional[int] = None
    sensor_ids: Optional[List[int]] = None

class Design(BaseModel):
    id: int
    name: str
    function_id: int
    magnet_id: int
    sensor_ids: List[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
