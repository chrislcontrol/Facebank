from src.domain.entities.client import Client
from src.domain.repositories.client_repository import ClientRepository
from src.infra.base_classes.repository import Repository
from src.infra.database.sql_alchemy.models.client import ClientDB


class PostgresClientRepository(ClientRepository, Repository):
    entity = ClientDB

    def create_client(self, *, username: str, password: bytes, email: str) -> Client:
        return self._create(username=username, password=password.decode('utf-8'), email=email)

    def get_by_username(self, username: str) -> Client:
        return self._get(username=username)

    def already_exists(self, username: str) -> bool:
        return bool(self.get_by_username(username=username))
