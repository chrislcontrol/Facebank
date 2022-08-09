from src.data.client.exceptions import ClientAlreadyExists
from src.domain.entities.client import Client
from src.infra.repositories.client_repository import ClientRepository
from src.presenters.serializers.client.register_client_serializer import RegisterClientSerializer


class RegisterClientUseCase:
    def __init__(self, client_repository: ClientRepository):
        self._client_repository = client_repository

    def register(self, input_data: RegisterClientSerializer) -> Client:
        input_data.is_valid(raise_exception=True)
        valid_data = input_data.validated_data
        already_exists = self._client_repository.get_by_username(username=valid_data['username'])
        if already_exists:
            raise ClientAlreadyExists()

        return self._client_repository.create_client(**valid_data)
