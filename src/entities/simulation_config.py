from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from src.entities.magnet import MagnetGeometry
from src.entities.sensor import SensorPosition


class MagnetAngle(BaseModel):
    x_angle: float = 0
    y_angle: float = 0
    z_angle: float = 0


class MagnetPosition(BaseModel):
    x_position: float = 0
    y_position: float = 0
    z_position: float = 0


class MagnetMovement(BaseModel):
    arc_length: Optional[float] = None
    final_x_position: Optional[float] = None
    final_y_position: Optional[float] = None
    final_z_position: Optional[float] = None


class SimSetting(BaseModel):
    angular_step_size: Optional[float] = None
    step_size: Optional[float] = None


class SensorInSimulation(BaseModel):
    sensor_id: str
    sensor_position: SensorPosition
    sensor_angle: Optional[MagnetAngle] = None
    custom_inputs: Optional[Dict[str, Any]] = None
    id: Optional[int] = None


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


class SimulationStartRequest(BaseModel):
    coercivity: float
    date_created: Optional[datetime] = None
    design_name: str
    function_id: int
    grade_id: int
    last_modified: Optional[datetime] = None
    magnet_angle: MagnetAngle
    magnet_geometry: MagnetGeometry
    magnet_id: int
    magnet_movement: MagnetMovement
    magnet_position: MagnetPosition
    material_id: int
    poles: int
    remanence: float
    select_remanence: str
    sensor: List[SensorInSimulation]
    sim_setting: SimSetting
    temperature: float
    temperature_coefficient: float
