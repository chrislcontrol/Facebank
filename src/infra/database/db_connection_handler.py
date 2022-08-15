from abc import ABC, abstractmethod
from typing import List

from src.domain.types.entity import Entity
from src.infra.repositories.objects.queryset import QuerySet


class DBConnectionHandler(ABC):
    @abstractmethod
    def close_pool_session(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def add(self, obj: Entity) -> Entity:
        raise NotImplementedError()

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def create(self, entity: Entity) -> Entity:
        raise NotImplementedError()

    @abstractmethod
    def filter(self, **params) -> QuerySet[Entity]:
        raise NotImplementedError()

    @abstractmethod
    def get(self, **params) -> Entity:
        raise NotImplementedError()

    def __del__(self):
        self.close_pool_session()
