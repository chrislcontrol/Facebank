from abc import abstractmethod, ABC
from typing import Tuple

from src.domain.entities.client import Client
from src.domain.entities.token import Token


class TokenRepository(ABC):
    @abstractmethod
    def get_or_create(self, *, client: Client) -> Tuple[bool, Token]:
        raise NotImplementedError()

    @abstractmethod
    def get_token(self, *, client: Client) -> Token:
        raise NotImplementedError()

    @abstractmethod
    def get_token_by_string_with_client(self, *, token: str) -> Token:
        raise NotImplementedError()
