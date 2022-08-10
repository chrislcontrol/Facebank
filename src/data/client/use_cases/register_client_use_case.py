from src.data.client.exceptions import ClientAlreadyExists
from src.data.interfaces.encryptor import IEncryptor
from src.domain.entities.client import Client
from src.infra.repositories.client_repository import ClientRepository
from src.presenters.serializers.client.register_client_serializer import RegisterClientSerializer


class RegisterClientUseCase:
    def __init__(self, client_repository: ClientRepository, encryptor: IEncryptor):
        self._client_repository = client_repository
        self._encryptor = encryptor

    def register(self, input_data: RegisterClientSerializer) -> Client:
        input_data.is_valid(raise_exception=True)
        valid_data = input_data.validated_data
        already_exists = self._client_repository.get_by_username(username=valid_data['username'])
        if already_exists:
            raise ClientAlreadyExists()

        hashed_password = self._encryptor.encrypt(value=valid_data.pop('password')).decode('utf-8')

        return self._client_repository.create_client(password=hashed_password, **valid_data)
