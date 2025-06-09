from enum import Enum
from typing import Optional

from pydantic import BaseModel


class MagnetShape(str, Enum):
    BAR = "bar"


class MagnetGeometry(BaseModel):
    magnet_length_x_dim: Optional[float] = None
    magnet_length_y_dim: Optional[float] = None
    magnet_length_z_dim: Optional[float] = None
    outer_diameter: Optional[float] = None
    inner_diameter: Optional[float] = None
    height: Optional[float] = None
    diameter: Optional[float] = None


class Magnet(BaseModel):
    id: int
    shape: MagnetShape
    multipole: bool
    magnet_geometry_default: MagnetGeometry
    description: Optional[str]

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
