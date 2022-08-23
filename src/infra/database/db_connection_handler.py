from abc import ABC, abstractmethod
from typing import Type

from src.domain.types.entity import Entity
from src.infra.base_classes.queryset import QuerySet


class DBHandler:
    model: Type[Entity]

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
    def filter(self, *, entity: Type[Entity], **params) -> QuerySet[Entity]:
        raise NotImplementedError()

    @abstractmethod
    def get(self, *, entity: Type[Entity], **params) -> Entity:
        raise NotImplementedError()


class DBConnectionHandler(ABC):
    model: Type[Entity]

    @abstractmethod
    def __enter__(self) -> DBHandler:
        raise NotImplementedError()

    @abstractmethod
    def __exit__(self, *args, **kwargs) -> None:
        raise NotImplementedError()
