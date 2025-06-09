from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from src.entities.magnet import MagnetGeometry, MagnetSpecification
from src.entities.sensor import SensorPosition


class CreateDesign(BaseModel):
    name: str = Field(..., min_length=1, max_length=256)
    function_id: int
    magnet_id: int
    sensor_ids: List[int]


class MagnetMotion(BaseModel):
    x_position: Optional[float] = None
    y_position: Optional[float] = None
    z_position: Optional[float] = None
    x_angle: Optional[float] = None
    y_angle: Optional[float] = None
    z_angle: Optional[float] = None
    final_x_position: Optional[float] = None
    final_y_position: Optional[float] = None
    final_z_position: Optional[float] = None
    arc_length: Optional[float] = None


class UpdateDesign(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=256)
    function_id: Optional[int] = None
    magnet_id: Optional[int] = None
    sensor_ids: Optional[List[int]] = None
    magnet_specification: Optional[MagnetSpecification] = None
    magnet_geometry: Optional[MagnetGeometry] = None
    magnet_motion: Optional[MagnetMotion] = None


class Design(BaseModel):
    id: int
    name: str
    function_id: int
    magnet_id: int
    sensor_ids: List[int]
    magnet_specification: Optional[MagnetSpecification] = None
    magnet_geometry: Optional[MagnetGeometry] = None
    magnet_motion: Optional[MagnetMotion] = None
    sensor_positions: Optional[SensorPosition] = None
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
