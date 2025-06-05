
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy import text
from testcontainers.postgres import PostgresContainer

from src import variables
from src.api.api import API


def initialize_database():
    db_container = PostgresContainer("postgres:14")
    db_container.start()
    db_url = db_container.get_connection_url()
    variables.database_url = db_url

    from src.database.database import Database
    Database.initialize(echo=True)


def initialize_services():
    from src.magneto.magneto import Magneto
    Magneto.initialize()


def initialize_api():
    from src.api.api import API
    API.initialize()


initialize_database()
initialize_services()
initialize_api()


class BaseTest:
    client = TestClient(app=API.app)

    @pytest.fixture(scope="function")
    def database_cleanup(self):
        from src.database.database import Database
        yield
        db: Session
        with Database.create_db_session() as db:
            db.execute(text(
                """
                
                """
            ))
            db.commit()
