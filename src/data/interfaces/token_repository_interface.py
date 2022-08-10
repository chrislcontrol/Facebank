from abc import abstractmethod

from src.domain.entities.client import Client
from src.domain.entities.token import Token
from src.infra.helpers.repository import Repository


class ITokenRepository(Repository):
    @abstractmethod
    def create(self, client: Client) -> Token:
        raise NotImplementedError()

    def get_or_create(self, *, client: Client) -> Token:
        raise NotImplementedError()
