from sqlalchemy import create_engine
from sqlalchemy.future import engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

from src.application.environments.variables import DATABASE_URL
from src.domain.types.entity import Entity
from src.infra.adapters.sql_alchemy.sql_alchemy_database_model import SQLAlchemyDatabaseModel
from src.infra.database.db_connection_handler import DBConnectionHandler
from src.infra.repositories.objects.queryset import QuerySet


class SQLAlchemyConnectionHandler(DBConnectionHandler):
    def __init__(self):
        self._session = self._create_session()

    def close_pool_session(self) -> None:
        self._session.close()

    def add(self, obj: SQLAlchemyDatabaseModel) -> Entity:
        return self._session.add(obj)

    def commit(self) -> None:
        return self._session.commit()

    def rollback(self) -> None:
        return self._session.rollback()

    def filter(self, db_model: SQLAlchemyDatabaseModel, **params) -> QuerySet[Entity]:
        return self._session.query(db_model).filter_by(**params)

    def _create_session(self):
        base = declarative_base()
        db_session = scoped_session(sessionmaker(autocommit=False,
                                                 autoflush=False,
                                                 bind=engine))
        base.query = db_session.query_property()
        new_engine = create_engine(DATABASE_URL)
        base.metadata.create_all(new_engine)
        session_maker = sessionmaker()
        return session_maker(bind=new_engine)
