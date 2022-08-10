from hmac import compare_digest
from operator import itemgetter

from src.data.authenticate.exceptions import InvalidPassword
from src.data.client.exceptions import ClientNotFound
from src.data.interfaces.client_repository_interface import IClientRepository
from src.data.interfaces.encryptor_interface import IEncryptor
from src.data.interfaces.token_repository_interface import ITokenRepository
from src.domain.entities.client import Client
from src.domain.entities.token import Token
from src.domain.use_cases.authenticate.authenticate_client_use_case import IAuthenticateClientUseCase
from src.presenters.serializers.authenticate.authenticate_client_serializer import AuthenticateClientSerializer


class AuthenticateClientUseCase(IAuthenticateClientUseCase):
    def __init__(self, token_repository: ITokenRepository,
                 client_repository: IClientRepository,
                 encryptor: IEncryptor):
        self._token_repository = token_repository
        self._client_repository = client_repository
        self._encryptor = encryptor

    def authenticate(self, *, input_data: AuthenticateClientSerializer) -> Token:
        input_data.is_valid(True)

        username, password = itemgetter("username", "password")(input_data.validated_data)

        client = self._get_client(username=username)
        self.validate_password(client=client, password=password)

        return self._token_repository.get_or_create(client=client)

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
