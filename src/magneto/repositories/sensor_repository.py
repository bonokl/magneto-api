from src.entities.sensor import Sensor

sensors = [
]


class SensorRepository:
    def get(self, sensor_id: int) -> Sensor | None:
        for s in sensors:
            if s.id == sensor_id:
                return s
        return None

    def get_all(self, ) -> list[Sensor]:
        return sensors
