from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel


class Magnet(BaseModel):
    id: int
    shape: str
    multipole: bool
    magnet_geometry_default: Dict[str, Any]
    description: Optional[str]
    magnet_image: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class MagnetSpecification(BaseModel):
    poles: int
    material_id: int
    grade_id: int
    select_remanence: str
    remanence: float
    temperature: float
    temperature_coefficient: float
    coercivity: float


class MagnetGeometry(BaseModel):
    magnet_length_x_dim: Optional[float] = None
    magnet_length_y_dim: Optional[float] = None
    magnet_length_z_dim: Optional[float] = None
    outer_diameter: Optional[float] = None
    inner_diameter: Optional[float] = None
    height: Optional[float] = None
    diameter: Optional[float] = None
