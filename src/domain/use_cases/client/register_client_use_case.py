from src.domain.entities.client import Client
from src.domain.helpers.encryptor import IEncryptor
from src.domain.types.use_case import UseCase
from src.infra.repositories.postgres.postgres_client_repository import PostgresClientRepository


class RegisterClientUseCase(UseCase):
    def __init__(self, client_repository: PostgresClientRepository, encryptor: IEncryptor):
        self._client_repository = client_repository
        self._encryptor = encryptor

    def register(self, *, username: str, password: str, email: str) -> Client:
        hashed_password = self._encryptor.encrypt(value=password).decode('utf-8')

        return self._client_repository.create_client(username=username, password=hashed_password, email=email)
