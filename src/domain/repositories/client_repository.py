from abc import abstractmethod, ABC
from typing import Type

from src.domain.entities.client import Client
from src.infra.repositories.base.repository import Repository


class ClientRepository(Repository):
    @property
    @abstractmethod
    def entity(self) -> Type[Client]:
        raise NotImplementedError()

    @abstractmethod
    def create_client(self, **kwargs) -> Client:
        raise NotImplementedError()

    @abstractmethod
    def get_by_username(self, username: str) -> Client:
        raise NotImplementedError()

    @abstractmethod
    def already_exists(self, username: str) -> bool:
        raise NotImplementedError()
