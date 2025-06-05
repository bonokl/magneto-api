from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class SimulationConfig(BaseModel):
    id: int
    design_id: int
    step_size: float
    start_point: Dict[str, Any]
    end_point: Dict[str, Any]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class CreateSimulationConfig(BaseModel):
    design_id: int
    step_size: float
    start_point: Dict[str, Any]
    end_point: Dict[str, Any]

class UpdateSimulationConfig(BaseModel):
    design_id: Optional[int] = None
    step_size: Optional[float] = None
    start_point: Optional[Dict[str, Any]] = None
    end_point: Optional[Dict[str, Any]] = None
