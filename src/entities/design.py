from enum import Enum
from typing import Optional

from pydantic import BaseModel

from src.entities.magnet import MagnetGeometry
from src.entities.sensor import Sensor


class MagnetPosition(BaseModel):
    x_position: float = 0
    y_position: float = 0
    z_position: float = 0


class MagnetAngle(BaseModel):
    x_angle: float = 0
    y_angle: float = 0
    z_angle: float = 0


class MagnetMovement(BaseModel):
    pass  # Extend as needed


class SensorPosition(BaseModel):
    x_position: Optional[float] = None
    y_position: Optional[float] = None
    z_position: Optional[float] = None


class SimSetting(BaseModel):
    pass  # Extend as needed


class CustomInputs(BaseModel):
    variant: Optional[str] = None


class RemanenceType(Enum):
    BR_AVERAGE = "br_average"
    BR_LOW = "br_low"
    BR_HIGH = "br_high"


class Design(BaseModel):
    id: int
    design_name: Optional[str] = None
    magnet_id: int
    poles: int
    material_id: int
    grade_id: int
    select_remanence: RemanenceType
    remanence: float
    temperature: float
    temperature_coefficient: float
    coercivity: float
    function_id: int
    magnet_geometry: MagnetGeometry
    magnet_position: MagnetPosition
    magnet_angle: MagnetAngle
    magnet_movement: Optional[MagnetMovement] = None
    sim_setting: Optional[SimSetting] = None
    date_created: Optional[str] = None
    last_modified: Optional[str] = None
    sensor: list[Sensor] = []


class CreateDesign(BaseModel):
    design_name: Optional[str] = None
    magnet_id: int
    poles: int
    material_id: int
    grade_id: int
    select_remanence: RemanenceType
    remanence: float
    temperature: float
    temperature_coefficient: float
    coercivity: float
    function_id: int
    magnet_geometry: MagnetGeometry
    magnet_position: MagnetPosition
    magnet_angle: MagnetAngle
    magnet_movement: Optional[MagnetMovement] = None
    sim_setting: Optional[SimSetting] = None
    date_created: Optional[str] = None
    last_modified: Optional[str] = None
    sensor: list[Sensor] = []
