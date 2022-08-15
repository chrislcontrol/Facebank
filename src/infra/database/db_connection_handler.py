from abc import ABC, abstractmethod

from src.domain.types.entity import Entity


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

    def __del__(self):
        self.close_pool_session()
