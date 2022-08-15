from abc import abstractmethod, ABC

from src.domain.entities.client import Client


class ClientRepository(ABC):
    @abstractmethod
    def create_client(self, **kwargs) -> Client:
        raise NotImplementedError()

    @abstractmethod
    def get_by_username(self, username: str) -> Client:
        raise NotImplementedError()

    @abstractmethod
    def already_exists(self, username: str) -> bool:
        raise NotImplementedError()
