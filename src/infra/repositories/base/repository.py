from abc import ABC, abstractmethod
from typing import Type

from src.domain.types.entity import Entity
from src.infra.repositories.objects.queryset import QuerySet


class Repository(ABC):
    @property
    @abstractmethod
    def entity(self) -> Type[Entity]:
        raise NotImplementedError()

    def create(self, **fields) -> Entity:
        obj = self.entity(**fields)
        return self.db_connection_handler.create(obj)

    def get(self, **fields) -> Entity:
        return self.db_connection_handler.get(entity=self.entity, **fields)

    def filter(self, **fields) -> QuerySet[Entity]:
        return self.db_connection_handler.filter(entity=self.entity, **fields)
