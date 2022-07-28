from src.data.exceptions import ValidationError
from src.infra.entities.client import Client
from src.infra.repositories.client_repository import ClientRepository


class RegisterClientUseCase:
    def __init__(self, client_repository: ClientRepository):
        self._client_repository = client_repository

    def register(self, username: str, password: str, email: str) -> Client:
        validate_entry = isinstance(username, str) and isinstance(password, str) and isinstance(email, str)
        if not validate_entry:
            raise ValidationError()

        return self._client_repository.create_client(username=username, password=password)
