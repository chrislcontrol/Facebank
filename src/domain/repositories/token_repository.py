from abc import abstractmethod, ABC

from src.domain.entities.client import Client
from src.domain.entities.token import Token


class TokenRepository(ABC):
    @abstractmethod
    def create(self, client: Client) -> Token:
        raise NotImplementedError()

    @abstractmethod
    def get_or_create(self, *, client: Client) -> Token:
        raise NotImplementedError()
