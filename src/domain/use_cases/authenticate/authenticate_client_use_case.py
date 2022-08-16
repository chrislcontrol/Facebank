from hmac import compare_digest

from src.domain.entities.client import Client
from src.domain.entities.token import Token
from src.domain.exceptions.client_not_found import ClientNotFound
from src.domain.exceptions.invalid_password import InvalidPassword
from src.domain.helpers.encryptor import Encryptor
from src.domain.repositories.client_repository import ClientRepository
from src.domain.repositories.token_repository import TokenRepository
from src.domain.types.use_case import UseCase


class AuthenticateClientUseCase(UseCase):
    def __init__(self, token_repository: TokenRepository,
                 client_repository: ClientRepository,
                 encryptor: Encryptor):
        self._token_repository = token_repository
        self._client_repository = client_repository
        self._encryptor = encryptor

    def authenticate(self, *, username: str, password: str) -> Token:
        client = self._get_client(username=username)
        self.validate_password(client=client, password=password)

        _, token = self._token_repository.get_or_create(client=client)

        return token

    def _get_client(self, username: str) -> Client:
        client = self._client_repository.get_by_username(username=username)
        if not client:
            raise ClientNotFound()

        return client

    def validate_password(self, *, client: Client, password: str) -> bool:
        client_password = client.password.encode()
        hashed_password = self._encryptor.encrypt(password, client_password)

        if not compare_digest(hashed_password, client_password):
            raise InvalidPassword()

        return True
