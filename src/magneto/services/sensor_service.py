from typing import List

from src.entities.sensor import Sensor
from src.magneto.interfaces.sensor_interface import SensorInterface
from src.magneto.repositories.sensor_repository import SensorRepository


class SensorService(SensorInterface):
    def __init__(self, sensor_repository: SensorRepository):
        self._sensor_repository = sensor_repository

    def get_all_sensors(self) -> List[Sensor]:
        return self._sensor_repository.get_all()

    def get_sensor(self, sensor_id: int) -> Sensor | None:
        return self._sensor_repository.get(sensor_id)
