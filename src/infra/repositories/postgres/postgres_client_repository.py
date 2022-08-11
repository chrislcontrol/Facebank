from src.domain.exceptions.client_already_exists import ClientAlreadyExists
from src.domain.repositories.client_repository import ClientRepository
from src.domain.entities.client import Client
from src.infra.repositories.object_values.repository import Repository
from src.infra.repositories.models.client import ClientDB


class PostgresClientRepository(ClientRepository, Repository):
    entity = Client

    def create_client(self, *, username: str, password: str, email: str) -> Client:
        already_exists = self.get_by_username(username=username)
        if already_exists:
            raise ClientAlreadyExists()

        client_db = ClientDB.create(username=username, password=password, email=email)
        return client_db

    def get_by_username(self, username: str) -> Client:
        query = ClientDB.query.filter_by(username=username).first()
        return self.convert(query)
