from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class Sensor(BaseModel):
    id: int
    design_id: int
    name: str
    sensor_type: str
    parameters: Dict[str, Any]
    position: Dict[str, Any]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class CreateSensor(BaseModel):
    design_id: int
    name: str = Field(..., min_length=1, max_length=256)
    sensor_type: str
    parameters: Dict[str, Any]
    position: Dict[str, Any]

class UpdateSensor(BaseModel):
    design_id: Optional[int] = None
    name: Optional[str] = Field(None, min_length=1, max_length=256)
    sensor_type: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
    position: Optional[Dict[str, Any]] = None
