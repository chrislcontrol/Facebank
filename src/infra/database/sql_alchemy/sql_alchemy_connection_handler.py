from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.domain.types.entity import Entity
from src.infra.database.db_connection_handler import DBConnectionHandler, DBHandler
from src.infra.environments.variables import DATABASE_URL
from src.infra.base_classes.queryset import QuerySet


class _DBHandler(DBHandler):
    def __init__(self, model, session, engine):
        self.model = model
        self.session = session
        self.engine = engine

    def close_pool_session(self) -> None:
        return self.session.close()

    def add(self, obj: Entity) -> Entity:
        return self.session.add(obj)

    def commit(self) -> None:
        return self.session.commit()

    def create(self, **fields) -> Entity:
        entity = self.model(**fields)
        self.add(entity)
        self.commit()
        return entity

    def rollback(self) -> None:
        return self.session.rollback()

    def filter(self, **params) -> QuerySet[Entity]:
        return self.session.query(self.model).filter_by(**params)

    def get(self, **params) -> Entity:
        queryset = self.filter(**params)
        count = queryset.count()
        if count > 1:
            raise ValueError(f"Expected result to be 1 and {count} was found.")

        return queryset.first()


class SQLAlchemyConnectionHandler(DBConnectionHandler):
    """ Sqlalchemy database connection """

    def __init__(self, model: Entity):
        self.__connection_string = DATABASE_URL
        self.model = model
        self.__session = None
        self.__engine = None
        self.__session_maker = sessionmaker()

    def __enter__(self):
        self.__engine = create_engine(self.__connection_string)
        self.__session = self.__session_maker(bind=self.__engine, expire_on_commit=False)
        return _DBHandler(engine=self.__engine, model=self.model, session=self.__session)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.close()
