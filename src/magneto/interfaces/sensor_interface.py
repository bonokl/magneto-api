from abc import ABC, abstractmethod
from typing import List, Optional
from src.entities.sensor import Sensor, CreateSensor, UpdateSensor

class SensorInterface(ABC):
    @abstractmethod
    def get_all_sensors(self, offset: int = 0, limit: int = 100, order_by: Optional[str] = None) -> (int, List[Sensor]):
        pass

    @abstractmethod
    def create_sensor(self, sensor: CreateSensor) -> Sensor:
        pass

    @abstractmethod
    def update_sensor(self, sensor_id: int, sensor: UpdateSensor) -> Sensor | None:
        pass

    @abstractmethod
    def get_sensor(self, sensor_id: int) -> Sensor | None:
        pass

    @abstractmethod
    def delete_sensor(self, sensor_id: int) -> bool:
        pass

