from abc import ABC, abstractmethod
from typing import Type

from src.domain.types.entity import Entity
from src.infra.database.db_connection_handler import DBConnectionHandler
from src.infra.repositories.objects.queryset import QuerySet


class Repository(ABC):
    def __init__(self, db_connection_handler: DBConnectionHandler):
        self.db_connection_handler = db_connection_handler

    @property
    @abstractmethod
    def entity(self) -> Type[Entity]:
        raise NotImplementedError()

    def _create(self, **fields) -> Entity:
        obj = self.entity(**fields)
        return self.db_connection_handler.create(obj)

    def _get(self, **fields) -> Entity:
        return self.db_connection_handler.get(entity=self.entity, **fields)

    def _filter(self, **fields) -> QuerySet[Entity]:
        return self.db_connection_handler.filter(entity=self.entity, **fields)
