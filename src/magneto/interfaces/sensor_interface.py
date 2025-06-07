from abc import ABC, abstractmethod

from src.entities.sensor import Sensor


class SensorInterface(ABC):
    @abstractmethod
    def get_all_sensors(self, ) -> [Sensor]:
        pass

    @abstractmethod
    def get_sensor(self, sensor_id: int) -> Sensor | None:
        pass
