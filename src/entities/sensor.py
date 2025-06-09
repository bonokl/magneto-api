from typing import List, Optional

from pydantic import BaseModel


class SensorSpecification(BaseModel):
    applied_vcc: Optional[float] = None
    averaging: Optional[list[int]] = None
    body_size_length: Optional[float] = None
    body_size_width: Optional[float] = None
    category: Optional[str] = None
    device: Optional[str] = None
    id: Optional[str] = None
    input_referred_noise: Optional[str] = None
    maximum_input: Optional[list[float]] = None
    maximum_package_height: Optional[float] = None
    maximum_vcc: Optional[float] = None
    minimum_input: Optional[float] = None
    minimum_vcc: Optional[float] = None
    package: Optional[str] = None
    package_rotation: Optional[float] = None
    pin_count: Optional[int] = None
    quiescent_output: Optional[float] = None
    sensitivity: Optional[float] = None
    sensitivity_direction: Optional[str] = None
    sensor_family: Optional[str] = None
    sensor_x_location: Optional[float] = None
    sensor_y_location: Optional[float] = None
    sensor_z_location: Optional[float] = None
    temperature_compensation: Optional[list[float]] = None
    variant: Optional[str] = None


class SensorPosition(BaseModel):
    x_position: Optional[float] = None
    y_position: Optional[float] = None
    z_position: Optional[float] = None
    x_angle: Optional[float] = None
    y_angle: Optional[float] = None
    z_angle: Optional[float] = None


class Sensor(BaseModel):
    id: str
    sensorName: str
    category: str
    variant: List[str]
    package: List[str]
    pin_count: List[str]
    specification: SensorSpecification
    position: Optional[SensorPosition] = None

    class Config:
        from_attributes = True
