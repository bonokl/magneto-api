from src.magneto.interfaces.sensor_interface import SensorInterface
from src.magneto.repositories.sensor_repository import SensorRepository
from src.entities.sensor import Sensor, CreateSensor, UpdateSensor
from typing import List, Optional, Tuple

class SensorService(SensorInterface):
    def __init__(self, sensor_repository: SensorRepository):
        self._sensor_repository = sensor_repository

    def get_all_sensors(self, offset: int = 0, limit: int = 100, order_by: Optional[str] = None) -> Tuple[int, List[Sensor]]:
        return self._sensor_repository.get_all(offset, limit, order_by)

    def create_sensor(self, sensor: CreateSensor) -> Sensor:
        return self._sensor_repository.create(sensor)

    def update_sensor(self, sensor_id: int, sensor: UpdateSensor) -> Sensor | None:
        return self._sensor_repository.update(sensor_id, sensor)

    def get_sensor(self, sensor_id: int) -> Sensor | None:
        return self._sensor_repository.get(sensor_id)

    def delete_sensor(self, sensor_id: int) -> bool:
        return self._sensor_repository.delete(sensor_id)
