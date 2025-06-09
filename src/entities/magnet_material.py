from typing import Optional

from pydantic import BaseModel


class MagnetMaterial(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True


class MaterialGrade(BaseModel):
    id: int
    material_id: int
    grade: str
    br_average: float
    br_high: float
    br_low: float
    coercivity: float
    temperature_coefficient: float
    description: Optional[str] = None

    class Config:
        from_attributes = True
