from src.domain.types.entity import Entity
from src.infra.adapters.sql_alchemy.session import create_session
from src.infra.database.db_connection_handler import DBConnectionHandler
from src.infra.environments.variables import DEBUG_DB_OPENINGS
from src.infra.repositories.objects.queryset import QuerySet


class SQLAlchemyConnectionHandler(DBConnectionHandler):
    def __init__(self):
        self._session = create_session()
        if DEBUG_DB_OPENINGS:
            print("DB Session openned.")

    def close_pool_session(self) -> None:
        if DEBUG_DB_OPENINGS:
            print('DB Session closed.')
        self._session.close()

    def add(self, obj: Entity) -> Entity:
        local_obj = self._session.merge(obj)
        return self._session.add(local_obj)

    def commit(self) -> None:
        return self._session.commit()

    def create(self, entity: Entity) -> Entity:
        try:
            self.add(entity)
            self.commit()
            return entity

        except Exception:
            self.rollback()
            raise

    def rollback(self) -> None:
        return self._session.rollback()

    def filter(self, entity: Entity, **params) -> QuerySet[Entity]:
        return self._session.query(entity).filter_by(**params)

    def get(self, entity: Entity, **params) -> Entity:
        queryset = self.filter(entity=entity, **params)
        count = queryset.count()
        if count > 1:
            raise ValueError(f"Expected result to be 1 and {count} was found.")

        return queryset.first()
