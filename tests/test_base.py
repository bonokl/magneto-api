import pytest

from fastapi.testclient import TestClient
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
    from src.arena_hub.arena_hub import ArenaHub
    ArenaHub.initialize()


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
        from src.database.models.app import App
        from src.database.database import Database
        yield
        with Database.create_db_session() as db:
            db.query(App).delete()
            db.commit()
