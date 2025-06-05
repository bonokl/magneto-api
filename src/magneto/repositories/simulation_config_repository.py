from src.database.models.simulation_config import SimulationConfig as DbSimulationConfig
from src.entities.simulation_config import SimulationConfig, CreateSimulationConfig, UpdateSimulationConfig
from src.database.database import Database
from sqlalchemy import update as sqlalchemy_update, literal_column
from typing import Optional, Tuple, List

class SimulationConfigRepository:
    def get(self, config_id: int) -> SimulationConfig | None:
        with Database.create_db_session() as db:
            config = db.query(DbSimulationConfig).filter(DbSimulationConfig.id == config_id).first()
            return SimulationConfig.model_validate(config) if config else None

    def get_all(self, offset: int = 0, limit: int = 100, order_by: Optional[str] = None) -> Tuple[int, List[SimulationConfig]]:
        result: List[SimulationConfig] = []
        with Database.create_db_session() as db:
            count_query = db.query(DbSimulationConfig)
            query = db.query(DbSimulationConfig)
            if order_by == 'id':
                query = query.order_by(DbSimulationConfig.id)
            elif order_by == 'id_desc':
                query = query.order_by(DbSimulationConfig.id.desc())
            query = query.offset(offset).limit(limit)
            count = count_query.count()
            db_configs = query.all()
            for db_config in db_configs:
                result.append(SimulationConfig.model_validate(db_config))
        return count, result

    def create(self, config: CreateSimulationConfig) -> SimulationConfig:
        with Database.create_db_session() as db:
            db_config = DbSimulationConfig(**config.model_dump(mode="json", exclude_unset=True))
            db.add(db_config)
            db.commit()
            db.refresh(db_config)
            return SimulationConfig.model_validate(db_config)

    def update(self, config_id: int, config: UpdateSimulationConfig) -> SimulationConfig | None:
        with Database.create_db_session() as db:
            current_config = db.query(DbSimulationConfig).filter(DbSimulationConfig.id == config_id).first()
            if current_config is None:
                return None
            updated_config = db.execute(
                sqlalchemy_update(DbSimulationConfig)
                .where(DbSimulationConfig.id == config_id)
                .values(**config.model_dump(mode="json", exclude_unset=True))
                .returning(literal_column("*"))
            ).one()
            db.commit()
            return SimulationConfig.model_validate(updated_config)

    def delete(self, config_id: int) -> bool:
        with Database.create_db_session() as db:
            config = db.query(DbSimulationConfig).filter(DbSimulationConfig.id == config_id).first()
            if config:
                db.delete(config)
                db.commit()
                return True
            return False
