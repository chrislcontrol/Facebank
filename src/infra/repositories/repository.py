from abc import ABC, abstractmethod

from src.domain.types.entity import Entity
from src.infra.database.database_model import DatabaseModel
from src.infra.database.db_connection_handler import DBConnectionHandler
from src.infra.repositories.objects.queryset import QuerySet


class Repository(ABC):
    @property
    @abstractmethod
    def connection_handler(self) -> DBConnectionHandler:
        raise NotImplementedError()

    @property
    @abstractmethod
    def db_model(self) -> DatabaseModel:
        raise NotImplementedError()

    @abstractmethod
    def create(self, obj: DatabaseModel) -> Entity:
        raise NotImplementedError()

    @abstractmethod
    def filter(self, **params) -> QuerySet[Entity]:
        raise NotImplementedError()

    @abstractmethod
    def get(self, **kwargs) -> Entity:
        raise NotImplementedError()
