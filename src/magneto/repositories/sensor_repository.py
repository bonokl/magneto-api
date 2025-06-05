from src.database.models.sensor import Sensor as DbSensor
from src.entities.sensor import Sensor, CreateSensor, UpdateSensor
from src.database.database import Database
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert
from typing import Optional, Tuple, List

class SensorRepository:
    def get(self, sensor_id: int) -> Sensor | None:
        with Database.create_db_session() as db:
            sensor = db.query(DbSensor).filter(DbSensor.id == sensor_id).first()
            return Sensor.model_validate(sensor) if sensor else None

    def get_all(self, offset: int = 0, limit: int = 100, order_by: Optional[str] = None) -> Tuple[int, List[Sensor]]:
        result: List[Sensor] = []
        with Database.create_db_session() as db:
            count_query = db.query(DbSensor)
            query = db.query(DbSensor)
            if order_by == 'name':
                query = query.order_by(DbSensor.name)
            elif order_by == 'name_desc':
                query = query.order_by(DbSensor.name.desc())
            elif order_by == 'id':
                query = query.order_by(DbSensor.id)
            elif order_by == 'id_desc':
                query = query.order_by(DbSensor.id.desc())
            query = query.offset(offset).limit(limit)
            count = count_query.count()
            db_sensors = query.all()
            for db_sensor in db_sensors:
                result.append(Sensor.model_validate(db_sensor))
        return count, result

    def create(self, sensor: CreateSensor) -> Sensor:
        with Database.create_db_session() as db:
            db_sensor = DbSensor(**sensor.model_dump(mode="json", exclude_unset=True))
            db.add(db_sensor)
            db.commit()
            db.refresh(db_sensor)
            return Sensor.model_validate(db_sensor)

    def update(self, sensor_id: int, sensor: UpdateSensor) -> Sensor | None:
        with Database.create_db_session() as db:
            current_sensor = db.query(DbSensor).filter(DbSensor.id == sensor_id).first()
            if current_sensor is None:
                return None
            updated_sensor = db.execute(
                insert(DbSensor)
                .where(DbSensor.id == sensor_id)
                .values(**sensor.model_dump(mode="json", exclude_unset=True))
                .returning(literal_column("*"))
            ).one()
            db.commit()
            return Sensor.model_validate(updated_sensor)

    def delete(self, sensor_id: int) -> bool:
        with Database.create_db_session() as db:
            sensor = db.query(DbSensor).filter(DbSensor.id == sensor_id).first()
            if sensor:
                db.delete(sensor)
                db.commit()
                return True
            return False
