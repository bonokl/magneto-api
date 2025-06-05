from src.database.models.function import Function as DbFunction
from src.entities.function import Function
from src.database.database import Database
from sqlalchemy.orm import Session
from typing import Optional, Tuple, List

class FunctionRepository:
    def get(self, function_id: int) -> Function | None:
        with Database.create_db_session() as db:
            function = db.query(DbFunction).filter(DbFunction.id == function_id).first()
            return Function.model_validate(function) if function else None

    def get_all(self, offset: int = 0, limit: int = 100, order_by: Optional[str] = None) -> Tuple[int, List[Function]]:
        result: List[Function] = []
        with Database.create_db_session() as db:
            count_query = db.query(DbFunction)
            query = db.query(DbFunction)
            if order_by == 'name':
                query = query.order_by(DbFunction.name)
            elif order_by == 'name_desc':
                query = query.order_by(DbFunction.name.desc())
            elif order_by == 'id':
                query = query.order_by(DbFunction.id)
            elif order_by == 'id_desc':
                query = query.order_by(DbFunction.id.desc())
            query = query.offset(offset).limit(limit)
            count = count_query.count()
            db_functions = query.all()
            for db_function in db_functions:
                result.append(Function.model_validate(db_function))
        return count, result

    def create(self, name: str, description: str = None) -> Function:
        with Database.create_db_session() as db:
            db_function = DbFunction(name=name, description=description)
            db.add(db_function)
            db.commit()
            db.refresh(db_function)
            return Function.model_validate(db_function)

    def delete(self, function_id: int) -> bool:
        with Database.create_db_session() as db:
            function = db.query(DbFunction).filter(DbFunction.id == function_id).first()
            if function:
                db.delete(function)
                db.commit()
                return True
            return False
