
from typing import Optional, Tuple, List

from src.database.models.design import Design as DbDesign
from src.database.models.sensor import Sensor as DbSensor
from src.entities.design import Design, CreateDesign, UpdateDesign
from src.database.database import Database

class DesignRepository:
    def get(self, design_id: int) -> Design | None:
        with Database.create_db_session() as db:
            design = db.query(DbDesign).filter(DbDesign.id == design_id).first()
            return Design.model_validate(design) if design else None

    def get_all(self, offset: int = 0, limit: int = 100, order_by: Optional[str] = None) -> Tuple[int, List[Design]]:
        result: List[Design] = []
        with Database.create_db_session() as db:
            count_query = db.query(DbDesign)
            query = db.query(DbDesign)
            if order_by == 'name':
                query = query.order_by(DbDesign.name)
            elif order_by == 'name_desc':
                query = query.order_by(DbDesign.name.desc())
            query = query.offset(offset).limit(limit)
            count = count_query.count()
            db_designs = query.all()
            for db_design in db_designs:
                result.append(Design.model_validate(db_design))
        return count, result

    def create(self, design: CreateDesign) -> Design:
        with Database.create_db_session() as db:
            db_design = DbDesign(
                name=design.name,
                function_id=design.function_id,
                magnet_id=design.magnet_id
            )
            db.add(db_design)
            db.commit()
            db.refresh(db_design)
            # Handle many-to-many sensors association
            if hasattr(db_design, 'sensors'):
                if design.sensor_ids:
                    sensors = db.query(DbSensor).filter(DbSensor.id.in_(design.sensor_ids)).all()
                    db_design.sensors = sensors
                    db.commit()
                    db.refresh(db_design)
            return Design.model_validate(db_design)

    def update(self, design_id: int, design: UpdateDesign) -> Design | None:
        with Database.create_db_session() as db:
            db_design = db.query(DbDesign).filter(DbDesign.id == design_id).first()
            if not db_design:
                return None
            update_data = design.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                if key == 'sensor_ids' and hasattr(db_design, 'sensors'):
                    sensors = db.query(DbSensor).filter(DbSensor.id.in_(value)).all()
                    db_design.sensors = sensors
                elif hasattr(db_design, key):
                    setattr(db_design, key, value)
            db.commit()
            return Design.model_validate(db_design)

    def delete(self, design_id: int) -> bool:
        with Database.create_db_session() as db:
            design = db.query(DbDesign).filter(DbDesign.id == design_id).first()
            if design:
                db.delete(design)
                db.commit()
                return True
            return False
