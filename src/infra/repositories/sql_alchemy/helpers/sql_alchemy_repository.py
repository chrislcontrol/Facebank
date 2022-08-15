from abc import abstractmethod

from src.domain.types.entity import Entity
from src.infra.adapters.sql_alchemy.sql_alchemy_connection_handler import SQLAlchemyConnectionHandler
from src.infra.adapters.sql_alchemy.sql_alchemy_database_model import SQLAlchemyDatabaseModel
from src.infra.exceptions.integrity_error import IntegrityError
from src.infra.repositories.objects.queryset import QuerySet
from src.infra.repositories.repository import Repository


class SQLAlchemyRepository(Repository):
    connection_handler = SQLAlchemyConnectionHandler()

    @property
    @abstractmethod
    def db_model(self) -> SQLAlchemyDatabaseModel:
        raise NotImplementedError()

    def create(self, obj: SQLAlchemyDatabaseModel) -> Entity:
        try:
            self.connection_handler.add(obj)
            self.connection_handler.commit()

            return obj
        except Exception:
            self.connection_handler.rollback()
            raise

    def filter(self, **params) -> QuerySet[Entity]:
        return self.connection_handler.filter(db_model=self.db_model, **params)

    def get(self, **kwargs) -> Entity:
        queryset = self.filter(**kwargs)  # noqa
        count = queryset.count()
        if count > 1:
            raise IntegrityError(f'Expected 1 result but got {count}.')

        return queryset.first()
