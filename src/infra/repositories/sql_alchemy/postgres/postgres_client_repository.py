from src.domain.entities.client import Client
from src.domain.repositories.client_repository import ClientRepository
from src.infra.repositories.sql_alchemy.models.client import ClientDB
from src.infra.repositories.sql_alchemy.helpers.sql_alchemy_repository import SQLAlchemyRepository


class PostgresClientRepository(ClientRepository, SQLAlchemyRepository):
    db_model = ClientDB

    def create_client(self, *, username: str, password: str, email: str) -> Client:
        obj = self.db_model(username=username, password=password, email=email)
        return self.create(obj)

    def get_by_username(self, username: str) -> Client:
        return self.get(username=username)

    def already_exists(self, username: str) -> bool:
        return bool(self.get_by_username(username=username))
