from src.data.interfaces.client_repository_interface import IClientRepository
from src.domain.entities.client import Client


class IRegisterClientUseCase:
    def __init__(self, client_repository: IClientRepository):
        self._client_repository = client_repository

    def register(self, username: str, password: str, email: str) -> Client:
        raise NotImplementedError()
