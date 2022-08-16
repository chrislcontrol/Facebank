from abc import ABC

from src.domain.entities.client import Client
from src.domain.entities.user import User


class UserRepository(ABC):
    def create_user(self, *, name: str, username: str, password: bytes, client: Client, attributes: dict) -> User:
        raise NotImplementedError()

    def already_exists(self, *, username: str, client: Client, raise_exception: bool) -> bool:
        raise NotImplementedError()
