from src.database.models.magnet import Magnet as DbMagnet
from src.entities.magnet import Magnet
from src.database.database import Database
from src.entities.magnet import CreateMagnet, UpdateMagnet
from sqlalchemy import update as sqlalchemy_update, literal_column
from typing import Any, Optional, Tuple, List

class MagnetRepository:
    def get(self, magnet_id: int) -> Magnet | None:
        with Database.create_db_session() as db:
            magnet = db.query(DbMagnet).filter(DbMagnet.id == magnet_id).first()
            return Magnet.model_validate(magnet) if magnet else None

    def get_all(self, offset: int = 0, limit: int = 100, order_by: Optional[str] = None) -> Tuple[int, List[Magnet]]:
        result: List[Magnet] = []
        with Database.create_db_session() as db:
            count_query = db.query(DbMagnet)
            query = db.query(DbMagnet)
            if order_by == 'name':
                query = query.order_by(DbMagnet.name)
            elif order_by == 'name_desc':
                query = query.order_by(DbMagnet.name.desc())
            elif order_by == 'id':
                query = query.order_by(DbMagnet.id)
            elif order_by == 'id_desc':
                query = query.order_by(DbMagnet.id.desc())
            query = query.offset(offset).limit(limit)
            count = count_query.count()
            db_magnets = query.all()
            for db_magnet in db_magnets:
                result.append(Magnet.model_validate(db_magnet))
        return count, result

    def create(self, magnet: CreateMagnet) -> Magnet:
        with Database.create_db_session() as db:
            db_magnet = DbMagnet(**magnet.model_dump(mode="json", exclude_unset=True))
            db.add(db_magnet)
            db.commit()
            db.refresh(db_magnet)
            return Magnet.model_validate(db_magnet)

    def update(self, magnet_id: int, magnet: UpdateMagnet) -> Magnet | None:
        with Database.create_db_session() as db:
            current_magnet = db.query(DbMagnet).filter(DbMagnet.id == magnet_id).first()
            if current_magnet is None:
                return None
            updated_magnet = db.execute(
                sqlalchemy_update(DbMagnet)
                .where(DbMagnet.id == magnet_id)
                .values(**magnet.model_dump(mode="json", exclude_unset=True))
                .returning(literal_column("*"))
            ).one()
            db.commit()
            return Magnet.model_validate(updated_magnet)

    def delete(self, magnet_id: int) -> bool:
        with Database.create_db_session() as db:
            magnet = db.query(DbMagnet).filter(DbMagnet.id == magnet_id).first()
            if magnet:
                db.delete(magnet)
                db.commit()
                return True
            return False
