from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.domain.types.entity import Entity
from src.infra.database.db_connection_handler import DBConnectionHandler, DBHandler
from src.infra.environments.variables import DATABASE_URL, DEBUG_DB
from src.infra.base_classes.queryset import QuerySet


class _DBHandler(DBHandler):
    def __init__(self, *, session, engine):
        self.session = session
        self.engine = engine

    def close_pool_session(self) -> None:
        return self.session.close()

    def add(self, obj: Entity) -> Entity:
        return self.session.add(obj)

    def commit(self) -> None:
        return self.session.commit()

    def create(self, entity: Entity) -> Entity:
        self.add(entity)
        self.commit()
        return entity

    def rollback(self) -> None:
        return self.session.rollback()

    def filter(self, *, entity: Entity, **params) -> QuerySet[Entity]:
        return self.session.query(entity).filter_by(**params)

    def get(self, *, entity: Entity, **params) -> Entity:
        queryset = self.filter(entity=entity, **params)
        count = queryset.count()
        if count > 1:
            raise ValueError(f"Expected result to be 1 and {count} was found.")

        return queryset.first()


class SQLAlchemyConnectionHandler(DBConnectionHandler):
    """ Sqlalchemy database connection """

    def __init__(self):
        self.__connection_string = DATABASE_URL
        self.__session = None
        self.__engine = None
        self.__session_maker = sessionmaker()

    def __enter__(self):
        self.__engine = create_engine(self.__connection_string)
        self.__session = self.__session_maker(bind=self.__engine, expire_on_commit=False)
        if DEBUG_DB:
            print('DB Session oppened.')
        return _DBHandler(engine=self.__engine, session=self.__session)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.close()
        if DEBUG_DB:
            print('DB Session closed.')
