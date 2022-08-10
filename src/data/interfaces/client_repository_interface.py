from abc import abstractmethod

from src.domain.entities.client import Client
from src.infra.helpers.repository import Repository


class IClientRepository(Repository):
    @abstractmethod
    def create_client(self, **kwargs) -> Client:
        raise NotImplementedError()

    @abstractmethod
    def get_by_username(self, username: str) -> Client:
        raise NotImplementedError()
