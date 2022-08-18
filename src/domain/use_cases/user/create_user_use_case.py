from src.domain.entities.client import Client
from src.domain.entities.user import User
from src.domain.helpers.encryptor import Encryptor
from src.domain.helpers.random_password import random_password
from src.domain.repositories.user_repository import UserRepository
from src.domain.types.use_case import UseCase


class CreateUserUseCase(UseCase):
    def __init__(self, user_repository: UserRepository, encryptor: Encryptor):
        self._user_repository = user_repository
        self._encryptor = encryptor

    def create(self, *, name: str, username: str, client: Client, password: str = None, attributes: dict = {}) -> User:
        hashed_password = self.__hash_password(password=password)
        self._user_repository.already_exists(username=username,
                                             client=client,
                                             raise_exception=True)

        return self._user_repository.create_user(name=name,
                                                 username=username,
                                                 password=hashed_password,
                                                 client=client,
                                                 attributes=attributes)

    def __hash_password(self, password: str = None):
        password = password or random_password(14)
        return self._encryptor.encrypt_password(password)
