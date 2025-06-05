import os
from contextlib import contextmanager

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session, declarative_base

from src import variables


class Database:
    BaseModel = None
    _SessionFactory = None

    @classmethod
    def initialize(cls, echo=False) -> None:
        engine = create_engine(variables.database_url, echo=echo)

        cls._SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        cls.BaseModel = declarative_base()

        cls._run_migrations()

    @classmethod
    def _run_migrations(cls) -> None:
        """
        This method finds the location of alembic.ini configuration file and
        the folder in which migration files are located. After that, creates a
        table named migration_lock if it doesn't exist. This table will be used
        to acquire an exclusive access lock by all python processes which are
        currently starting up. The first python process to acquire an exclusive
        lock on the table will run alembic migrations, while all other python
        processes will wait for the first one to finish.
        Once the first process is finished with the migration, the lock is lifted
        and other python processes won't execute the migration because the
        alembic version will already be upgraded by that time.
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        alembic_config_file_path = os.path.join(dir_path, "alembic.ini")

        alembic_cfg = Config(alembic_config_file_path)
        migrations_file_path = os.path.join(dir_path, "migrations")
        alembic_cfg.set_main_option("script_location", migrations_file_path)
        alembic_cfg.set_main_option("sqlalchemy.url", variables.database_url)

        db: Session
        with cls.create_db_session() as db:
            db.execute(text(
                """
                create table if not exists migration_lock(
                    id serial primary key
                );
                """
            ))
            db.commit()

        with cls.create_db_session() as db:
            db.execute(text(
                """
                LOCK TABLE migration_lock IN ACCESS EXCLUSIVE MODE;
                """
            ))
            command.upgrade(alembic_cfg, "head")
            db.commit()

    @classmethod
    @contextmanager
    def create_db_session(cls) -> Session:
        session = cls._SessionFactory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
